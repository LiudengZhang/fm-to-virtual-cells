#!/usr/bin/env python3
"""Build the FM-to-Virtual-Cells citation scatter plot.

Reads the curated paper list from docs/talks/_data/fm-papers.yaml,
fetches citation counts from the Semantic Scholar Graph API,
writes the merged dataset to docs/talks/_data/fm-citations.csv,
and renders two outputs:
  - docs/talks/assets/fm-citation-plot.png   (static, for print/PDF)
  - docs/talks/assets/fm-citation-plot.html  (interactive Plotly, for the site)

Usage:
    python scripts/fm_citation_plot.py            # fetch + render
    python scripts/fm_citation_plot.py --no-fetch # render from cached CSV
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import math
import sys
import time
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import requests
import yaml
from adjustText import adjust_text

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_YAML = REPO_ROOT / "docs/talks/_data/fm-papers.yaml"
CITATIONS_CSV = REPO_ROOT / "docs/talks/_data/fm-citations.csv"
PLOT_PNG = REPO_ROOT / "docs/talks/assets/fm-citation-plot.png"
PLOT_HTML = REPO_ROOT / "docs/talks/assets/fm-citation-plot.html"

ERAS = [
    ("2023 paradigm", "2022-09", "2024-05", "#dde7f0"),
    ("2024 ambition", "2024-05", "2025-06", "#e6f0d8"),
    ("2025 reckoning", "2025-06", "2025-12", "#f5d9d9"),
    ("2026 response", "2025-12", "2026-06", "#f0e1c8"),
]

S2_BASE = "https://api.semanticscholar.org/graph/v1/paper/{pid}"
S2_FIELDS = "title,citationCount,year,publicationDate"

CATEGORY_COLOR = {
    "model": "#1f77b4",         # blue — things people built
    "critique": "#d62728",      # red — the reckoning
    "benchmark": "#9467bd",     # purple — substrate
    "position": "#2ca02c",      # green — framing
    "architecture": "#ff7f0e",  # orange — the response
}
CATEGORY_LABEL = {
    "model": "FM release",
    "critique": "Critique / eval",
    "benchmark": "Benchmark",
    "position": "Position / vision",
    "architecture": "New architecture",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--no-fetch",
        action="store_true",
        help="skip S2 API; use the existing CSV cache",
    )
    return parser.parse_args()


def load_curated() -> list[dict]:
    with PAPERS_YAML.open() as f:
        data = yaml.safe_load(f)
    return data["papers"]


def fetch_one(pid: str, name: str) -> int | None:
    """Fetch citationCount for one paper with retry-on-429."""
    url = S2_BASE.format(pid=pid)
    delays = [1.5, 5, 15, 30, 60]
    for attempt, delay in enumerate(delays, start=1):
        try:
            r = requests.get(url, params={"fields": S2_FIELDS}, timeout=20)
        except requests.RequestException as exc:
            print(f"  ! {name}: request failed ({exc})", file=sys.stderr)
            return None
        if r.status_code == 200:
            return r.json().get("citationCount")
        if r.status_code == 429:
            print(
                f"  · {name}: rate-limited (attempt {attempt}); "
                f"sleeping {delay}s",
                file=sys.stderr,
            )
            time.sleep(delay)
            continue
        if r.status_code == 404:
            print(f"  ! {name}: 404 for {pid}", file=sys.stderr)
            return None
        print(f"  ! {name}: HTTP {r.status_code}", file=sys.stderr)
        return None
    print(f"  ! {name}: gave up after {len(delays)} attempts", file=sys.stderr)
    return None


def fetch_citations(papers: list[dict]) -> pd.DataFrame:
    rows = []
    for p in papers:
        pid = p["s2_id"]
        name = p["name"]
        if "manual_cites" in p and p["manual_cites"] is not None:
            citation_count = int(p["manual_cites"])
            print(f"  ⊙ {name}: manual={citation_count}")
        else:
            citation_count = fetch_one(pid, name)
            time.sleep(1.1)  # be polite to the free tier
        rows.append(
            {
                "name": name,
                "s2_id": pid,
                "release_date": p["release_date"],
                "category": p["category"],
                "is_sc_fm": p.get("is_sc_fm", False),
                "annotate": p.get("annotate", False),
                "citation_count": citation_count,
            }
        )
    return pd.DataFrame(rows)


def compute_per_year(df: pd.DataFrame, today: dt.date) -> pd.DataFrame:
    df = df.copy()
    df["release_dt"] = pd.to_datetime(df["release_date"] + "-01")
    delta_years = (
        (pd.Timestamp(today) - df["release_dt"]).dt.days / 365.25
    ).clip(lower=0.25)
    df["citations_per_year"] = df["citation_count"] / delta_years
    return df


def render_plot(df: pd.DataFrame, out_path: Path, today: dt.date) -> None:
    fig, ax = plt.subplots(figsize=(17, 8.5))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("#fafafa")

    df_plot = df.dropna(subset=["citation_count"]).copy()
    # Floor at 1 cit/yr so log-axis can render zero-citation papers
    df_plot["cpy_plot"] = df_plot["citations_per_year"].clip(lower=1.0)

    # Era bands — drawn BEFORE points so points sit on top
    eras = ERAS
    for label, start, end, color in eras:
        ax.axvspan(
            pd.Timestamp(start), pd.Timestamp(end),
            color=color, alpha=0.35, zorder=1,
        )

    # Scatter — split each category by sc-FM-or-not so we can style edges
    for cat in CATEGORY_COLOR:
        sub_cat = df_plot[df_plot["category"] == cat]
        if sub_cat.empty:
            continue
        for is_sc in (True, False):
            sub = sub_cat[sub_cat["is_sc_fm"] == is_sc]
            if sub.empty:
                continue
            sizes = (
                (sub["citation_count"].fillna(0).clip(lower=1)) ** 0.55 * 14 + 40
            )
            ax.scatter(
                sub["release_dt"],
                sub["cpy_plot"],
                s=sizes,
                c=CATEGORY_COLOR[cat],
                alpha=0.85 if is_sc else 0.45,
                edgecolors="#111" if is_sc else "#bbb",
                linewidths=1.6 if is_sc else 0.8,
                label=CATEGORY_LABEL[cat] if is_sc else None,
                zorder=4 if is_sc else 3,
            )

    # Annotations placed by adjustText to avoid overlaps
    annotated = df_plot[df_plot["annotate"]].copy()
    texts = []
    for _, row in annotated.iterrows():
        texts.append(
            ax.text(
                row["release_dt"], row["cpy_plot"], row["name"],
                fontsize=8.5, color="#222",
                bbox=dict(
                    boxstyle="round,pad=0.18",
                    fc="white", ec="#999", alpha=0.92,
                    linewidth=0.7,
                ),
            )
        )

    # Era labels at the top
    ax.set_yscale("log")
    y_lo, y_hi = 0.7, df_plot["cpy_plot"].max() * 4
    ax.set_ylim(y_lo, y_hi)
    for label, start, end, _ in eras:
        mid = pd.Timestamp(start) + (pd.Timestamp(end) - pd.Timestamp(start)) / 2
        ax.text(
            mid, y_hi / 1.4, label, ha="center", va="top",
            fontsize=10, color="#444", fontweight="bold",
        )

    ax.set_xlim(pd.Timestamp("2022-08-01"), pd.Timestamp("2026-06-01"))
    ax.set_xlabel("Release date", fontsize=11)
    ax.set_ylabel("Citations per year (S2, log scale)", fontsize=11)
    ax.set_title(
        "Foundation models for cell biology — the 2023–2026 arc\n"
        "sc-FM-related papers shown with dark edges; adjacent FM families "
        "(pathology / genomic / protein) shown muted",
        fontsize=12,
        pad=14,
    )
    ax.grid(True, which="both", color="#ddd", linestyle="--", alpha=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.legend(
        loc="lower right",
        fontsize=9,
        frameon=True,
        framealpha=0.95,
        edgecolor="#bbb",
    )

    # Auto-place annotation labels to avoid overlap.
    # Bias movement upward (y-only) so labels stack vertically above their
    # dense cluster instead of fighting horizontally.
    if texts:
        adjust_text(
            texts,
            ax=ax,
            arrowprops=dict(arrowstyle="-", color="#888", lw=0.6),
            expand_points=(1.4, 2.4),
            expand_text=(1.15, 1.5),
            force_text=(0.25, 1.2),
            force_points=(0.2, 0.6),
            lim=500,
            only_move={"text": "y+", "points": "y"},
            avoid_self=True,
        )

    # Footer with fetch date
    fig.text(
        0.99, 0.01,
        f"Semantic Scholar citation counts fetched {today.isoformat()}",
        ha="right", va="bottom", fontsize=8, color="#666",
    )

    fig.tight_layout()
    fig.savefig(out_path, dpi=170, bbox_inches="tight")
    print(f"  → wrote {out_path.relative_to(REPO_ROOT)}")


def render_plotly(df: pd.DataFrame, out_path: Path, today: dt.date) -> None:
    """Render the interactive Plotly version (self-contained HTML).

    Same encoding as the matplotlib plot — log y, era bands, sc-FM papers
    dark-edged, marker size by raw citation count — but every point carries
    a hover card and the reader can zoom into the dense 2026 cluster instead
    of relying on adjustText to place labels.
    """
    df_plot = df.dropna(subset=["citation_count"]).copy()
    df_plot["cpy_plot"] = df_plot["citations_per_year"].clip(lower=1.0)

    fig = go.Figure()

    # Era bands as vrects, drawn first so points sit on top. The era label
    # is added as a separate annotation — add_vrect's own annotation helper
    # can't take a datetime x range.
    for label, start, end, color in ERAS:
        t0, t1 = pd.Timestamp(start), pd.Timestamp(end)
        fig.add_vrect(
            x0=t0, x1=t1,
            fillcolor=color, opacity=0.5, layer="below", line_width=0,
        )
        fig.add_annotation(
            x=t0 + (t1 - t0) / 2, y=1.0, yref="paper",
            text=label, showarrow=False, yanchor="bottom",
            font=dict(size=11, color="#444"),
        )

    # One trace per category × sc-FM flag so the legend reads by category
    # and the sc-FM papers get the dark edge.
    for cat in CATEGORY_COLOR:
        sub_cat = df_plot[df_plot["category"] == cat]
        if sub_cat.empty:
            continue
        for is_sc in (True, False):
            sub = sub_cat[sub_cat["is_sc_fm"] == is_sc]
            if sub.empty:
                continue
            cites = sub["citation_count"].fillna(0).clip(lower=1)
            sizes = cites ** 0.5 * 2.4 + 9
            fig.add_trace(
                go.Scatter(
                    x=sub["release_dt"],
                    y=sub["cpy_plot"],
                    mode="markers",
                    name=(
                        f"{CATEGORY_LABEL[cat]} — sc-FM"
                        if is_sc
                        else f"{CATEGORY_LABEL[cat]} — adjacent"
                    ),
                    legendgroup=cat,
                    marker=dict(
                        size=sizes,
                        color=CATEGORY_COLOR[cat],
                        opacity=0.9 if is_sc else 0.5,
                        line=dict(
                            color="#111" if is_sc else "#bbb",
                            width=1.8 if is_sc else 0.8,
                        ),
                    ),
                    customdata=sub[
                        ["name", "release_date", "citation_count",
                         "citations_per_year", "category"]
                    ].values,
                    hovertemplate=(
                        "<b>%{customdata[0]}</b><br>"
                        "Released %{customdata[1]}<br>"
                        "Total citations: %{customdata[2]:.0f}<br>"
                        "Citations / year: %{customdata[3]:.1f}<br>"
                        "Category: %{customdata[4]}"
                        "<extra></extra>"
                    ),
                )
            )

    # Persistent labels on the annotate==True papers — but the reader can
    # toggle them off via the legend or just zoom past overlaps.
    annotated = df_plot[df_plot["annotate"]]
    if not annotated.empty:
        fig.add_trace(
            go.Scatter(
                x=annotated["release_dt"],
                y=annotated["cpy_plot"],
                mode="text",
                text=annotated["name"],
                textposition="top center",
                textfont=dict(size=9, color="#222"),
                name="Key-paper labels",
                hoverinfo="skip",
            )
        )

    y_hi = df_plot["cpy_plot"].max() * 4
    fig.update_layout(
        title=dict(
            text=(
                "Foundation models for cell biology — the 2023–2026 arc<br>"
                "<sub>sc-FM papers shown with dark edges; adjacent FM families "
                "(pathology / genomic / protein) shown muted. "
                "Hover for detail, drag to zoom.</sub>"
            ),
            font=dict(size=15),
        ),
        xaxis=dict(
            title="Release date",
            range=["2022-08-01", "2026-06-01"],
            gridcolor="#e6e6e6",
        ),
        yaxis=dict(
            title="Citations per year (Semantic Scholar, log scale)",
            type="log",
            range=[math.log10(0.7), math.log10(y_hi)],
            gridcolor="#e6e6e6",
        ),
        plot_bgcolor="#fafafa",
        paper_bgcolor="white",
        legend=dict(
            title="Paper category",
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#bbb",
            borderwidth=1,
            x=1.01, xanchor="left",
            y=1.0, yanchor="top",
        ),
        margin=dict(l=70, r=210, t=80, b=110),
        height=560,
        annotations=[
            dict(
                text=(
                    "Semantic Scholar citation counts fetched "
                    f"{today.isoformat()}"
                ),
                xref="paper", yref="paper",
                x=1.0, y=-0.18, xanchor="right", yanchor="bottom",
                showarrow=False,
                font=dict(size=10, color="#666"),
            )
        ],
    )

    fig.write_html(
        out_path,
        include_plotlyjs="cdn",
        full_html=True,
        config={"responsive": True, "displaylogo": False},
    )
    print(f"  → wrote {out_path.relative_to(REPO_ROOT)}")


def main() -> int:
    args = parse_args()
    today = dt.date.today()

    papers = load_curated()
    print(f"Curated paper list: {len(papers)} entries")

    if args.no_fetch and CITATIONS_CSV.exists():
        print(f"Using cached CSV: {CITATIONS_CSV.relative_to(REPO_ROOT)}")
        df = pd.read_csv(CITATIONS_CSV)
    else:
        print(f"Fetching citation counts from S2 …")
        df = fetch_citations(papers)
        CITATIONS_CSV.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(CITATIONS_CSV, index=False, quoting=csv.QUOTE_NONNUMERIC)
        print(f"  → wrote {CITATIONS_CSV.relative_to(REPO_ROOT)}")

    df = compute_per_year(df, today)
    missing = df[df["citation_count"].isna()]
    if not missing.empty:
        print(
            f"WARN: {len(missing)} papers have no citation count "
            "(unresolved S2 IDs):"
        )
        for _, r in missing.iterrows():
            print(f"    - {r['name']} ({r['s2_id']})")
        print(
            "  → Add a `manual_cites: <N>` field to those entries in "
            "fm-papers.yaml if you want them on the plot."
        )

    PLOT_PNG.parent.mkdir(parents=True, exist_ok=True)
    render_plot(df, PLOT_PNG, today)
    render_plotly(df, PLOT_HTML, today)
    return 0


if __name__ == "__main__":
    sys.exit(main())
