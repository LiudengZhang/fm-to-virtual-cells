# The model glossary — every FM in the talk, one sentence each

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). The flat quick-reference: every foundation model and virtual cell named anywhere in the talk corpus, one sentence apiece, grouped by family. When a name comes up mid-prep and you just need "what is that again," look here. For the deep version of the 11 anchor models — resources, framework, unique feature, gap exposed — see [supplementary §A](../fm-to-virtual-cells-supplementary.md#a-model-dossiers-the-11-anchor-models).*

Models marked **★** are the talk's 11 anchor models and link to their full dossier.

## Single-cell foundation models & virtual cells

- **scGPT ★** — the sc-FM that defined the category: first to tokenize both genes *and* cells, enabling cross-cell and cross-gene attention ([§A.1](../fm-to-virtual-cells-supplementary.md#a1-scgpt-cui-et-al-nature-methods-2024)).
- **Geneformer V2 ★** — encoder-only BERT with rank-based tokenization; the 104M cancer-curated variant matches the 316M general model at ⅓ the compute, killing the "scale wins" narrative ([§A.2](../fm-to-virtual-cells-supplementary.md#a2-geneformer-v2-huggingface-dec-2024-update-of-theodoris-et-al-nature-2023)).
- **UCE (Universal Cell Embedding) ★** — the cross-species sc-FM: handles 8 species in one embedding space by bridging through ESM2 protein embeddings ([§A.3](../fm-to-virtual-cells-supplementary.md#a3-uce-universal-cell-embedding-rosen-et-al-biorxiv-2023-nature-methods-2024)).
- **STATE ★** — Arc Institute's Tahoe-100M-native virtual cell: a State Embedding module plus a State Transition module that predicts perturbation outcomes, the first production virtual cell at 100M-cell scale ([§A.4](../fm-to-virtual-cells-supplementary.md#a4-state-arc-institute-2025)).
- **TranscriptFormer ★** — CZ Biohub's first generative cross-species sc-FM, trained on 112M cells across 12 species spanning 1.53B years of evolution ([§A.5](../fm-to-virtual-cells-supplementary.md#a5-transcriptformer-pearce-et-al-science-2025-cz-biohub)).
- **Generative Virtual Cells ★** — a workshop proof-of-concept (<$250 compute) demonstrating the design pattern: a joint planner + world model updated under validation gating, not offline-trained on a frozen snapshot ([§A.6](../fm-to-virtual-cells-supplementary.md#a6-generative-virtual-cells-lewis-zueco-iclr-2026-gen2-workshop)).
- **scFoundation** — large sc-FM (BioMap) notable for read-depth-aware attention; one of the four models the 2025 reckoning repeatedly tested and found wanting on perturbation prediction.
- **CellPLM** — cell-as-token sc-FM (Wen et al., ICLR 2024) that, with scTab, beats scGPT and Geneformer on cell-typing at 10–20× less training cost.
- **scBERT** — the early BERT-style single-cell model that pre-dated the 2023 sc-FM wave; mostly of historical interest now.
- **scMulan** — a multitask single-cell language model; one of the seven scFMs benchmarked in CellBench-LS.
- **GenePT / scELMo** — not trained sc-FMs at all: frozen LLM embeddings of gene *names* plus a logistic-regression head (~$200 compute) that match or beat scGPT zero-shot on cell-type annotation.
- **xVERSE** — the 2026 architectural response: a transcriptomics-native (non-language-model) sc-FM that beats LM-derived sc-FMs by 17.9% on representation and resolves rare cell types from as few as 4 cells.
- **TxPert** — Wenkel et al.'s *Nature Biotechnology* 2026 perturbation-prediction model using multiple knowledge graphs as the inductive bias — "the reckoning answering itself," since Wenkel co-authored the 2025 `latent-additive` critique.
- **MAP** — a knowledge-driven sc-FM offering zero-shot prediction for unprofiled drugs; a 2026 exemplar of biology-specific inductive bias.
- **Nicheformer** — Theis lab's spatial-omics sc-FM (~80M params, ~110M dissociated + spatial cells, ~$25k) trained with a niche-aware objective.
- **CellFM** — a single-cell foundation model from Zhang et al. (*Nature Communications* 2025).
- **scPRINT** — Kalfon et al.'s sc-FM (*Nat Commun* 2025) pretrained on 50M cells, aimed specifically at robust zero-shot gene-network inference rather than perturbation prediction.
- **scPRINT-2** — the bioRxiv 2025.12 successor (Kalfon, Peyré & Cantini), pitched as a next-generation cell FM *and* a benchmark suite for evaluating them.

## Pathology foundation models

- **Virchow2 ★** — the current pathology-FM SOTA and the most hardware-transparent: a 632M-param ViT-H/14 trained on ~2B H&E/IHC tiles from ~225k patients ([§A.7](../fm-to-virtual-cells-supplementary.md#a7-virchow2-paige-msk-zimmermann-et-al-arxiv-240800738)).
- **UNI2-h ★** — the Mahmood-stack flagship tile encoder (681M params) and the opaque counterpoint to Virchow2; HF-gated since Jan 2025 ([§A.8](../fm-to-virtual-cells-supplementary.md#a8-uni2-h-mahmood-lab-jan-14-2025-update-of-chen-et-al-nature-medicine-2024)).
- **UNI** — the original Mahmood-lab pathology tile encoder (*Nature Medicine* 2024), predecessor of UNI2-h.
- **Virchow / Virchow2G** — the Paige + MSK pathology FM line: Virchow is the V1 tile encoder; Virchow2G is the 1.85B-param scale-up on the same fleet.
- **CHIEF** — a pathology FM for cancer detection and prognosis across tissue types.
- **Prov-GigaPath** — a whole-slide pathology FM (Microsoft + Providence) trained on real-world clinical slides.
- **Phikon / Phikon-v2** — Owkin's pathology FMs, notable as Apache-2.0 exceptions in a family that is otherwise license-restrictive.
- **H-optimus-0** — Bioptimus's open-weights pathology tile encoder, another permissive-license exception.
- **Hibou** — an open pathology FM (Apache-2.0).
- **CONCH** — a contrastive vision-language pathology FM from the Mahmood lab.
- **TITAN** — the slide-level model in the Mahmood vertical stack, sitting above the UNI2-h tile encoder.
- **PathChat / PathChat-2 / PathChat-DX** — the Mahmood lab's vision-language pathology assistant; PathChat-DX is the first generative-AI pathology tool with FDA Breakthrough Designation (Jan 2025).

## Genomic foundation models

- **AlphaGenome ★** — DeepMind's variant-effect SOTA: a single U-Net + transformer model that wins 25/26 regulatory variant-effect benchmarks at 1-Mb context ([§A.9](../fm-to-virtual-cells-supplementary.md#a9-alphagenome-deepmind-avsec-et-al-nature-2025)).
- **Evo2 ★** — Arc + NVIDIA's generative genomic FM (7B/40B params, ~$5M training): the only genomic FM with demonstrated in-context learning and a 1M-token context ([§A.10](../fm-to-virtual-cells-supplementary.md#a10-evo2-arc-institute-nvidia-stanford-ucb-ucsf-brixi-et-al-nature-2026)).
- **Nucleotide Transformer** — an early DNA foundation model (InstaDeep) pretrained across many genomes for variant and regulatory tasks.
- **DNABERT-2** — a BPE-tokenized DNA FM, the efficiency-focused successor to the original DNABERT.
- **HyenaDNA** — a state-space (non-transformer) genomic FM built for very long context at single-nucleotide resolution.
- **Caduceus** — a bidirectional, reverse-complement-equivariant state-space DNA FM for long-range genomic tasks.
- **Enformer** — the pre-FM-era DeepMind model predicting gene expression from sequence via attention; one of the single-task models AlphaGenome replaces.
- **Borzoi** — Calico's RNA-seq-coverage prediction model, an Enformer successor, also subsumed by AlphaGenome's single-model approach.

## Protein foundation models

- **ESM-3 ★** — EvolutionaryScale's 98B-param multimodal protein FM with 7 token tracks; generated esmGFP de novo and sets the cleanest compute-disclosure benchmark in biology FMs ([§A.11](../fm-to-virtual-cells-supplementary.md#a11-esm-3-evolutionaryscale-hayes-et-al-science-2025)).
- **ESM-2** — the open-weights predecessor protein language model; still the workhorse for most academic reproductions.
- **ESMFold** — the ESM-2-based structure predictor: fast single-sequence folding without an MSA.
- **AlphaFold 3** — DeepMind / Isomorphic's structure predictor extended to complexes — proteins with nucleic acids, ions, and ligands.
- **Proteina / Proteina Complexa** — generative protein-design FMs; Proteina Complexa reports a 63.5% wet-lab hit rate on a PDGFR binder-design task.

## Multimodal / vision-language

- **BioMedCLIP** — a biomedical image–text contrastive model trained on large-scale figure–caption pairs.
- **Med-Gemini** — Google's medical multimodal model family for clinical reasoning and medical-image Q&A.

## Agentic systems built *on* foundation models

*Not foundation models themselves, but they recur throughout the talk because the 2026 story is agentic AI and FMs converging.*

- **rBio** — a Qwen model post-trained to *reason over* a virtual cell, using TranscriptFormer as a verifier.
- **VCHarness** — an autonomous agent that *builds* virtual-cell models end to end.
- **CellVoyager** — an agent that *analyzes* single-cell data autonomously (*Nature Methods* 2026).
- **MedAgentGym** — an agentic environment / benchmark for training and evaluating medical AI agents.
- **PathChat-DX** — an LLM agent that calls a pathology FM as a tool; the clearest example of "agents use FMs."

## Where to go next

- **[The paper map](paper-map.md)** — the interactive literature network + a systematic reading order for the papers behind these models.
- **[Supplementary §A — the 11 anchor model dossiers](../fm-to-virtual-cells-supplementary.md#a-model-dossiers-the-11-anchor-models)** — full resources / framework / unique feature / gap-exposed for the starred models.
- **[What is a foundation model?](what-is-a-foundation-model.md)** — the five-families taxonomy these models sort into.
- **[What does each FM cost?](what-does-each-fm-cost.md)** — the compute-disclosure landscape.
- **[Why do linear baselines win?](why-linear-baselines-win.md)** — why the single-cell family is in crisis.
- **[Foundation Models cross-vault index](../../foundation-models.md)** — every FM page across all conference vaults.

---

*Last updated 2026-05-14.*
