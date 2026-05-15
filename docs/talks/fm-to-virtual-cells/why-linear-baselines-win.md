# Why do single-cell foundation models fail to beat linear baselines?

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). Answers the question someone asks during Act 1 §1.3 when you say "the 2025 reckoning." The short answer: it's not one cause; it's four overlapping ones — and the honest position in May 2026 is that the reckoning has a contrarian voice too.*

## The headline

A linear regression on average post-perturbation expression — *with no training, no fine-tuning, no FM* — is competitive or better than every published single-cell FM on perturbation prediction as originally defined. **Ten independent evaluation papers** have replicated this by May 2026 (see [the catalog](evaluation-papers-catalog.md)).

But the cause isn't simple. Four overlapping explanations have surfaced, plus one contrarian voice and one theoretical framing.

<iframe src="../../assets/fm-four-causes.html" width="100%" height="470" frameborder="0" loading="lazy" title="Why linear baselines win — four overlapping causes"></iframe>

*Interactive — the reckoning decomposed: bar length = independent lines of evidence in the May-2026 literature; colour = whether the cause is structural (scale alone won't fix it), already corrected by the reckoning, or contested by the contrarian voice. Hover any bar for the small-lab track that addresses it.*

## Cause 1: The training objective optimizes the wrong thing

Next-gene-prediction (scGPT) and masked-gene-modeling (Geneformer) optimize *correlation* between adjacent gene tokens. The downstream task — perturbation prediction — asks for *causal counterfactual* prediction: what would expression be if I knocked out gene X? **These are different problems.** Correlation-based pretraining doesn't automatically transfer to causal prediction.

**Evidence**:
- A linear baseline that predicts "the mean of training perturbations" already captures the correlational signal. It's hard to beat because most of the variance in perturbation outcomes is well-explained by the average shift, which is a correlational quantity.
- Geneformer V2-104M_CLcancer (cancer-curated continual pretraining) doesn't improve perturbation prediction over the general model. The improvement is on classification, not on the causal task.

**The track that addresses this**: [Track 2 in the supplementary](../fm-to-virtual-cells-supplementary.md#c2-track-2-new-pretraining-objectives-that-target-causality) — counterfactual pretraining objectives (IRM, contrastive perturbation losses, energy-based causal priors).

## Cause 2: The architecture inherits NLP, not biology

All major sc-FMs (scGPT, Geneformer, UCE, scFoundation, CellPLM) are transformer-based, mostly BERT- or GPT-shaped. The transformer was designed for language — sequential, dense, ordered tokens. **Single-cell transcriptomics is sparse, unordered, and biologically structured** in ways the transformer ignores.

**Evidence**:
- **xVERSE (Jiang & Xie, bioRxiv 2026.04)**: transcriptomics-native FM (non-LM architecture) beats leading sc-FMs by **17.9% on representation, 11.4% on batch correction, 34.3% on spatial imputation**. The architectural choice is empirically load-bearing.
- **[TxPert (Wenkel et al. 2026 *Nat Biotech*)](https://doi.org/10.1038/s41587-026-03113-4)**: uses *multiple knowledge graphs* as the inductive bias for transcriptomic-perturbation prediction. Notable for *who* wrote it — Wenkel co-authored the 2025 `latent-additive` critique (Cause 3 below). **TxPert is the reckoning answering itself**: the critics' own next move was not "abandon FMs" but "give the FM a knowledge-graph prior the transformer lacks."
- **scFoundation**'s read-depth-aware attention is the closest existing sc-FM to architecture–biology co-design — but most of that design space is unexplored.

**The track that addresses this**: [Track 4 in the supplementary](../fm-to-virtual-cells-supplementary.md#c4-track-4-architectures-with-biology-specific-inductive-biases) — graph-attention, pathway priors, lineage-aware encoders.

## Cause 3: The evaluation methodology was systematically biased

The pre-2025 published evaluations had three structural issues:

1. **Splitting on cells, not on perturbations.** Many published evaluations split train/test on cells but kept perturbations shared across splits. The FM only had to interpolate within a perturbation, not extrapolate to a new one. Linear baselines trivially do this.
2. **Reporting averaged metrics over many perturbations.** Mean R² masks the fact that most perturbations have small effects, so "predict the mean" is hard to beat in aggregate even when it has zero signal on the big-effect perturbations the field cares about.
3. **Selective benchmark curation.** Papers chose perturbation datasets where their model did well; a linear baseline was sometimes computed but reported as an afterthought.

**This wasn't fraud** — it was the slow accretion of methodological choices that all individually seemed reasonable but collectively created a false leaderboard.

**Evidence**: the Csendes scPerturBench paper found the original scGPT split was leaky. The Wenkel paper proposed `latent-additive + scGPT-embeddings` as a stronger baseline; it still beats current sc-FMs consistently.

**The track that addresses this**: [Track 6 in the supplementary](../fm-to-virtual-cells-supplementary.md#c6-track-6-causal-evaluation-frameworks-post-ahlmann-eltze) — causal-recovery benchmarks with MR-validated + LINCS L1000 + ENCODE TF-target test sets.

## Cause 4: What sc-FMs actually encode

The 2025–2026 SAE-on-biology-FMs wave (Adams 2025 *PNAS* protein FMs, Simon & Zou 2026 sc-FMs, Hibou-LP 2024 pathology FMs) gives a mechanistic explanation:

- **Sparse autoencoders trained on sc-FM activations recover** *cell-type* and *pathway* features cleanly.
- They **fail to recover** *regulatory* and *causal* features.

In plain English: scGPT and Geneformer know "this is an endothelial cell" and "this is in the apoptosis pathway." They don't know "knocking out TP53 will activate the apoptosis pathway." **The first kind of knowledge is correlational; the second is causal. The reckoning is the discovery that current sc-FMs encode only the first kind.**

**Evidence**:
- Simon & Zou 2026 *arXiv* 2603.02952 — "Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT" — the headline finding matches the reckoning at the *mechanism* level.

**The track that addresses this**: [Track 1 in the supplementary](../fm-to-virtual-cells-supplementary.md#c1-track-1-mechanistic-interpretability) — but the cancer-curated SAE angle is the small-lab differentiator now that the general-domain wave has broken.

## The theoretical framing — causal transportability

**[Virtual Cells Need Context, Not Just Scale (bioRxiv 2026.02.04)](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1)** introduces the cleanest theoretical lens on the reckoning so far:

> The field has a **causal transportability problem** in Pearl's sense. A model trained on distribution P(X | do(Y), Z=z₁) does not automatically predict in P(X | do(Y), Z=z₂) when context Z changes.

In plain English: train an sc-FM on lab-cultured cells, test on patient samples — the predictions don't transfer because the *context* (lab medium, donor demographics, batch effects, technical platform) is different. **This isn't a capacity problem** (more data won't fix it directly); it's a *structural* problem about which causal pathways the model can identify.

**The paper demonstrates** the framework on a 22M-cell immunology SOTA model. It **names** the problem but does **not** give the field a transportability benchmark — that's [Track 9 in the supplementary](../fm-to-virtual-cells-supplementary.md#c9-track-9-causal-transportability-benchmarks-new-2026), the wide-open frontier project.

## The contrarian voice

**[Foundation Models Improve Perturbation Response Prediction (bioRxiv 2026.02.18)](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** argues — directly opposing Ahlmann-Eltze, Liu, the Wu papers, and the parameter-free baseline paper — that **with sufficient data, FMs *do* significantly improve genetic and chemical perturbation predictions, and approach fundamental performance limits**.

The honest position in May 2026: the reckoning is **not a one-sided consensus**. The 10 reckoning papers all evaluated *current scFMs trained on current data with current evals*. The contrarian paper argues that as data scales further (Tahoe-100M and beyond), the picture changes. Citing both is necessary intellectual honesty.

**Why this matters for project selection**: if you bet that the reckoning is permanent, you work on architectural alternatives (xVERSE, Track 4) or on better evaluation (Tracks 3, 6, 8, 9). If you bet the contrarian is right, you work on scaling and on data curation (Lane 3, Lane 5). The pitches in Act 4 of the talk are deliberately neutral on which bet wins.

## The composite answer

**Why do sc-FMs fail to beat linear baselines?** Because:

1. The training objective optimizes correlation (Cause 1), not causality, and the downstream task wants causality.
2. The architecture inherits NLP (Cause 2), not biology. xVERSE 2026 is the first published evidence that architectural choice is empirically load-bearing.
3. The historical evaluations had structural biases (Cause 3) that the 2025 reckoning corrected — but the corrected evaluations also expose Cause 1 and 2.
4. Interpretability work shows sc-FMs encode pathway/cell-type features but not regulatory logic (Cause 4) — a mechanistic explanation of Cause 1.
5. The Pearl framework gives a theoretical name to the failure (causal transportability) — *not capacity-bounded, structural*.

**The contrarian view** says (1–4) may improve with more data, faster than expected.

**The May 2026 honest framing**: it's a paradigm question that's still open, not a settled defeat.

<iframe src="../../assets/fm-cause-track-matrix.html" width="100%" height="560" frameborder="0" loading="lazy" title="Cause × small-lab-track matrix"></iframe>

*Interactive — the bridge from diagnosis to project: rows are the 9 small-lab innovation tracks from [supplementary §C](../fm-to-virtual-cells-supplementary.md#c-track-dossiers-the-9-small-lab-innovation-tracks), columns are the four causes plus the theoretical framing. Every cause has at least one track aimed directly at it. Hover a cell for the track's open problem.*

## Where to go next

- **[The main talk page Act 1](../fm-to-virtual-cells.md#act-1-the-20232026-arc-10-min)** — the chronological narrative of the reckoning.
- **[The evaluation papers catalog](evaluation-papers-catalog.md)** — all 10 reckoning papers + the contrarian + the substrate papers.
- **[Supplementary §C — full track dossiers](../fm-to-virtual-cells-supplementary.md#c-track-dossiers-the-9-small-lab-innovation-tracks)** — the small-lab projects that address each cause above.
- **[Ahlmann-Eltze & Huber 2025 *Nature Methods*](https://www.nature.com/articles/s41592-025-02772-6)** — the canonical reckoning paper.
- **[Virtual Cells Need Context, Not Just Scale](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1)** — the causal-transportability framing.
- **[Foundation Models Improve Perturbation Response Prediction](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** — the contrarian voice.

---

*Last updated 2026-05-13.*
