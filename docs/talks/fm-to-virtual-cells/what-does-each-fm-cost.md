# What does each foundation model cost to train?

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). Answers the question someone asks during Act 1 or Act 2: "can a small lab even compete on training?" The short answer is no — but the longer answer shapes which lane is yours.*

## The headline

**$20k to $5M+** for the full training run of a frontier biology FM, as of May 2026. Geneformer V2-104M_CLcancer ($17k disclosed) is the cheapest fully-disclosed anchor model in our matrix; Evo2 ($5M, 2,048× H100 over months) is the most expensive disclosed. **Everything in between exists, but most labs disclose less than NVIDIA-co-authored ones do** — see the disclosure-correlates-with-sponsorship pattern below.

## The full matrix

| Model | Family | Params | GPU type × count | GPU-hours | $ (on-demand) | Disclosure | Source |
|---|---|---|---|---|---|---|---|
| **Geneformer V2-104M** | sc-FM | 104M | 64× A100 80GB | 6,656 | **~$17k** | ✅ DISCLOSED | NVIDIA BioNeMo recipe |
| Geneformer V2-316M | sc-FM | 316M | 128× A100 | 11,576 | ~$30k | ✅ DISCLOSED | NVIDIA BioNeMo recipe |
| Virchow2 | pathology | 632M | 512× V100 32GB | ~140,000 | **~$170k** | ✅ DISCLOSED | Zimmermann 2024 arXiv |
| Virchow2G | pathology | 1.85B | 512× V100 (same fleet) | ~280,000 | ~$340k | ✅ DISCLOSED | Zimmermann 2024 arXiv |
| **Evo2 (40B)** | genomic | 40B | 2,048× H100 | ~2,000,000 | **~$5M** | ✅ DISCLOSED | Brixi 2026 *Nature* + NVIDIA |
| **ESM-3 (98B)** | protein | 98B | (10²⁴ FLOPs disclosed) | ~990,000 H100-eq | $2.5M–$8M | ✅ DISCLOSED | Hayes 2025 *Science* |
| AlphaGenome | genomic | ~450M | 8× TPU v3 per replica × 4-fold ensemble + distill | UNKNOWN | ~$200k est. | ⚠️ partial | Avsec 2025 *Nature* |
| **scGPT** | sc-FM | 51M | UNKNOWN | 10³–10⁵ A100-h (50× band) | $2.6k–$250k est. | ❌ UNKNOWN | Cui 2024 *Nat Methods* |
| UNI2-h | pathology | 681M | UNKNOWN ("extensive A100") | ~30,000 est. | ~$75k est. | ❌ UNKNOWN | Chen 2024 HF card |
| UCE | sc-FM | 650M | UNKNOWN | 1,275–70,000 A100-h | $3k–$175k est. | ❌ UNKNOWN | Rosen 2024 *Nat Methods* |
| STATE | sc-FM | 600M SE + ST | UNKNOWN | unknown | ~$125k est. | ❌ UNKNOWN | Adduri 2025 bioRxiv |
| TranscriptFormer | sc-FM | 100M+ | UNKNOWN | unknown | unknown | ⚠️ partial | Pearce 2025 *Science* |
| Generative VC POC | sc-FM (POC) | tiny | 1× consumer GPU | <100 | **<$250** | ✅ DISCLOSED | Lewis & Zueco ICLR 2026 |

**Methodology**: FLOPs ≈ 6 × parameters × tokens (Chinchilla heuristic, Epoch AI 2024). Hours → cost at on-demand: A100 80GB ~$2.5/hr (DGX cloud), V100 32GB ~$1.20/hr, H100 ~$2.5–4/hr, TPU v3 ~$2/hr (vendor pricing).

## Four patterns the matrix makes visible

### 1. Disclosure correlates with hardware sponsorship

Every ✅ DISCLOSED entry has an NVIDIA / DGX-Cloud / TPU co-authorship or framework partnership. Academic labs *without* a hardware co-marketer disclose much less — that's structural, not random. Disclosure is itself a co-marketing artifact.

| ✅ DISCLOSED | Sponsor |
|---|---|
| Geneformer V2 | NVIDIA BioNeMo (Theodoris lab) |
| Virchow2 | Paige's V100 fleet |
| Evo2 | NVIDIA + DGX Cloud (Arc + NVIDIA paper) |
| ESM-3 | EvolutionaryScale's H100 fleet |
| AlphaGenome | Google TPU v3 (partial) |

| ❌ UNKNOWN | Lab |
|---|---|
| scGPT | Bo Wang lab (no hardware co-marketer) |
| UNI / UNI2-h | Mahmood lab |
| UCE | Leskovec + Quake / Stanford |
| STATE | Arc Institute (no co-author for this one) |

### 2. The $20k floor — what's the cheapest reproducible sc-FM training?

**Geneformer V2-104M_CLcancer**: 64× A100 80GB × 4d 8h = 6,656 A100-hours = **$16,640 on-demand**. Plus ~$3k for the 14M-cancer-cell continual-pretraining step. **$20k all-in, fully disclosed, NVIDIA BioNeMo recipe public.** This is the only published academic sc-FM training where a small lab can verify the cost from a complete recipe.

Everything below $20k is a POC (Lewis & Zueco, $250) or undisclosed. Everything above $20k that's *also disclosed* needs a hardware partner.

### 3. The $5M ceiling — what's the most expensive disclosed biology FM?

**Evo2 (40B)**: 2,048× H100 on NVIDIA DGX Cloud (AWS), "several months." ~2M H100-hours, ~$5M on-demand. Evo2's *Nature* paper explicitly discloses: "~150× more compute than AlphaFold, ~2× the FLOPs of ESM-3" — the cleanest cross-model compute ratio published in 2025–2026.

**ESM-3 (98B)**: 1.07 × 10²⁴ FLOPs disclosed as a single number in *Science*. Practitioners can cost-compare any equivalent FLOPs budget on their preferred hardware. EvolutionaryScale released this number as the field's compute reference point.

### 4. Pathology FMs are mid-tier ($75k–$340k) and disclose more than sc-FMs

The pathology family is the *transparency outlier*. Virchow2 / Virchow2G publish hardware count + patient-level provenance. UNI / UNI2-h hide compute behind "extensive A100 hours." This split is institutional: Paige (commercial spinout, needs hardware-disclosure for vendor trust) vs Mahmood lab (academic, no co-marketer).

## What this means for small-lab planning

**You cannot compete on pretraining.** $5M is concentrated at ~5 institutions worldwide. Even $170k (Virchow2) requires the V100 fleet a commercial pathology lab can muster. Academic single-cell labs without NVIDIA co-authorship cannot reproduce a frontier sc-FM training run from the published recipe.

**But the small-lab playbook isn't pretraining.** It's:

- **Lane 1 — frozen-embedding work** ($0–$500): inference-only, 1× consumer GPU, weeks.
- **Lane 2 — PEFT / LoRA / adapters** ($500–$5k): 1–8× A100 for days, 2–4 months. The adapter is the contribution; the pretraining is rented.
- **Lane 3 — domain-specific small FM** ($10k–$50k): the Geneformer V2-104M_CLcancer playbook on your disease area. 6–12 months.
- **Lane 4 — replication / critique** ($0–$2k): inference + linear regression. Ahlmann-Eltze retired the entire sc-FM perturbation-prediction leaderboard at <$2k.

See [the main talk's Act 3 § 3.1](../fm-to-virtual-cells.md#31-the-9-application-lanes-budget-tier-overview) for the full 9-lane budget tier overview.

## How to read a compute claim

When you see a paper claiming an FM cost X to train, check:

1. **DISCLOSED vs ESTIMATED vs UNKNOWN.** Did the authors state the GPU count, hours, and hardware type? If they only said "extensive A100 hours," that's UNKNOWN — back-of-envelope estimates have wide uncertainty bands.
2. **Single run or many?** Frontier training runs often retry. The reported cost is usually the *successful* run. If a paper says "we trained on 64 A100s for a week" but doesn't say how many failed runs preceded it, multiply by 2–10× for true total cost.
3. **Inference cost vs training cost.** Some papers conflate them. Training is one-time and expensive; inference is per-use and cheap. For Lane 1 (frozen embeddings), only inference matters.
4. **Pretraining cost vs fine-tuning cost.** If the paper reports "$X to train," check whether that's pretraining only or includes downstream fine-tuning. Fine-tuning is usually 10–100× cheaper than pretraining.
5. **Software stack.** NVIDIA BioNeMo, JAX, MosaicML, etc. each have different cost profiles per FLOP. A NVIDIA-co-authored paper with BioNeMo recipe is the most reproducible disclosure pattern.

## Where to go next

- **[The main talk page](../fm-to-virtual-cells.md)** — full 5-act outline.
- **[Supplementary §D — compute & resources matrix](../fm-to-virtual-cells-supplementary.md#d-compute-resources)** — fuller resources table with arithmetic.
- **[`_resources-matrix.md`](../_resources-matrix.md)** — full compute / cost / team / data matrix with DISCLOSED / ESTIMATED / UNKNOWN tags and arithmetic shown.
- **[NVIDIA BioNeMo training recipes](https://github.com/NVIDIA/bionemo-framework)** — the only public training-cost reproduction recipe for Geneformer V2.
- **[Epoch AI training-compute methodology](https://epoch.ai/blog/estimating-training-compute)** — the FLOPs ≈ 6 × params × tokens heuristic.
- **[Cottier et al. 2024 *arXiv*](https://arxiv.org/abs/2405.21015)** — "The Rising Costs of Training Frontier AI Models" — the methodology this corpus follows.

---

*Last updated 2026-05-13.*
