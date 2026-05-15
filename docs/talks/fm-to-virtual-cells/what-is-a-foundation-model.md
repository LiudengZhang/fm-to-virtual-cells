# What is a foundation model — and how do we categorize them?

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). Answers the question someone asks during Act 2 when you say "the five FM families."*

## The one-line definition

A **foundation model (FM)** is a neural network pretrained on a large, general substrate that can then be adapted to many downstream tasks — by fine-tuning, prompting, or used as a frozen encoder. The "foundation" part: the pretraining is the load-bearing investment; everything downstream inherits it.

In biology this means: train once on millions of cells / billions of base pairs / hundreds of thousands of slides; then use the pretrained representation for cell-type classification, perturbation prediction, variant-effect prediction, protein-binder design, or pathology slide interpretation.

## The five families — at a glance

| Family | What's tokenized | Anchor models | Substrate scale | 2026 status |
|---|---|---|---|---|
| **Single-cell** | Genes + cells as tokens (or cells as ordered gene rankings) | scGPT, Geneformer, UCE, scFoundation, CellPLM, TranscriptFormer | 33M–112M cells | In crisis — re-evaluating perturbation prediction post-reckoning |
| **Pathology** | H&E (or H&E + IHC) tiles → embeddings → slide-level aggregation | UNI, Virchow / Virchow2, CHIEF, Prov-GigaPath, PathChat, TITAN | 200M–2B tiles, 100k–350k slides | Healthiest — plateauing around ViT-H/14; FDA paths open |
| **Genomic** | DNA bases or k-mers | Nucleotide Transformer, DNABERT-2, HyenaDNA, AlphaGenome, Evo2 | 8B–9T tokens | Split — track-prediction (AlphaGenome) vs generative (Evo2) |
| **Protein** | Amino-acid sequences + structure tokens | ESM-2, ESM-3, AlphaFold 3, Proteina Complexa | 2.78B proteins, 771B tokens (ESM-3) | Maturing — Proteina Complexa hits 63.5% wet-lab hit rate on PDGFR |
| **Multimodal / vision-language** | Image + text co-tokenized; medical-imaging or biology Q&A | BioMedCLIP, PathChat-2, MedAgentGym, Med-Gemini | >1M instruction pairs | Closest to clinical deployment — PathChat DX FDA Breakthrough |

## Why these five?

Each family is defined by **what's tokenized**. The tokenization choice determines what the model can attend over, which determines what tasks it can solve.

- **Single-cell**: tokens are genes (scGPT, scFoundation) or rankings of genes (Geneformer) or cells as sequences. The model attends over the transcriptome.
- **Pathology**: tokens are image patches (224×224 H&E tiles). The model attends over a slide.
- **Genomic**: tokens are nucleotides (Evo2) or k-mers (DNABERT). The model attends over DNA sequence.
- **Protein**: tokens are amino acids plus optional structure (ESM-3's 7 token tracks). The model attends over a protein.
- **Multimodal**: tokens are images + text co-encoded. The model attends across modalities.

**What's NOT a foundation family**: dedicated diagnostic models (e.g., DeepVariant), traditional sklearn pipelines, classical deep-learning models for one task. The "foundation" criterion is *pretraining at scale on a general substrate that then transfers to many tasks*.

## What makes the single-cell family different?

The single-cell family is where the talk lives, and where the 2025 reckoning happened. Three structural features distinguish it from the others:

1. **The substrate is sparser.** A cell has ~2,000–10,000 detected genes (out of ~20,000 protein-coding genes in human). That's >50% sparsity. Pathology tiles are dense pixel arrays; DNA is a dense sequence; proteins are dense sequences. Single-cell expression is genuinely sparse — and modeling that sparsity is non-trivial.
2. **The downstream task is causal, not perceptual.** Pathology FMs predict "what is this tissue?" (perception). Single-cell FMs are asked to predict "what would happen if I perturbed gene X?" (causal counterfactual). The 2025 reckoning is essentially the discovery that the second task is much harder than the first.
3. **The training corpora are skewed.** CELLxGENE Census is ~70% Anglophone sequencing centers. Tahoe-100M is 50 immortalized cell lines. Cross-donor and cross-cell-type generalization is barely measured because the substrate to measure it doesn't exist at scale.

## Why does the "foundation model" framing matter?

Three reasons:

1. **Compute amortization.** Pretraining costs $20k–$5M; downstream use is a few hundred dollars. The economics of academic biology change when the heavy lift is a one-time cost paid by Arc Institute / DeepMind / EvolutionaryScale.
2. **Transfer learning is the only path for most clinical tasks.** Rare cancers, rare cell types, rare donors — none have enough labeled data to train a deep model from scratch. Frozen-embedding + small classifier (Lane 1) is the small-lab winning pattern *because* it inherits the pretraining.
3. **The license layer matters.** Open weights (Apache-2.0 / MIT) unlock commercial use; CC-BY-NC + HF gating restricts it. **The bifurcation is by family**: sc-FMs uniformly permissive; pathology FMs uniformly restrictive; genomic FMs split. Track licenses carefully — UNI's Jan 2025 HF gating shift is the cautionary tale.

## Common misconceptions

**"Foundation model = transformer."** Most current biology FMs are transformer-based, but the category doesn't require it. State-space models (HyenaDNA, Caduceus) and graph-augmented transformers count if they meet the pretrain-once-adapt-many criterion. The 2026 xVERSE paper explicitly argues for *transcriptomics-native* (non-transformer) architectures.

**"Bigger model = better FM."** Geneformer V2-104M_CLcancer matches the 316M general-domain model at ⅓ the compute. xVERSE beats LM-derived sc-FMs by 17.9%. **Domain curation and architectural choice often beat parameter count** in biology — different from NLP, where scale tends to win.

**"FMs are universally better than classical methods."** False in single-cell as of May 2026. Linear baselines (`mean-of-training-perturbations`, `latent-additive + scGPT-embeddings`) beat every published sc-FM on perturbation prediction. See [Why do linear baselines win?](why-linear-baselines-win.md).

**"FMs and agentic AI are competing paradigms."** They're complementary. Agents *use* FMs (PathChat-DX = LLM agent calling pathology FM as a tool); agents *train* FMs (VCHarness — autonomous virtual-cell-builder); agents *reason over* FMs (rBio — Qwen post-trained on TranscriptFormer as verifier). See [How agentic AI meets foundation models](agentic-meets-foundation.md).

## Where to go next

- **[The main talk page](../fm-to-virtual-cells.md)** — full 5-act outline.
- **[The model glossary](model-glossary.md)** — every FM named in the talk, one sentence each, grouped by family.
- **[Supplementary §A — the 11 anchor model dossiers](../fm-to-virtual-cells-supplementary.md#a-model-dossiers-the-11-anchor-models)** — full per-model resources / framework / unique features / gaps exposed.
- **[What does each FM cost?](what-does-each-fm-cost.md)** — the disclosure landscape.
- **[Foundation Models cross-vault index](../../foundation-models.md)** — every FM page across all conference vaults.

---

*Last updated 2026-05-13.*
