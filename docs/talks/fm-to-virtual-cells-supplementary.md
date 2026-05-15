# FM to Virtual Cells — Supplementary

> Long-form companion to [the talk page](fm-to-virtual-cells.md). The talk page is the speaker's outline (~700 lines, slides + tables + decision trees). This page is the *book of tables* — what you read the night before the talk, what you look up mid-prep, what you cite from the talk's footnotes.
>
> Eight load-bearing tables, each followed by the prose dossier that explains its rows. Appendix carryover at the end (Q&A scripts, datasets, ~110-reference reading list, timing cheat sheet, 2026 updates catalog).

**Last updated:** 2026-05-13. Field status reflects the May 2026 state.

---

## §A. Model dossiers — the 11 anchor models

The master comparison table. Each row links to its detailed dossier below. The columns are the 5 questions every FM should answer; the rows are the 11 models the talk uses as exemplars. For a flat one-sentence-each glossary of *every* model named in the talk corpus — not just these 11 — see [the model glossary](fm-to-virtual-cells/model-glossary.md).

| # | Model | Family | Params | Compute disclosed? | Public weights | The one thing it's best at | Where it breaks |
|---|---|---|---|---|---|---|---|
| A.1 | **scGPT** | single-cell | 51M | ❌ UNKNOWN (50× uncertainty band) | ✅ MIT | First sc-FM with gene + cell as tokens; defined the category | Zero-shot perturbation prediction fails vs linear baseline |
| A.2 | **Geneformer V2** | single-cell | 104M / 316M | ✅ DISCLOSED ($17k V2-104M) | ✅ Apache-2.0 (HF) | Domain-curated 104M beats general 316M at ⅓ compute — kills "scale wins" | Same perturbation-prediction gap as scGPT |
| A.3 | **UCE** | single-cell | 650M | ❌ UNKNOWN | ✅ MIT | Cross-species (8 species via ESM2 protein-embedding bridge) | Cross-species gain is positive but small; least transparent on cost |
| A.4 | **STATE** | single-cell (virtual cell) | 600M SE + ST | ❌ UNKNOWN (~$125k est.) | ✅ open weights | First production virtual cell at Tahoe-100M scale | No online-update loop; you re-train to add perturbations |
| A.5 | **TranscriptFormer** | single-cell (cross-species generative) | 100M+ | ⚠️ partial | ✅ open weights | First generative cross-species sc-FM; 112M cells × 12 species × 1.53B years of evolution | Cancer-specific evaluation not published; SOTA on healthy tissues only |
| A.6 | **Generative Virtual Cells** | single-cell (POC) | tiny | ✅ <$250 | ✅ MIT | The *design pattern*: joint planner + world model with validation gating | A workshop POC, not a deployed model; scaling unproven |
| A.7 | **Virchow2** | pathology | 632M / 1.85B | ✅ DISCLOSED (512× V100, ~$170k) | ⚠️ CC-BY-NC | Most transparent pathology FM; current SOTA on Campanella 2025 panel | Lead over UNI2-h is ≤2 pts; ViT-H/14 + 200M tiles plateauing |
| A.8 | **UNI2-h** | pathology | 681M | ❌ UNKNOWN (~$75k est.) | ⚠️ CC-BY-NC + HF-gated since Jan 2025 | Full vertical stack: tile encoder → slide → vision-language → retrieval | License-shift risk realized; opaque training cost |
| A.9 | **AlphaGenome** | genomic | ~450M | ⚠️ partial (TPU only) | ⚠️ non-commercial (source Jan 2026) | Single model wins 25/26 regulatory variant-effect benchmarks at 1-Mb context | Can't do in-context learning; non-commercial license blocks industry |
| A.10 | **Evo2** | genomic | 7B / 40B | ✅ DISCLOSED (2,048× H100, ~$5M) | ✅ Apache-2.0 | Only genomic FM with demonstrated ICL; 1M-token context | $5M training cost concentrates capability at ~5 institutions |
| A.11 | **ESM-3** | protein (multimodal) | 1.4B / 7B / 98B | ✅ DISCLOSED (1.07 × 10²⁴ FLOPs) | ⚠️ 1.4B open, 7B/98B gated | Cleanest compute disclosure in biology FMs; generated esmGFP de novo | esmGFP is one anecdote; wet-lab validation at scale is rare |

**Two patterns the table makes visible:** (1) **Disclosure correlates with hardware sponsorship** — every ✅ DISCLOSED model has an NVIDIA / DGX-Cloud / TPU partnership. (2) **License posture is bifurcating** — sc-FMs uniformly permissive (MIT/Apache); pathology uniformly restrictive (CC-BY-NC + gating); genomic split (Evo2 open, AlphaGenome closed).

### A.1 scGPT (Cui et al. *Nature Methods* 2024)

The single-cell FM that defined the category.

- **Resources** — ~51M params; 33M cells from CellxGene Census; **GPU compute: UNKNOWN — Cui 2024 does not disclose**; **ESTIMATED ~10³–10⁵ A100-hours** (a 50× uncertainty band); **cost $2.6k–$250k [ESTIMATED]**. Team: Bo Wang lab, U. Toronto + Vector Institute / Haotian Cui.
- **Framework** — encoder-decoder transformer. Gene tokens + cell-state tokens. Masked-value-prediction pretraining objective.
- **Unique** — first single-cell FM with both **gene** and **cell** as tokens, enabling cross-cell and cross-gene attention.
- **Gap exposed** — scGPT's zero-shot perturbation predictions don't beat `mean-of-training-perturbations` baselines (Ahlmann-Eltze & Huber 2025). The architectural achievement did *not* translate to perturbation generalization. The 50× uncertainty band on training cost makes "scGPT is expensive to reproduce" claims unverifiable.

### A.2 Geneformer V2 (HuggingFace, Dec 2024 update of Theodoris et al. *Nature* 2023)

The model that inverted the scale-wins narrative — and the cleanest compute disclosure in single-cell FM space.

- **Resources** — V2-104M: 104M params, 104M-cell base + 14M cancer cells continual (CLcancer). **DISCLOSED via NVIDIA BioNeMo: 64× A100 80GB × 4d 8h = 6,656 A100-hours = ~$17k on-demand.** V2-316M: 128× A100 × 3d 19h = 11,576 A100-hours. Team: Theodoris lab, Gladstone Institutes / UCSF.
- **Framework** — encoder-only BERT. Rank-based tokenization (cells become ordered gene lists, ranked by relative expression). MLM objective.
- **Unique** — **rank-based tokenization** sidesteps the normalization problem entirely.
- **Gap exposed** — V2-104M_CLcancer matches the 316M general-domain model at one-third the compute cost. **Scale does not win; domain-curated pretraining does.** V2-104M is the **only single-cell FM in this matrix where the full training cost is publicly costable**.

### A.3 UCE — Universal Cell Embedding (Rosen et al. bioRxiv 2023 → *Nature Methods* 2024)

The cross-species single-cell FM.

- **Resources** — 650M params; 33 transformer layers; ~36M cells × 8 species (Integrated Mega-scale Atlas; ESM2-tokenized via protein-sequence embeddings); **GPU compute: UNKNOWN**; **ESTIMATED ~7 × 10⁴ A100-hours upper, ~1,275 floor**; **cost $3k–$175k [ESTIMATED]**. Team: Leskovec + Quake labs, Stanford.
- **Framework** — encoder-only ViT-style transformer. Gene-set tokenization mapped across species via orthology (ESM2 protein embeddings as the cross-species bridge). Self-supervised contrastive objective.
- **Unique** — **species-agnostic via protein-language embeddings**. First sc-FM that handles 8 species in one embedding space.
- **Gap exposed** — Cross-species transfer is positive but small in magnitude. UCE is the largest published sc-FM at 650M params but also the *least* transparent on training cost.

### A.4 STATE (Arc Institute, 2025)

The Tahoe-100M-native virtual cell.

- **Resources** — Two interlocking modules: **State Embedding (SE-600M)** at 600M params trained on 167M observational human cells; **State Transition (ST)** at undisclosed params trained on 100M+ perturbed cells (Tahoe-100M + Parse + Replogle); **GPU compute: UNKNOWN**; **cost UNKNOWN** (order-of-magnitude ~$125k). Team: Arc Institute (Hsu + Goodarzi labs). [Adduri et al. bioRxiv 2025.06.26.661135](https://www.biorxiv.org/content/10.1101/2025.06.26.661135v1).
- **Framework** — bidirectional transformer with self-attention over **sets of cells**. SE learns observational embedding; ST predicts perturbation transitions. Trained offline on frozen snapshots.
- **Unique** — **first production-grade virtual-cell model at Tahoe-100M scale**.
- **Gap exposed** — STATE is *trained on the snapshot*; **no online-update or active-learning loop** in the published version. Arc's disclosure pattern (data scale foregrounded, compute buried) is structural.

### A.5 TranscriptFormer (Pearce et al. *Science* 2025, CZ Biohub)

The first generative cross-species sc-FM. **The model that turns CZ Biohub from a substrate-only lab into a model-shipping lab.**

- **Resources** — 100M+ params; 112M cells × 12 species spanning 1.53B years of evolution. Open weights (Apache-2.0). Team: CZ Biohub Pearce et al. [Science 2025](https://www.science.org/doi/10.1126/science.aec8514) · [GitHub](https://github.com/czi-ai/transcriptformer) · [bioRxiv 2025.04.25](https://www.biorxiv.org/content/10.1101/2025.04.25.650731v1).
- **Framework** — generative transformer; joint generation over gene tokens with phylogenetic conditioning.
- **Unique** — **first generative cross-species sc-FM**. SOTA on cross-species cell-type classification (incl. species separated by 685M years) and zero-shot disease-state ID in human cells.
- **Gap exposed** — Cancer-specific evaluation is unpublished. The published validation is on developmental, immune, and neural tissues. Track 7 (§C.7) — cancer cross-species — is the open project this model unlocks. Breaks the §3.11 "substrate vs model split" observation that was true through mid-2025.

### A.6 Generative Virtual Cells (Lewis & Zueco, ICLR 2026 Gen² Workshop)

The methods paper proposing closed-loop virtual cells. **Position paper, not a frontier training run.**

- **Resources** — small MLP/transformer trained on a toy Perturb-seq simulator. **<$250 compute. <100 GPU-hours total.** Team: AIXC Research / Lewis & Zueco.
- **Framework** — joint planner + world model trained with validation gating.
- **Unique** — **jointly updated** under validation feedback, not offline-trained on a frozen snapshot. The contribution is the **design pattern**.
- **Gap exposed** — Workshop POC, not deployed; validation feedback assumes cheap high-throughput experiments. The gap between $250 workshop POC and $5M Evo2-scale model is enormous.

### A.7 Virchow2 (Paige + MSK, Zimmermann et al. arXiv 2408.00738)

The current pathology FM SOTA — and **the most transparent pathology FM on hardware**.

- **Resources** — 632M-param ViT-H/14; 3.1M WSIs / ~225,000 patients / ~2B tiles / ~200 tissue types. **DISCLOSED: 512× NVIDIA V100 32GB, batch 4,096, AdamW.** **ESTIMATED ~1.4 × 10⁵ V100-hours = ~$170k.** Virchow2G (1.85B) on same fleet. Team: Paige + MSK / Eric Zimmermann (V2), Eugene Vorontsov (V1).
- **Framework** — DINOv2 self-supervised pretraining on mixed-magnification 224×224 H&E (V2 adds IHC) tiles; attention-pooling for slide-level aggregation.
- **Unique** — **dual transparency: hardware count + patient-level provenance**.
- **Gap exposed** — Lead over UNI2-h is small (~1–2 points). **The pathology FM curve appears to be plateauing around ViT-H/14 + 200M tiles.**

### A.8 UNI2-h (Mahmood lab, Jan 14 2025 update of Chen et al. *Nature Medicine* 2024)

The Mahmood-stack flagship — and the **opaque counterpoint to Virchow2**.

- **Resources** — 681M-param ViT-H/14; 200M+ tiles across 350K+ WSIs (H&E + IHC). **GPU compute: UNKNOWN** ("extensive A100 hours" in HF card). **ESTIMATED ~3 × 10⁴ A100-hours = ~$75k**. HF gated since Jan 2025. Team: Mahmood Lab, Harvard/MGB.
- **Framework** — DINOv2 on histology tiles. Companion models: TITAN (slide-level), PathChat / PathChat-2 (vision-language), SlideSeek (retrieval).
- **Unique** — **full vertical stack**. PathChat DX = first generative-AI pathology tool with FDA Breakthrough Designation (Jan 2025).
- **Gap exposed** — Two compounding gaps: opaque training cost (can't argue scaling vs curation) + license-shift risk realized via Jan 2025 HF gating.

### A.9 AlphaGenome (DeepMind, Avsec et al. *Nature* 2025)

The current genomic FM SOTA on variant effects.

- **Resources** — ~450M params [VENDOR-ASSERTED]; ENCODE + GTEx + FANTOM5 + 4DN across 5,930 human + 1,128 mouse tracks; 1-Mb input windows. **DISCLOSED hardware: 8× TPU v3 per replica with sequence parallelism.** **Total TPU-hours UNKNOWN.** **ESTIMATED ~$200k** ($46k/fold × 4-fold ensemble + distillation). Source code released Jan 2026; non-commercial license. Team: Google DeepMind / Žiga Avsec.
- **Framework** — U-Net + transformer bottleneck. 1-Mb input window. Multi-track output prediction simultaneously.
- **Unique** — **single-model multi-track prediction at 1-Mb context**. Replaces Enformer + Borzoi + Splam etc.
- **Gap exposed** — Cannot do in-context learning. The **non-commercial license** is the binding industry constraint, not compute.

### A.10 Evo2 (Arc Institute + NVIDIA + Stanford + UCB + UCSF, Brixi et al. *Nature* 2026)

The generative + ICL genomic FM. **Second-most-expensive biology FM publicly trained.**

- **Resources** — 7B and 40B params; **OpenGenome2: 8.8T tokens (~9.3B bp) from 100,000 species**. **DISCLOSED: 2,048× NVIDIA H100 on DGX Cloud (AWS), several months.** **ESTIMATED ~2 × 10⁶ H100-hours = ~$5M.** Discloses FLOPs ratio: "~150× more compute than AlphaFold, ~2× the FLOPs of ESM-3" — the cleanest cross-model compute comparison in 2025-2026 biology. Open weights (Apache-2.0). Team: Arc + NVIDIA + Stanford + Berkeley + UCSF / Garyk Brixi.
- **Framework** — StripedHyena 2 (hybrid state-space + attention). Byte-level (single-nucleotide) tokenization. Causal LM objective. 1M-token context.
- **Unique** — **only genomic FM with demonstrated in-context learning**.
- **Gap exposed** — Prompt-engineering is ad-hoc; **no systematic prompt-template benchmark for biological FMs**. The 2,048-H100 fleet is **only available to ~5 institutions worldwide**.

### A.11 ESM-3 (EvolutionaryScale, Hayes et al. *Science* 2025)

The 98B-param multimodal protein FM. **Sets the floor for "frontier biology FM compute" at 10²⁴ FLOPs.**

- **Resources** — 98B params largest (also 1.4B / 7B); **2.78B proteins, 771B unique tokens; 1.07 × 10²⁴ FLOPs DISCLOSED**. **ESTIMATED ~9.9 × 10⁵ H100-hours; cost ~$2.5M–$8M**. Team: EvolutionaryScale / Thomas Hayes. 1.4B open under Cambrian NC; 7B/98B Forge-API-gated.
- **Framework** — multimodal generative transformer with **7 token tracks**: sequence + 3D coordinates + structure tokens (4,096-codebook VQ-VAE) + SS8 + SASA + function keywords + InterPro annotations.
- **Unique** — **multimodal generation + cleanest compute disclosure**. Generated **esmGFP** *de novo* (36% identical to avGFP / equivalent to ~500M years of evolution).
- **Gap exposed** — esmGFP is one anecdote. The 1.4B open variant is what most academic reproductions use — the 98B weights are gated.

---

## §B. Lane dossiers — the 9 small-lab application lanes

How a small lab can ship FM-area work without a $5M GPU budget. Lanes 8–9 are net-new in 2026 (opened by xVERSE / TranscriptFormer / VCHarness).

| Lane | Typical $ | Compute | Time | Risk | 2-3 exemplars | Top venues |
|---|---|---|---|---|---|---|
| **B.1** Embeddings as features | $0–$500 | inference-only, 1× consumer GPU | weeks | low | AACR #5470 UNI2-h+MIL HER2; AACR #1441 UNI2-h+CLAM prostate; AACR #2758 UNI2-h+ABMIL rhabdo | *Cancer Discovery*, *JCO CCI*, *npj Precision Oncology*, CSHL BDS 2026 |
| **B.2** PEFT / LoRA / adapters | $500–$5k | 1–8× A100 for days | 2–4 mo | medium | sc-FM PertAdapter (ICLR 2026 LMRL); scGPT-spatial LoRA; GenePT/scELMo | ICLR / NeurIPS LMRL, *Genome Biology*, ISMB 2026 |
| **B.3** Domain-specific small FM | $10k–$50k | 8–64× A100 ~1 week | 6–12 mo | medium-high | Geneformer V2-104M_CLcancer ($20k); Nicheformer ($25k); scTab + CellPLM | *Nat Methods*, *Genome Biology*, *Cell Systems*, CSHL BDS 2026 |
| **B.4** Negative results / replication | $0–$2k | inference + linear regression | 3–6 mo | low scientifically | Ahlmann-Eltze; Kedzierska; Wenkel; Wu *Nat Methods*; Liu *Adv Sci*; parameter-free; CellBench-LS; Han et al.; PertEval-scFM; Csendes scPerturBench; cellular-dynamics zero-shot — **11 papers in 2025-2026** | *Nat Methods*, *Genome Biology*, *Adv Sci*, RECOMB 2026 |
| **B.5** Benchmark / dataset curation | $0–$5k + curator time | de minimis compute | 6–18 mo | low | Replogle Perturb-seq; Open Problems v2; HEST-1k; Tahoe-100M | NeurIPS D&B, *Scientific Data*, *Nat Methods* Resource, Single Cell Genomics 2026 |
| **B.6** FM-wrapper tools / pipelines | $0–$5k | dev box + inference for tests | 6–12 mo | low (adoption is the risk) | signifinder (Bioconductor); mia / miaTime / miaViz; SpatialData; CytoVerse (browser-native) | GBCC / EuroBioC, *Bioinformatics*, *JOSS*, *F1000Research* |
| **B.7** FM-aided wet-lab / clinical | $5k–$50k FM-side | mostly inference | 12–24 mo | low (FM side) | AACR #4163 KRONOS; AACR #1442 Virchow2+VIDCellTyper; AACR #1444 H-optimus+ABMIL; **Janowczyk *Nat Med* 2025** (UNI EGFR, 197 patients, 43% testing avoidance — the first deployment-grade clinical paper) | *Clin Cancer Res*, *JCO CCI*, *npj Precision Oncology*, *Nat Med* (deployment), AACR Annual |
| **B.8** **Data-augmentation engine** (new 2026) | $0–$2k | inference + small classifier | 3–6 mo | medium (synthetic-data bias control) | **xVERSE** (rare cell types resolved with 4 cells); TranscriptFormer (cross-species synthesis); scDiffusion; CellPLM | *Nat Methods* Resource, *Genome Biology*, NeurIPS LMRL workshop |
| **B.9** **FM-aided experimental design / active learning** (new 2026) | $1k–$10k FM-side | inference per iteration | 12–18 mo | medium (wet-lab partner; baseline matters) | CRADLE-VAE (Bunne); scPRINT; **VCHarness** (BioMap, autonomous virtual-cell builder); rBio (reasoning interface) | *Nat Methods*, *Cell Systems*, *Mol Syst Biol*, NeurIPS active-learning workshops |

**Decision tree:** see the talk page §6.11. **Combinations:** see talk page §6.13 — six load-bearing two-lane patterns. The single most-cited posters at AACR 2026 combine **two** lanes, not one.

### B.1 Lane 1 — FM embeddings as features ($0–$500)

A 1B-param model trained on someone else's $200k cluster, used as a frozen encoder, is the cheapest 2026 way to publish a clinically-meaningful classifier — and the field has stopped pretending the wrapper architecture is the contribution.

**Anchor exemplar — AACR 2026 poster #5470** (academic, not Mahmood/Paige): UNI2-h tile embeddings → attention-MIL → HER2 prediction in breast cancer. **AUC 0.715, tied with full UNI2-h**, but with lower runtime and lower scanner cost — the publishable finding is *parity at a fraction of deployment cost*. Compute: <$500, inference-only.

Other AACR 2026 examples: **#1441** (UNI2-h + CLAM for prostate-cancer risk stratification) · **#2758** (UNI2-h + ABMIL for PAX3/7::FOXO1 fusion detection in rhabdomyosarcoma — first published H&E predictor of a pathognomonic fusion in this rare paediatric disease).

### B.2 Lane 2 — PEFT / LoRA / adapters ($500–$5k)

A <1% parameter adapter is the highest-leverage technical contribution a small lab can make — it inherits the base model's $250k of pretraining and slots into a public benchmark.

- **Exemplar A — sc-FM Perturbation Adapter** (Maleki et al., ICLR 2026 LMRL): drug-conditional adapter, <1% trainable params, frozen scGPT/Geneformer/scFoundation backbone. **Win**: zero-shot generalisation to unseen drugs and cell lines where CPA / GEARS / scGen cannot extrapolate.
- **Exemplar B — scGPT-spatial / LoRA-fine-tuned scGPT**: LoRA rank-8 adapters on scGPT's attention layers for Visium decomposition. ~$1.5k on a single 8× A100 node over 24–48h.
- **Exemplar C — GenePT / scELMo** (Yale, Stanford): frozen LLM embeddings of gene names + a logistic-regression head. ~$200 compute. Matches or beats scGPT zero-shot on cell-type annotation.

### B.3 Lane 3 — Domain-specific small FM ($10k–$50k)

Continual-pretrain a *smaller* general model on *your* domain corpus. 2025 evidence shows this consistently matches the 3× larger general model on in-domain tasks.

- **Exemplar A — Geneformer V2-104M_CLcancer** (Dec 2024): **$16,640 disclosed** for V2-104M base + ~<$3k for the 14M-cancer-cell continual step ≈ **$20k all-in**. Matches V2-316M at ⅓ parameters and ⅓ compute. The cleanest published evidence that *domain curation beats parameter count*.
- **Exemplar B — Nicheformer** (Theis, bioRxiv 2024): 80M-param transformer pretrained on ~110M dissociated + spatial cells with a niche-aware objective. ~$25k estimated.
- **Exemplar C — scTab + CellPLM**: both beat scGPT and Geneformer on cell-typing benchmarks at 10–20× less training cost.

### B.4 Lane 4 — Negative results / replication / critique ($0–$2k)

The single most-published lane of 2025–2026. **11 critique papers** are now in the canon (see §E for the catalog). To differentiate a 2026 Lane-4 paper, target an *uncovered axis*: (1) donor-split benchmarks; (2) cross-tissue transfer; (3) time-resolved perturbation; (4) cancer-cell-line → primary-tumor transfer; (5) rare-cohort robustness.

**Anchor exemplar — Ahlmann-Eltze, Gerard, Huber** (EMBL Heidelberg) — *Nature Methods* 2025: pure inference on six published FMs + a one-line `mean-of-training-perturbations` linear baseline. **<$2k compute. Retired the entire sc-FM perturbation-prediction leaderboard.**

### B.5 Lane 5 — Benchmark curation / dataset contribution ($0–$5k + time)

Held-out splits, donor-split benchmarks, and modality-specific evaluation suites are the most under-priced contributions in the FM era — your dataset becomes infrastructure every subsequent model has to cite.

**Exemplars**: **Replogle et al. 2022 *Cell*** (Weissman lab — genome-wide Perturb-seq) · **Open Problems for Single Cell** (Luecken, Lance, Dann et al. — *Nat Biotechnol* 2024) · **HEST-1k** (Jaume et al., NeurIPS D&B 2024). Tahoe-100M (Vevo + Arc, Feb 2025) is the *contribution pattern* — open-source as benchmark infrastructure.

### B.6 Lane 6 — FM-wrapper tools / pipelines ($0–$5k)

Scverse and Bioconductor still want maintainers. A well-designed wrapper that lets non-Python users feed their data to scGPT or UNI will out-cite the underlying FM in clinical-application papers.

**Exemplars**: **signifinder** (Calura lab, U Padua) · **mia / miaTime / miaViz** (Borman, Turku) · **SpatialData** (Marconato, Palla et al., Theis + Stegle labs) · **CytoVerse** (bioRxiv 2026.01 — browser-native scFM via ONNX).

### B.7 Lane 7 — FM-aided wet-lab / clinical application ($5k–$50k)

Once an FM is publicly available, using it as instrumentation inside a clinical or wet-lab study is *a clinical paper that happens to use a frozen FM*.

**The 2026 frozen-encoder menu is now bigger than 4 options.** Pathology: UNI / UNI2-h, Virchow / Virchow2 / Virchow2G, CONCH, CHIEF, PathChat / PathChat-DX, Phikon / Phikon-v2 / H-optimus-0, Prov-GigaPath, Hibou, PLUTO, **TITAN, mSTAR, GPFM, PathOrchestra, PathPT**. Single-cell: scGPT, Geneformer V2, scFoundation, UCE, CellPLM, CancerFoundation, scMulan, LangCell, Nicheformer (spatial), OmniCell (spatial), **TranscriptFormer** (cross-species generative).

**Beyond AACR — the first published real-world clinical deployment**: **Janowczyk et al. 2025 *Nature Medicine*** — fine-tuned UNI identifies EGFR mutations from H&E in a 197-patient clinical trial, **potentially preventing further genetic testing in 43% of cases**.

**Lane 7 + Track 5 (UQ) is the regulatory-grade combination.** The honest 2026 Lane-7 paper includes a post-hoc UQ wrapper (deep ensemble, MC dropout, Laplace, conformal). FDA-pathway requires it.

### B.8 Lane 8 — FM as generative data-augmentation engine ($0–$2k) — *new 2026*

Before April 2026, FMs were *encoders* (Lane 1) or *adapters' substrate* (Lane 2). xVERSE and TranscriptFormer changed the menu: a generative cell FM can synthesize labeled training data for downstream tasks.

**Anchor — [xVERSE](https://www.biorxiv.org/content/10.64898/2026.04.12.718016v1)** (Jiang & Xie, April 2026): synthesizes virtual cells indistinguishable from real (AUROC ≈ 0.5) and **resolves rare cell types with as few as 4 cells**.

**A 12-month project**: pick a rare-cancer scRNA-seq cohort (<500 cells published). Synthesize a 10–50× expanded labeled corpus with xVERSE or TranscriptFormer. Train downstream classifier on (real + synthetic) vs (real only). Report (1) classifier-AUC lift, (2) calibration on held-out *real* test set, (3) qualitative validation that synthetic cells preserve known cancer signatures.

**Caveat**: synthetic cells can launder the FM's training-distribution biases into your downstream classifier. The honest write-up requires a held-out *real* test set and a calibration plot.

### B.9 Lane 9 — FM-aided experimental design / active learning ($1k–$10k FM-side) — *new 2026*

The closed-loop version of Lane 7. Lane 7 uses a frozen FM as *instrumentation*; Lane 9 uses the FM to *prioritize which experiment to run next*. This is the pattern JPM-2026 buyers (Recursion, Insitro, Latent Labs, Vevo) actually pay for. Bunne 2025 *Cell* names it as a canonical virtual-cell use case.

**Companions**: **VCHarness** (BioMap, bioRxiv 2026.04) — autonomous AI system that constructs perturbation-response models AND prioritizes next experiments. **rBio** (CZ Biohub) — natural-language interface to active-learning queries.

**A 12-month project**: partner with a wet-lab running CRISPRi or drug-perturb screens. Implement FM-guided selection on 200 candidate KOs in a single cancer cell line. Two arms: (1) FM-guided 50 perturbations, (2) random or literature-prior–weighted 50. Compare phenotype enrichment + cost.

**Caveat**: random selection isn't enough as baseline; use StringDB-prioritized as the honest comparator.

---

## §C. Track dossiers — the 9 small-lab innovation tracks

How a small lab can contribute methods work *on* FMs (not just *with* them). Tracks 7–9 are net-new in 2026.

| Track | Open problem | Compute | Exemplar | Paired track |
|---|---|---|---|---|
| **C.1** Mechanistic interpretability | What do scGPT/Geneformer/UNI actually learn? | <$2k | Simon & Zou 2026 SAE atlas; Adams 2025 *PNAS* protein-FM SAEs; Hibou-LP 2024 pathology SAE | T6 |
| **C.2** New pretraining objectives that target causality | Next-gene-prediction optimizes correlation — that's *why* FMs lose to linear baselines | $5–20k | Lopez/Hsu 2025 *Nat Methods* causal repr; CINEMA-OT; STATE pre-training | T6, T9 |
| **C.3** Compositional generalization benchmarks + theory | Does A+B generalize when model saw only A and B? | <$2k | Hetzel 2024 NeurIPS LMRL; Norman 2019 substrate; Boiarsky 2023 baseline-warning | T8, T9 |
| **C.4** Architectures with biology-specific inductive biases | BERT clones ignore pathway / network / lineage priors | $5–15k | **xVERSE** (transcriptomics-native, +17.9% vs LM-derived); MAP (knowledge-driven); HyenaDNA, Caduceus, Enformer | T2 |
| **C.5** UQ / OOD detection for clinical-grade FMs | Every FDA path needs calibrated uncertainty; FMs don't have it | $1–5k | van Amersfoort 2024 deep DUQ; Angelopoulos 2023 conformal; **no published clinical-grade pathology-FM UQ as of May 2026** | B7 |
| **C.6** Causal evaluation frameworks | What's the *correct* test for causality, post-Ahlmann-Eltze? | <$3k | Wenkel `latent-additive` baseline; Lopez/Hsu causal repr | C2, C9 |
| **C.7** **Cross-species transfer / phylogenetic priors** (new 2026) | Does cross-species pretraining help or hurt for cancer biology? | <$2k | **TranscriptFormer** (open); UCE 8-species ablations; no cancer-specific benchmark published | §5.2 gap |
| **C.8** **Synergistic-info evaluation of multimodal FMs** (new 2026) | Which fusion strategies buy cross-modal information vs being redundant? | <$2k | **Microsoft Beyond Alignment / SIS metric** (Feb 2026); apply across multimodal FM zoo (scGPT-spatial, Nicheformer, OmniCell, CLM-X, CELLama, SpatialFusion, mSTAR, TITAN) | C3, C9 |
| **C.9** **Causal transportability benchmarks** (new 2026) | What's the right test for cross-context generalization, post-VCsNC? | <$3k | **Virtual Cells Need Context** (bioRxiv 2026.02) — names the framework; multi-context benchmark unwritten. Pearl + Bareinboim transportability formula + Replogle/Norman as substrate | C6, C8 |

### C.1 Track 1 — Mechanistic interpretability

The first wave broke in 2025–2026. Published SAE work uses general-domain sc-FMs (scGPT, Geneformer on CELLxGENE). **No one has run SAEs on a *cancer-curated* sc-FM** (Geneformer V2-104M_CLcancer, CancerFoundation) to ask: do cancer-domain features differ, and do they predict therapy response or resistance?

**A 12-month project (revised)**: train SAEs on Geneformer V2-104M_CLcancer's residual stream, compare feature atlas vs V2-104M_general. Validate by knockout in held-out perturbation data. **Compute: <$2k.** Now it's a *cancer mechanism* paper, not a *first-SAE* paper.

### C.2 Track 2 — New pretraining objectives that target causality

Next-gene-prediction (scGPT) and masked-gene-modeling (Geneformer) optimize *correlation*. That's structurally why both lose to linear baselines on perturbation prediction.

**A 12-month project**: design a **counterfactual pretraining objective** — for each cell, predict gene expression *under a held-out perturbation* using invariant risk minimization (Arjovsky 2019) or contrastive perturbation losses. Pretrain a 20M-param model on Tahoe-100M; show it beats scGPT-33M on Norman + Replogle held-out splits. **Compute: $5–20k.**

### C.3 Track 3 — Compositional generalization benchmarks + theory

When a model sees perturbations A and B separately, does it generalize to A+B? Norman 2019 has 287 combinatorial splits — but **no published sc-FM has been formally evaluated for compositional generalization with theoretical guarantees**.

**A 12-month project**: build a held-out compositional-perturbation benchmark from Norman + Replogle. Score every sc-FM. **Then prove a theoretical lower bound** on what an additive baseline achieves. Find regimes where FMs *should* beat additivity — and show whether they do. **Compute: <$2k.**

### C.4 Track 4 — Architectures with biology-specific inductive biases

All current biology FMs are domain-agnostic transformer clones. But biology has **rich exploitable structure**: gene-gene interaction networks, pathway hierarchies, cell-lineage trees, regulatory grammar, evolutionary conservation.

**A 12-month project**: build a **graph-attention transformer** that takes a gene-gene interaction graph (StringDB / Reactome / OmniPath) as a fixed prior on attention weights. Pretrain on a 1M-cell subset of CELLxGENE. Hypothesis: pathway-aware attention beats general attention at this scale. **Compute: $5–15k.**

**Real exemplars (2026 wave)**: **xVERSE** (transcriptomics-native, beats LM-derived sc-FMs by 17.9% on representation), **MAP** (knowledge-driven, zero-shot prediction for unprofiled drugs), **[TxPert (Wenkel et al., *Nat Biotech* 2026)](https://doi.org/10.1038/s41587-026-03113-4)** — uses *multiple knowledge graphs* as the inductive bias for transcriptomic-perturbation prediction. **TxPert is the reckoning answering itself**: Wenkel co-authored the 2025 `latent-additive` critique, and TxPert is the methodological response from inside the critique camp. The "all sc-FMs are scGPT-shaped" frame is out of date.

### C.5 Track 5 — UQ / OOD detection for clinical-grade FMs

Every FDA-deployable model needs calibrated uncertainty and OOD detection. **None of the current biology FMs provide either.** PathChat DX got Breakthrough Designation *in spite of this*.

**A 12-month project**: implement four UQ methods on top of frozen UNI2-h embeddings — (1) deep ensembles, (2) MC dropout, (3) Laplace approximation, (4) conformal prediction. Evaluate calibration + selective-prediction accuracy + OOD detection on TCGA → CPTAC distribution shift. **Compute: $1–5k.**

**Real exemplars**: van Amersfoort et al. 2024 (deep deterministic UQ); Angelopoulos & Bates 2023 conformal prediction tutorial. **No published clinical-grade UQ work for pathology FMs as of May 2026.**

### C.6 Track 6 — Causal evaluation frameworks (post-Ahlmann-Eltze)

Wenkel proposed `latent-additive` as the new baseline — but that's still a *correlational* baseline. **What's the right test for whether a model recovered causal structure?**

**A 12-month project**: build a **causal-recovery benchmark** with three test sets: (a) MR-validated genetic effects, (b) validated drug MOA on cell lines (LINCS L1000), (c) ENCODE TF-target relationships. Score every sc-FM. Define a "causal F1" metric. Publish as a public leaderboard. **Compute: <$3k.**

### C.7 Track 7 — Cross-species transfer / phylogenetic priors — *new 2026*

TranscriptFormer pretrained on 12 species × 1.53B years of evolution and beat human-only sc-FMs on cross-species cell-type classification. **But: does cross-species pretraining extend to cancer biology**, where mouse models, organoids, and PDX systems are the daily substrate?

**A 12-month project**: build a **cancer cross-species transfer benchmark** — paired mouse-tumor scRNA-seq + matched human tumor (TCGA-style or patient-matched PDX cohorts). Score TranscriptFormer vs human-only sc-FMs on (1) mouse-to-human cell-state mapping, (2) drug-response transfer from GEMM studies, (3) immune-microenvironment cross-species alignment. **Compute: <$2k.**

**No published cancer cross-species sc-FM benchmark as of May 2026.**

### C.8 Track 8 — Synergistic-information evaluation of multimodal FMs — *new 2026*

Microsoft's [Beyond Alignment paper (Feb 2026)](https://www.biorxiv.org/content/10.64898/2026.02.23.707420v3) introduced the **Synergistic Information Score (SIS)** — a metric for whether a multimodal FM extracts *new* information from cross-modal interactions vs just repeating unimodal signal. **No one has applied SIS across the multimodal cell FM zoo yet.**

**A 12-month project**: implement SIS on ≥5 published multimodal sc / spatial / pathology FMs on a common task set. Identify which fusion strategies actually buy synergy and which are redundant-aligned-fusion in disguise. **Compute: <$2k.**

### C.9 Track 9 — Causal transportability benchmarks — *new 2026*

[Virtual Cells Need Context, Not Just Scale (bioRxiv 2026.02)](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1) frames the sc-FM-doesn't-generalize problem as a **causal transportability problem** in Pearl's sense. The paper **names** the framework but does not give the field a transportability benchmark suite.

**A 12-month project**: define a **transportability benchmark** with explicit cross-context splits — (a) train on cell-line X, test on cell-line Y under same drug; (b) train on healthy donors, test on cancer patients; (c) train on bulk-screened perturbations, test on combinatorial; (d) train on one timepoint, test on another. Score every published sc-FM using a transportability-explicit metric. **Compute: <$3k.**

**The first paper that operationalizes this owns the post-reckoning evaluation citation for the next 3–5 years.**

---

## §D. Compute & resources

Detailed compute / cost / team / data table with arithmetic and DISCLOSED / ESTIMATED / UNKNOWN tags lives in [`_resources-matrix.md`](_resources-matrix.md). Key rows summarized below.

| Model | GPU type × count | GPU-hours | $ (on-demand) | Disclosure tag | Source |
|---|---|---|---|---|---|
| **Geneformer V2-104M** | 64× A100 80GB | 6,656 | ~$17k | ✅ DISCLOSED | NVIDIA BioNeMo recipe |
| **Geneformer V2-316M** | 128× A100 | 11,576 | ~$30k | ✅ DISCLOSED | NVIDIA BioNeMo recipe |
| **Virchow2** | 512× V100 32GB | ~140,000 | ~$170k | ✅ DISCLOSED | Zimmermann 2024 arXiv |
| **Evo2** | 2,048× H100 | ~2,000,000 | ~$5M | ✅ DISCLOSED | Brixi 2026 *Nature* + NVIDIA |
| **ESM-3 (98B)** | (10²⁴ FLOPs disclosed) | ~990,000 H100-eq | $2.5–8M | ✅ DISCLOSED | Hayes 2025 *Science* |
| AlphaGenome | 8× TPU v3 per replica × 4-fold ensemble + distill | UNKNOWN | ~$200k est. | ⚠️ partial | Avsec 2025 *Nature* |
| **scGPT** | UNKNOWN | 10³–10⁵ A100-h (50× band) | $2.6k–$250k est. | ❌ UNKNOWN | Cui 2024 *Nat Methods* |
| UNI2-h | UNKNOWN ("extensive A100") | ~30,000 est. | ~$75k est. | ❌ UNKNOWN | Chen 2024 HF card |
| UCE | UNKNOWN | 1,275–70,000 A100-h | $3k–$175k est. | ❌ UNKNOWN | Rosen 2024 *Nat Methods* |
| STATE | UNKNOWN | unknown | ~$125k est. | ❌ UNKNOWN | Adduri 2025 bioRxiv |
| **TranscriptFormer** | UNKNOWN | unknown | unknown | ⚠️ partial | Pearce 2025 *Science* |
| Generative VC POC | 1× consumer GPU | <100 | <$250 | ✅ DISCLOSED | Lewis & Zueco ICLR 2026 |

**Methodology**: FLOPs ≈ 6 × parameters × tokens (Chinchilla heuristic, Epoch AI 2024). Hours → cost at on-demand: A100 80GB ~$2.5/hr (DGX cloud), V100 32GB ~$1.20/hr, H100 ~$2.5–4/hr, TPU v3 ~$2/hr (vendor pricing).

**The patterns**:
1. **Disclosure correlates with sponsorship**: every DISCLOSED entry has NVIDIA, TPU, or DGX-Cloud co-authorship. Academic labs without hardware co-marketers disclose less.
2. **The $20k floor**: Geneformer V2-104M is the cheapest fully-disclosed sc-FM training. Anything below that on the chart is either a POC or undisclosed.
3. **The $5M ceiling**: Evo2 + ESM-3 define the frontier. Both required vendor compute partnerships ~5 institutions can access.
4. **Pathology FMs are mid-tier ($75k–$170k)** and disclose more than sc-FMs.

---

## §E. 2025–2026 evaluation papers catalog

The full reckoning canon, organized by what each paper evaluated. **As of May 2026, Lane 4 (replication / critique) is the most-published lane of 2025–2026 by a wide margin.**

| # | Paper | Evaluated | Method | Headline finding | Axis covered |
|---|---|---|---|---|---|
| E.1 | **Ahlmann-Eltze & Huber 2025 *Nat Methods*** | 6 sc-FMs (scGPT, Geneformer, scFoundation, GEARS, CPA + Universal baseline) | inference + `mean-of-training-perturbations` linear baseline | none beats linear baseline on Norman / Replogle / Jurkat held-out perturbations | perturbation prediction |
| E.2 | **Kedzierska et al. 2025 *Genome Biology*** | scGPT, Geneformer, UCE + scFoundation | zero-shot embedding eval; PCA + kNN baseline | scFMs lose to PCA + kNN on cell-type and batch-correction in zero-shot | zero-shot embeddings |
| E.3 | **Wenkel et al. 2025 *Nat Methods*** | sc-FMs vs PCA + linear-additive baseline | proposes `latent-additive + scGPT-embeddings` as the new baseline floor | current sc-FMs still don't beat the latent-additive baseline | perturbation, w/ new baseline |
| E.4 | **Wu et al. 2025 *Nat Methods*** (27 × 29 × 6) | 27 methods × 29 datasets × 6 metrics | comprehensive benchmark | axis-by-axis failure decomposition — each FM family fails on different metrics | perturbation (scaled) |
| E.5 | **Wu et al. 2025 *Genome Biology*** (Oct 2025) | 6 scFMs (Geneformer, scGPT, UCE, scFoundation, LangCell, scCello) | gene-level + cell-level tasks, cell-ontology-grounded metrics | *"no single scFM consistently outperforms others across all tasks"* | task-dependence |
| E.6 | **Liu et al. 2026 *Adv Sci*** (scEval) | 10 scFMs × 8 tasks | scEval framework | *"may not consistently outperform task-specific methods … challenges the necessity of developing FMs for single-cell analysis"* | paradigm-level |
| E.7 | **Parameter-free baseline 2026** (bioRxiv 2026.02) | sc-FMs vs parameter-free representations | direct successor to Ahlmann-Eltze | parameter-free reps outperform sc-FMs on downstream benchmarks | downstream tasks |
| E.8 | **PertEval-scFM ICML 2025** | scFM embeddings | standardized perturbation framework | most models don't outperform simple baselines, particularly on strong / atypical perturbations | perturbation (formal venue) |
| E.9 | **CellBench-LS** (bioRxiv 2026.04) | 7 scFMs + PCA / UMAP / scVI | stratified low-supervision protocol | FMs lead on cell-type recognition; classical methods stay competitive on gene-expression quantification | low-supervision |
| E.10 | **Han et al. — real-world RNA-seq** (bioRxiv 2026.04, industry) | scFMs in pharma-relevant deployment | real-world data integration robustness | industry-grade evaluation finds robustness gaps | real-world deployment |
| E.11 | **Cellular-dynamics zero-shot** (bioRxiv 2026.03) | zero-shot scFM embeddings on dynamics | RNA-velocity / dynamics reconstruction | scFMs fail to recover cellular dynamics in zero-shot | RNA velocity / dynamics |
| E.12 | **Csendes scPerturBench** (BM2 Lab) | scGPT replication | adversarial-split benchmark | original scGPT split was leaky; cleaner splits expose failure | replication w/ adversarial split |
| **E.contrarian** | **Foundation Models Improve Perturbation Response Prediction** (bioRxiv 2026.02) | sc-FMs with sufficient data | re-evaluation | **with sufficient data, FMs DO significantly improve genetic + chemical perturbation predictions** | perturbation (counter-evidence) |

**Uncovered axes (Lane 4 frontier as of May 2026)**: (1) **donor-split benchmarks** — cross-donor generalization barely measured; (2) **cross-tissue transfer** — pretraining on tissue A, evaluating on tissue B; (3) **time-resolved perturbation** — 0h vs 6h vs 24h; (4) **cancer-cell-line → primary-tumor transfer**; (5) **rare-cohort robustness** (xVERSE-style: how does FM performance degrade with <100 cells per class?). Each is open and publishable at <$2k.

**Where to publish**: *Nature Methods*, *Genome Biology*, *Advanced Science*, bioRxiv. **RECOMB 2026** for methods-track. **NeurIPS D&B** for the data-side contribution.

---

## §F. Institutional landscape

The compact table from talk page §3.11, then the extended dossier prose.

| Tier | Institute / Lab | PI(s) | Ships | Why they matter |
|---|---|---|---|---|
| **Academic FM builders** | **Arc Institute** (Palo Alto, non-profit, founded 2021) | Patrick Hsu + Hani Goodarzi | Evo2, STATE, Tahoe-100M (with Vevo) | Largest non-DeepMind compute (2,048× H100 via NVIDIA DGX Cloud); sets the perturbation-atlas substrate |
| | **Mahmood Lab** (Harvard / BWH / MGB) | Faisal Mahmood | UNI, UNI2-h, CONCH, PathChat, PathChat-DX, TITAN, CHIEF, HEST-1k | Full pathology vertical stack; PathChat-DX = first FDA Breakthrough Designation for generative-AI pathology (Jan 2025) |
| | **Theodoris Lab** (Gladstone / UCSF) | Christina Theodoris | Geneformer V1, V2-104M / V2-316M / `_CLcancer` (Dec 2024) | Only academic sc-FM lab with full NVIDIA BioNeMo compute disclosure |
| | **Bo Wang Lab** (U. Toronto / Vector / UHN) | Bo Wang | scGPT, scGPT-spatial, MedSAM | Defined the sc-FM category; AACR 2026 plenary |
| | **Leskovec + Quake** (Stanford / SNAP) | Jure Leskovec + Steve Quake | UCE (Universal Cell Embedding) | Cross-species (8 species via ESM2-bridged tokenization) |
| **Industrial FM builders** | **Google DeepMind** | Žiga Avsec et al. | AlphaGenome, AlphaFold 2 / 3, Med-Gemini | Closed-weights + hosted-API model; TPU-scale; Isomorphic Labs is the commercial arm |
| | **EvolutionaryScale** (ex-Meta FAIR, 2024) | Alex Rives, Tom Sercu, Thomas Hayes | ESM-3 (1.4B / 7B / 98B) | Cleanest published FLOPs disclosure in biology FM (10²⁴) |
| | **Paige + MSK** | Thomas Fuchs (Paige) + Zimmermann / Vorontsov | Virchow, Virchow2, Virchow2G, FullFocus | First FDA 510(k)-cleared general-purpose pathology AI (Jan 2025) |
| | **Owkin** (Paris / NYC, founded 2016) | Industry consortium + academic partners | Phikon, Phikon-v2, H-optimus-0, MOSAIC | Only major industrial pathology player shipping open weights (Apache-2.0) |
| | **NVIDIA BioNeMo** (infrastructure layer) | (framework team) | BioNeMo framework; Geneformer V2 recipe; Evo2 co-author | Sets the compute-disclosure norm by making it a co-marketing artifact |
| **Funders & substrates + models** | **CZ Biohub + CZI** (SF / Chicago / NY) | Theofanis Karaletsos, Steve Quake, Angela Pisco | CELLxGENE Census, Tabula Sapiens, Virtual Cell Platform, **TranscriptFormer** (*Science* 2025), **rBio** (2025) | Started substrate-only; TranscriptFormer + rBio now ship *both* substrate and model. Breaks the §3.11 observation that no institute did both. |
| **Critique anchors** | **Ahlmann-Eltze / Huber** (EMBL); **Kedzierska / Lu** (Oxford / MSR); **Theis Lab** (Helmholtz Munich) | (multiple) | The 2025 reckoning trio + Lotfollahi causal / compositional work | Without these, §4 of the talk doesn't exist |
| **2026 emergence** | **BioMap Research + MBZUAI** | Le Song, Eric Xing | VCHarness (autonomous virtual-cell builder), xTrimo PGLM | The China/Middle-East-side competitor to CZ Biohub stack |

### F.1 Extended dossiers

- **[Arc Institute](https://arcinstitute.org/)** — Palo Alto non-profit (founded 2021). Hosts [Hsu Lab](https://arcinstitute.org/labs/hsulab) and [Goodarzi Lab](https://arcinstitute.org/labs/goodarzilab). Shipped: Evo (*Science* 2024), Evo2 (*Nature* 2026 with NVIDIA), STATE (bioRxiv 2025), [Tahoe-100M](https://www.tahoe.ai) (with Vevo, Feb 2025). **Disclosure norm**: foregrounds data scale; buries compute except where NVIDIA is a co-author. Strategic move 2025: launched "Virtual Cell Atlas" branding and co-sponsored the $50k [Virtual Cell Challenge](https://virtualcellchallenge.org/) with CZ Biohub.

- **[Mahmood Lab](https://faisal.ai/)** (Harvard / BWH / MGB) — PI Faisal Mahmood. Ships a *fleet* rather than a single FM: UNI / UNI2-h, CONCH, PathChat / PathChat-DX, TITAN, CHIEF, [HEST-1k](https://github.com/mahmoodlab/HEST). **Disclosure norm**: opaque on compute; HF gating tightened Jan 2025. Strategic move 2025: PathChat-DX FDA Breakthrough Designation — first generative-AI pathology tool. AACR 2026: [ISBI 2026 keynote](https://liudengzhang.github.io/conference-vaults/conferences/isbi-2026/tools/mahmood-pathology-fm-keynote/) on the three-tier FM stack.

- **[Theodoris Lab](https://www.theodorislab.gladstone.org/)** (Gladstone / UCSF) — PI Christina Theodoris. Shipped: Geneformer V1 (*Nature* 2023), [Geneformer V2-104M / V2-316M / V2-104M_CLcancer](https://huggingface.co/ctheodoris/Geneformer). **Disclosure norm**: the only academic sc-FM lab with full compute disclosure via [NVIDIA BioNeMo](https://github.com/NVIDIA/bionemo-framework). **Only reproducible academic sc-FM training run.** Strategic move: domain curation matched the 316M general-domain model at ⅓ the parameters.

- **[Bo Wang Lab](https://wanglab.ai/)** (U. Toronto / Vector / UHN) — PI Bo Wang. Ships: scGPT, scGPT-spatial, MedSAM, BulkRNABERT. **Disclosure norm**: opaque on scGPT training compute (50× uncertainty band). Strategic move 2025: explicit agentic-AI pivot — Wang's [AACR 2026 talk](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/sessions/2026-04-20-am-ai-revolution-in-cancer-research/) is framed around clinical agents.

- **Leskovec + Quake** (Stanford / [SNAP](https://snap.stanford.edu/)) — Jure Leskovec + Steve Quake. Shipped: [UCE](https://github.com/snap-stanford/uce), CRADLE-VAE, scGenePT. **Disclosure norm**: UCE neither preprint nor *Nat Methods* version discloses training compute — least transparent of major sc-FMs.

- **[Google DeepMind](https://deepmind.google/)** — life-sciences team under Kohli + Hassabis. Shipped: AlphaFold 2, AlphaFold 3, [AlphaGenome](https://doi.org/10.1038/s41586-025-10014-0), Med-PaLM / Med-Gemini. **Disclosure norm**: discloses architecture and benchmarks; rarely full compute. Closed weights + free hosted API non-commercial. The [AlphaFold 3 controversy](https://retractionwatch.com/2024/05/14/nature-earns-ire-over-lack-of-code-availability-for-google-deepmind-protein-folding-paper/) pressured Jan 2026 AlphaGenome code release.

- **[EvolutionaryScale](https://www.evolutionaryscale.ai/)** — founded 2024 by ex-Meta FAIR protein team (Rives, Sercu, Hayes). Shipped: ESM-3. **Disclosure norm**: cleanest compute disclosure in biology FM (10²⁴ FLOPs as a single number). License-tiered (1.4B Cambrian NC; 7B / 98B Forge-gated).

- **[Paige.AI](https://paige.ai/) + MSK** — commercial spinout (founded 2018) + Memorial Sloan Kettering (Thomas Fuchs lab). Shipped: Virchow ([arXiv 2408.00738](https://arxiv.org/abs/2408.00738)), Virchow2, Virchow2G, [FullFocus FDA 510(k) Jan 2025](https://paige.ai/news). **Disclosure norm**: clean compute disclosure (512× V100 32GB, ~$170k). License: CC-BY-NC academic; commercial requires Paige license.

- **[Owkin](https://owkin.com/)** — Paris/NYC biotech (founded 2016, ~$300M Series C 2024). Shipped: Phikon, Phikon-v2, H-optimus-0, MOSAIC. **Disclosure norm**: federated-learning-first; weights MIT / Apache-2.0. **Only major industrial pathology player shipping open weights.** AACR 2026: H-optimus-0 in poster #1444.

- **[NVIDIA BioNeMo](https://github.com/NVIDIA/bionemo-framework)** — infrastructure team within NVIDIA Healthcare. Not an FM builder per se, but the only public reproduction recipe for Geneformer V2, silent co-author behind Evo2, the [Lilly + NVIDIA $1B AI Co-Innovation Lab (JPM 2026)](https://liudengzhang.github.io/conference-vaults/conferences/jpm-2026/themes/). **Disclosure norm**: treats compute disclosure as co-marketing artifact.

- **[CZ Biohub + CZI](https://chanzuckerberg.com/science/programs-resources/virtual-cells-initiative/)** — [Theofanis Karaletsos](https://tech.chanzuckerberg.com/ai-powering-biomedical-science/) heads AI for Science; Angela Pisco leads single-cell. Funds + ships: CELLxGENE Census, Tabula Sapiens, [Virtual Cell Platform](https://virtualcellmodels.cziscience.com/), [TranscriptFormer](https://github.com/czi-ai/transcriptformer) (*Science* 2025), [rBio](https://github.com/czi-ai/rbio) (Qwen-2.5-3B post-trained with GRPO using TranscriptFormer as verifier). **Strategic posture (revised 2025–2026)**: started substrate-only; TranscriptFormer + rBio mean CZ Biohub now ships *both*.

- **[Ahlmann-Eltze](https://const-ae.name/) + [Huber Group](https://www.huber.embl.de/)** (EMBL Heidelberg) — Constantin Ahlmann-Eltze (now Isomorphic Labs) + Wolfgang Huber. Authored the [2025 *Nat Methods* linear-baseline paper](https://www.nature.com/articles/s41592-025-02772-6) that retired the sc-FM perturbation leaderboard. **Ahlmann-Eltze's EMBL → Isomorphic transition is itself a market signal** — the most influential FM critic was hired by Alphabet's biology arm.

- **[Theis Lab](https://www.helmholtz-munich.de/en/icb/pi/fabian-theis)** (Helmholtz Munich) — PI Fabian Theis. Long-running single-cell methods group; built [scvi-tools](https://scvi-tools.org/), scArches, framework vocabulary every sc-FM paper inherits. **The methodological reference class for the entire field.** Author of the 2026 *Cell Systems* compositional-FM Perspective.

- **[Zitnik Lab](https://zitniklab.hms.harvard.edu/)** (Harvard Med) — PI Marinka Zitnik. Ships [TxGNN](https://www.nature.com/articles/s41591-024-03233-x), [TDC-2](https://tdcommons.ai/). **Strategic posture**: graph-FM-for-clinic — the bridge between sc-FMs (gene-level) and agentic-clinical-AI (patient-level).

- **[Aviv Regev @ Genentech](https://www.gene.com/scientists/our-scientists/aviv-regev)** — Head of gRED. Not shipping FMs as PI, but the **agenda-setter for "causal foundation models of cells"** (Rood + Hupalowska + Regev 2024 *Cell*). Genentech under Regev is the largest pharma buyer for academic sc-FM tools.

---

## §G. Cross-references

### G.1 The 5 gaps × 9 lanes × 9 tracks matrix

The connective tissue between "what's broken" and "what we'd work on."

| Gap (§5) | Apply via §B lane | Innovate via §C track |
|---|---|---|
| 5.1 Donor diversity | B7 — FM-aided application on under-represented cohort; B8 — synthetic augmentation for rare cohorts | C4 — architecture with donor-conditioning priors; C9 — transportability benchmark with donor-split |
| 5.2 Cross-species | B3 — domain FM on non-human-cell corpus | **C7 — cross-species transfer / phylogenetic priors** (post-TranscriptFormer); C4 — cross-species equivariance priors |
| 5.3 Causal vs correlational | B4 — linear-baseline audit; B9 — active-learning loop targets causal direction | C2 — causality-targeting pretraining; C6 — causal benchmarks; **C9 — causal transportability** |
| 5.4 Compute asymmetry | B6 — wrapper tool that democratizes access; B8 — synthetic-data engine reduces wet-lab cost | C1 — interpretability tells us what the compute bought |
| 5.5 Evaluation honesty | B5 — benchmark curation; B4 — replication catalog (now 11 papers, see §E) | C3 — compositional benchmarks; C6 — causal benchmarks; **C8 — synergistic-info evaluation; C9 — transportability** |

### G.2 The three §9 pitches × lanes × tracks × buyer

The talk's payoff conversation — three concrete project pitches the group could take on at <$25k each.

| Pitch | §6 lane | §7 track | Compute | Time | Buyer archetype | Output |
|---|---|---|---|---|---|---|
| **A** Pathology FM interpretability + clinical UQ | B7 | C1 + C5 | <$3k | 12 mo | Clinical-AI (Paige, PathAI, Tempus, Modella → AZ) | NeurIPS Mech-Interp + *Nat Methods* Resource + AACR poster |
| **B** Compositional perturb benchmark + linear-baseline re-audit (cancer) | B4 | C3 | <$2k | 8 mo | AI-native biotech (Recursion, Insitro, Latent, Vevo) | NeurIPS D&B + *Nat Methods* |
| **C** Rare-cancer FM-aided subtyping + small domain FM | B7 + B3 | (applied focus) | <$25k | 18–24 mo | Pharma rare-disease (Pfizer, Sanofi, AZ, Vertex) | AACR poster + *Clin Cancer Res* + *Nat Methods* |

### G.3 Pitch detail

**Pitch A — Pathology FM interpretability + clinical UQ.** Take UNI2-h (or Virchow2 — pick based on license), train sparse autoencoders on its residual-stream activations over a TCGA slice, cluster features and map them to histology grammar (tumor regions, stromal compartments, immune infiltrate patterns). Then layer a post-hoc Bayesian or conformal-prediction head and evaluate calibration on TCGA → CPTAC distribution shift. **Output**: NeurIPS Mech-Interp workshop (interpretability), *Nature Methods* Resource (UQ), AACR-Annual-style clinical poster. **Why us**: builds on existing TCGA familiarity; no wet-lab required.

**Pitch B — Compositional perturbation benchmark + linear-baseline re-audit on cancer perturb-seq.** Rebuild scGPT + Geneformer + UCE evaluation pipelines on Norman 2019 + Replogle 2022 + Tahoe-100M with cancer-specific cell-line subsets. Add the Ahlmann-Eltze linear baseline and the Wenkel latent-additive baseline. Then design a formal compositional split (A+B held out when A and B seen separately) and prove a theoretical lower bound on what additivity achieves. **Output**: NeurIPS D&B (benchmark), *Nature Methods* (linear-baseline replication in cancer context), maybe a second *Genome Biology* paper. **Why us**: leverages the AACR-corpus context; cancer-specific findings are differentiating.

**Pitch C — FM-aided rare-cancer subtyping + small domain FM.** Pick a rare-cancer cohort the public pathology-FM training corpora missed (rhabdomyosarcoma, ATC, NET, mesothelioma, etc.). First publish a frozen-encoder application paper (like AACR #2758 PAX3/7::FOXO1 in rhabdomyosarcoma — Lane 7). Then continual-pretrain a Geneformer-V2-104M-style domain FM on the cohort's matched scRNA-seq + a 100k-cell rare-cancer reference. **Output**: AACR poster + *Clinical Cancer Research* or *npj Precision Oncology* (Year 1), then *Nature Methods* domain-FM paper (Year 2). **Why us**: most defensible if we have a clinical collaborator with a rare-cancer cohort.

---

## §H. Appendix carryover

### H.1 Likely Q&A questions + scripted answers

**Q: Are FMs ready for clinical deployment?**
A: In pathology, yes — PathChat DX has FDA Breakthrough Designation, and Virchow2 / UNI2-h are in active clinical-grade evaluation. In single-cell biology, no — the linear-baseline reckoning means we don't yet have a single-cell FM whose predictions can be trusted for clinical decisions. Genomic FMs (AlphaGenome) are intermediate: predict variant effects well in benchmark settings but not deployed against clinical decision-making at scale.

**Q: Why doesn't more compute solve this?**
A: It might for pathology — Virchow2G at 1.85B is the latest scale push and we don't yet know if the curve is plateauing. For single-cell, the Geneformer-V2-104M_CLcancer result suggests *more* compute on *general* data is not the bottleneck. Domain curation and evaluation are.

**Q: What about agentic AI / LLM-driven pipelines?**
A: MedAgentGym (ICLR 2026) is the strongest demonstration so far: 72k-task sandboxed code-exec gym + Med-Copilot-7B that orchestrates biomedical analyses. Agentic AI is the *interface layer* on top of the FMs — it doesn't fix underlying FM accuracy problems but makes them more accessible. CZ Biohub's **rBio** (2025) is the first reasoning model trained on virtual-cell simulations; BioMap's **VCHarness** (2026) is the first autonomous virtual-cell-builder agent.

**Q: Will any of these be available with permissive licenses?**
A: Mixed picture. Single-cell FMs (scGPT, Geneformer, UCE, scFoundation, CellPLM, GET, TranscriptFormer) are mostly MIT/Apache-2.0. Pathology FMs are mostly CC-BY-NC with the Hibou and Owkin Phikon/H-optimus exceptions (Apache-2.0). Protein FMs split (ESM-2 open, ESM-3 partially gated). Genomic FMs mostly open except AlphaGenome. **Track licenses carefully** — UNI's Jan 2025 HF gating shift is the cautionary tale.

**Q: What benchmark would I actually trust?**
A: For single-cell FMs: PerturBench `latent-additive + scGPT-embeddings` baseline is the floor; clear it first, then report your task. For pathology: Campanella et al. 2025 *Nature Communications* multi-task panel. For genomic: gnomAD-pathogenic + ENCODE/GTEx variant-effect benchmark. For protein: CASP15/16 + retro-validated novel-binder hit rates.

**Q: What about the contrarian voice in 2026?**
A: *Foundation Models Improve Perturbation Response Prediction* (bioRxiv 2026.02.18) argues that with sufficient data, FMs *do* improve perturbation prediction. Honest framing: the reckoning was *current scFMs trained on current data with current evals* fail to clear linear baselines; whether the *FM paradigm* fails is separate and still open. *Virtual Cells Need Context* (bioRxiv 2026.02) argues it's a **causal transportability problem**, not a capacity problem.

### H.2 Datasets, weights, code — concrete starting points

**Datasets**:
- [Tahoe-100M](https://www.tahoe.ai) — 100M cells × 1,100 drugs × 50 cell lines (Vevo / Arc Institute)
- [CellxGene Census](https://cellxgene.cziscience.com) — ~50M+ standardized cells, the canonical scRNA atlas
- [Replogle Perturb-seq](https://gwps.wi.mit.edu/) — gold-standard whole-genome perturbation dataset
- [Open Problems for Single Cell](https://openproblems.bio) — benchmark hub
- [HEST-1k](https://github.com/mahmoodlab/HEST) — 1k WSI spatial transcriptomics benchmark

**Weights**:
- [scGPT (HuggingFace)](https://huggingface.co/wangshenguiuc/scGPT) — MIT
- [Geneformer V2 (HuggingFace)](https://huggingface.co/ctheodoris/Geneformer) — Apache-2.0
- [UCE](https://github.com/snap-stanford/uce) — MIT
- [scFoundation](https://github.com/biomap-research/scFoundation) — Apache-2.0
- [TranscriptFormer](https://github.com/czi-ai/transcriptformer) — open
- [UNI / UNI2-h (HuggingFace)](https://huggingface.co/MahmoodLab/UNI) — CC-BY-NC, gated
- [Virchow (HuggingFace)](https://huggingface.co/paige-ai/Virchow) — CC-BY-NC
- [Hibou (HuggingFace)](https://huggingface.co/histai/hibou-b) — Apache-2.0
- [Evo2](https://github.com/ArcInstitute/evo2) — Apache-2.0
- [ESM-3 (1.4B)](https://github.com/evolutionaryscale/esm) — Cambrian Non-Commercial

**Code / benchmarks**:
- [PerturBench](https://github.com/altoslabs/perturbench) — single-cell perturbation benchmark
- [scPerturBench](https://github.com/bm2-lab/scPerturBench) — adversarial split benchmark
- [Open Problems](https://github.com/openproblems-bio/openproblems) — community benchmark hub

### H.3 Recommended reading — ~110 references

The bibliography is organized into 12 buckets. **Bold** = read first. URLs are direct. Several algorithm and review papers that are *adjacent* to the talk's topic — perturbation prediction, generative modelling, the architecture debate — without being FM papers have their own dossiers in [Adjacent methods](fm-to-virtual-cells/adjacent-methods/index.md).

#### Position papers — start here

- **Bunne, Roohani, Rosen, et al. 2024 *Cell* — ["How to build the virtual cell with artificial intelligence: Priorities and opportunities"](https://www.cell.com/cell/fulltext/S0092-8674(24)01332-1)** — the canonical virtual-cell thesis.
- **Rood, Hupalowska, Regev 2024 *Cell* — ["The future of rapid and automated single-cell data analysis using reference mapping"](https://doi.org/10.1016/j.cell.2024.07.030)** — Aviv Regev's framing.
- **Theis et al. 2026 *Cell Systems* — "From modality-specific to compositional foundation models for cell biology"** — the post-reckoning forward path.
- **Adduri et al. 2025 *Cell* — "Virtual Cell Challenge: Toward a Turing test for the virtual cell"** — what success looks like.
- Lähnemann et al. 2020 *Genome Biology* — "Eleven grand challenges in single-cell data science" — the pre-FM landscape.
- Marx 2024 *Nat Methods* tech feature — "AI builds models of biology" — accessible field overview.
- Singh et al. 2025 *Exp Mol Med* — "Single-cell foundation models: bringing AI into cell biology" — clean mid-2025 review.
- Cao, Lu & Qiu 2026 *Nat Methods* — "Towards predictive virtual embryos" — virtual *embryo* extension.
- **[Rao et al. 2026 *Nat Biotech* — "Generalist biological artificial intelligence in modeling the language of life"](https://doi.org/10.1038/s41587-026-03064-w)** — the generalist-biology-AI position paper; sits alongside Bunne and Theis as a "what is the field building toward" reference.
- **[Li et al. 2026 *Nat Biotech* — "Agentic AI and the rise of in silico team science in biomedical research"](https://doi.org/10.1038/s41587-026-03035-1)** — the agentic-FM intersection framed at the *team-science* level; the position paper behind the [agentic-meets-foundation explainer](fm-to-virtual-cells/agentic-meets-foundation.md).

#### The 2025 critique trio — the reckoning

- **[Ahlmann-Eltze & Huber 2025 *Nature Methods* 22:1657–1661](https://www.nature.com/articles/s41592-025-02772-6)** — "Deep-learning-based predictions of gene expression do not generalize."
- **[Kedzierska et al. 2025 *Genome Biology* 26:101](https://doi.org/10.1186/s13059-025-03574-x)** — "Assessing the limits of zero-shot foundation models in single-cell biology."
- Wenkel et al. 2025 — proposes `latent-additive` as the new baseline.
- [Csendes, Lugo-Martinez et al. 2024](https://www.biorxiv.org/content/10.1101/2024.09.30.615579) — scGPT replication exposing train/test leakage.
- Boiarsky et al. 2023 NeurIPS workshop — earliest "linear baselines are competitive" warning.
- See §E for the full 2025–2026 evaluation paper catalog.

#### Single-cell FM technical papers

- **Cui et al. 2024 *Nat Methods* — [scGPT](https://doi.org/10.1038/s41592-024-02201-0)** — defined the field shape.
- **Theodoris et al. 2023 *Nature* — [Geneformer](https://doi.org/10.1038/s41586-023-06139-9)** — first atlas-pretrained transformer.
- [Geneformer-V2 HuggingFace card (Dec 2024)](https://huggingface.co/ctheodoris/Geneformer) — domain-curated `_CLcancer` matches 316M at ⅓ params.
- Rosen, Brbić et al. 2024 — [UCE](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2) — cross-species via protein-language tokens.
- Hao et al. 2024 *Nat Methods* — [scFoundation](https://doi.org/10.1038/s41592-024-02305-7).
- Yang et al. 2022 *Nat Mach Intell* — [scBERT](https://doi.org/10.1038/s42256-022-00534-z).
- Wen et al. 2024 *ICLR* — [CellPLM](https://openreview.net/forum?id=BKXvPDekud).
- **Pearce et al. 2025 *Science* — [TranscriptFormer](https://www.science.org/doi/10.1126/science.aec8514)** — first generative cross-species sc-FM.
- Adduri et al. 2025 bioRxiv — STATE (Arc Institute).
- Schaar et al. 2025 *Nat Methods* — [Nicheformer](https://www.nature.com/articles/s41592-025-02814-z) — spatial-omics sc-FM.
- Zhang et al. 2025 *Nat Commun* — [CellFM](https://www.nature.com/articles/s41467-025-59926-5).
- Jiang & Xie 2026 — [xVERSE (bioRxiv 2026.04)](https://www.biorxiv.org/content/10.64898/2026.04.12.718016v1) — transcriptomics-native.
- Kalfon et al. 2025 *Nat Commun* — [scPRINT](https://doi.org/10.1038/s41467-025-58699-1) — pretrained on 50M cells for robust zero-shot gene-network inference.
- Kalfon, Peyré & Cantini 2025 — [scPRINT-2 (bioRxiv 2025.12)](https://doi.org/10.64898/2025.12.11.693702) — next-generation cell FM *and* a benchmark suite.

#### Pathology FM technical papers

- **Chen et al. 2024 *Nat Medicine* — [UNI](https://doi.org/10.1038/s41591-024-02857-3)**.
- **Vorontsov et al. 2024 *Nat Medicine* — Virchow**.
- Zimmermann et al. 2024 *arXiv* — [Virchow2 / Virchow2G](https://arxiv.org/abs/2408.00738).
- **Wang et al. 2024 *Nature* — [CHIEF](https://doi.org/10.1038/s41586-024-07894-z)**.
- Xu et al. 2024 *Nature* — [Prov-GigaPath](https://www.nature.com/articles/s41586-024-07441-w).
- Lu et al. 2024 *Nat Medicine* — [CONCH](https://www.nature.com/articles/s41591-024-02856-4).
- Lu et al. 2024 *Nature* — [PathChat](https://www.nature.com/articles/s41586-024-07618-3).
- Nechaev et al. 2024 *arXiv* — [Hibou-L / Hibou-B](https://arxiv.org/abs/2406.05074) — Apache-2.0 top-tier option.
- Filiot et al. 2024 — Phikon-v2.
- Saillard et al. 2024 *Nat Medicine* — [H-Optimus-0](https://www.nature.com/articles/s41591-024-03281-3).
- Ding et al. 2025 *Nat Med* — TITAN.
- Xu et al. 2025 *Nat Commun* — mSTAR.
- Yan et al. 2025 *npj Digit Med* — PathOrchestra.
- Ma et al. 2026 *Nat Biomed Eng* — GPFM.
- [Campanella et al. 2025 *Nat Communications*](https://www.nature.com/articles/s41467-025-58245-z) — clinical-grade benchmark.
- Janowczyk et al. 2025 *Nat Med* — first real-world clinical UNI deployment.

#### Genomic / DNA FM technical papers

- Dalla-Torre et al. 2025 *Nat Methods* — [Nucleotide Transformer](https://doi.org/10.1038/s41592-024-02523-z).
- Zhou et al. 2024 *ICLR* — [DNABERT-2](https://openreview.net/forum?id=oMLQB4EZE1).
- Ji et al. 2021 — [DNABERT](https://doi.org/10.1093/bioinformatics/btab083).
- Nguyen et al. 2023 *NeurIPS* — [HyenaDNA](https://proceedings.neurips.cc/paper_files/paper/2023/hash/86ab6927ee4ae9bde4247793c46797c7-Abstract-Conference.html).
- **Nguyen et al. 2024 *Science* — [Evo (v1)](https://www.science.org/doi/10.1126/science.ado9336)**.
- **Brixi et al. 2026 *Nature* — Evo 2** ([DOI 10.1038/s41586-026-10176-5](https://www.nature.com/articles/s41586-026-10176-5)).
- **[Avsec et al. 2025 *Nature* — AlphaGenome](https://doi.org/10.1038/s41586-025-10014-0)**.
- Avsec et al. 2021 *Nat Methods* — [Enformer](https://doi.org/10.1038/s41592-021-01252-x).
- Schiff et al. 2024 *ICML* — [Caduceus](https://openreview.net/forum?id=8c5BvLBHgD).
- Consens et al. 2025 *Nat Mach Intell* — ["Transformers and genome language models"](https://doi.org/10.1038/s42256-025-01007-9) — review of the genome-LM landscape. → [resource page](fm-to-virtual-cells/adjacent-methods/genome-language-models.md).
- Tiezzi et al. 2025 *Nat Mach Intell* — ["Back to recurrent processing at the crossroad of transformers and state-space models"](https://doi.org/10.1038/s42256-025-01034-6) — architecture review behind the transformer-vs-SSM choice (HyenaDNA / Caduceus / xVERSE). → [resource page](fm-to-virtual-cells/adjacent-methods/transformers-vs-state-space.md).

#### Protein FM technical papers

- **Hayes et al. 2025 *Science* — [ESM-3](https://www.science.org/doi/10.1126/science.ads0018)**.
- **Lin et al. 2023 *Science* — [ESM-2 / ESMFold](https://www.science.org/doi/10.1126/science.ade2574)**.
- **Abramson et al. 2024 *Nature* — [AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w)**.
- Jumper et al. 2021 *Nature* — [AlphaFold 2](https://doi.org/10.1038/s41586-021-03819-2).
- Watson et al. 2023 *Nature* — [RFdiffusion](https://doi.org/10.1038/s41586-023-06415-8).
- Madani et al. 2023 *Nat Biotechnol* — [ProGen2](https://doi.org/10.1038/s41587-022-01618-2).
- Notin et al. 2023 *NeurIPS* — ProteinGym benchmark.

#### Virtual cell-specific work

- **Bunne et al. 2024 *Cell* — virtual cell perspective** (canonical).
- **CZ Biohub Virtual Cell Program** — [program page](https://chanzuckerberg.com/science/programs-resources/virtual-cells-initiative/).
- **Roohani, Hsu et al. 2025 — Tahoe-100M** — first large-scale perturbation atlas framed as virtual-cell training data.
- Arc Institute 2025 — [Virtual Cell Atlas + STATE](https://arcinstitute.org/manuscripts/state).
- [CZ Biohub Virtual Cell Challenge 2025](https://virtualcellchallenge.org/) — first community benchmark, $50k prize.
- Lotfollahi et al. 2023 *Nat Cell Biol* — CPA (Compositional Perturbation Autoencoder).
- Roohani et al. 2024 *Nat Biotechnol* — [GEARS](https://www.nature.com/articles/s41587-023-01905-6).
- Cheng et al. (BioMap, Le Song / Eric Xing) 2026 bioRxiv — **VCHarness** — autonomous virtual-cell builder.
- CZ Biohub 2025 — **rBio** — reasoning model trained on TranscriptFormer.

#### Benchmarks & datasets

- Replogle et al. 2022 *Cell* — Whole-genome Perturb-seq.
- Norman et al. 2019 *Science* — combinatorial Perturb-seq.
- Open Problems v2 — [openproblems.bio](https://openproblems.bio).
- PerturBench / scPerturBench / PertEval-scFM / CellBench-LS — see §E.
- Tabula Sapiens Consortium 2022 *Science*.
- CELLxGENE Census.
- HuBMAP 2023 *Nature*.
- HEST-1k.
- CASP15 / CAPRI.

#### Mechanistic interpretability — the 2025–2026 wave

- Adams et al. 2025 *PNAS* — SAEs uncover features in protein language model representations.
- Simon & Zou 2026 *arXiv* 2603.02952 — SAEs reveal organized biology but minimal regulatory logic in sc-FMs.
- bioRxiv 2025 — SAEs Reveal Interpretable Features in Single-Cell FMs (independent confirmation on scGPT).
- Hibou-LP team 2024–2025 *arXiv* 2407.10785 — first pathology-FM SAE.
- bioRxiv 2026 — "What Do Biological Foundation Models Compute?" — synthesis across families.
- Hunklinger & Ferruz 2026 *Nat Mach Intell* — ["Towards the explainability of protein language models"](https://doi.org/10.1038/s42256-026-01232-w) — review of interpretability methods for protein FMs. → [resource page](fm-to-virtual-cells/adjacent-methods/protein-lm-explainability.md).

#### Compute / cost methodology

- [Cottier, Rahman et al. 2024 *arXiv*](https://arxiv.org/abs/2405.21015) — "The Rising Costs of Training Frontier AI Models."
- [Epoch AI training-compute methodology](https://epoch.ai/blog/estimating-training-compute) — the FLOPs heuristic.
- [Hoffmann et al. 2022 — Chinchilla](https://arxiv.org/abs/2203.15556).
- [NVIDIA Evo 2 announcement (Feb 2025)](https://blogs.nvidia.com/blog/evo-2-biomolecular-ai/).

#### Industry / strategy / clinical context

- [PathAI 2025 Series E announcement](https://www.pathai.com/news).
- [Paige.AI FullFocus FDA 510(k) clearance (Jan 2025)](https://paige.ai/news).
- [Owkin MOSAIC platform](https://owkin.com).
- [Tempus AI S-1 (2024)](https://www.sec.gov).
- [Recursion Pharmaceuticals R&D updates](https://www.recursion.com).
- [Insitro pipeline](https://insitro.com) — Daphne Koller's applied virtual-cell case study.
- [Latent Labs](https://latentlabs.com) — Simon Kohl + DeepMind alumni virtual-cell startup.
- Sukumaran et al. 2025 *JCO Precision Oncology* — clinical-decision-support evaluation framework.
- [Schönhuth 2025 *Nat Mach Intell* — "From data chaos to precision medicine"](https://doi.org/10.1038/s42256-025-01015-9) — short framing commentary on the data-to-clinic gap.
- AstraZeneca acquires Modella AI (JPM 2026 announcement).

#### Cross-vault index

- [Foundation Models](../foundation-models.md) — cross-vault FM index.
- [AACR 2026 Virtual Cells topic](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/virtual-cells/).
- [AACR 2026 Agentic AI topic](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/agentic-ai/).
- [AACR 2026 Bioinfo/AI methods topic](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/).
- [ICLR 2026 tools](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/).
- [ISBI 2026 pathology FM keynote](https://liudengzhang.github.io/conference-vaults/conferences/isbi-2026/tools/mahmood-pathology-fm-keynote/).
- [JPM 2026 themes](https://liudengzhang.github.io/conference-vaults/conferences/jpm-2026/themes/).

### H.4 People to follow

- **Christina Theodoris** (Gladstone / UCSF) — Geneformer creator. [Lab](https://www.theodorislab.gladstone.org/) · [bio](https://gladstone.org/people/christina-theodoris).
- **Bo Wang** (U. Toronto / Vector / UHN) — scGPT PI. [WangLab](https://wanglab.ai/) · [X @BoWang87](https://x.com/bowang87).
- **Mohammad Lotfollahi** (Wellcome Sanger / Open Targets) — scArches, scPoli. [Lab](https://lotfollahi.com/research/).
- **Aviv Regev** (Genentech) — Head of gRED; HCA co-founder. [bio](https://www.gene.com/scientists/our-scientists/aviv-regev).
- **Patrick Hsu** (Arc Institute) — Evo2 + STATE co-PI. [Hsu Lab @ Arc](https://arcinstitute.org/labs/hsulab) · [patrickhsu.com](https://patrickhsu.com/).
- **Faisal Mahmood** (Harvard / BWH / MGB) — UNI, CONCH, PathChat, TITAN. [faisal.ai](https://faisal.ai/).
- **Jure Leskovec** (Stanford / SNAP) — UCE co-PI. [stanford.edu/~jure](https://cs.stanford.edu/people/jure/).
- **Sara Mostafavi** (UW Allen School) — deep-learning models of differential gene expression. [Lab](http://saramostafavi.github.io/).
- **Constantin Ahlmann-Eltze** (Isomorphic Labs, ex-Huber/EMBL) — 2025 linear-baseline first author. [const-ae.name](https://const-ae.name/).
- **Wolfgang Huber** (EMBL Heidelberg) — Bioconductor + statistics-of-genomics elder. [Huber Group](https://www.huber.embl.de/).
- **Theofanis Karaletsos** (CZI, Head of AI for Science) — runs virtual-cell program + rBio. [CZI tech blog](https://tech.chanzuckerberg.com/ai-powering-biomedical-science/).
- **Kasia Z. Kedzierska** (Oxford / MSR) — zero-shot critique first author. [Scholar](https://scholar.google.com/citations?user=lvJpQGUAAAAJ).
- **Hani Goodarzi** (Arc / UCSF) — STATE co-lead. [Goodarzi Lab](https://arcinstitute.org/labs/goodarzilab).
- **Fabian Theis** (Helmholtz Munich) — author of 2026 *Cell Systems* compositional-FM Perspective. [Theis Lab](https://www.helmholtz-munich.de/en/icb/pi/fabian-theis).
- **Le Song / Eric Xing** (BioMap Research + MBZUAI) — VCHarness; the autonomous virtual-cell-builder direction.
- **Marinka Zitnik** (Harvard Med) — TxGNN, TDC-2. [Zitnik Lab](https://zitniklab.hms.harvard.edu/).

### H.5 Newsletters / blogs / podcasts

- **Owl Posting** — Abhishaike Mahajan's biology + ML essays. [owlposting.com](https://www.owlposting.com/).
- **Decoding Bio** — weekly biotech + AI papers digest. [decodingbio.substack.com](https://decodingbio.substack.com/).
- **Asimov Press** — long-form bio writing. [press.asimov.com](https://press.asimov.com/).
- **CZ Biohub Data Science blog** — Tabula, CELLxGENE, virtual-cell engineering. [ds.czbiohub.org/blog](https://ds.czbiohub.org/blog/).
- **Arc Institute News** — STATE, Evo2, Virtual Cell Atlas releases. [arcinstitute.org/news](https://arcinstitute.org/news).
- **M2D2 — Molecular Modelling & Drug Discovery** — weekly reading group + podcast. [portal.valencelabs.com/m2d2](https://portal.valencelabs.com/m2d2).
- **The Gradient** — ML-for-science long-form. [thegradient.pub](https://thegradient.pub/).
- **Latent Space** — Swyx & Alessio's ML podcast; hosts bio-FM founders. [latent.space](https://www.latent.space/).
- **Eric Topol's Substack** — biomedical AI clinical perspective. [erictopol.substack.com](https://erictopol.substack.com/).
- **PreLights** (Company of Biologists) — preprint commentary. [prelights.biologists.com](https://prelights.biologists.com/).

### H.6 Live benchmarks / leaderboards

- **Open Problems for Single Cell v2** — [openproblems.bio](https://openproblems.bio).
- **PerturBench** (Altos Labs) — [github.com/altoslabs/perturbench](https://github.com/altoslabs/perturbench).
- **scPerturBench** (BM2-Lab) — [bm2-lab.github.io/scPerturBench-reproducibility](https://bm2-lab.github.io/scPerturBench-reproducibility/).
- **CZI Virtual Cells Platform Benchmarks** — [virtualcellmodels.cziscience.com/benchmarks](https://virtualcellmodels.cziscience.com/benchmarks).
- **Arc Virtual Cell Challenge** — [arcinstitute.org/news/behind-the-data-virtual-cell-challenge](https://arcinstitute.org/news/behind-the-data-virtual-cell-challenge).
- **Polaris Hub** — [polarishub.io](https://polarishub.io/).
- **Therapeutics Data Commons (TDC-2)** — [tdcommons.ai](https://tdcommons.ai/).
- **CASP / CAPRI** — [predictioncenter.org](https://predictioncenter.org/).
- **HEST-1k** — [github.com/mahmoodlab/HEST](https://github.com/mahmoodlab/HEST).

### H.7 Recorded talks / lecture series

- **M2D2 Talks** (Valence + Mila) — ~200 archived ML-for-drug-discovery seminars.
- **CZI Virtual Cells Platform — workshops & webinars** — recorded sessions on FM training, benchmarks, evaluation.
- **scverse community talks** — annual conference recordings.
- **Simons Institute "ML & Statistics for Single-Cell Genomics"** — public lectures.
- **Broad Institute MIA seminars** — bio-ML talks.
- **NeurIPS / ICLR Generative & Experimental Perturbations workshops** — annual recordings.

### H.8 Communities / Discord / Slack

- **scverse Zulip** — Scanpy / AnnData / squidpy / scvi-tools developer chat. [scverse.zulipchat.com](https://scverse.zulipchat.com/).
- **Open Problems community** — GitHub Discussions + Slack. [github.com/openproblems-bio](https://github.com/openproblems-bio).
- **Polaris Hub Slack** — drug-discovery ML benchmark community.
- **Hugging Face Biology / Bio-ML** — model cards + discussion. [huggingface.co/biology](https://huggingface.co/biology).
- **EleutherAI #biology channel** — open-research; *Discord invite via [eleuther.ai](https://www.eleuther.ai/)*.

### H.9 Timing cheat sheet

#### The talk in 12 slides — speaker's eye view

| # | Slide | Source |
|---|---|---|
| 1 | Title + operational definition of virtual cell | Act 1 opening |
| 2 | Why now — 2024–25 inflection (CZ Biohub, Tahoe-100M, PathChat FDA) | Act 1 |
| 3 | **The scatter plot** — 2023 paradigm → 2024 ambition → 2025 reckoning → 2026 response | Act 1 |
| 4 | Today's institutional landscape table | Act 2 |
| 5 | The 5 FM families | Act 2 |
| 6 | The 2025 reckoning — linear baseline + contrarian + theoretical underpinning + new architectures | Act 1 close |
| 7 | The 5 gaps mapped to lanes and tracks | Act 3 open |
| 8 | The 9 lanes table + decision tree + combinations | Act 3 part A |
| 9 | The 9 tracks table + unifying frame | Act 3 part B |
| 10 | Commercial — 3 buyer archetypes + per-pitch buyer map | Act 4 open |
| 11 | The 3 pitches table | Act 4 close |
| 12 | AACR 2026 as the live evaluation surface | Act 5 |

#### Recommended plan — 62 min, Acts 1–5 + group discussion

| Section | Time | Slides | Discussion pivot |
|---|---|---|---|
| Act 1 — the 2023–2026 arc + scatter plot | 10 min | 3 | "Where on the plot would *our* work go?" |
| Act 2 — today's landscape | 5 min | 2 | "Which family is closest to our existing work?" |
| Act 3 — 9 lanes + 9 tracks | 15 min | 5 | "Lane 1 + Lane 7 are the AACR posters; Lane 8 + Lane 9 are the 2026 frontier. Which of our datasets fits?" |
| Act 4 — commercial + pitches | 10 min | 3 | "Of the three pitches, which has the clearest non-academic check writer?" |
| Group discussion | 15 min | 2 | The whole point |
| Act 5 — close | 3 min | 1 | — |
| Buffer | 4 min | — | — |
| **Total** | **62 min** | **16** | — |

If 75 min: expand group discussion to 25 min. If 45 min: cut Act 3 to lanes-only (skip tracks), trim Act 4 to per-pitch buyer map only.

### H.10 2026 updates — the 37-paper catalog

> Carried over from talk-page §11.6, organized as in the original. **Bold** = new in this revision wave. Each is annotated with what changed because of it.

#### New benchmarks confirming or extending the 2025 reckoning

- **[Wu et al. 2025 *Nat Methods*](https://www.nature.com/articles/s41592-025-02980-0)** — 27 methods × 29 datasets × 6 metrics.
- **[Liu et al. 2026 *Adv Sci*](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)** — scEval framework; broadens past perturbation-only.
- **[Wu et al. 2025 *Genome Biology*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492631/)** — 6 scFMs across gene-/cell-level tasks; no scFM consistently outperforms.
- **[Parameter-free baseline](https://www.biorxiv.org/content/10.64898/2026.02.11.705358v1)** (Feb 2026) — direct successor to Ahlmann-Eltze.
- **[PertEval-scFM, ICML 2025](https://icml.cc/virtual/2025/poster/43799)**.
- **[CellBench-LS](https://www.biorxiv.org/content/10.64898/2026.04.01.714123v1)** (April 2026).
- **[Han et al. real-world RNA-seq](https://www.biorxiv.org/content/10.64898/2026.04.17.719314v1)** (April 2026, industry).
- **[Cellular-dynamics zero-shot](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)** (Mar 2026).
- **[Hossain et al. *arXiv* 2412.13478](https://arxiv.org/abs/2412.13478)** — PEFT/LoRA recipe for sc-FMs.
- **[Foundation Models Improve Perturbation Response](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** (Feb 2026) — **the contrarian voice**.
- **[MAP — knowledge-driven framework](https://www.biorxiv.org/content/10.64898/2026.02.25.708091v1)** (Feb 2026).
- **[TxPert (Wenkel et al. 2026 *Nat Biotech*)](https://doi.org/10.1038/s41587-026-03113-4)** — multiple-knowledge-graph perturbation prediction. **The reckoning answering itself**: Wenkel co-authored the 2025 `latent-additive` critique; TxPert is the methodological response from inside the critique camp. **Fold into**: Act 1 §1.3 (architectural response), §C.4 Track 4.

#### Position / framing papers

- **[Roohani et al. 2025 *Cell*](https://www.cell.com/cell/fulltext/S0092-8674(25)00675-0)** — Virtual Cell Challenge Turing test.
- **[Theis 2026 *Cell Systems*](https://www.cell.com/cell-systems/abstract/S2405-4712(26)00016-5)** — compositional FMs.
- **[Virtual Cells Need Context](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1)** — causal transportability framing.
- **[Beyond Alignment (SIS)](https://www.biorxiv.org/content/10.64898/2026.02.23.707420v3)** (Microsoft, Feb 2026).
- **[Cao, Lu & Qiu — virtual embryos](https://www.nature.com/articles/s41592-026-03055-4)** (*Nat Methods* 2026).
- **[Rao et al. 2026 *Nat Biotech* — Generalist biological AI](https://doi.org/10.1038/s41587-026-03064-w)** — the generalist-biology-AI position paper.
- **[Li et al. 2026 *Nat Biotech* — Agentic AI + in silico team science](https://doi.org/10.1038/s41587-026-03035-1)** — the agentic-FM intersection at the team-science level.
- [Adduri et al. 2025 STATE preprint](https://www.biorxiv.org/content/10.1101/2025.06.26.661135v1).
- [Singh et al. 2025 *Exp Mol Med*](https://www.nature.com/articles/s12276-025-01547-5) — review.

#### The virtual-X wave — beyond the single cell

- **[Zhou et al. 2026 *Nat Biotech* — Digital twins of ex vivo human lungs](https://doi.org/10.1038/s41587-026-03121-4)** — personalized therapeutic-efficacy evaluation on virtual *organs*. The "virtual X" agenda forks: virtual cell (this talk) → virtual embryo (Cao/Lu/Qiu 2026) → virtual organ (Zhou 2026).
- **[Computational generation of high-content digital organs at single-cell resolution, *Nat Methods* 2025](https://www.nature.com/articles/s41592-025-02996-6)** — 38M-cell mouse-brain virtual atlas reconstructed from sparse spatial transcriptomics. Confirms the digital-organ pattern is a real 2025–2026 wave, not a one-off.

#### New agentic-AI-for-biology systems

- **[Alber et al. 2026 *Nat Methods* — CellVoyager](https://doi.org/10.1038/s41592-026-03029-6)** — autonomous AI comp-bio agent that analyzes single-cell data and generates new insights. The third agentic pattern: rBio *reasons over* a virtual cell, VCHarness *builds* virtual cells, **CellVoyager *analyzes* with the FM as substrate**. **Fold into**: [agentic-meets-foundation explainer](fm-to-virtual-cells/agentic-meets-foundation.md).

#### New single-cell / spatial foundation models

- **[Pearce et al. 2025 *Science* — TranscriptFormer](https://www.science.org/doi/10.1126/science.aec8514)** — CZ Biohub flagship.
- **[xVERSE](https://www.biorxiv.org/content/10.64898/2026.04.12.718016v1)** (April 2026) — transcriptomics-native.
- **[OmniCell](https://www.biorxiv.org/content/10.64898/2025.12.29.696804v1)** (Dec 2025).
- **[VCHarness](https://www.biorxiv.org/content/10.64898/2026.04.11.717183v1)** (April 2026, BioMap).
- **[SpatialFusion](https://www.biorxiv.org/content/10.64898/2026.03.16.712056v1)** (Mar 2026).
- **[rBio v1](https://virtualcellmodels.cziscience.com/model/rbio)** (CZ Biohub 2025).
- [Schaar et al. 2025 *Nat Methods* — Nicheformer](https://www.nature.com/articles/s41592-025-02814-z).
- [Zhang et al. 2025 *Nat Commun* — CellFM](https://www.nature.com/articles/s41467-025-59926-5).
- [CLM-X](https://www.biorxiv.org/content/10.64898/2026.02.17.704943v1) (Feb 2026).
- [CytoVerse](https://www.biorxiv.org/content/10.64898/2026.01.29.702554v1) (Jan 2026) — browser-native.
- [CELLama](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202513210) (*Adv Sci* 2026).
- [CancerFoundation](https://www.biorxiv.org/content/10.1101/2024.11.01.621087v1).
- [scPRINT](https://doi.org/10.1038/s41467-025-58699-1) (Kalfon et al., *Nat Commun* 2025) — 50M-cell pretraining for gene-network inference.
- **[scPRINT-2](https://doi.org/10.64898/2025.12.11.693702)** (bioRxiv Dec 2025) — next-generation cell FM + benchmark suite; pairs a model release with its own evaluation harness.

#### New pathology foundation models

- [Ding et al. 2025 *Nat Med* — TITAN](https://www.nature.com/articles/s41591-025-03982-3) (Nov 2025).
- [Xu et al. 2025 *Nat Commun* — mSTAR](https://www.nature.com/articles/s41467-025-66220-x) (Dec 2025).
- [Ma et al. 2026 *Nat Biomed Eng* — GPFM](https://www.nature.com/articles/s41551-025-01488-4).
- [Janowczyk et al. 2025 *Nat Med*](https://www.nature.com/articles/s41591-025-03780-x) — first real-world clinical deployment.
- [PathPT (*Nat Commun* 2026)](https://www.nature.com/articles/s41467-026-71715-2).
- [Yan et al. 2025 *npj Digit Med* — PathOrchestra](https://www.nature.com/articles/s41746-025-02027-w).

#### Mechanistic interpretability — the wave that broke between drafts

- [Adams et al. 2025 *PNAS*](https://www.pnas.org/doi/10.1073/pnas.2506316122) — SAEs on protein FMs.
- [Simon & Zou 2026 *arXiv* 2603.02952](https://arxiv.org/abs/2603.02952) — SAEs on Geneformer + scGPT.
- [bioRxiv 2025 SAE on scGPT](https://www.biorxiv.org/content/10.1101/2025.10.22.681631v2) — independent confirmation.
- [Hibou-LP SAE](https://arxiv.org/abs/2407.10785) — first pathology-FM SAE.
- [bioRxiv 2026 SAEs synthesis](https://www.biorxiv.org/content/10.64898/2026.03.04.709491v1).

#### Genomic FM follow-ups

- [*Cell Research* 2026 — AlphaGenome non-coding variant effects](https://www.nature.com/articles/s41422-026-01249-1) — independent eval.

#### Net effect on the talk (May 2026 revision)

- **Act 1 thesis** gets sharper: Liu + Theis generalize past perturbation. The question is no longer "do scFMs predict perturbations" but "does the monolithic-FM paradigm earn its compute at all."
- **Act 2 institutional landscape** revised: CZ Biohub now ships both substrate and model (TranscriptFormer, rBio). Breaks the §3.11 substrate-vs-model split.
- **Act 1 reckoning** evidence base is now **ten papers, not three**.
- **Act 1 gains the contrarian voice**: FMs Improve Perturbation (bioRxiv 2026.02).
- **Act 1 gains theoretical underpinning**: Virtual Cells Need Context — causal transportability problem, structural not capacity-bounded.
- **Act 3 Tracks 7, 8, 9** are net-new in 2026: cross-species, SIS, causal transportability.
- **Act 4 commercial framing** notes: CZ Biohub (TranscriptFormer + rBio) and BioMap (VCHarness) as the two fully-open / open-research stacks.
- **Act 3 Track 4** gains TxPert — the reckoning's own authors (Wenkel) now publishing knowledge-graph-driven methodological responses. The reckoning → response loop is closing.
- **Act 5 closing** now has a *virtual-X-is-forking* point: virtual cell (this talk) → virtual embryo (Cao/Lu/Qiu 2026) → virtual organ (Zhou 2026 lungs + digital-organ *Nat Methods* 2025).
- **Agentic ↔ FM convergence is now three-way**: rBio reasons, VCHarness builds, CellVoyager analyzes. Plus the Li et al. 2026 *Nat Biotech* "in silico team science" position paper frames the whole intersection.

---

## Pointers back to the main talk

- [Talk page (Acts 1–5, ~720 lines)](fm-to-virtual-cells.md)
- [Compute matrix](_resources-matrix.md)
- [Foundation Models cross-vault index](../foundation-models.md)
- [90-min Speed Read](../speed-read.md)
- [2026 Timeline](https://liudengzhang.github.io/conference-vaults/timeline/)

*Last updated: 2026-05-13.*
