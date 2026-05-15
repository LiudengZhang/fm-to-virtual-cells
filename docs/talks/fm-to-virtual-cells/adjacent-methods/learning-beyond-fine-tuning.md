# Learning beyond fine-tuning

> *[Adjacent methods](index.md) resource for the [FM-to-Virtual-Cells talk](../../fm-to-virtual-cells.md). Zheng, Shen, Tang et al., "Learning from models beyond fine-tuning", [*Nat Mach Intell* 2025, 7:6–17](https://doi.org/10.1038/s42256-024-00961-0).*

## What it is

A review of the ways you can build on a pretrained model **without** the default move of full fine-tuning. It maps the landscape: parameter-efficient adaptation (adapters, LoRA, prompts), knowledge distillation, model reuse and merging, using a model as a frozen feature extractor, and learning *from* a model's outputs rather than its weights. The unifying point: a pretrained model is a reusable asset, and fine-tuning is only one — often the most expensive — way to cash it in.

## How it connects to the talk

This is the methods map behind **Act 3 of the talk** — the small-lab lanes. The talk's whole "how does a lab without a $5M GPU budget ship FM-area work" argument is, mechanically, a question of *learning beyond fine-tuning*:

- **[Lane 1](../../fm-to-virtual-cells-supplementary.md#b1-lane-1-fm-embeddings-as-features-0500)** — FM embeddings as frozen features. This is "model as feature extractor" from the review.
- **[Lane 2](../../fm-to-virtual-cells-supplementary.md#b2-lane-2-peft-lora-adapters-5005k)** — PEFT / LoRA / adapters. This is "parameter-efficient adaptation" from the review.
- The talk's recurring finding — [GenePT/scELMo](../model-glossary.md) matching scGPT zero-shot for ~$200 — is a "learn from the model's outputs, not its weights" result.

So the review is the general-ML backbone for the talk's economic argument: the reason a small lab *can* compete is that fine-tuning is not the only adaptation path, and the cheaper paths are often competitive.

## Why it's adjacent, not core

General machine-learning, not biology-specific and not a foundation model — it earns a resource page, not a paper-map node. But it is the right citation when someone asks "why is Lane 1 a real strategy and not just a shortcut": the answer is that the adaptation-methods literature says frozen-feature reuse is a first-class technique, not a compromise.

## Read more

- **[Zheng et al. 2025 *Nat Mach Intell* — Learning from models beyond fine-tuning](https://doi.org/10.1038/s42256-024-00961-0)** — the paper.
- [Supplementary §B — the 9 small-lab application lanes](../../fm-to-virtual-cells-supplementary.md#b-lane-dossiers-the-9-small-lab-application-lanes) — the lanes this review underpins.
- [What does each FM cost?](../what-does-each-fm-cost.md) — why the cheap adaptation paths matter economically.

---

*Last updated 2026-05-14.*
