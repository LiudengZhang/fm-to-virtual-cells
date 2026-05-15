# Foundation Models in Biology — 2026 State of Play

A cross-vault synthesis of every foundation-model (FM) dossier in this corpus. Links resolve to per-tool deep dives in the AACR / ICLR / ISBI / Single-Cell-Genomics vaults.

The corpus distinguishes **15 net-new dossiers** written for this synthesis (single-cell, pathology, genomic, protein, multimodal) from **12 existing dossiers** that received an FM-comparison deepening pass in May 2026. The 27 entries cover the FMs that AACR 2026 sessions and ICLR/ISBI 2026 papers either build on or directly evaluate.

---

## At a glance

| Family | Anchor model(s) | 2026 SOTA | Load-bearing benchmark | Open question |
|---|---|---|---|---|
| **Single-cell** | scGPT, Geneformer | scGPT-spatial (Feb 2025); Geneformer-V2-104M_CLcancer | SC-Arena, PerturBench, scPerturBench, Open Problems v2 | Can any sc-FM beat `mean-of-training-perturbations` on perturbation prediction? |
| **Pathology** | UNI, Prov-GigaPath, CHIEF | Virchow2 / UNI2-h (Jan 2025) | Campanella et al. 2025 clinical benchmark; HEST-1k; BACH; CRC polyp | Where does the scale curve plateau? (Virchow2G at 1.85B is the current ceiling) |
| **Genomic / DNA** | Evo2, Enformer | AlphaGenome (Nature 2026) — 25/26 variant-effect wins | gnomAD-pathogenic, ENCODE/GTEx tracks, GUE/GUE+, NT 18-task | Is ICL still a viable genomic capability after AlphaGenome's track-prediction win? |
| **Protein** | ESM-2 / ESM-3, AlphaFold3 | ESM-3 (Science 2025; 98B params) | Long-context folding; novel-binder design hit rates | Generative protein design vs structure-prediction — which yields wet-lab hits faster? |
| **Multimodal** | BioMedCLIP, PathChat, LLaVA-Med | PathChat-2 (Nature 2024 extension; >1M instructions) | PMC-VQA, SLAKE, VQA-RAD, PathQABench | Will FDA-cleared generative pathology copilots (PathChat DX got Breakthrough Designation Jan 2025) ship in 2026? |

---

## The two biggest stories of 2025-2026

### 1. The linear-baseline reckoning for single-cell FMs

Three independent 2025 papers — [Ahlmann-Eltze & Huber, *Nature Methods*](https://www.nature.com/articles/s41592-025-02772-6), Kedzierska et al. *Genome Biology*, and Wenkel et al. *Nature Methods* — showed that scGPT, Geneformer, scFoundation, and UCE **fail to beat trivial linear baselines** (`mean-of-training-perturbations` or `latent-additive`) on perturbation-prediction tasks that the original papers reported as wins. PerturBench's `latent-additive + scGPT-embeddings` baseline is now the floor every new claim must clear.

Consequences:

- **AACR 2026 has zero posters with scGPT/Geneformer/UCE in the title** (the [pathology-FM stack](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/synthesis-fm-pathology-traction/) appears in 18 posters by contrast).
- The [SC-Arena](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/sc-arena/) ICLR 2026 paper is now a *scorecard*, not a contestant.
- [Geneformer V2](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/geneformer/) inverts the scale-wins narrative: the cancer-domain `V2-104M_CLcancer` checkpoint (14M cancer cells, 104M params) matches or beats the 316M deep model. Domain-specific pretraining beat raw scale.

This is the *clearest discipline correction* in single-cell ML since 2023. The frame moving forward: any sc-FM that wants to claim utility for AACR-style downstream tasks must publish (a) cell-type classification, (b) drug-perturbation prediction, and (c) cross-tissue transfer numbers *all against* the LA-on-scGPT baseline.

### 2. The Virchow rebalancing in pathology FMs

The Nature 2024 ordering (Prov-GigaPath → UNI → CHIEF) flipped in 2025:

- **[Virchow2](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/virchow/)** (Paige+MSK, 632M ViT-H, 3.1M WSIs) took first place on the Campanella et al. 2025 *Nature Communications* clinical benchmark.
- **[UNI2-h](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/uni/)** released Jan 14 2025 — 681M ViT-H/14, 200M+ tiles, added IHC — and now leads on BACH (1.0 BAcc) and several Mahmood-stack downstream tasks.
- **[CHIEF](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/chief/)** has shipped no v2 in 2025. AGPL-3.0 + gated weights is now a real adoption tax versus Apache-2.0 alternatives, explaining its near-zero AACR 2026 traction.
- **[PathChat / PathChat DX](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/pathchat/)** received **FDA Breakthrough Device Designation in January 2025** — the first generative-AI pathology tool to do so.
- **[Hibou](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/hibou/)** (HistAI — *not Owkin*) is the only Apache-2.0 top-tier pathology FM. Owkin's analogue is Phikon / Phikon-v2.

The corollary: pathology FMs are the *only* family in this corpus with FDA-track regulatory activity in 2025-2026. Single-cell, genomic, and protein FMs remain pre-clinical-tool.

---

## Family deep dives

### Single-cell FMs

Five major models. Two existed pre-2025; three landed in 2024-2025 alongside the linear-baseline critique.

| Model | Architecture | Params | Pretraining corpus | Public weights | Page |
|---|---|---|---|---|---|
| **scGPT** | Encoder-decoder transformer | 51M | 33M cells | ✅ MIT | [scgpt.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/scgpt/) |
| **Geneformer** | Encoder-only BERT | 10M / 104M / 316M | 30M / 95M cells (V2) | ✅ Apache-2.0 | [geneformer.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/geneformer/) |
| **UCE** | Encoder-only ViT-style | 650M | ~36M cells / 8 species | ✅ MIT | [uce.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/uce/) |
| **scFoundation** | xTrimoGene encoder | 100M | 50M+ human cells | ✅ Apache-2.0 | [scfoundation.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/scfoundation/) |
| **GET** | Multi-modal transformer | ~50M | scATAC + scRNA, ~1.3M cells | ✅ MIT | [get.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/get/) |
| **CellPLM** | Cell-as-token transformer | ~80M | scRNA, paired spatial | ✅ MIT | [cellplm.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/cellplm/) |

Non-FM but adjacent: **[Cell2Location](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/cell2location/)** — the Bayesian incumbent for spatial deconvolution, now threatened by scGPT-spatial + CellPLM as pretrained alternatives.

Generative virtual-cell models (a separate sub-class):
- **[Generative Virtual Cells](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/generative-virtual-cells/)** (Lewis & Zueco, ICLR 2026) — jointly-updated planner + world model
- **STATE** (Arc Institute, 2025) — frozen Tahoe-100M snapshot

### Pathology FMs

| Model | Architecture | Pretraining corpus | Public weights | License | Page |
|---|---|---|---|---|---|
| **UNI / UNI2-h** | ViT-L/16 → ViT-H/14 | 100M tiles → 200M+ tiles | ✅ (gated 2025) | CC-BY-NC | [uni.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/uni/) |
| **Prov-GigaPath** | DINOv2 ViT-G/14 | 1.4B tiles from 171K WSIs | ✅ | CC-BY-NC | [prov-gigapath.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/prov-gigapath/) |
| **CHIEF** | ViT-L + CTransPath | 60K WSIs | ✅ (gated) | AGPL-3.0 | [chief.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/chief/) |
| **Virchow / Virchow2** | DINOv2 ViT-H | 1.5M / 3.1M WSIs | ✅ Virchow only | CC-BY-NC | [virchow.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/virchow/) |
| **Hibou-B / Hibou-L** | DINOv2 ViT | 1.14M slides | ✅ | Apache-2.0 | [hibou.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/hibou/) |
| **PathChat / PathChat-2** | Vision-language (LLaVA-style) | 457K instructions (PathChat-2: >1M) | ❌ (FDA Breakthrough) | Proprietary | [pathchat.md](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/tools/pathchat/) |

Synthesis context: [Mahmood pathology FM keynote](https://liudengzhang.github.io/conference-vaults/conferences/isbi-2026/tools/mahmood-pathology-fm-keynote/) (ISBI 2026) and [FM-pathology-traction landscape](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/topics/bioinfo-tools/synthesis-fm-pathology-traction/).

### Genomic / DNA FMs

| Model | Architecture | Context | Params | Tokenization | Page |
|---|---|---|---|---|---|
| **Nucleotide Transformer** | Encoder-only | 6 kb | 50M–2.5B | 6-mer (vocab 4,104) | [nucleotide-transformer.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/nucleotide-transformer/) |
| **DNABERT-2** | Encoder + ALiBi + FlashAttn | 128 bp (pre-tr) | 117M | BPE (vocab 4,096) | [dnabert-2.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/dnabert-2/) |
| **HyenaDNA** | Hyena implicit-conv (no attention) | up to 1M | 6.6M–1.6B | Single-nucleotide (vocab 12) | [hyenadna.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/hyenadna/) |
| **Evo2** | StripedHyena SSM | up to 1M | 7B / 40B | Byte-level | [genomic-icl-evo2.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/genomic-icl-evo2/) |
| **AlphaGenome** | U-Net + transformer bottleneck | 1 Mb | ~450M (vendor) | Single-nucleotide | [alphagenome.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/alphagenome/) |

The line dividing this family: **track-prediction transformers** (Enformer, AlphaGenome) vs **generative DNA LMs** (Evo2, HyenaDNA). AlphaGenome wins 25/26 on regulatory variant-effect evaluations, but Evo2 holds unique ICL ground because you cannot prompt a track-prediction model.

### Protein + multimodal FMs

| Model | Modality | Notes | Page |
|---|---|---|---|
| **ESM-3** | Protein (3-track: seq + structure + function) | 98B params; generated esmGFP de novo (36% identity to avGFP) | [esm-3.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/esm-3/) |
| **Proteina Complexa** | Atomistic protein binder design | 63.5% PDGFR hit rate; first de novo carbohydrate binders | [proteina-complexa.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/proteina-complexa/) |
| **TEA** | De novo protein with epitope conditioning | ICLR 2026 | [tea-de-novo-protein.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/tea-de-novo-protein/) |
| **BioMedCLIP** | Vision-language (biomedical) | PMC-15M (15.3M image-text pairs); MIT licensed | [biomedclip.md](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/biomedclip/) |

---

## Virtual cells — why the problem is hard

A "virtual cell" is shorthand for *a learned model that can predict any cell's gene expression under any perturbation*. Three orthogonal problems block it:

1. **Evaluation** — most "virtual cell" papers report SOTA on tasks that turn out to be dominated by linear baselines once you run the right control. [SC-Arena](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/sc-arena/) is the post-2025 attempt at honest scorekeeping.
2. **Training data** — Tahoe-100M (Vevo / Arc Institute, 2025) is the largest perturbation atlas, but coverage is still drug-skewed and donor-shallow.
3. **Generation vs prediction** — do you (a) condition a generative model on a perturbation token and sample, or (b) train a deterministic head to predict perturbed expression? Lewis & Zueco's [Generative Virtual Cells](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/generative-virtual-cells/) bets on (a); Arc's STATE bets on (b).

What success looks like in 2026: an FM that beats `latent-additive + scGPT-embeddings` *on perturbation prediction held out by perturbation, donor, and cell type*. As of May 2026, no public model has cleared all three splits.

---

## Open questions for 2026

1. **Single-cell:** Will any FM beat the LA-on-scGPT baseline on the post-2025 splits? (If not, the field needs a new pretraining objective, not more cells.)
2. **Pathology:** Does Virchow2G (1.85B) signal that pathology FM scale still pays, or did UNI2-h's `H/14 + 200M tiles` already hit the curve plateau?
3. **Genomic:** Is ICL still useful for genomics now that AlphaGenome wins 25/26 on variant effects without prompting? Or is Evo2's ICL territory niche?
4. **Protein:** Will ESM-3's de novo design hit rate hold up at wet-lab scale, or is esmGFP a single anecdote?
5. **Clinical:** Will any second generative-pathology copilot (after PathChat DX) reach FDA Breakthrough Designation in 2026?

---

## How to use this page

- **Linked from individual conference vaults**: each dossier above sits in its host vault (AACR / ICLR / ISBI). This page is the cross-vault map.
- **Linked from the [Speed Read](speed-read.md)**: the 0:35–1:15 segment of the 90-minute path covers the highest-value FM dossiers.
- **Backed by primary sources**: every numeric claim in the dossiers ends with a citation (Nature / *Nature Methods* / Science / ICLR / NeurIPS / arXiv / bioRxiv / HuggingFace model card).

If you're tracking a specific FM family, start at the family-deep-dive table above and follow the tool links. If you're tracking the discipline-level debate, the **linear-baseline reckoning** and **Virchow rebalancing** sections summarize 2025-2026's two biggest course-corrections.
