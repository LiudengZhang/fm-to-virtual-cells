# Genome language models — a review

> *[Adjacent methods](index.md) resource for the [FM-to-Virtual-Cells talk](../../fm-to-virtual-cells.md). Consens, Dufault, Wainberg et al., "Transformers and genome language models", [*Nat Mach Intell* 2025, 7:346–362](https://doi.org/10.1038/s42256-025-01007-9).*

## What it is

A review of how transformer architectures have been applied to DNA — the **genome language model** (gLM) family. It covers tokenization choices (single nucleotides, k-mers, byte-level), the architectural variants used to handle very long genomic context, the pretraining objectives, and the downstream tasks (variant-effect prediction, regulatory-element annotation, generative genome design). It is the orientation read for the genomic corner of the foundation-model world.

## How it connects to the talk

The talk treats genomic FMs as **one of the five FM families**, and several of them are anchor models or paper-map nodes:

- **AlphaGenome**, **Evo 2**, **Nucleotide Transformer**, **DNABERT-2**, **HyenaDNA**, **Enformer**, **Caduceus** — all appear in the [model glossary](../model-glossary.md) and most in the [paper map](../paper-map.md)'s "other-family FM" cluster.

This review is the connective tissue for that cluster: it explains *why* the genomic family splits the way the talk says it does (track-prediction à la AlphaGenome vs generative à la Evo 2), and it gives the tokenization vocabulary needed to compare a gLM to a single-cell FM fairly. When the talk argues that **tokenization choice defines a family**, this review is the genomic-side evidence.

## Why it's adjacent, not core

It is a review, not a model — no paper-map node. But it is the single best background citation for anyone whose project touches the genomic family, and it pairs naturally with the [transformers-vs-state-space-models review](transformers-vs-state-space.md) for the architecture half of the story.

## Read more

- **[Consens et al. 2025 *Nat Mach Intell* — Transformers and genome language models](https://doi.org/10.1038/s42256-025-01007-9)** — the paper.
- [What is a foundation model?](../what-is-a-foundation-model.md) — the five-families taxonomy genomic FMs sit in.
- [The model glossary — genomic FMs](../model-glossary.md#genomic-foundation-models) — one-liners for the models this review surveys.

---

*Last updated 2026-05-14.*
