# How to read a foundation-model paper critically

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). The checklist that turns a 2026 reader from "this model achieved 0.94 AUC" to "did it actually clear the floor?" Reusable beyond this talk — apply to any biology FM paper you encounter.*

## The 8-item checklist

For every FM paper you read in 2026, verify the eight items below before believing the result. If 3+ items fail, treat the result as a hypothesis, not an established finding.

1. **Is a linear baseline reported alongside the FM?**
2. **Is the train/test split on cells, on perturbations, or on donors?**
3. **Were the evaluation metrics averaged or stratified?**
4. **What's the donor / cell-line / tissue diversity of the test set?**
5. **Is compute disclosed (hardware, hours, cost)?**
6. **Is the license open or restrictive — and has it shifted?**
7. **Did the authors compare to the most recent linear-baseline paper?**
8. **Is the SOTA claim on a benchmark someone else maintains?**

## Item 1: Is a linear baseline reported alongside the FM?

**Why it matters**: the 2025 reckoning was the discovery that linear baselines beat every published sc-FM on perturbation prediction. **Post-2025, no sc-FM perturbation claim should be published without a linear baseline alongside it.** If the baseline is absent, the paper is structurally pre-reckoning regardless of submission date.

**What to look for**:

- ✅ **Strong signal**: `latent-additive`, `mean-of-training-perturbations`, ridge regression on cell embeddings, or scGPT-embeddings-fed-to-linear-regression appears as a baseline.
- ⚠️ **Mixed signal**: A "PCA + kNN baseline" is reported but the linear regression isn't. PCA+kNN is a non-trivial baseline but doesn't fully cover the Ahlmann-Eltze trap.
- ❌ **Red flag**: only "scVI" or "Harmony" appears as the comparator. These are pre-FM methods, not the post-2025 baselines.

## Item 2: Is the train/test split on cells, on perturbations, or on donors?

**Why it matters**: the most common pre-2025 mistake was splitting on **cells** while keeping **perturbations** shared across train and test. The FM only had to interpolate within a perturbation, not extrapolate to a new one. Linear baselines trivially do this.

**What to look for**:

- ✅ **Strong**: train and test split on *perturbations* — held-out perturbations the model has never seen.
- ✅ **Stronger**: train and test split on *donors* — held-out donors the FM never trained on (rare; barely measured at scale).
- ✅ **Strongest**: cross-context split — train on healthy donors, test on cancer patients; or train on cell-line X, test on cell-line Y. This is the [Track 9 transportability frontier](../fm-to-virtual-cells-supplementary.md#c9-track-9-causal-transportability-benchmarks-new-2026).
- ❌ **Red flag**: "train/test split was random over cells" — this is the pre-Ahlmann-Eltze trap.

## Item 3: Were the evaluation metrics averaged or stratified?

**Why it matters**: mean R² across many perturbations averages out the cases that matter. Most perturbations have small effects, so "predict the mean" looks good in aggregate even when it has zero signal on the big-effect perturbations the field actually cares about.

**What to look for**:

- ✅ **Strong**: per-perturbation R², histogram of per-perturbation correlations, separate metrics for strong vs weak perturbations.
- ✅ **Stronger**: axis-by-axis breakdown (some perturbations are combinatorial, some are dose-response, some are cell-type-specific). The Wu *Nat Methods* paper sets the standard.
- ❌ **Red flag**: only "Pearson r = 0.78 averaged across all perturbations" — the headline number that hides the failure modes.

## Item 4: What's the donor / cell-line / tissue diversity of the test set?

**Why it matters**: Tahoe-100M is ~50 immortalized cell lines, no patient-derived. CELLxGENE Census is ~70% Anglophone sequencing centers. A model that's great on the training distribution can fail catastrophically on patient samples — the *causal transportability* problem from [Virtual Cells Need Context (2026)](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1).

**What to look for**:

- ✅ **Strong**: the test set includes patient-derived primary cells or organoids the training data didn't see.
- ✅ **Stronger**: cross-donor cohorts (HTAN, AACR-style real-world heterogeneity).
- ⚠️ **Mixed**: "evaluated on a held-out subset of CellxGENE Census" — the diversity inherits the substrate's biases.
- ❌ **Red flag**: "evaluated on K562 + RPE1 cell lines only" — narrow substrate, narrow claim.

## Item 5: Is compute disclosed (hardware, hours, cost)?

**Why it matters**: without disclosure, "scGPT is too expensive to reproduce" and "scGPT is cheap to retrain on your data" can both be argued with equal force. The 50× uncertainty band on scGPT's training cost is the canonical example. **The DISCLOSED / ESTIMATED / UNKNOWN distinction is structurally important.**

**What to look for**:

- ✅ **Strong**: GPU type + count + hours + on-demand cost (e.g., "64× A100 80GB × 4d 8h = 6,656 A100-hours = ~$17k").
- ✅ **Stronger**: total FLOPs disclosed as a single number (ESM-3 = 10²⁴ FLOPs).
- ⚠️ **Mixed**: "trained on TPU v3 with 8 replicas" but no total hours.
- ❌ **Red flag**: "extensive A100 hours" or "on our cluster" — UNKNOWN. Treat with skepticism.

See [What does each FM cost?](what-does-each-fm-cost.md) for the full pattern: disclosure correlates with hardware sponsorship.

## Item 6: Is the license open or restrictive — and has it shifted?

**Why it matters**: a CC-BY-NC license blocks commercial use; HF-gated weights can shift access norms unilaterally (UNI's Jan 2025 gating shift is the cautionary tale). License posture determines who can build downstream products.

**What to look for**:

- ✅ **Strong (permissive)**: MIT, Apache-2.0, CC-BY. Single-cell FMs are mostly here (scGPT, Geneformer, UCE, scFoundation, CellPLM, TranscriptFormer).
- ⚠️ **Restrictive (academic-only)**: CC-BY-NC, often with HF gating. Pathology FMs are mostly here (UNI, Virchow, CHIEF).
- ⚠️ **Tiered**: 1.4B open, 7B/98B gated (ESM-3 pattern).
- ❌ **Red flag**: License has changed since publication (UNI Jan 2025 gating). Check the *current* license card on HF, not the published one.

## Item 7: Did the authors compare to the most recent linear-baseline paper?

**Why it matters**: as of May 2026, **10 evaluation papers** beat the sc-FM perturbation leaderboard. Any new sc-FM paper should engage with at least Ahlmann-Eltze + one of (Wu, Liu, parameter-free, CellBench-LS). If the paper ignores them, it's structurally pre-reckoning.

**What to look for**:

- ✅ **Strong**: directly compares against Ahlmann-Eltze's `mean-of-training-perturbations` and Wenkel's `latent-additive` baselines.
- ✅ **Stronger**: engages with the contrarian voice ([FMs Improve Perturbation, Feb 2026](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)) — argues *for* or *against* it based on this paper's data.
- ⚠️ **Mixed**: cites the reckoning trio in the introduction but doesn't run the baseline.
- ❌ **Red flag**: claims SOTA without citing any of the 2025–2026 evaluation papers.

See [the evaluation papers catalog](evaluation-papers-catalog.md) for the full reckoning corpus.

## Item 8: Is the SOTA claim on a benchmark someone else maintains?

**Why it matters**: pre-2025, papers often introduced their own benchmark *in the same paper as the model* and reported SOTA on it. This is structurally vulnerable to selective benchmark curation. **Post-reckoning, SOTA claims should be on third-party-maintained benchmarks**: PerturBench (Altos), Open Problems v2, scPerturBench (BM2 Lab), Tahoe-100M.

**What to look for**:

- ✅ **Strong**: the SOTA claim is on PerturBench / Open Problems v2 / scPerturBench / sc-Arena — a benchmark the authors don't maintain.
- ✅ **Stronger**: the paper includes results on the Campanella 2025 *Nat Communications* multi-task pathology panel (for pathology FMs).
- ⚠️ **Mixed**: SOTA on a new dataset the authors introduce, with the dataset framed as a contribution.
- ❌ **Red flag**: SOTA on a benchmark introduced in the same paper, with no third-party validation.

## Bonus item: Are the authors NVIDIA-co-authored?

**Why this is worth checking** (but is a soft signal, not a red flag): every fully-disclosed biology FM as of May 2026 has NVIDIA / DGX-Cloud / TPU partnership disclosure. This is structural — disclosure is a co-marketing artifact, not a random virtue. The implication: NVIDIA-co-authored papers tend to be more reproducible *but* also tend to be the frontier-compute papers (Evo2, ESM-3, AlphaGenome) that academic labs cannot directly compete with on training scale.

When you read a NVIDIA-co-authored paper, the question shifts from "is the compute disclosed?" (yes, by construction) to "is the recipe portable, or does it depend on DGX-Cloud-specific tooling?"

## The synthesis: a 30-second triage

If you have 30 seconds to triage a new FM paper:

1. **Read the methods section** for "linear baseline" or "Ahlmann-Eltze." Absent → skip.
2. **Read the train/test split description**. If it says "cells" without specifying "perturbation-held-out" → skip.
3. **Find the compute disclosure**. If it says "extensive" without numbers → flag as UNKNOWN.

If all three pass, the paper is worth a deeper read.

## What this checklist enables for *writing*

If you're writing an FM paper in 2026, the checklist tells you what reviewers will check. The bar is now:

- **Linear baseline + held-out perturbation/donor split** are not optional.
- **Per-perturbation + averaged metrics** both reported.
- **Compute disclosed** even if the result wasn't a frontier run.
- **License + benchmark choice** made explicitly defensible.

The [Lane 4 (negative results / replication) playbook in the talk](../fm-to-virtual-cells.md#31-the-9-application-lanes-budget-tier-overview) is exactly the inverse of this checklist: take a published FM that fails any of items 1–8 and re-evaluate it under the proper protocol. *Nature Methods* takes those papers.

## Where to go next

- **[The main talk page](../fm-to-virtual-cells.md)** — full 5-act outline.
- **[Why do linear baselines win?](why-linear-baselines-win.md)** — the mechanism behind the checklist.
- **[Evaluation papers catalog](evaluation-papers-catalog.md)** — the 10 critique papers + contrarian.
- **[Supplementary §B.4 — Lane 4 negative results / replication / critique](../fm-to-virtual-cells-supplementary.md#b4-lane-4-negative-results-replication-critique-02k)** — how to ship a paper that applies this checklist.

---

*Last updated 2026-05-13.*
