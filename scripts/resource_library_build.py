"""Render the FM-to-virtual-cells resource library.

Loads `data/resource-library/fm-to-virtual-cells.yaml`, validates every item
against the controlled vocabulary declared at the top of the file, and emits
`docs/talks/fm-to-virtual-cells/resource-library.md`.

The rendered page is a filterable card grid: a row of chips per facet
(kind / status / org-type / region) plus a topic chip rail and a free-text
search box; the JS is vanilla and lives inline.

The YAML doubles as the source for a future export to papermap (items with
`papermap_category:` set on a `kind: paper` row are eligible).
"""

from __future__ import annotations

import html
import json
import pathlib
import sys

import yaml

REPO = pathlib.Path(__file__).resolve().parents[1]
DATA = REPO / "data" / "resource-library" / "fm-to-virtual-cells.yaml"
OUT = REPO / "docs" / "talks" / "fm-to-virtual-cells" / "resource-library.md"


def load() -> dict:
    with DATA.open() as f:
        return yaml.safe_load(f)


def validate(doc: dict) -> None:
    """Fail-fast on any unknown tag — surfaces typos before they hit the page."""
    vocab = doc["vocab"]
    kinds = set(vocab["kind"].keys())
    topics = set(vocab["topics"])
    statuses = set(vocab["status"].keys())
    org_types = set(vocab["org_type"].keys())
    regions = set(vocab["region"].keys())
    pm_cats = set(doc.get("papermap_categories", []))

    seen_ids: set[str] = set()
    errors: list[str] = []
    for i, item in enumerate(doc["items"]):
        loc = f"item #{i} (id={item.get('id', '?')})"
        for required in ("id", "kind", "name"):
            if required not in item:
                errors.append(f"{loc}: missing required field `{required}`")
        if item["id"] in seen_ids:
            errors.append(f"{loc}: duplicate id `{item['id']}`")
        seen_ids.add(item["id"])
        if item["kind"] not in kinds:
            errors.append(f"{loc}: unknown kind `{item['kind']}`")
        for t in item.get("topics", []):
            if t not in topics:
                errors.append(f"{loc}: unknown topic `{t}`")
        s = item.get("status")
        if s and s not in statuses:
            errors.append(f"{loc}: unknown status `{s}`")
        ot = item.get("org_type")
        if ot and ot not in org_types:
            errors.append(f"{loc}: unknown org_type `{ot}`")
        r = item.get("region")
        if r and r not in regions:
            errors.append(f"{loc}: unknown region `{r}`")
        pm = item.get("papermap_category")
        if pm and pm not in pm_cats:
            errors.append(f"{loc}: unknown papermap_category `{pm}`")

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        raise SystemExit(f"\n{len(errors)} validation errors — fix YAML first.")


# ----------------------------------------------------------- card rendering

KIND_LABELS = {
    "paper": "paper",
    "review": "review",
    "commentary": "blog/news",
    "tool": "tool",
    "dataset": "dataset",
    "benchmark": "benchmark",
    "org": "org/lab",
    "event": "event",
    "competition": "competition",
    "move": "move",
    "talk": "talk",
    "person": "person",
}


def _chip(text: str, cls: str = "rl-chip") -> str:
    return f'<span class="{cls}">{html.escape(text)}</span>'


def _card(item: dict) -> str:
    topics = item.get("topics", []) or []
    data = {
        "kind": item["kind"],
        "status": item.get("status", ""),
        "org": item.get("org_type", ""),
        "region": item.get("region", ""),
        "topics": " ".join(topics),
        "search": (
            item["name"]
            + " "
            + str(item.get("authors", ""))
            + " "
            + str(item.get("venue", ""))
            + " "
            + str(item.get("why", ""))
        ).lower(),
    }
    data_attrs = " ".join(
        f'data-{k}="{html.escape(v)}"' for k, v in data.items()
    )
    name_html = html.escape(item["name"])
    if item.get("url"):
        name_html = f'<a href="{html.escape(item["url"])}" target="_blank" rel="noopener">{name_html}</a>'

    meta_parts = []
    if item.get("authors"):
        meta_parts.append(html.escape(str(item["authors"])))
    venue = item.get("venue")
    year = item.get("year")
    if venue and year:
        meta_parts.append(f"{html.escape(str(venue))} · {year}")
    elif venue:
        meta_parts.append(html.escape(str(venue)))
    elif year:
        meta_parts.append(str(year))
    meta = (
        f'<div class="rl-meta">{" — ".join(meta_parts)}</div>' if meta_parts else ""
    )

    why = item.get("why", "")
    why_html = (
        f'<div class="rl-why">{html.escape(why)}</div>' if why else ""
    )

    chips = [_chip(KIND_LABELS.get(item["kind"], item["kind"]), "rl-chip rl-kind")]
    if item.get("status"):
        chips.append(_chip(item["status"], "rl-chip rl-status"))
    if item.get("org_type"):
        chips.append(_chip(item["org_type"], "rl-chip rl-org"))
    if item.get("region"):
        chips.append(_chip(item["region"], "rl-chip rl-region"))
    for t in topics:
        chips.append(_chip(t, "rl-chip rl-topic"))
    if item.get("papermap_category"):
        chips.append(
            _chip(
                f"papermap: {item['papermap_category']}",
                "rl-chip rl-pm",
            )
        )

    source = ""
    if item.get("source"):
        source = f'<div class="rl-source">via {html.escape(item["source"])}</div>'

    return (
        f'<div class="rl-card" {data_attrs}>'
        f'<div class="rl-name">{name_html}</div>'
        f"{meta}"
        f"{why_html}"
        f'<div class="rl-chips">{"".join(chips)}</div>'
        f"{source}"
        f"</div>"
    )


# ----------------------------------------------------------- filter UI

CSS = """
<style>
.rl-controls { display: flex; flex-direction: column; gap: 0.55rem; margin: 1rem 0 1.2rem; }
.rl-controls input[type=text] {
  width: 100%; padding: 0.55rem 0.8rem; border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 6px; font-size: 0.92rem;
  background: var(--md-default-bg-color); color: var(--md-default-fg-color);
}
.rl-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.32rem; }
.rl-row-label { font-size: 0.78rem; color: var(--md-default-fg-color--light); margin-right: 0.4rem; min-width: 4.5rem; text-transform: uppercase; letter-spacing: 0.04em; }
.rl-filter {
  display: inline-block; padding: 0.18rem 0.55rem; border-radius: 11px;
  font-size: 0.78rem; cursor: pointer; user-select: none;
  border: 1px solid var(--md-default-fg-color--lightest);
  background: var(--md-default-bg-color);
}
.rl-filter:hover { border-color: var(--md-accent-fg-color); }
.rl-filter.active {
  background: var(--md-accent-fg-color); color: var(--md-accent-bg-color);
  border-color: var(--md-accent-fg-color);
}
.rl-reset {
  padding: 0.18rem 0.7rem; border-radius: 11px; font-size: 0.78rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  background: transparent; cursor: pointer; color: var(--md-default-fg-color--light);
}
.rl-reset:hover { color: var(--md-accent-fg-color); border-color: var(--md-accent-fg-color); }
.rl-count { font-size: 0.85rem; color: var(--md-default-fg-color--light); margin-bottom: 0.4rem; }
.rl-grid {
  display: grid; gap: 0.85rem;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
}
.rl-card {
  border: 1px solid var(--md-default-fg-color--lightest); border-radius: 8px;
  padding: 0.8rem 0.9rem; display: flex; flex-direction: column; gap: 0.35rem;
  background: var(--md-default-bg-color);
}
.rl-card.hidden { display: none; }
.rl-name { font-weight: 600; font-size: 0.96rem; line-height: 1.25; }
.rl-name a { color: inherit; text-decoration: none; border-bottom: 1px dotted; }
.rl-name a:hover { color: var(--md-accent-fg-color); }
.rl-meta { font-size: 0.8rem; color: var(--md-default-fg-color--light); }
.rl-why { font-size: 0.88rem; line-height: 1.4; }
.rl-chips { display: flex; flex-wrap: wrap; gap: 0.22rem; margin-top: 0.2rem; }
.rl-chip {
  display: inline-block; padding: 0.06rem 0.4rem; border-radius: 9px;
  font-size: 0.72rem; line-height: 1.4;
  background: var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color--light);
}
.rl-chip.rl-kind { background: #e8f1ff; color: #1f4d80; }
.rl-chip.rl-status { background: #f5f0e6; color: #6a4a18; }
.rl-chip.rl-org { background: #eef7ee; color: #235c3a; }
.rl-chip.rl-region { background: #f5e9f1; color: #7a2e63; }
.rl-chip.rl-pm { background: #ffe4d1; color: #8a3a06; }
.rl-source { font-size: 0.72rem; color: var(--md-default-fg-color--light); opacity: 0.7; }
[data-md-color-scheme="slate"] .rl-chip.rl-kind { background: #1b2e44; color: #b0c8e6; }
[data-md-color-scheme="slate"] .rl-chip.rl-status { background: #3a2f17; color: #e0c98e; }
[data-md-color-scheme="slate"] .rl-chip.rl-org { background: #1d3424; color: #a3d2b2; }
[data-md-color-scheme="slate"] .rl-chip.rl-region { background: #3a2333; color: #d9a8c5; }
[data-md-color-scheme="slate"] .rl-chip.rl-pm { background: #3e2515; color: #f0b890; }
</style>
"""


def _filter_row(label: str, dim: str, values: list[str]) -> str:
    chips = "".join(
        f'<span class="rl-filter" data-dim="{dim}" data-val="{html.escape(v)}">{html.escape(v)}</span>'
        for v in values
    )
    return (
        f'<div class="rl-row"><span class="rl-row-label">{label}</span>{chips}</div>'
    )


JS_TEMPLATE = """
<script>
(function() {
  const grid = document.getElementById('rl-grid');
  if (!grid) return;
  const cards = Array.from(grid.querySelectorAll('.rl-card'));
  const filters = Array.from(document.querySelectorAll('.rl-filter'));
  const search = document.getElementById('rl-search');
  const reset = document.getElementById('rl-reset');
  const counter = document.getElementById('rl-count');
  const total = cards.length;

  const active = { kind: new Set(), status: new Set(), org: new Set(), region: new Set(), topic: new Set() };

  function apply() {
    const q = (search.value || '').trim().toLowerCase();
    let shown = 0;
    cards.forEach(card => {
      const k = card.dataset.kind;
      const s = card.dataset.status;
      const o = card.dataset.org;
      const r = card.dataset.region;
      const topics = (card.dataset.topics || '').split(' ').filter(Boolean);
      const text = card.dataset.search || '';
      const passKind = !active.kind.size || active.kind.has(k);
      const passStatus = !active.status.size || active.status.has(s);
      const passOrg = !active.org.size || active.org.has(o);
      const passRegion = !active.region.size || active.region.has(r);
      const passTopic = !active.topic.size || topics.some(t => active.topic.has(t));
      const passText = !q || text.includes(q);
      const ok = passKind && passStatus && passOrg && passRegion && passTopic && passText;
      card.classList.toggle('hidden', !ok);
      if (ok) shown += 1;
    });
    counter.textContent = `Showing ${shown} of ${total}`;
  }

  filters.forEach(el => el.addEventListener('click', () => {
    const dim = el.dataset.dim;
    const val = el.dataset.val;
    const set = active[dim];
    if (!set) return;
    if (set.has(val)) { set.delete(val); el.classList.remove('active'); }
    else { set.add(val); el.classList.add('active'); }
    apply();
  }));

  search.addEventListener('input', apply);
  reset.addEventListener('click', () => {
    filters.forEach(f => f.classList.remove('active'));
    Object.values(active).forEach(s => s.clear());
    search.value = '';
    apply();
  });

  apply();
})();
</script>
"""


# --------------------------------------------------------------- main


def render(doc: dict) -> str:
    items = doc["items"]
    vocab = doc["vocab"]
    title = doc.get("title", "Resource library")
    subtitle = doc.get("subtitle", "")

    used_kinds = sorted(set(i["kind"] for i in items))
    used_statuses = sorted(set(i["status"] for i in items if i.get("status")))
    used_orgs = sorted(set(i["org_type"] for i in items if i.get("org_type")))
    used_regions = sorted(set(i["region"] for i in items if i.get("region")))
    used_topics: set[str] = set()
    for i in items:
        for t in i.get("topics", []) or []:
            used_topics.add(t)
    used_topics_sorted = sorted(used_topics)

    cards = "\n".join(_card(i) for i in items)

    controls = (
        '<div class="rl-controls">'
        '<input id="rl-search" type="text" placeholder="Search names, authors, descriptions…" />'
        f'{_filter_row("Kind", "kind", used_kinds)}'
        f'{_filter_row("Status", "status", used_statuses)}'
        f'{_filter_row("Org", "org", used_orgs)}'
        f'{_filter_row("Region", "region", used_regions)}'
        f'{_filter_row("Topic", "topic", used_topics_sorted)}'
        '<div class="rl-row" style="margin-top:0.2rem"><button id="rl-reset" class="rl-reset">Reset filters</button>'
        f'<span id="rl-count" class="rl-count" style="margin-left:auto">Showing {len(items)} of {len(items)}</span></div>'
        "</div>"
    )

    header = (
        f"# {title}\n\n"
        f"> *{subtitle.strip()}*\n\n"
        f"This is the FM-to-virtual-cells **resource library** — a landscape monitor, not a citation graph. "
        f"It catalogues every paper, tool, lab, dataset, event, competition, blog, and signal we've collected, "
        f"including items that are still just a name with a slide-trail attached. "
        f"For the **citable subgraph** with relations and layout, see the [paper map](paper-map.md); "
        f"for the methods *next door* see [adjacent methods](adjacent-methods/index.md); "
        f"for the one-line model index see the [model glossary](model-glossary.md).\n\n"
        f"**How filtering works.** Each card carries faceted tags (kind / status / org / region / topic). "
        f"Click any chip in the filter bar to narrow. Multiple chips in the same row are OR; rows AND together. "
        f"The search box matches across name, authors, venue, and the why-it-matters line.\n\n"
        f"**Source of truth.** Everything here is generated from "
        f"`data/resource-library/fm-to-virtual-cells.yaml` by `scripts/resource_library_build.py`. "
        f"Add an item to the YAML, rerun the build, and it lands on the page with its tags wired up. "
        f"The YAML is also the export point for [papermap](https://github.com/LiudengZhang/papermap): "
        f"items with `kind: paper` and `papermap_category:` set are export-eligible.\n\n"
    )

    body = (
        CSS
        + "\n"
        + controls
        + '\n<div id="rl-grid" class="rl-grid">\n'
        + cards
        + "\n</div>\n"
        + JS_TEMPLATE
    )

    # tiny "last built" footer
    footer = (
        "\n\n---\n\n"
        f"*{len(items)} items · last built from `{DATA.relative_to(REPO)}`.*\n"
    )
    return header + body + footer


def main() -> None:
    doc = load()
    validate(doc)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(doc))
    print(f"Wrote {OUT.relative_to(REPO)} ({len(doc['items'])} items)")


if __name__ == "__main__":
    main()
