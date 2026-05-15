# From Foundation Models to Virtual Cells

> **The operational definition** *(what the field has actually built, May 2026)*: **a virtual cell is a perturbation-prediction model based on zero-shot foundation models.** That's the implementation. The broader [Bunne 2024 *Cell* "world-model-of-a-cell" vision](https://www.cell.com/cell/fulltext/S0092-8674(24)01332-1) is the aspiration. **The gap between the two is the talk.**

## TL;DR

Foundation models have arrived in biology but they are **not yet virtual cells**. In 2025, an evaluation wave (Ahlmann-Eltze, Kedzierska, Wenkel, Wu, Liu, parameter-free, PertEval-scFM, CellBench-LS, Han et al., cellular-dynamics — ten papers by May 2026) showed that scGPT / Geneformer / UCE / scFoundation fail to beat linear baselines on perturbation prediction and most cell-level tasks. The reckoning has a contrarian voice (FMs Improve Perturbation, Feb 2026) and a theoretical underpinning (Virtual Cells Need Context, Feb 2026 — frames it as a causal transportability problem). The 2026 response is architectural (xVERSE, transcriptomics-native), generative + cross-species (TranscriptFormer, CZ Biohub *Science*), agentic (rBio, VCHarness), and compositional (Theis *Cell Systems*).

This talk maps that arc, then asks: **what can a small lab do in this era?** 9 application lanes + 9 innovation tracks + 3 concrete project pitches sized for one PhD student over 12 months.

## How to use this page

The page is the **speaker's running order** for a 60-min group meeting. The five acts:

- **[Act 1](#act-1-the-20232026-arc-10-min)** (10 min) — the chronological narrative, anchored by [the interactive citation scatter plot](assets/fm-citation-plot.html)
- **[Act 2](#act-2-todays-landscape-5-min)** (5 min) — the five FM families + institutional landscape today
- **[Act 3](#act-3-what-you-can-do-15-min)** (15 min) — the 9 lanes and 9 tracks for small-lab work
- **[Act 4](#act-4-commercial-reality-group-decision-10-min)** (10 min) — who pays, three pitches, group conversation
- **[Act 5](#act-5-close-3-min)** (3 min) — AACR 2026 as the live evaluation surface

For prep depth — the 11 model dossiers, per-lane and per-track 12-month projects, the 37-paper 2026 updates catalog, ~110-reference reading list, institute dossiers, Q&A scripts — see **[the supplementary page](fm-to-virtual-cells-supplementary.md)**.

---

## Act 1. The 2023–2026 arc (10 min)

### 1.1 The thesis

A virtual cell, as the field has actually built it, is **a perturbation-prediction model based on zero-shot foundation models**. The broader vision — a queryable computational system that predicts and simulates cellular function across modalities and scales ([Bunne et al. 2024 *Cell*](https://www.cell.com/cell/fulltext/S0092-8674(24)01332-1)) — is the aspiration. **The gap between the two is the field's most concrete research agenda.**

### 1.2 The citation arc — one slide

<iframe src="../assets/fm-citation-plot.html" width="100%" height="580" frameborder="0" loading="lazy" title="Foundation models for cell biology: the 2023–2026 citation arc"></iframe>

*Interactive — hover any point for the paper detail, drag to zoom into the dense 2026 cluster, click a legend entry to toggle a category. sc-FM-related papers shown with dark edges; adjacent FM families (pathology / genomic / protein) shown muted. Citation counts from Semantic Scholar. Log y-axis so the 2026 newborns (0–2 citations) and the 2023 anchors (300–620 citations / year) both fit on one view. Static fallback for print/PDF: [fm-citation-plot.png](assets/fm-citation-plot.png).*

### 1.3 The four eras

<iframe src="../assets/fm-arc-timeline.html" width="100%" height="420" frameborder="0" loading="lazy" title="The 2023–2026 arc — three interleaved swimlanes"></iframe>

*Interactive — the four eras as three swimlanes on one time axis: sc-FM releases, the reckoning corpus, and the framing-and-agentic response. The point of the layout: the architecture critiques land **while** the next-generation models ship — the arc is interleaved, not sequential. Hover any marker.*

**2023 paradigm — scBERT, scGPT, Geneformer.** The field's gravity wells. scGPT (~440 cit/yr) and Geneformer (~310 cit/yr) define what an sc-FM looks like: transformer architecture imported from NLP, masked-gene-modeling or rank-based tokenization, atlas pretraining on CELLxGENE Census.

**2024 ambition — the Arc Institute Virtual Cell Challenge, the Bunne *Cell* perspective, CZ Biohub announcement, Tahoe-100M.** The field commits to a goal: build virtual cells. UCE adds cross-species (8 species via ESM2). scFoundation adds read-depth-aware attention. CellPLM moves to cell-as-token. The pathology FMs (UNI, Virchow, CHIEF, Prov-GigaPath) arrive as a parallel family.

**2025 reckoning — the linear baseline wins.** Ahlmann-Eltze & Huber *Nat Methods* shows scGPT / Geneformer / UCE / scFoundation fail to beat a one-line linear baseline on perturbation prediction. Kedzierska *Genome Biology* extends to zero-shot. Wenkel proposes `latent-additive`. Wu *Nat Methods* confirms at 27-method scale. Liu *Adv Sci* generalizes past perturbation to most cell-level tasks. By the end of 2025, **ten independent evaluation papers** establish: current scFMs don't yet earn their compute against simple baselines.

**2026 response — four positions.** The field forks into:

1. **The reckoning canon (10 papers).** Linear baselines beat sc-FMs on perturbation prediction and most cell-level tasks.
2. **The contrarian voice ([FMs Improve Perturbation, bioRxiv 2026.02](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)).** With sufficient data, FMs *do* improve perturbation prediction and approach fundamental performance limits.
3. **The theoretical underpinning ([Virtual Cells Need Context, bioRxiv 2026.02](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1)).** The failure is a *causal transportability problem* (Pearl framework) — structural, not capacity-bounded.
4. **The architectural response.** [xVERSE](https://www.biorxiv.org/content/10.64898/2026.04.12.718016v1) (transcriptomics-native, +17.9% representation, +34.3% spatial imputation over LM-derived sc-FMs); [TranscriptFormer](https://www.science.org/doi/10.1126/science.aec8514) (generative cross-species, 112M cells × 12 species × 1.53B years of evolution); [TxPert (Wenkel et al. 2026 *Nat Biotech*)](https://doi.org/10.1038/s41587-026-03113-4) — multiple-knowledge-graph perturbation prediction, and notably **the reckoning answering itself**: Wenkel co-authored the 2025 `latent-additive` critique; [Theis *Cell Systems*](https://www.cell.com/cell-systems/abstract/S2405-4712(26)00016-5) (compositional FMs — stop training bigger monolithic sc-FMs, start composing modality-specific FMs); [rBio](https://virtualcellmodels.cziscience.com/model/rbio) + [VCHarness](https://www.biorxiv.org/content/10.64898/2026.04.11.717183v1) + [CellVoyager](https://doi.org/10.1038/s41592-026-03029-6) (agentic ↔ virtual-cell convergence — reasons / builds / analyzes).

<iframe src="../assets/fm-reckoning-corpus.html" width="100%" height="560" frameborder="0" loading="lazy" title="The 2025 reckoning becomes a corpus — 12 evaluation papers"></iframe>

*Interactive — the cumulative step line shows the reckoning hardening into a 12-paper corpus across 2024–2026; colour marks the evaluation axis each paper opened; the green ✕ below the axis is the contrarian voice. Hover any point for venue + headline.*

<iframe src="../assets/fm-lineage-tree.html" width="100%" height="580" frameborder="0" loading="lazy" title="Foundation-model lineage — NLP origin to the 2026 architectural response"></iframe>

*Interactive — the four eras as a lineage: the Gen-1 sc-FMs inherited the NLP transformer, lost to a linear baseline, and the 2026 response fixes the causes (edge colour = which cause it addresses). Hover any node for detail.*

→ Going deeper on the reckoning: [why do linear baselines win?](fm-to-virtual-cells/why-linear-baselines-win.md) (the four causes) · [the evaluation papers catalog](fm-to-virtual-cells/evaluation-papers-catalog.md) (the full corpus) · [the paper map](fm-to-virtual-cells/paper-map.md) (the literature as an interactive network + reading order).

### 1.4 Glossary — eight terms this talk leans on

| Term | Operational meaning in this talk |
|---|---|
| **Foundation model (FM)** | A neural network pretrained on a large, general substrate that can be adapted (fine-tuned, prompted, or used as a frozen encoder) to many downstream tasks. |
| **Virtual cell** | (Operational) A perturbation-prediction model based on a zero-shot foundation model. (Aspirational) A computational system predicting cellular function across modalities + scales. |
| **Zero-shot / few-shot** | Zero-shot = run pretrained model on a new task with no labeled examples. Few-shot = handful of labeled examples. The benchmark that exposed the 2025 crisis was zero-shot perturbation prediction. |
| **Linear baseline** | The simplest possible predictor (linear regression / ridge / `latent-additive`) used as a sanity floor. Ahlmann-Eltze 2025 showed every published sc-FM fails to beat this floor on perturbation prediction. |
| **Causal transportability** | Pearl/Bareinboim framework: when a model trained on context Z=z₁ predicts in context Z=z₂. The diagnosis the 2026 theoretical wave (Virtual Cells Need Context) gives to the reckoning. |
| **In-context learning (ICL)** | Few-shot prediction via examples in the prompt, without weight updates. Demonstrated for Evo2 on DNA; not yet for sc-FMs at scale. |
| **PEFT / LoRA / adapter** | Parameter-efficient fine-tuning. Tiny (<1% of params) module on top of frozen FM weights. Lane 2. |
| **Sparse autoencoder (SAE)** | Interpretability method: a sparse dictionary over an FM's residual stream that recovers human-readable features. The 2025–2026 wave (Adams *PNAS*, Simon & Zou) applied this to biology FMs. |

---

## Act 2. Today's landscape (5 min)

### 2.1 Five FM families — one slide each

| Family | Anchor models | 2026 SOTA | Status |
|---|---|---|---|
| **Single-cell** | scGPT, Geneformer, UCE, scFoundation, CellPLM, **TranscriptFormer**, xVERSE | Geneformer V2-104M_CLcancer ties scGPT at ⅓ compute; TranscriptFormer leads on cross-species; **no sc-FM beats `latent-additive + scGPT-embeddings` on perturbation** | **In crisis** — re-evaluating what perturbation prediction means |
| **Pathology** | UNI / UNI2-h, Virchow / Virchow2, CHIEF, Prov-GigaPath, CONCH, PathChat, **TITAN, mSTAR, GPFM, PathOrchestra** | Virchow2 first on Campanella 2025 panel; UNI tied for second; PathChat DX = first FDA Breakthrough Designation for generative-AI pathology | **Healthiest family** — plateauing around ViT-H/14 + 200M tiles |
| **Genomic** | Nucleotide Transformer, DNABERT-2, HyenaDNA, AlphaGenome, Evo2 | AlphaGenome wins 25/26 regulatory variant-effect benchmarks; Evo2 retains generative + ICL territory AlphaGenome cannot match | **Split** — track-prediction and generative are distinct sub-families |
| **Protein** | ESM-2 / ESM-3, AlphaFold3, Proteina Complexa, RFdiffusion | ESM-3 for generative (98B params, esmGFP de novo); AlphaFold3 for structure (multimodal: proteins + DNA + RNA + ligands) | **Maturing fast** — Proteina Complexa hits 63.5% wet-lab hit rate on PDGFR binders |
| **Multimodal / vision-language** | BioMedCLIP, PathChat / PathChat-2, MedAgentGym, MMedAgent-RL | PathChat-2 (>1M instruction pairs); PathChat DX FDA Breakthrough Jan 2025 | **Closest to clinical deployment** |

Cross-link: [What is a foundation model?](fm-to-virtual-cells/what-is-a-foundation-model.md) · [the model glossary](fm-to-virtual-cells/model-glossary.md) · [Foundation Models cross-vault index](../foundation-models.md) · [supplementary §A — full model dossiers](fm-to-virtual-cells-supplementary.md#a-model-dossiers-the-11-anchor-models).

**Per-task winners for sc-FMs** — what each model actually wins on, and where they all still lose. The "SOTA" row above flattens a more interesting picture:

| Task | Best 2026 model | Margin over linear baseline |
|---|---|---|
| Cell-type classification (Tabula Sapiens, scTab) | Geneformer V2-104M_CLcancer | +2–4 pts macro-F1 over scGPT; ties 316M at ⅓ compute |
| Batch integration / atlas alignment | scVI **still competitive** | ≤1 pt FM lift; depends on metric |
| Cross-species cell-state alignment | **TranscriptFormer** (12 species), then UCE (8) | Positive; first credible cross-species story |
| **Zero-shot perturbation prediction** | **`latent-additive + scGPT-embeddings`** linear baseline — **no FM beats it consistently** | 0; floor is the ceiling |
| Spatial-transcriptomics integration | Nicheformer / OmniCell / SpatialFusion | Very early; no settled benchmark |

### 2.2 Who builds what — the institutional landscape

| Tier | Institute / Lab | Ships | Why they matter |
|---|---|---|---|
| **Academic FM builders** | Arc Institute (Hsu + Goodarzi) | Evo2, STATE, Tahoe-100M | Largest non-DeepMind compute (2,048× H100); sets the perturbation-atlas substrate |
| | Mahmood Lab (Harvard / BWH / MGB) | UNI, UNI2-h, CONCH, PathChat, PathChat-DX, TITAN, CHIEF | Full pathology vertical stack; PathChat-DX = first FDA Breakthrough for generative-AI pathology |
| | Theodoris Lab (Gladstone / UCSF) | Geneformer V1 / V2 / V2-CLcancer | Only academic sc-FM lab with full NVIDIA BioNeMo compute disclosure (~$17k recipe) |
| | Bo Wang Lab (Toronto / Vector / UHN) | scGPT, scGPT-spatial, MedSAM | Defined the sc-FM category |
| | Leskovec + Quake (Stanford / SNAP) | UCE | Cross-species (8 species via ESM2-bridge) |
| **Industrial FM builders** | Google DeepMind | AlphaGenome, AlphaFold 2/3, Med-Gemini | TPU-scale; non-commercial license; Isomorphic Labs commercial arm |
| | EvolutionaryScale | ESM-3 (1.4B / 7B / 98B) | Cleanest published FLOPs disclosure in biology FM (10²⁴) |
| | Paige + MSK | Virchow / Virchow2 / Virchow2G, FullFocus | First FDA 510(k)-cleared general-purpose pathology AI (Jan 2025) |
| | Owkin | Phikon, Phikon-v2, H-optimus-0, MOSAIC | Only major industrial pathology player shipping open weights |
| | NVIDIA BioNeMo | Framework + Geneformer V2 recipe; Evo2 co-author | Sets the compute-disclosure norm as co-marketing artifact |
| **Funders + models** | **CZ Biohub + CZI** (revised 2026) | CELLxGENE Census, Tabula Sapiens, **TranscriptFormer, rBio** | **Now ships both substrate AND model.** Breaks the 2024 "substrate-only" stereotype. |
| **2026 emergence** | BioMap Research + MBZUAI | VCHarness | China/Middle-East-side competitor to CZ Biohub stack |
| **Critique anchors** | Ahlmann-Eltze + Huber (EMBL); Kedzierska + Lu (Oxford / MSR); Theis Lab (Helmholtz Munich) | (multiple) | Without these, Act 1 §1.3 reckoning doesn't exist |

→ See [supplementary §F](fm-to-virtual-cells-supplementary.md#f-institutional-landscape) for the extended 15-institute dossiers with disclosure norms and strategic moves.

<iframe src="../assets/fm-institutional-landscape.html" width="100%" height="560" frameborder="0" loading="lazy" title="The institutional landscape — who builds FMs vs who audits them"></iframe>

*Interactive — the same institutes placed by FM-building activity (x) vs evaluation/critique activity (y): most sit bottom-right (build, don't audit) or top-left (audit, don't build), and only CZ Biohub and the Theis Lab sit near the "does both" diagonal. Axes are a qualitative reading of supplementary §F — a speaker's judgement, not a measured metric. Hover for what each ships.*

### 2.3 What's still missing — the 5-gap framework

These are the gaps that, if closed, would let "foundation model" and "virtual cell" reasonably coexist. Each is a research agenda you can frame talks, grants, or papers around — and each maps cleanly to the small-lab playbook in Act 3.

| Gap | What's broken | The 2026 lens |
|---|---|---|
| **5.1 Donor diversity** | Tahoe-100M ≈ 50 immortalized cell lines, no patient-derived; CELLxGENE ~70% Anglophone sequencing centers | Cross-donor generalization not systematically benchmarked because the data doesn't exist at scale |
| **5.2 Cross-species** | Most sc-FMs human-only. UCE (8 species) and TranscriptFormer (12 species) are exceptions, but cancer cross-species transfer is unbenchmarked | Open question: does cross-species pretraining hurt within-species, or help via shared regulatory grammar? |
| **5.3 Causal vs correlational** | Next-gene-prediction + masked-gene-modeling optimize correlation. That's structurally why FMs lose to linear baselines on perturbation. | Pearl/Bareinboim causal-transportability framework (Virtual Cells Need Context 2026) is the new theoretical lens |
| **5.4 Compute asymmetry** | Evo2 + ESM-3 = >$7M of the ~$15M total identified FM training spend across 14 models; concentrated at ~5 institutions | Academic single-cell labs cannot directly compete on training scale |
| **5.5 Evaluation honesty** | 10 critique papers by May 2026; the "scFMs beat baselines" narrative was an artifact of biased train/test splits, averaged metrics, and selective benchmark curation | Each new sc-FM claim must clear the linear floor first; reviewers know to ask |

<iframe src="../assets/fm-compute-landscape.html" width="100%" height="580" frameborder="0" loading="lazy" title="The compute landscape — params vs training cost, and the linear baseline"></iframe>

*Interactive — gap 5.4 made visual: training cost spans ~$250 to ~$5M across four FM families; filled markers are cost-disclosed, open markers estimated (bars show the band). The red star is the parameter-free linear baseline that beats every sc-FM on perturbation prediction. Hover for the source.*

### 2.4 The 5 gaps × 9 lanes × 9 tracks matrix

The connective tissue between "what's broken" and "what we'd work on." Vertical reading: pick a gap → see how to contribute. Horizontal reading: pick a project → see which gap it closes.

| Gap | Apply via Act 3 lane | Innovate via Act 3 track |
|---|---|---|
| 5.1 Donor diversity | Lane 7 — application on under-represented cohort; Lane 8 — synthetic augmentation for rare cohorts | Track 4 — donor-conditioning priors; Track 9 — transportability with donor-split |
| 5.2 Cross-species | Lane 3 — domain FM on non-human-cell corpus | **Track 7 — cross-species transfer / phylogenetic priors** (post-TranscriptFormer); Track 4 — cross-species equivariance |
| 5.3 Causal vs correlational | Lane 4 — linear-baseline audit; Lane 9 — active-learning targets causal direction | Track 2 — causality-targeting pretraining; Track 6 — causal benchmarks; **Track 9 — causal transportability** |
| 5.4 Compute asymmetry | Lane 6 — wrapper democratizes access; Lane 8 — synthetic data reduces wet-lab cost | Track 1 — interpretability tells us what the compute bought |
| 5.5 Evaluation honesty | Lane 5 — benchmark curation; Lane 4 — replication catalog (now 11 papers) | Track 3 — compositional benchmarks; Track 6 — causal benchmarks; **Track 8 — synergistic-info evaluation; Track 9 — transportability** |

→ See [supplementary §G](fm-to-virtual-cells-supplementary.md#g-cross-references) for the per-cell exemplar paper in this matrix.

---

## Act 3. What you can do (15 min)

> §3 priced the frontier: $20k (Geneformer V2-104M_CLcancer, the cheapest fully-disclosed model) to $5M+ (Evo2, ESM-3). The middle does not exist as a *training* tier. So if your lab cannot pretrain, the right question is: **what kind of FM-area contribution is publishable at <$5k?**
>
> Two parallel menus: **9 lanes** for *applying* existing FMs, **9 tracks** for *innovating* on FMs. Each has real 2023–2026 exemplars. Lanes 8–9 and Tracks 7–9 are net-new in 2026.

### 3.1 The 9 application lanes — budget tier overview

| Lane | Typical $ | Compute | Time | Risk |
|---|---|---|---|---|
| 1. FM embeddings as features | $0–$500 | inference-only, 1× consumer GPU | weeks | low |
| 2. PEFT / LoRA / adapters | $500–$5k | 1–8× A100 for days | 2–4 mo | medium |
| 3. Domain-specific small FM | $10k–$50k | 8–64× A100 ~1 week | 6–12 mo | medium-high |
| 4. Negative results / replication | $0–$2k | inference + linear regression | 3–6 mo | low scientifically |
| 5. Benchmark / dataset curation | $0–$5k + curator time | de minimis | 6–18 mo | low |
| 6. FM-wrapper tools / pipelines | $0–$5k | dev box + inference for tests | 6–12 mo | low (adoption is the risk) |
| 7. FM-aided wet-lab / clinical study | $5k–$50k FM-side | mostly inference | 12–24 mo | low (FM side) |
| **8. FM as generative data-augmentation engine** *(new 2026)* | $0–$2k | inference + small classifier | 3–6 mo | medium (synthetic-data bias) |
| **9. FM-aided experimental design / active learning** *(new 2026)* | $1k–$10k FM-side | inference per iteration | 12–18 mo | medium (wet-lab partner) |

**One-sentence lane summaries** (full prose in [supplementary §B](fm-to-virtual-cells-supplementary.md#b-lane-dossiers-the-9-small-lab-application-lanes)):

1. **Lane 1** — frozen UNI2-h / scGPT embeddings → attention-MIL → clinical readout. AACR 2026 #5470 / #1441 / #2758 all use this pattern. **Win**: clinical relevance at zero pretraining cost.
2. **Lane 2** — <1% trainable adapter on top of frozen scGPT/Geneformer/UNI2. Inherits $250k of pretraining; you contribute the adapter. **Win**: zero-shot generalization to unseen drugs / cell lines.
3. **Lane 3** — continual-pretrain a smaller model on your domain corpus. Geneformer V2-104M_CLcancer ($20k) matches the 316M general model at ⅓ params. **Win**: domain curation beats scale.
4. **Lane 4** — replicate a published FM claim against a linear baseline. **Lane 4 is the most-published lane of 2025–2026** (11 papers). To differentiate in 2026, target an uncovered axis: donor-split, cross-tissue, time-resolved, cancer-line→primary, rare-cohort robustness.
5. **Lane 5** — curate a held-out split or new benchmark dataset. Replogle, Open Problems, HEST-1k are the patterns. **Win**: your dataset becomes infrastructure every subsequent model cites.
6. **Lane 6** — wrap a popular FM in a tool your audience can't run themselves (Bioconductor / scverse / browser-native). signifinder, SpatialData, CytoVerse. **Win**: adoption-driven citations.
7. **Lane 7** — use a frozen FM as instrumentation in a clinical or wet-lab study. **Janowczyk 2025 *Nat Med*** is the first deployment-grade exemplar (UNI for EGFR detection, 43% genetic-testing avoidance). Pairs with Track 5 (UQ) for regulatory-grade.
8. **Lane 8** *(new 2026)* — use a generative FM (xVERSE, TranscriptFormer) to synthesize labeled training cells for rare cohorts. **xVERSE resolves rare cell types with as few as 4 cells**. Caveat: held-out *real* test set required to prevent synthetic-bias leakage.
9. **Lane 9** *(new 2026)* — FM-guided experimental-design loop. CRADLE-VAE, scPRINT, VCHarness, rBio. **Win**: the pattern AI-native biotechs (Recursion, Insitro, Vevo) actually pay for.

<iframe src="../assets/fm-lanes-map.html" width="100%" height="560" frameborder="0" loading="lazy" title="The 9 application lanes — cost vs time-to-result"></iframe>

*Interactive — the budget table above as a 2-D map: horizontal position is typical project cost (bars show the range), vertical is months to first result, colour is project risk. Hover any bubble for the one-line summary and the win.*

#### Decision tree — which lane is yours?

```
Do you have wet-lab/clinical data the FM authors did not see?
├── YES → Lane 7 (FM-aided application).
└── NO
    │
    Do you have a wet-lab partner who runs perturbation screens?
    ├── YES → Lane 9 (FM-aided active learning).
    └── NO
        │
        Do you have a rare-cohort scRNA-seq dataset (<500 cells)?
        ├── YES → Lane 8 (FM as data-augmentation engine).
        └── NO
            │
            Do you have a curated dataset or held-out split no public benchmark uses?
            ├── YES → Lane 5 (benchmark / dataset).
            └── NO
                │
                Can you write a model adapter / LoRA layer in PyTorch?
                ├── YES → Lane 2 (PEFT).
                └── NO
                    │
                    Do you have ~$10k of cloud credit + a domain corpus?
                    ├── YES → Lane 3 (domain FM).
                    └── NO
                        │
                        Strong R/Python/Bioconductor maintainer?
                        ├── YES → Lane 6 (wrapper tool).
                        └── NO
                            │
                            Default → Lane 1 (embeddings) OR Lane 4 (replication).
```

#### Combination plays — the AACR-corpus observation

The single most consistent pattern in the AACR 2026 corpus is that the *highest-impact* posters combine **two** lanes:

| Combination | What it means | Why it wins |
|---|---|---|
| Lane 1 + Lane 5 | Frozen embeddings on a held-out / curated dataset | The dataset is the contribution; the FM is the off-the-shelf tool |
| Lane 1 + Lane 7 | Frozen embeddings → clinical readout | Clinical relevance + zero pretraining cost |
| Lane 4 + Lane 6 | Replicate then ship a Bioc/scverse package | Methods paper + adoption pathway in one project |
| **Lane 7 + Track 5** | Clinical FM application + post-hoc UQ wrapper | Regulatory-grade; clinical-AI vendors write the check |
| Lane 8 + Lane 3 | Synthetic-data augmentation → domain-specific FM | Rare-cohort feasibility unlocked at <$5k total |
| Lane 9 + Lane 5 | Active learning + benchmark contribution | The benchmark *is* the active-learning evaluation |

### 3.2 The 9 innovation tracks — frontier methods at <$10k compute

| Track | Open problem | Compute |
|---|---|---|
| 1. Mechanistic interpretability of biology FMs | What do scGPT/Geneformer/UNI actually learn? | <$2k |
| 2. New pretraining objectives that target causality | Next-gene-prediction optimizes correlation — that's *why* FMs lose to linear baselines | $5–20k |
| 3. Compositional generalization benchmarks + theory | Does A+B generalize when model saw only A and B? | <$2k |
| 4. Architectures with biology-specific inductive biases | BERT clones ignore pathway / network / lineage priors | $5–15k |
| 5. Uncertainty / OOD detection for clinical-grade FMs | Every FDA path needs calibrated uncertainty; FMs don't have it | $1–5k |
| 6. Causal evaluation frameworks | What's the *correct* test for causality, post-Ahlmann-Eltze? | <$3k |
| **7. Cross-species transfer / phylogenetic priors** *(new 2026)* | Does cross-species pretraining help or hurt for cancer biology? | <$2k |
| **8. Synergistic-information evaluation of multimodal FMs** *(new 2026)* | Which fusion strategies actually buy cross-modal info vs being redundant? | <$2k |
| **9. Causal transportability benchmarks** *(new 2026)* | What's the right test for cross-context generalization, post-VCsNC? | <$3k |

**One-sentence track summaries** (full prose in [supplementary §C](fm-to-virtual-cells-supplementary.md#c-track-dossiers-the-9-small-lab-innovation-tracks)):

1. **Track 1** — train SAEs on a *cancer-curated* sc-FM (Geneformer V2-104M_CLcancer); compare features vs general-domain. SAE wave broke 2025–2026 but cancer-specific angle is open.
2. **Track 2** — design counterfactual pretraining objectives (IRM, contrastive perturbation). The objective, not the architecture, is misaligned.
3. **Track 3** — formal compositional benchmark on Norman + Replogle; theoretical lower bound on additive baseline.
4. **Track 4** — biology-specific inductive biases (graph-attention on StringDB / Reactome). **xVERSE** (transcriptomics-native) and **MAP** (knowledge-driven) are the 2026 exemplars; "all sc-FMs are scGPT-shaped" is out of date.
5. **Track 5** — post-hoc UQ on frozen UNI2-h / Virchow2 (deep ensembles, MC dropout, Laplace, conformal). **No published clinical-grade UQ for pathology FMs as of May 2026.**
6. **Track 6** — causal-recovery benchmark with MR-validated + LINCS L1000 + ENCODE TF-target test sets.
7. **Track 7** *(new)* — cancer cross-species sc-FM benchmark on paired mouse + human tumors. TranscriptFormer weights open; no published cancer cross-species sc-FM benchmark.
8. **Track 8** *(new)* — apply Microsoft's [SIS metric](https://www.biorxiv.org/content/10.64898/2026.02.23.707420v3) across scGPT-spatial / Nicheformer / OmniCell / CLM-X / CELLama / SpatialFusion. The cleanest weekend-compute paper of 2026.
9. **Track 9** *(new)* — operationalize the [Virtual Cells Need Context](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1) causal-transportability framework into a multi-context benchmark suite. **First paper that lands owns the post-reckoning evaluation citation for 3–5 years.**

#### The unifying frame (30 sec)

**The bottleneck on every track above is intellectual, not financial.** Big labs spend $5M+ on bigger models; the small lab's edge is in:

- **Interpretability** (Track 1) — nobody is doing the work
- **Better objectives** (Track 2) — better objective beats more compute, repeatedly
- **Better benchmarks** (Tracks 3, 6, 8, 9) — what you measure shapes what gets built; SIS + transportability are the post-2026 frontier
- **Better priors** (Track 4) — biology's structure isn't in transformer attention
- **Calibration** (Track 5) — clinical deployment needs it; FMs don't have it
- **Phylogenetic / cross-species priors** (Track 7) — TranscriptFormer made this concrete; cancer cross-species is unexplored

**The one-liner**: the virtual-cell vision won't be solved by scaling existing FMs. It'll be solved by someone who builds the right *evaluation framework* (Tracks 3, 6, 8, 9), the right *causal objective* (Track 2), the right *interpretability tools* (Track 1), and the right *cross-context generalization theory* (Tracks 7, 9) — and that someone could be in your lab.

---

## Act 4. Commercial reality + group decision (10 min)

> The Act 3 inventory was the academic landscape. The Act 4 question is fundability: *who would sponsor, license, or acquire this work?* The commercial money chases regulatory-grade methods (UQ, interpretability, causal evaluation) and clinical-grade applications — not another scGPT clone.

### 4.1 The three buyer archetypes

| Archetype | Named players (2026) | What they buy from academia | Typical funding |
|---|---|---|---|
| **A. Big pharma — drug discovery / target ID** | Lilly, AstraZeneca, Pfizer, Novartis, Roche/Genentech, BMS, Merck, Sanofi | target-ID validation, FMs for cell painting / phenotypic screens, biomarker discovery for trial enrichment, regulatory-grade UQ | sponsored research $100k–$2M, talent pipeline, postdoc-funded internships |
| **B. AI-native biotech / discovery platforms** | Recursion, Insitro, Isomorphic Labs (Alphabet), Owkin, Latent Labs, Vevo / Arc, Cellarity, BenchSci | licensable FM weights, dataset-curation partnerships, methods that improve internal models, acquisitions | sponsored research $50–200k, co-authored papers, dataset access, equity-for-IP |
| **C. Clinical-AI / pathology-AI vendors** | PathAI, Paige (FullFocus FDA-cleared), Tempus AI, Aignostics, Proscia, **Modella AI (→ AstraZeneca)**, Roche Tissue Diagnostics | clinical-grade UQ, pathology FM weights, FDA-pathway-ready interpretability, sponsored validation studies | sponsored validation $100–500k, co-marketing, acquisitions |

**Pharma (A) buys de-risked science; AI-native biotech (B) buys methods that move their leaderboard; clinical-AI vendors (C) buy regulatory ammunition.** The audience for your paper is one of these three — pick before you start writing.

### 4.2 The 2024–2026 commercial signals timeline

The money pattern: **2024 = platform launches; 2025 = FDA pathway proofs; 2026 = acquisitions + infrastructure commitments.**

| Date | Event | Why it matters |
|---|---|---|
| Jun 2024 | Tempus AI IPO (NYSE) | First multimodal-clinical-AI public listing |
| Aug 2024 | Recursion + Exscientia merger | Largest cell-painting + generative-design consolidation |
| Dec 2024 | CZ Biohub Virtual Cell program | Multi-billion-dollar non-dilutive commitment |
| **Jan 2025** | **Paige FullFocus FDA 510(k) clearance** | First general-purpose pathology AI cleared by FDA |
| **Jan 2025** | **PathChat DX FDA Breakthrough Device Designation** | First generative-AI pathology tool to win Breakthrough |
| Feb 2025 | Arc + Vevo release Tahoe-100M | Largest perturbation atlas; substrate competitors must compete with |
| 2025 | Latent Labs founded | DeepMind alumni virtual-cell startup; venture-grade signal |
| **Jan 12, 2026 (JPM Day 1)** | **Lilly + NVIDIA $1B AI Co-Innovation Lab** | Largest pharma–AI infrastructure commitment ever announced at JPM |
| **Jan 13, 2026 (JPM Day 2)** | **AstraZeneca acquires Modella AI** | **First big-pharma acquisition of an AI firm.** Partnership-→-ownership shift |
| Jan 14, 2026 | Pfizer: "embed AI across the business" | Buyer-side commitment broader than any single deal |
| Apr 17–22, 2026 | **AACR 2026 ED03 + AT02 + 4/22 Oncologist sessions** | First AACR with FM/agentic-AI on main program — buyer-meets-builder venue |

**The line**: *the academic field had its discipline crisis in 2025 (Ahlmann-Eltze); the commercial field had its acquisition wave in 2026 (Modella → AstraZeneca, Lilly + NVIDIA). Those happened in the same six months. That's the climate we're choosing a project in.*

### 4.3 The three pitches × buyer map

| Pitch | Lane × Track | Compute | Time | Primary buyer | Output |
|---|---|---|---|---|---|
| **A — Pathology FM interpretability + clinical UQ** | Lane 7 + Track 1 + Track 5 | <$3k | 12 mo | C (clinical-AI: Paige, PathAI, Tempus, Modella → AstraZeneca) | NeurIPS Mech-Interp + *Nat Methods* Resource + AACR poster |
| **B — Compositional perturb benchmark + linear-baseline re-audit (cancer)** | Lane 4 + Track 3 | <$2k | 8 mo | B (AI-native biotech: Recursion, Insitro, Latent, Vevo) | NeurIPS D&B + *Nat Methods* |
| **C — Rare-cancer FM-aided subtyping + small domain FM** | Lane 7 + Lane 3 | <$25k | 18–24 mo | A (pharma rare-disease: Pfizer, Sanofi, AZ, Vertex) | AACR poster + *Clin Cancer Res* + *Nat Methods* |

**Pitch A — Pathology FM interpretability + clinical UQ.** Take UNI2-h (or Virchow2, license-dependent), train sparse autoencoders on its residual-stream activations over a TCGA slice, cluster features and map them to histology grammar (tumor regions, stromal compartments, immune infiltrate). Layer a post-hoc Bayesian or conformal-prediction head; evaluate calibration on TCGA → CPTAC distribution shift. **Why us**: builds on existing TCGA familiarity; no wet-lab required.

**Pitch B — Compositional perturbation benchmark + linear-baseline re-audit on cancer perturb-seq.** Rebuild scGPT + Geneformer + UCE evaluation pipelines on Norman 2019 + Replogle 2022 + Tahoe-100M with cancer-specific cell-line subsets. Add Ahlmann-Eltze linear baseline + Wenkel `latent-additive`. Design a formal compositional split (A+B held out when A and B seen separately); prove a theoretical lower bound on additivity. **Why us**: leverages the AACR-corpus context; cancer-specific findings differentiating.

**Pitch C — FM-aided rare-cancer subtyping + small domain FM.** Pick a rare-cancer cohort the public pathology-FM training corpora missed (rhabdomyosarcoma, ATC, NET, mesothelioma). Year 1: publish a frozen-encoder application paper (like AACR #2758 PAX3/7::FOXO1 in rhabdomyosarcoma — Lane 7). Year 2: continual-pretrain a Geneformer-V2-104M-style domain FM on the cohort's matched scRNA-seq. **Why us**: most defensible if we have a clinical collaborator with a rare-cancer cohort.

### 4.4 Decision questions for the group

**Strengths**

- Which of the five FM families is closest to existing group expertise?
- Of the 11 anchor models, which two could anyone here actually rederive on a whiteboard?
- Do we have any in-house data the public FM training corpora *didn't* see (rare cohort, novel modality, new tissue type)?

**Constraints**

- Real cloud / on-prem GPU budget per year for FM work specifically?
- Any postdoc / PhD-student bandwidth that could be 50%-allocated to one of these for 12 months?
- Wet-lab or clinical collaborators we'd need to recruit for Pitch C?

**Strategic**

- Which is more valuable for our PI's tenure / grant story — *applied paper in a clinical venue* (Pitch C Year 1) or *methods paper in a top ML venue* (Pitches A or B)?
- Are we trying to attract ML talent (Pitches A/B do this) or clinical talent (Pitch C does this)?
- 6-month-output project (Pitch B replication) or 18-month-output project (Pitch C subtype FM)?

**Tactical**

- Of the three pitches, who would lead each? Who would co-author?
- Can we run TWO in parallel — one applied (Pitch C Year 1) + one methods (Pitch A or B)?
- What's the no-go signal that tells us to drop a pitch at month 3?

### 4.5 The honest framing

The talk's Act 1 thesis: *the gap between FMs and virtual cells is the most concrete research agenda single-cell biology has had in a decade*. Act 3 Track-side specifies the gap. Act 3 Lane-side specifies the work that's adjacent enough to be safe. **The right project for this group is one lane plus one track, run in parallel, so we publish a low-risk applied paper while a higher-risk methods paper develops.**

---

## Act 5. Close (3 min)

> The conferences are not where you *see* FMs in biology — they are the *evaluation surface*. Methods conferences (NeurIPS / ICLR / ICML) tell you what works on benchmarks; clinical conferences (AACR / ASCO / ESMO) tell you what works on cancer. AACR 2026 — Apr 17–22, the week before ICLR — is the live case study.

### 5.1 The two-track timeline

| Year | Methods conferences / journals | Clinical / industry signal |
|---|---|---|
| 2023 | scGPT, Geneformer, UNI submitted | — |
| 2024 | UCE, scFoundation, AlphaFold3, Virchow, CHIEF | **Bunne et al. *Cell*** coins the virtual-cell thesis |
| **Dec 2024** | — | **CZI announces Virtual Cell Program** |
| **Jan 2025** | — | **PathChat DX FDA Breakthrough** |
| **Feb 2025** | — | **Arc + Vevo release Tahoe-100M** |
| 2025 | **The reckoning** — Ahlmann-Eltze + Kedzierska + Wenkel + Wu | Virchow2 wins Campanella et al. clinical benchmark |
| **2026 Q1** | **The response** — TranscriptFormer (*Science*); Theis *Cell Systems*; Virtual Cells Need Context; FMs Improve Perturbation; xVERSE; VCHarness | **JPM 2026**: Lilly + NVIDIA $1B; AstraZeneca acquires Modella AI |
| Apr 2026 | ICLR 2026 (Apr 23–27, Rio) | **AACR 2026 (Apr 17–22, Chicago)** — first AACR with dedicated FM + agentic-AI sessions |

**The visual punchline**: *the clinical track is one year behind the methods track on awareness, and one year ahead on accountability. The reckoning didn't come from ICLR — it came from *Nature Methods*. The deployment bar isn't being set by NeurIPS — it's being set by the FDA.*

### 5.2 "Virtual X" is forking — cell → embryo → organ

The "virtual cell" agenda is no longer the only scale. As of mid-2026 it has visibly forked into three:

- **Virtual cell** — this talk. Perturbation prediction on zero-shot FMs.
- **Virtual embryo** — [Cao, Lu & Qiu 2026 *Nat Methods*](https://www.nature.com/articles/s41592-026-03055-4): integrate single-cell + spatial data to model mammalian embryogenesis across scales.
- **Virtual organ** — [Zhou et al. 2026 *Nat Biotech*](https://doi.org/10.1038/s41587-026-03121-4): digital twins of ex vivo human lungs for personalized therapeutic-efficacy evaluation; and [computational generation of high-content digital organs at single-cell resolution (*Nat Methods* 2025)](https://www.nature.com/articles/s41592-025-02996-6) — a 38M-cell mouse-brain virtual atlas from sparse spatial transcriptomics.

Each scale has different evaluation constraints — a virtual organ can be validated against ex vivo therapeutic response in a way a virtual cell cannot. The takeaway for project selection: **the "virtual cell" reckoning is cell-scale-specific; the embryo- and organ-scale tracks have not had their reckoning yet, which makes them either an opportunity or a warning depending on whether you think the cell-scale lessons transfer.**

### 5.3 AACR 2026 as the case study

The corpus from this site ([aacr-2026.pages.dev](https://aacr-2026.pages.dev/conferences/aacr-2026/)): **25 unique sessions, ~464,000 words of transcripts, 2,241 poster abstracts (~871,000 words)** — organized into five axes: agentic AI, single-cell/spatial, virtual cells, bioinfo/AI methods, clinical trials.

Three things AACR 2026 gives us that ICLR/NeurIPS structurally cannot:

1. **The deployment reality check — [ED03 "Foundation Models and Multimodal AI for Cancer Research"](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/sessions/2026-04-17-pm-foundation-models-multimodal-ai-cancer-research/) (Fri Apr 17)** with **Bunne / Yeung-Levy / Moor**. Bunne wrote the 2024 virtual-cell perspective. The field's first AACR-stage definitional panel — not "does our model beat a benchmark," but "what does deployment even mean here?"
2. **The donor-diversity stress test — [single-cell & spatial track](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/single-cell-spatial-omics/)** (20 sessions, 1,015 posters). ML conferences evaluate FMs on synthetic perturb-seq splits; AACR is where the actual heterogeneity surface lives. **§5.1 donor-diversity gap either shows up here loudly, or it doesn't.**
3. **The agentic-AI-for-discovery proof — [AT02 "Agentic AI as the Cancer Researcher" (Tue Apr 21)](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/sessions/2026-04-21-at02-agentic-ai-cancer-researcher/) + ["Agentic AI as the Oncologist" (Wed Apr 22)](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/sessions/2026-04-22-agentic-ai-as-the-oncologist/)**. ICLR 2026 gave us MedAgentGym (72k task sandbox); AACR gives us *the actual research and clinical workflows*. Two sessions in one week is a deliberate field statement.

### 5.4 What we knew before → what AACR 2026 changes

| The five gaps | What we knew before AACR 2026 | What AACR 2026 lets us answer |
|---|---|---|
| **Donor diversity** | sc-FMs trained on CELLxGENE Census, donor-skewed | Do AACR spatial/HTAN posters show real heterogeneity coverage, or the same skew? |
| **Cross-species** | Mouse-only models still dominate; TranscriptFormer is the exception | 1,015 single-cell/spatial posters are mostly human-patient — first real-population test |
| **Causal vs correlational** | sc-Arena, PerturBench show benchmark concerns; Virtual Cells Need Context names the causal-transport framing | AT02 + ED03 are the first venues where agentic AI is asked to *propose interventions* |
| **Compute access** | Evo2 + ESM-3 = >$7M of ~$15M total identified FM training spend | Is academic single-cell FM work competitive at AACR, or do industry-trained models dominate? |
| **Honest evaluation** | 10 critique papers + the contrarian voice (Feb 2026) | Does AACR 2026 cite the linear-baseline papers in FM-using posters, or quietly ignore them? |

**The closing line**: *the talk's thesis was that the gap between FMs and virtual cells is the field's most concrete research agenda. The corpus on this site is one way to track whether the field is actually closing that gap, conference by conference.*

---

## Companion resources

### Explainer pages

Each explainer answers one question someone asks during the talk. They are reachable from the top nav, or jump straight in:

- **[What is a foundation model?](fm-to-virtual-cells/what-is-a-foundation-model.md)** — the definition and the five-families taxonomy (Act 2).
- **[The model glossary](fm-to-virtual-cells/model-glossary.md)** — every FM and virtual cell named in the talk, one sentence each.
- **[What does each FM cost?](fm-to-virtual-cells/what-does-each-fm-cost.md)** — the compute-disclosure landscape (Act 2, gap 5.4).
- **[How agentic AI meets foundation models](fm-to-virtual-cells/agentic-meets-foundation.md)** — the four agentic ↔ FM patterns (Act 1 §1.3, Act 5).
- **[Why do linear baselines win?](fm-to-virtual-cells/why-linear-baselines-win.md)** — the four causes behind the 2025 reckoning (Act 1 §1.3).
- **[Reading an FM paper critically](fm-to-virtual-cells/reading-an-fm-paper-critically.md)** — the 8-item checklist (Act 3).
- **[The evaluation papers catalog](fm-to-virtual-cells/evaluation-papers-catalog.md)** — the full reckoning corpus (Act 1 §1.3).
- **[The paper map](fm-to-virtual-cells/paper-map.md)** — the literature as an interactive network + a systematic reading order.
- **[Adjacent Methods — the catalog](fm-to-virtual-cells/adjacent-methods/index.md)** — ~55 non-FM algorithm, benchmark, and methodology papers next to the talk's topic.
- **[The resource library](fm-to-virtual-cells/resource-library.md)** — the landscape monitor: ~250 items (papers, tools, labs, datasets, events, money moves, blogs) with faceted filters across kind / status / org / region / topic.

### Deep references

- **[Supplementary — long-form companion](fm-to-virtual-cells-supplementary.md)** — table-first deep dives: 11 model dossiers, 9 lane-by-lane projects, 9 track-by-track projects, compute matrix, 12-paper evaluation catalog, 15-institute landscape, ~110-reference reading list, 37-paper 2026 updates, Q&A scripts, timing cheat sheet.
- **[`_resources-matrix.md`](_resources-matrix.md)** — full compute / cost / team / data matrix with arithmetic and DISCLOSED / ESTIMATED / UNKNOWN tags.
- **[Foundation Models](../foundation-models.md)** — cross-vault FM index.
- **[90-min Speed Read](../speed-read.md)** — abbreviated overview.
- **[2026 Timeline](https://liudengzhang.github.io/conference-vaults/timeline/)** — Gantt of 36 conferences.

---

*Last updated: 2026-05-13. The page reflects the May 2026 state: 11 anchor models, the 10-paper reckoning canon, the Feb 2026 contrarian + theoretical wave, and the architectural response (TranscriptFormer, xVERSE, compositional FMs, agentic ↔ virtual-cell bidirectional convergence). For prep depth, the supplementary page is the book of tables.*
