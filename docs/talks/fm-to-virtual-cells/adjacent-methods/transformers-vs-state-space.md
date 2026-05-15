# Transformers vs state-space models — a review

> *[Adjacent methods](index.md) resource for the [FM-to-Virtual-Cells talk](../../fm-to-virtual-cells.md). Tiezzi, Casoni, Betti et al., "Back to recurrent processing at the crossroad of transformers and state-space models", [*Nat Mach Intell* 2025, 7:678–688](https://doi.org/10.1038/s42256-025-01034-6).*

## What it is

A review of the architectural middle ground between transformers, classical recurrent networks, and modern state-space models (SSMs). It works through the trade-offs — quadratic attention vs linear-time recurrence, parallel training vs sequential inference, how each handles very long context — and argues that recurrent/state-space processing is back on the table as a serious alternative to pure attention.

## How it connects to the talk

This is the architecture-debate background for one of the reckoning's four causes. **[Cause 2 of "why linear baselines win"](../why-linear-baselines-win.md#cause-2-the-architecture-inherits-nlp-not-biology)** is that single-cell FMs *inherited the transformer from NLP* — a sequential, dense, ordered-token architecture — and applied it to sparse, unordered, biologically-structured data.

The 2026 architectural response in the talk is partly about *leaving the transformer behind*:

- **xVERSE** is explicitly transcriptomics-native — a non-language-model architecture that the talk cites as the first evidence the architectural choice is load-bearing.
- **HyenaDNA** and **Caduceus**, in the genomic family, are state-space models — exactly the architecture class this review covers.

So when the talk says "not every FM is transformer-shaped, and that matters," this review is the general-ML grounding for *why* SSMs and recurrent processing are credible alternatives, not fringe choices.

## Why it's adjacent, not core

A general-ML architecture review — not biology-specific, not a model — so it is a resource page rather than a paper-map node. But it is the citation to reach for when defending the architectural-response thread: the claim "the transformer was a borrowed default, and there are real alternatives" is one this review backs up.

## Read more

- **[Tiezzi et al. 2025 *Nat Mach Intell* — Transformers and state-space models](https://doi.org/10.1038/s42256-025-01034-6)** — the paper.
- [Why do linear baselines win? — Cause 2](../why-linear-baselines-win.md#cause-2-the-architecture-inherits-nlp-not-biology) — the talk's architecture critique.
- [Genome language models](genome-language-models.md) — the companion review for the genomic-FM architectures.

---

*Last updated 2026-05-14.*
