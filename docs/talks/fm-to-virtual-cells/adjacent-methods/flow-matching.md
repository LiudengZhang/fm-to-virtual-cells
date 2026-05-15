# Flow matching in computational biology

> *[Adjacent methods](index.md) resource for the [FM-to-Virtual-Cells talk](../../fm-to-virtual-cells.md). Morehead, Atanackovic, Hegde et al., "Flow matching for generative modelling in bioinformatics and computational biology", [*Nat Mach Intell* 2026, 8:517–534](https://doi.org/10.1038/s42256-026-01220-0).*

## What it is

Flow matching is a generative-modelling technique — a training objective for learning a continuous transformation from a simple noise distribution to a complex data distribution. It is the close cousin of diffusion models, but typically simpler to train and faster to sample from. This paper is a **review**: it surveys how flow matching is being applied across bioinformatics and computational biology — molecular structure generation, protein design, single-cell trajectory and perturbation modelling, and more.

## How it connects to the talk

The talk's framing of a *virtual cell* is increasingly a **generative** one — a model you can sample from to ask "what would this cell look like under perturbation X." Several of the models in the [paper map](../paper-map.md) are generative by design:

- **TranscriptFormer** is a generative cross-species sc-FM.
- **Generative Virtual Cells** is explicitly a generative design pattern.
- The broader virtual-cell goal in [Bunne et al.](../paper-map.md) is a model you can run forward to predict cell state.

Flow matching is one of the main engines under that hood. Knowing the technique matters for reading those papers critically — and for the small-lab [Lane 8](../../fm-to-virtual-cells-supplementary.md#b8-lane-8-fm-as-generative-data-augmentation-engine-02k-new-2026) (FM as a generative data-augmentation engine), where the generative method's sampling quality is the whole ballgame.

## Why it's adjacent, not core

It is a *technique review*, not a foundation model and not a single algorithm — so it does not earn a node in the paper map. But it is the right background read before you evaluate any claim that a generative virtual cell "samples realistic cells": the realism depends on the generative objective, and flow matching is now one of the default choices.

## Read more

- **[Morehead et al. 2026 *Nat Mach Intell* — Flow matching review](https://doi.org/10.1038/s42256-026-01220-0)** — the paper.
- [What is a foundation model?](../what-is-a-foundation-model.md) — where generative sc-FMs sit in the family taxonomy.
- [How agentic AI meets foundation models](../agentic-meets-foundation.md) — generative world-models inside agentic virtual-cell loops.

---

*Last updated 2026-05-14.*
