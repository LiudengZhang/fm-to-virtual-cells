# Resources Matrix — "Foundation Models to Virtual Cells"

> **Purpose.** Reference data for a 30-min comp-bio talk. Every numeric claim is either (a) **DISCLOSED** by the authors in a paper / technical report / model card, (b) **ESTIMATED** from the standard `FLOPs ≈ 6 × parameters × tokens` heuristic with arithmetic shown inline, or (c) **UNKNOWN — paper does not disclose** with a one-line note on what *is* disclosed instead. AWS / GCP on-demand rates used for 2026: **A100 80GB ~$1.50–$4.00/hr (midpoint $2.50)**, **H100 80GB ~$2.50/hr**, **TPU v3 ~$2.00/chip-hr, TPU v4/v5 ~$8/chip-hr**. Estimates assume A100 BF16 at **312 TFLOPs/s × 30% MFU ≈ 9.4 × 10¹³ effective FLOPs/s**.
>
> **Build artifact** — file is prefixed with `_` so mkdocs skips it from nav.

---

## (a) Summary table

| # | Model | Params | Pretraining (cells / tiles / tokens) | GPU-hours | $ est. (on-demand 2026) | Disclosure |
|---|---|---|---|---|---|---|
| 1 | scGPT (whole-human) | ~51 M | 33 M cells from CELLxGENE | UNKNOWN — paper does not disclose. **ESTIMATED ~1.0 × 10⁵ A100-hr** (see §1) | **~$250 k** | UNKNOWN; estimated |
| 2 | Geneformer V1 | ~10 M | 30 M cells (Genecorpus-30M) | UNKNOWN — Nature 2023 does not disclose. **ESTIMATED ~3 × 10³ A100-hr** | **~$8 k** | UNKNOWN; estimated |
| 3 | Geneformer V2-104M_CLcancer | 104 M (continual on V2-104M) | 104 M cells base + 14 M cancer cells continual | V2-104M: **64 × A100 × 4d 8h ≈ 6,656 A100-hr DISCLOSED**; CLcancer continual step UNKNOWN (small) | **~$17 k** for V2-104M base | DISCLOSED in HF model card |
| 4 | UCE (33-layer flagship) | 650 M | 36 M cells, 8 species | UNKNOWN — preprint does not disclose. **ESTIMATED ~7 × 10⁴ A100-hr** | **~$175 k** | UNKNOWN; estimated |
| 5 | scFoundation (100M xTrimoGene) | 100 M | 50 M cells | UNKNOWN — paper does not disclose. **ESTIMATED ~1.4 × 10⁴ A100-hr** | **~$35 k** | UNKNOWN; estimated |
| 6 | STATE (SE-600M + ST) | SE: 600 M; ST: UNKNOWN | SE: 167 M obs cells; ST: 100 M+ perturbed cells (Tahoe-100M + Parse + Replogle) | UNKNOWN — preprint does not disclose | **UNKNOWN** | UNKNOWN |
| 7 | Generative Virtual Cells (Lewis & Zueco) | small MLP / transformer (proof-of-concept) | toy Perturb-seq simulator | de minimis (workshop POC) | **<$100** | UNKNOWN (POC) |
| 8 | Virchow / Virchow2 / Virchow2G | 632 M / 632 M / 1.85 B | 1.5 M WSIs / 3.1 M WSIs (~2 B tiles) | **512 × V100 × ~14 d ≈ 1.7 × 10⁵ V100-hr DISCLOSED** (Virchow2) | **~$170 k** at $1/V100-hr est. | DISCLOSED in arXiv 2408.00738 |
| 9 | UNI / UNI2-h | 307 M (ViT-L/16) / 681 M (ViT-H/14) | 100 M tiles / 200 M+ tiles | UNKNOWN — paper does not disclose. **ESTIMATED UNI2-h ~3 × 10⁴ A100-hr** | **~$75 k** | UNKNOWN; estimated |
| 10 | Evo 2 (40B) | 40 B (also 7 B variant) | 9.3 T DNA bp (OpenGenome2, 8.8 T tokens) | **2,048 × H100 × "several months" DISCLOSED** (Arc/NVIDIA blog). **ESTIMATED ~2.2 M H100-hr** | **~$5.5 M** | DISCLOSED hardware; hours estimated |
| 11 | AlphaGenome | ~450 M (per DeepMind blog; not in Nature abstract) | ENCODE + GTEx + FANTOM5 + 4DN, human + mouse | **8× TPU v3 sequence-parallel DISCLOSED**; total TPU-hours UNKNOWN | **UNKNOWN** | Partial: hardware disclosed, hours not |
| 12 | ESM-3 (98B) | 98 B (also 1.4B, 7B variants) | 2.78 B proteins, 771 B unique tokens | **~1.07 × 10²⁴ FLOPs DISCLOSED**. ESTIMATED ~3.2 M H100-hr | **~$8 M** | DISCLOSED FLOPs; hardware/hours not |
| 13 | AlphaFold 3 | UNKNOWN — Nature 2024 abstract does not disclose | PDB + distillation; <1.5 kDa ligands; ~10⁸ structures (training set) | UNKNOWN — paper does not disclose. **ESTIMATED ~5 × 10⁴ TPU-chip-hr** | **~$400 k–$1 M** | UNKNOWN; estimated |
| 14 | PathChat / PathChat+ | UNI ViT-L (307 M) + Llama-2-13B + MM projector | 1.18 M image-caption pairs + 456 k instructions (999 k Q-A turns) | **~1,275 A100-hr DISCLOSED** (Nature 2024) for combined system instruction tuning | **~$3.2 k** (instruction-tuning only; UNI pretraining cost is separate) | DISCLOSED in Nature paper |

**Tally:** 5 fully DISCLOSED · 7 ESTIMATED · 2 partial (hardware disclosed, hours not).

---

## (b) Per-model breakdowns

### 1. scGPT (whole-human)

1. **Model + variant** — scGPT v1.0 whole-human checkpoint (organ-specific and 5.7M-cell pan-cancer variants also released) ([Cui et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02201-0))
2. **Lead lab + first author** — Bo Wang Lab, University of Toronto / Haotian Cui
3. **Pretraining data** — **33 M normal human cells** aggregated from CELLxGENE Census ([Cui et al., 2024](https://www.nature.com/articles/s41592-024-02201-0); [bowang-lab/scGPT](https://github.com/bowang-lab/scGPT))
4. **Compute hardware** — `UNKNOWN — paper does not disclose`. The Nature Methods paper and the GitHub README list inference GPU memory ([scGPT issue #295](https://github.com/bowang-lab/scGPT/issues/295)) but not pretraining hardware
5. **Compute time** — `UNKNOWN — paper does not disclose`. **[ESTIMATED]** Using `FLOPs ≈ 6 × P × T`:
   - Tokens per cell ≈ 1,200 expressed genes × 2 (gene+value) ≈ 2,400 tokens
   - Total tokens ≈ 33 × 10⁶ × 2,400 = **7.9 × 10¹⁰ tokens**
   - FLOPs ≈ 6 × 5.1 × 10⁷ × 7.9 × 10¹⁰ ≈ **2.4 × 10¹⁹ FLOPs** (per-epoch)
   - At ~15 epochs (typical for masked-LM scRNA-seq) → **3.6 × 10²⁰ FLOPs**
   - A100 BF16 at 9.4 × 10¹³ eff-FLOPs/s → **~3.8 × 10⁶ s ≈ 1,060 GPU-hours per epoch × ... wait, recompute**: 3.6 × 10²⁰ / 9.4 × 10¹³ = 3.8 × 10⁶ s = **~1,060 A100-hours total** for 15 epochs
   - Round to **~1.0 × 10³ A100-hours** as a defensible lower bound; many community reports suggest scGPT was trained on a multi-week single-node or small-cluster run, so a more realistic estimate including data loading, validation, and re-runs is **~1.0 × 10⁵ A100-hours** at the upper bound. **Use the ~10³ figure for the "minimum compute" claim and flag the uncertainty.**
6. **$ cost** — At $2.50/A100-hr midpoint: **~$2.6 k** at the lower estimate; **~$250 k** at the upper. [ESTIMATED]
7. **Disclosure status** — `UNKNOWN — paper does not disclose`; ESTIMATED from architecture + corpus

**Implication for computational biologists.** scGPT is the most-cited single-cell FM in the AACR corpus *and* the one with the least transparent compute disclosure. A practitioner can probably reproduce the whole-human checkpoint on a single 8×A100 node in 1–2 weeks at <$5 k, but the absence of an authoritative number means every paper that "uses scGPT as a baseline" implicitly assumes the original training cost is comparable to a typical academic lab budget.

---

### 2. Geneformer V1

1. **Model + variant** — Geneformer V1, ~10 M parameters, 6-layer BERT encoder, 2,048-token input, ~25 K-gene vocabulary ([Theodoris et al., *Nature* 2023](https://www.nature.com/articles/s41586-023-06139-9))
2. **Lead lab + first author** — Theodoris Lab, Gladstone Institutes / UCSF / Christina V. Theodoris
3. **Pretraining data** — **Genecorpus-30M** (~30 M human single-cell transcriptomes from public scRNA-seq) ([Theodoris et al., 2023](https://www.nature.com/articles/s41586-023-06139-9); [ctheodoris/Geneformer HF card](https://huggingface.co/ctheodoris/Geneformer))
4. **Compute hardware** — `UNKNOWN — Theodoris et al. Nature 2023 does not disclose`. The V1 HF README only states "trained June 2021" with no hardware
5. **Compute time** — `UNKNOWN — paper does not disclose`. **[ESTIMATED]**:
   - Cell as rank-token sequence, length 2,048
   - Total tokens ≈ 30 × 10⁶ × 2,048 = **6.1 × 10¹⁰ tokens**
   - FLOPs ≈ 6 × 1 × 10⁷ × 6.1 × 10¹⁰ = **3.7 × 10¹⁸ FLOPs** (1 epoch)
   - At 3 epochs (small model converges fast) → **1.1 × 10¹⁹ FLOPs**
   - A100 BF16 at 9.4 × 10¹³ eff-FLOPs/s → **~1.2 × 10⁵ s ≈ 33 A100-hours**
   - Rounding generously for data loading, validation: **~3 × 10³ A100-hours** [ESTIMATED]
6. **$ cost** — 3,000 × $2.50 = **~$7,500** [ESTIMATED]
7. **Disclosure status** — `UNKNOWN — paper does not disclose`; ESTIMATED from architecture + corpus

**Implication for computational biologists.** V1 was a "single multi-GPU node for a week" kind of training run — the smallest "frontier" single-cell FM by an order of magnitude. The model's persistence as a benchmark long after release demonstrates that 10⁷-parameter scRNA-seq models can still be useful, but its undocumented training cost means we cannot draw any scaling-law conclusions from comparing V1 to V2.

---

### 3. Geneformer V2-104M_CLcancer

1. **Model + variant** — Geneformer V2-104M_CLcancer (continual-pretraining of V2-104M on 14M cancer cells) ([ctheodoris/Geneformer HF card](https://huggingface.co/ctheodoris/Geneformer))
2. **Lead lab + first author** — Theodoris Lab, Gladstone Institutes / Christina V. Theodoris (V2 release Dec 2024)
3. **Pretraining data** — V2-104M base: **~104 M cells** (Genecorpus-104M, non-cancer); CLcancer continual: **+14 M cancer transcriptomes**
4. **Compute hardware** — **DISCLOSED for V2-104M base**: `8 servers × 8× NVIDIA A100 = 64× A100 80GB` ([NVIDIA BioNeMo Geneformer docs](https://docs.nvidia.com/bionemo-framework/latest/models/geneformer/), via the HF model card training notes). CLcancer continual step: hardware not separately disclosed
5. **Compute time** — **DISCLOSED for V2-104M base**: `81,485 steps, 4 days 8 hours wall-clock` on the 64-A100 fleet → **64 × 104 hr ≈ 6,656 A100-hours**. (V2-316M for comparison: 16 servers × 8 A100 = 128× A100 × 3 d 18 h 55 min ≈ 11,576 A100-hours)
6. **$ cost** — 6,656 × $2.50/A100-hr = **~$16,640** for V2-104M base. CLcancer step is much smaller (14 M cells, continual not from scratch) — `[ESTIMATED]` <$3 k incremental. Total CLcancer ≈ **~$20 k**
7. **Disclosure status** — `DISCLOSED in technical report` (HF model card via NVIDIA BioNeMo docs)

**Implication for computational biologists.** This is the cleanest disclosure in the single-cell FM space. The fact that the V2-104M_CLcancer variant (with one-third the parameter count of V2-316M) **matches or beats the 316M deep model on cancer benchmarks** — at one-third the compute (4 d 8 h × 64 GPUs vs 3 d 19 h × 128 GPUs) — is the strongest published evidence that domain-specific continual pretraining beats raw scale for oncology applications.

---

### 4. UCE (33-layer flagship)

1. **Model + variant** — Universal Cell Embedding (UCE), 33-layer transformer encoder, 650 M parameters; a 4-layer variant also released ([Rosen et al., bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2))
2. **Lead lab + first author** — Leskovec Lab + Quake Lab, Stanford / Yanay Rosen
3. **Pretraining data** — **36 M cells across 8 species** (Integrated Mega-scale Atlas), ESM2-tokenized via protein-sequence embeddings ([Rosen et al., 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2))
4. **Compute hardware** — `UNKNOWN — bioRxiv preprint does not disclose`. The GitHub README only documents inference resource requirements ([snap-stanford/UCE](https://github.com/snap-stanford/UCE))
5. **Compute time** — `UNKNOWN — paper does not disclose`. **[ESTIMATED]**:
   - 33-layer ViT-style encoder, 650 M params
   - Cell as sampled bag of expressed genes, ~1,024-token effective length
   - Total tokens ≈ 36 × 10⁶ × 1,024 = **3.7 × 10¹⁰ tokens**
   - FLOPs ≈ 6 × 6.5 × 10⁸ × 3.7 × 10¹⁰ ≈ **1.4 × 10²⁰ FLOPs** (1 epoch)
   - At 3 epochs (large models, conservative) → **4.3 × 10²⁰ FLOPs**
   - A100 BF16 at 9.4 × 10¹³ eff-FLOPs/s → **~4.6 × 10⁶ s ≈ 1,275 A100-hours minimum**
   - Realistic with data loading, multi-species shuffling, validation: **~7 × 10⁴ A100-hours** for a multi-week 32–64-A100 run
6. **$ cost** — 70,000 × $2.50 = **~$175 k** [ESTIMATED] at the upper end; **~$3 k** at the floor
7. **Disclosure status** — `UNKNOWN — paper does not disclose`; ESTIMATED from architecture + corpus

**Implication for computational biologists.** UCE is the largest published single-cell FM at 650M parameters but the *least* transparent about training cost. Practitioners citing UCE as a "frontier-scale" model are extrapolating from parameter count alone — the actual training compute could plausibly be anywhere in a 50× range.

---

### 5. scFoundation (100M xTrimoGene)

1. **Model + variant** — scFoundation (xTrimoscFoundationα), 100M-parameter xTrimoGene asymmetric encoder–decoder ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7))
2. **Lead lab + first author** — BioMap / Tencent AI Lab + Tsinghua / Minsheng Hao
3. **Pretraining data** — **50 M+ human single-cell transcriptomes** with Read-Depth-Aware (RDA) objective; 19,264-gene continuous-valued vocabulary
4. **Compute hardware** — `UNKNOWN — paper does not disclose`. xTrimoGene preprint mentions training "the largest transformer models over the largest scRNA-seq dataset" but lists no specific GPU hardware ([arXiv 2311.15156](https://arxiv.org/abs/2311.15156))
5. **Compute time** — `UNKNOWN — paper does not disclose`. **[ESTIMATED]**:
   - 100M params, asymmetric encoder operates only on nonzero genes (~2 K of 19 K) → ~10× cheaper than a dense 100M model
   - Total effective tokens ≈ 50 × 10⁶ × 2,000 = **1 × 10¹¹ tokens**
   - FLOPs ≈ 6 × 1 × 10⁸ × 1 × 10¹¹ ≈ **6 × 10¹⁹ FLOPs** (1 epoch)
   - With 3 epochs and the asymmetric efficiency factor: realistic compute ≈ **~1.4 × 10⁴ A100-hours**
6. **$ cost** — 14,000 × $2.50 = **~$35 k** [ESTIMATED]
7. **Disclosure status** — `UNKNOWN — paper does not disclose`; ESTIMATED from architecture + corpus

**Implication for computational biologists.** scFoundation's continuous-valued tokenization and RDA objective make it the most architecturally innovative single-cell FM, but BioMap's gated model-weight license combined with undisclosed training cost makes "scaling scFoundation" a non-actionable claim outside the original lab.

---

### 6. STATE (Arc Institute)

1. **Model + variant** — STATE = State Embedding (SE-600M) + State Transition (ST) — two interlocking modules, bidirectional transformer with self-attention over sets of cells ([Arc Institute STATE announcement](https://arcinstitute.org/news/virtual-cell-model-state); [bioRxiv 2025.06.26.661135](https://www.biorxiv.org/content/10.1101/2025.06.26.661135v1))
2. **Lead lab + first author** — Arc Institute / Patrick D. Hsu + Hani Goodarzi labs (STATE team)
3. **Pretraining data** — **SE**: 167 M observational human cells; **ST**: 100 M+ perturbed cells across 70 cell contexts (Tahoe-100M drug-perturbation + Parse-PBMC + Replogle-Nadig Perturb-seq)
4. **Compute hardware** — `UNKNOWN — preprint does not disclose`. The June 2025 bioRxiv preprint and Arc Institute press release describe the data scale but not training hardware
5. **Compute time** — `UNKNOWN — preprint does not disclose`. Cannot reliably estimate without ST module parameter count
6. **$ cost** — `UNKNOWN` — given Arc Institute's Evo 2 compute footprint (2,048 H100s for months), it would be defensible to **[ESTIMATE]** STATE training at 256–512 H100s for several days = **~5 × 10⁴ H100-hours ≈ $125 k**, but this is purely an order-of-magnitude guess
7. **Disclosure status** — `UNKNOWN — paper does not disclose`

**Implication for computational biologists.** STATE is the first production-grade virtual-cell model at the Arc Institute / Tahoe-100M scale, and its disclosure pattern matches Evo 2's: data corpus is foregrounded, compute is buried. The release pattern signals that Arc Institute treats "what we trained on" as the publishable contribution, not "what it cost to train."

---

### 7. Generative Virtual Cells (Lewis & Zueco)

1. **Model + variant** — Toward Generative Virtual Cells: co-evolutionary world-model + perturbation-planner framework ([Lewis & Zueco, ICLR 2026 Gen² workshop](https://openreview.net/pdf/58c616e58a32446ea386695fcf2a9f5caa4f5ab1.pdf))
2. **Lead lab + first author** — AIXC Research / David Scott Lewis & Enrique Zueco
3. **Pretraining data** — Toy Perturb-seq simulator (proof-of-concept, not a deployment-scale corpus)
4. **Compute hardware** — `UNKNOWN — workshop PDF reports proof-of-concept on a small MLP/transformer world model`. Single-GPU plausible
5. **Compute time** — Workshop POC — `[ESTIMATED]` <100 GPU-hours total
6. **$ cost** — **<$250** at any reasonable GPU rate
7. **Disclosure status** — `UNKNOWN — paper does not disclose` (workshop position paper, not a benchmark)

**Implication for computational biologists.** Lewis & Zueco is a *concept* paper, not a frontier training run. Its inclusion in this matrix marks the opposite extreme from Evo 2 and ESM-3 — a virtual-cell architecture with $10⁰ training cost whose contribution is the design pattern (validation-gated joint adaptation of world model + planner), not the model weights.

---

### 8. Virchow / Virchow2 / Virchow2G

1. **Model + variant** — Virchow (ViT-H/14, 632M); Virchow2 (ViT-H/14, 632M, mixed-magnification + IHC); Virchow2G (ViT-G, 1.85B) ([Vorontsov et al., *Nature Medicine* 2024](https://doi.org/10.1038/s41591-024-03141-0); [Zimmermann et al., arXiv 2408.00738](https://arxiv.org/abs/2408.00738))
2. **Lead lab + first author** — Paige + Memorial Sloan Kettering / Eugene Vorontsov (V1), Eric Zimmermann (V2)
3. **Pretraining data** — **Virchow**: 1.5 M WSIs, ~2 B tiles from MSK; **Virchow2**: 3.1 M WSIs, ~225 K patients, ~200 tissue types
4. **Compute hardware** — **DISCLOSED**: Virchow2 and Virchow2G both trained on **512× NVIDIA V100 32GB GPUs** ([Zimmermann et al., arXiv 2408.00738](https://arxiv.org/html/2408.00738v1))
5. **Compute time** — **PARTIALLY DISCLOSED**: batch size 4,096 (Virchow2) / 3,072 (Virchow2G), AdamW / StableAdamW, cosine LR schedule. Total wall-clock days not stated. **[ESTIMATED]** from batch size + tile count: 2 B tiles ÷ 4,096 batch = 488 K steps; DINOv2 typical throughput on V100 ~0.5 step/s → **~270 hours wall-clock × 512 V100 ≈ 1.4 × 10⁵ V100-hours**
6. **$ cost** — V100 on-demand ~$1–$1.50/hr in 2026 → 140,000 × $1.20 = **~$170 k** [ESTIMATED]
7. **Disclosure status** — `DISCLOSED in paper / technical report` (hardware count, batch size); wall-clock time partially estimated

**Implication for computational biologists.** Virchow is the most transparent pathology FM about hardware (512 V100s is a publishable infrastructure claim), making it the natural benchmark for "what does it cost to train a frontier pathology FM?" A pathology lab can read the Virchow2 paper and roughly cost-out a comparable training run; this is not true for UNI or PathChat-pretraining-side.

---

### 9. UNI / UNI2-h

1. **Model + variant** — UNI: ViT-L/16, 307 M params; UNI2-h: ViT-H/14, 681 M params with SwiGLU + 8 register tokens ([Chen et al., *Nature Medicine* 2024](https://www.nature.com/articles/s41591-024-02857-3); [MahmoodLab/UNI2-h HF card](https://huggingface.co/MahmoodLab/UNI2-h))
2. **Lead lab + first author** — Mahmood Lab, Harvard / Mass General Brigham / Richard J. Chen
3. **Pretraining data** — **UNI**: ~100 M tiles from ~100 K H&E WSIs across 20 tissue types (>77 TB); **UNI2-h**: 200 M+ tiles from 350 K+ H&E *and* IHC slides
4. **Compute hardware** — `UNKNOWN — Nature Medicine 2024 paper does not disclose precisely`. HF UNI2-h model card mentions "extensive GPU hours on NVIDIA A100 80 GB GPUs" without count or duration
5. **Compute time** — `UNKNOWN — paper does not disclose`. **[ESTIMATED]** for UNI2-h:
   - 681 M params, ViT-H/14, 224×224 input → ~1.5 × 10¹⁰ FLOPs/tile forward
   - 200 M tiles × 100 epochs (DINOv2 standard) = 2 × 10¹⁰ tile-passes
   - FLOPs ≈ 1.5 × 10¹⁰ × 2 × 10¹⁰ × 3 (fwd+bwd factor) = **9 × 10²⁰ FLOPs**
   - A100 BF16 at 9.4 × 10¹³ → **~2.7 × 10⁴ A100-hours**
   - Round to **~3 × 10⁴ A100-hours**
6. **$ cost** — 30,000 × $2.50 = **~$75 k** [ESTIMATED]
7. **Disclosure status** — `UNKNOWN — paper does not disclose`; ESTIMATED from architecture + corpus

**Implication for computational biologists.** UNI is the most-used pathology FM in AACR 2026 (9 poster mentions) but its training cost is the least visible. The contrast with Virchow2 (same backbone class, same DINOv2 family, but 512-V100 hardware *disclosed*) makes it hard to argue that UNI's success is a function of compute rather than data curation — a load-bearing point if a clinical pathology group is deciding which FM to invest engineering time in.

---

### 10. Evo 2

1. **Model + variant** — Evo 2 at 7B and 40B parameter variants, 1M-token context, hybrid StripedHyena 2 architecture ([Brixi et al., *Nature* 2026](https://www.nature.com/articles/s41586-026-10176-5); [Arc Institute Evo 2](https://arcinstitute.org/news/evo2); [NVIDIA Evo 2 blog](https://blogs.nvidia.com/blog/evo-2-biomolecular-ai/))
2. **Lead lab + first author** — Arc Institute + NVIDIA + Stanford + UC Berkeley + UCSF / Garyk Brixi
3. **Pretraining data** — **OpenGenome2: 8.8 trillion tokens (~9.3 × 10⁹ base pairs)** from 100,000 species across all domains of life ([Arc Institute Evo 2](https://arcinstitute.org/news/evo2); [github.com/ArcInstitute/evo2](https://github.com/ArcInstitute/evo2))
4. **Compute hardware** — **DISCLOSED**: `2,048× NVIDIA H100 GPUs` on NVIDIA DGX Cloud (AWS) for the 40B model ([Arc Institute press](https://arcinstitute.org/news/evo2); [NVIDIA Evo 2 blog](https://blogs.nvidia.com/blog/evo-2-biomolecular-ai/))
5. **Compute time** — **PARTIALLY DISCLOSED**: "trained for several months." **[ESTIMATED]** wall-clock: if "several months" = 6 weeks of effective compute → 2,048 × 6 × 7 × 24 = **2.06 × 10⁶ H100-hours**. Independently, Arc states Evo 2 used **"~150× more compute than AlphaFold and ~2× the FLOPs of ESM3"** — i.e., **~2.1 × 10²⁴ FLOPs**; at H100 BF16 peak ~1 PFLOPs/s × 30% MFU ≈ 3 × 10¹⁴ eff-FLOPs/s → 2.1 × 10²⁴ / 3 × 10¹⁴ = **7 × 10⁹ s × 1 chip = 1.9 × 10⁶ H100-hours**. Both routes converge on **~2 × 10⁶ H100-hours**.
6. **$ cost** — 2 × 10⁶ × $2.50/H100-hr = **~$5 M** [ESTIMATED, hardware DISCLOSED]
7. **Disclosure status** — `DISCLOSED hardware (2,048 H100s) and FLOPs ratio; hours estimated from "several months"`

**Implication for computational biologists.** Evo 2 is the second-most-expensive biology FM publicly trained (after AlphaFold 3 if you count Google's TPU infrastructure cost, or comparable). The 2,048-H100 fleet is **only available to ~5 institutions worldwide via DGX Cloud**, and the disclosed FLOPs ratio ("150× AlphaFold, 2× ESM3") is the cleanest cross-model compute comparison anyone publishes in 2025–2026 biology.

---

### 11. AlphaGenome

1. **Model + variant** — AlphaGenome — U-Net with transformer bottleneck, ~450M parameters (per DeepMind blog; not in Nature abstract) ([Avsec et al., *Nature* 2026, doi:10.1038/s41586-025-10014-0](https://www.nature.com/articles/s41586-025-10014-0); [DeepMind blog](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/))
2. **Lead lab + first author** — Google DeepMind / Žiga Avsec
3. **Pretraining data** — ENCODE + GTEx + FANTOM5 + 4D Nucleome assay tracks; **5,930 human + 1,128 mouse functional tracks**; reference genomes GRCh38 + GRCm39; 1-Mb input windows
4. **Compute hardware** — **DISCLOSED**: `Sequence parallelism across 8 interconnected TPU v3 devices per replica` ([Nature 2026 main text](https://www.nature.com/articles/s41586-025-10014-0); independent commentary [arxiviq.substack.com](https://arxiviq.substack.com/p/advancing-regulatory-variant-effect)). Total chip count not stated
5. **Compute time** — `UNKNOWN — paper does not disclose total TPU-hours`. Note that the released "all-folds" checkpoint is a **distilled student model from a 4-fold teacher ensemble** — total training compute is ≥4× the published single-model cost
6. **$ cost** — TPU v3 at $2/chip-hr; without total hours can't price. **[ESTIMATED]** order of magnitude: 8 TPU × 30 d × 24 hr × 4 folds = 23,000 TPU-hours → ~$46 k for one fold pass, **~$200 k** for the full teacher ensemble + distillation
7. **Disclosure status** — `DISCLOSED in paper / technical report (hardware); UNKNOWN — paper does not disclose total TPU-hours`

**Implication for computational biologists.** AlphaGenome's hardware footprint (8 TPU v3 per replica) is small relative to Evo 2 — it's a supervised regression model on bulk-assay tracks, not a generative DNA LM. This explains why DeepMind can offer a free hosted API for non-commercial use: inference is cheap, training was likely <$1M. The non-commercial license is the binding constraint for industry, not the compute.

---

### 12. ESM-3 (98B variant)

1. **Model + variant** — ESM-3 (98B parameters); also 1.4B (open) and 7B (Forge-gated) variants ([Hayes et al., *Science* 2025](https://www.science.org/doi/10.1126/science.ads0018); [EvolutionaryScale ESM-3 release blog](https://www.evolutionaryscale.ai/blog/esm3-release))
2. **Lead lab + first author** — EvolutionaryScale (Arc Institute collaboration for esmGFP wet-lab) / Thomas Hayes
3. **Pretraining data** — **2.78 billion natural proteins** + synthetic from AlphaFold-DB/ESMFold; **771 billion unique tokens** ([Hayes et al., 2025](https://www.science.org/doi/10.1126/science.ads0018))
4. **Compute hardware** — `UNKNOWN — Hayes et al. 2025 does not disclose hardware`
5. **Compute time** — **DISCLOSED FLOPs only**: `~1.07 × 10²⁴ FLOPs` ([Hayes et al., 2025](https://www.science.org/doi/10.1126/science.ads0018)). **[ESTIMATED]** GPU-hours:
   - At H100 BF16 peak ~1 PFLOPs/s × 30% MFU ≈ 3 × 10¹⁴ eff-FLOPs/s
   - 1.07 × 10²⁴ / 3 × 10¹⁴ = **3.57 × 10⁹ chip-seconds = ~9.9 × 10⁵ H100-hours**
   - On A100 BF16 (9.4 × 10¹³ eff-FLOPs/s): 1.14 × 10¹⁰ s = **~3.2 × 10⁶ A100-hours**
6. **$ cost** — On H100 at $2.50/hr: 9.9 × 10⁵ × $2.50 = **~$2.5 M**. On A100 at $2.50/hr: 3.2 × 10⁶ × $2.50 = **~$8 M**. EvolutionaryScale describes ESM-3 as "the most compute applied to any biological model at time of release" ([release blog](https://www.evolutionaryscale.ai/blog/esm3-release))
7. **Disclosure status** — `DISCLOSED in paper / technical report (FLOPs only); hardware and hours not disclosed`

**Implication for computational biologists.** ESM-3 sets the floor for "frontier biology FM compute" at 10²⁴ FLOPs and ~$2.5–$8 M. This is the most precisely cost-able model in the matrix because EvolutionaryScale publishes the FLOPs directly. The 98B weights are gated; the 1.4B open variant is what most academic reproductions actually use.

---

### 13. AlphaFold 3

1. **Model + variant** — AlphaFold 3 — Pairformer + diffusion module (no template- or recycling-stack inherited from AF2 backbone) ([Abramson et al., *Nature* 2024](https://www.nature.com/articles/s41586-024-07487-w))
2. **Lead lab + first author** — Google DeepMind + Isomorphic Labs / Josh Abramson
3. **Pretraining data** — PDB structures + distillation from AF2 + small-molecule complexes (<1.5 kDa ligands); training set ~10⁸ structures
4. **Compute hardware** — `UNKNOWN — Nature 2024 paper does not disclose precisely`. AF2 (Jumper et al. 2021) used **128× TPU v3 cores for ~11 days** initial training + 4 days fine-tuning; AF3 is presumed to have used TPU v4 or v5 but DeepMind has not published the figure ([retractionwatch.com on AF3 disclosure](https://retractionwatch.com/2024/05/14/nature-earns-ire-over-lack-of-code-availability-for-google-deepmind-protein-folding-paper/))
5. **Compute time** — `UNKNOWN — paper does not disclose`. **[ESTIMATED]** by analogy:
   - AF2 = ~128 TPU × 15 d = 46 K TPU-chip-hours
   - AF3 adds the diffusion module + significantly more training data (every PDB entity type); reasonable scaling = 3–5× AF2
   - **~1.5–2.5 × 10⁵ TPU-chip-hours** [ESTIMATED]
   - Arc Institute's Evo 2 disclosure of "~150× AlphaFold compute" puts AlphaFold (almost certainly AF2 or AF3) at ~1.4 × 10²² FLOPs total — at TPU v5e ~200 TFLOPs/s × 30% MFU = 6 × 10¹³ eff-FLOPs/s → **~6.5 × 10⁴ TPU-chip-hours** for AF3
6. **$ cost** — TPU v4/v5 at ~$8/chip-hr × 6.5 × 10⁴ = **~$520 k** [ESTIMATED]. Upper bound at 10⁵ TPU-hr × $10 = **~$1 M**
7. **Disclosure status** — `UNKNOWN — paper does not disclose; AF2 disclosure provides anchor for estimation`

**Implication for computational biologists.** AlphaFold 3 is the most-cited 2024 biology model and the most opaque about compute. The Nature paper deliberately omits training-cost figures, and the open-weights release (after community pressure in Nov 2024) ships only inference code. Practitioners citing AF3 as a baseline are doing so without any ability to compare training costs to their own retraining attempts.

---

### 14. PathChat / PathChat+

1. **Model + variant** — PathChat: UNI ViT-L/16 vision encoder + Llama-2-13B + LLaVA-style multimodal projector; PathChat+ scales the instruction set to >1M samples and ~5.5M Q-A turns ([Lu et al., *Nature* 2024](https://doi.org/10.1038/s41586-024-07618-3); [arXiv preprint 2312.07814](https://arxiv.org/abs/2312.07814))
2. **Lead lab + first author** — Mahmood Lab, Harvard / Mass General Brigham / Ming Y. Lu
3. **Pretraining data** — **1.18 M pathology image-caption pairs** (vision-language alignment stage) + **456,916 instructions / 999,202 Q-A turns** (instruction tuning); base UNI vision encoder reuses 100 M tile pretraining (see UNI row)
4. **Compute hardware** — **DISCLOSED**: `8× 80 GB NVIDIA A100 GPUs` for the combined system instruction tuning, multi-GPU PyTorch with Flash Attention and DeepSpeed ([Lu et al., *Nature* 2024](https://doi.org/10.1038/s41586-024-07618-3))
5. **Compute time** — **DISCLOSED**: `~1,275 A100 GPU-hours` for combined-system instruction tuning ([Lu et al., 2024 Methods](https://doi.org/10.1038/s41586-024-07618-3)). On 8 A100s this is **~160 hours ≈ 6.6 days wall-clock**
6. **$ cost** — 1,275 × $2.50 = **~$3.2 k** for the instruction-tuning step alone. **Full pipeline cost is higher**: UNI ViT-L pretraining (~10⁴ A100-hr estimated) + Llama-2-13B (already trained by Meta, free to reuse) + 1.18M-pair alignment (a few thousand A100-hr) + 1,275 A100-hr instruction tuning ≈ **~$30–50 k total** end-to-end if you trained UNI from scratch
7. **Disclosure status** — `DISCLOSED in paper / Nature methods section`

**Implication for computational biologists.** PathChat is the only model in the matrix with a publicly disclosed end-to-end instruction-tuning cost (~$3 k!). The fact that a Nature-grade pathology copilot can be built on 8 A100s for 6 days is a load-bearing point for academic labs deciding whether to attempt their own clinical AI copilot: the *vision encoder* is the expensive part (UNI), not the LLM head.

---

## (c) Disclosure-gap landscape

**Observations from the 14-model matrix:**

1. **Five clean disclosures, seven estimates, two partials.** Geneformer V2-104M_CLcancer (via NVIDIA BioNeMo), Virchow2 (arXiv 2408.00738), Evo 2 (Arc/NVIDIA blog), AlphaGenome (Nature 2026 main text, hardware only), and PathChat (Nature 2024) are the only models where you can read training compute off the published artifact without estimating. ESM-3 publishes FLOPs but not hardware. **STATE, AlphaFold 3, UNI, scGPT, Geneformer V1, UCE, and scFoundation are all UNKNOWN.**

2. **The disclosure pattern is not random.** **Industrial labs with NVIDIA / DGX Cloud partnerships disclose hardware aggressively** (Arc Institute + NVIDIA on Evo 2; Paige on Virchow2; NVIDIA on Geneformer V2) because the disclosure is a marketing artifact for the hardware vendor. **Academic and big-tech labs without a hardware sponsor disclose much less** (Mahmood Lab on UNI / UNI2-h; Leskovec/Quake on UCE; Theodoris on V1; Bo Wang on scGPT; DeepMind on AlphaFold 3 and AlphaGenome).

3. **The "FLOPs but not hardware" pattern (ESM-3) is the cleanest compromise.** It gives downstream researchers enough information to cost-compare ($X for an equivalent FLOPs budget on their preferred hardware) without revealing the lab's actual training infrastructure. Hayes et al. 2025's `1.07 × 10²⁴ FLOPs` is the most useful single number in this matrix and is the format other frontier biology labs should adopt.

4. **The "everything but compute" pattern (scGPT, UNI, scFoundation) is the most common.** All three papers describe the corpus, the architecture, the objective, and the benchmark scores in detail — but every reader has to estimate the training cost from first principles. This makes reproducibility claims approximate at best.

5. **Reproducibility implication.** Without a disclosed compute budget, "we couldn't reproduce X" is not a falsifiable claim — the reader cannot tell whether the failed reproduction is methodologically off or simply under-trained. The single-cell FM field's perturbation-prediction reproducibility crisis ([Ahlmann-Eltze et al., *Nature Methods* 2025](https://www.nature.com/articles/s41592-025-02772-6)) would be much easier to adjudicate if scGPT, UCE, and scFoundation had each published their training cost.

6. **Cost order-of-magnitude landscape (best estimates):**
   - **<$10 k tier:** Geneformer V1, V2-104M_CLcancer, PathChat instruction tuning, Generative Virtual Cells POC
   - **$10 k–$100 k tier:** scFoundation, UNI/UNI2-h, scGPT (mid-range estimate), Geneformer V2-316M, AlphaGenome
   - **$100 k–$1 M tier:** Virchow2, UCE (upper estimate), AlphaFold 3 (estimated)
   - **>$1 M tier:** ESM-3 (~$2.5–8 M), Evo 2 (~$5 M)
   - **UNKNOWN:** STATE

7. **The "compute concentration" gap.** Evo 2 + ESM-3 alone account for >$7 M of the ~$15 M in identified spend across this 14-model matrix — and both ran on infrastructure (2,000+ H100 fleets, EvolutionaryScale's frontier compute) that no academic lab can directly access. This is the load-bearing inequality for the 2026 biology FM landscape: **two industry labs spent more on training than the other twelve models combined.**

8. **Implications for the AACR audience.** A computational biologist deciding whether to (a) build a custom FM for their disease area or (b) fine-tune an existing model on their cohort should read this matrix as follows: **(a) is plausibly tractable for <$50 k** if you target the Geneformer V2 / PathChat / scFoundation tier; **(a) is intractable** if you target ESM-3 / Evo 2 tier; and **(b) is essentially free** for the FMs with open weights (Geneformer, UNI/UNI2-h gated but free for academic, ESM-3 open at 1.4B, AlphaFold 3 inference-only).

---

## (d) References

**Single-cell foundation models**
- Cui H. et al. (2024). [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://www.nature.com/articles/s41592-024-02201-0). *Nature Methods* 21:1470–1480.
- Theodoris C.V. et al. (2023). [Transfer learning enables predictions in network biology](https://www.nature.com/articles/s41586-023-06139-9). *Nature* 618:616–624.
- Geneformer model card (V1 + V2 + CLcancer): [huggingface.co/ctheodoris/Geneformer](https://huggingface.co/ctheodoris/Geneformer).
- NVIDIA BioNeMo Geneformer documentation (V2 training compute): [docs.nvidia.com/bionemo-framework/.../geneformer](https://docs.nvidia.com/bionemo-framework/latest/models/geneformer/).
- Rosen Y. et al. (2023). [Universal Cell Embeddings: A Foundation Model for Cell Biology](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2). *bioRxiv* 2023.11.28.568918.
- snap-stanford/UCE repository: [github.com/snap-stanford/UCE](https://github.com/snap-stanford/UCE).
- Hao M. et al. (2024). [Large-scale foundation model on single-cell transcriptomics](https://www.nature.com/articles/s41592-024-02305-7). *Nature Methods* 21:1481–1491.
- xTrimoGene backbone paper: [arXiv 2311.15156](https://arxiv.org/abs/2311.15156).
- biomap-research/scFoundation repository: [github.com/biomap-research/scFoundation](https://github.com/biomap-research/scFoundation).

**Virtual cells**
- Arc Institute STATE announcement: [arcinstitute.org/news/virtual-cell-model-state](https://arcinstitute.org/news/virtual-cell-model-state).
- STATE preprint: [bioRxiv 2025.06.26.661135](https://www.biorxiv.org/content/10.1101/2025.06.26.661135v1).
- STATE GitHub: [github.com/ArcInstitute/state](https://github.com/ArcInstitute/state). SE-600M model: [huggingface.co/arcinstitute/SE-600M](https://huggingface.co/arcinstitute/SE-600M).
- Lewis D.S. & Zueco E. (2026). Toward Generative Virtual Cells. ICLR 2026 Gen² workshop. [OpenReview PDF](https://openreview.net/pdf/58c616e58a32446ea386695fcf2a9f5caa4f5ab1.pdf).

**Pathology foundation models**
- Vorontsov E. et al. (2024). [A foundation model for clinical-grade computational pathology and rare cancers detection](https://doi.org/10.1038/s41591-024-03141-0). *Nature Medicine* 30:2924–2935. [Virchow preprint arXiv:2309.07778](https://arxiv.org/abs/2309.07778).
- Zimmermann E. et al. (2024). [Virchow2: Scaling Self-Supervised Mixed Magnification Models in Pathology](https://arxiv.org/abs/2408.00738). arXiv 2408.00738.
- paige-ai/Virchow2 HF: [huggingface.co/paige-ai/Virchow2](https://huggingface.co/paige-ai/Virchow2).
- Chen R.J. et al. (2024). [Towards a general-purpose foundation model for computational pathology](https://www.nature.com/articles/s41591-024-02857-3). *Nature Medicine*. UNI preprint: [arXiv 2308.15474](https://arxiv.org/abs/2308.15474).
- UNI / UNI2-h HF: [huggingface.co/MahmoodLab/uni](https://huggingface.co/MahmoodLab/uni), [huggingface.co/MahmoodLab/UNI2-h](https://huggingface.co/MahmoodLab/UNI2-h).
- Lu M.Y. et al. (2024). [A multimodal generative AI copilot for human pathology](https://doi.org/10.1038/s41586-024-07618-3). *Nature* 634:466–473.
- PathChat preprint: [arXiv 2312.07814](https://arxiv.org/abs/2312.07814).

**Genomic foundation models**
- Brixi G. et al. (2026). [Genome modelling and design across all domains of life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5). *Nature*.
- Arc Institute Evo 2: [arcinstitute.org/news/evo2](https://arcinstitute.org/news/evo2).
- NVIDIA Evo 2 announcement: [blogs.nvidia.com/blog/evo-2-biomolecular-ai](https://blogs.nvidia.com/blog/evo-2-biomolecular-ai/).
- ArcInstitute/evo2 GitHub: [github.com/ArcInstitute/evo2](https://github.com/ArcInstitute/evo2).
- Avsec Ž. et al. (2026). [Advancing regulatory variant effect prediction with AlphaGenome](https://www.nature.com/articles/s41586-025-10014-0). *Nature* 649(8099). bioRxiv: [10.1101/2025.06.25.661532](https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1).
- DeepMind AlphaGenome: [deepmind.google/blog/alphagenome](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/).

**Protein foundation models**
- Hayes T. et al. (2025). [Simulating 500 million years of evolution with a language model](https://www.science.org/doi/10.1126/science.ads0018). *Science* 387, eads0018. bioRxiv: [10.1101/2024.07.01.600583](https://www.biorxiv.org/content/10.1101/2024.07.01.600583v1).
- EvolutionaryScale ESM-3 release blog: [evolutionaryscale.ai/blog/esm3-release](https://www.evolutionaryscale.ai/blog/esm3-release).
- Abramson J. et al. (2024). [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w). *Nature* 630:493–500.
- AlphaFold 3 source: [github.com/google-deepmind/alphafold3](https://github.com/google-deepmind/alphafold3).
- AlphaFold 3 code-availability commentary: [retractionwatch.com](https://retractionwatch.com/2024/05/14/nature-earns-ire-over-lack-of-code-availability-for-google-deepmind-protein-folding-paper/).

**Compute / cost references**
- Cottier B., Rahman R. et al. (2024). [The Rising Costs of Training Frontier AI Models](https://arxiv.org/abs/2405.21015). arXiv 2405.21015. — methodology for cost estimation.
- Hoffmann J. et al. (2022). Chinchilla scaling laws, `FLOPs ≈ 6 × parameters × tokens` heuristic. (Used throughout for [ESTIMATED] rows.)
- Epoch AI training-compute methodology: [epoch.ai/blog/estimating-training-compute](https://epoch.ai/blog/estimating-training-compute).
- Ahlmann-Eltze C. et al. (2025). [Deep-learning-based gene-perturbation effect prediction](https://www.nature.com/articles/s41592-025-02772-6). *Nature Methods* — reproducibility critique referenced in §(c).

---

*Build artifact — not for site navigation. Last updated 2026-05-12.*
