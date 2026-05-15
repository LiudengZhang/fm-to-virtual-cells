# Protein-LM explainability — a review

> *[Adjacent methods](index.md) resource for the [FM-to-Virtual-Cells talk](../../fm-to-virtual-cells.md). Hunklinger & Ferruz, "Towards the explainability of protein language models", [*Nat Mach Intell* 2026](https://doi.org/10.1038/s42256-026-01232-w).*

## What it is

A review of interpretability and explainability methods for protein language models — attention analysis, probing classifiers, sparse autoencoders (SAEs), and the rest of the toolkit for asking *what a protein FM has actually learned*. It is the protein-side survey of the same question the talk raises for single-cell FMs.

## How it connects to the talk

The talk's [mechanistic-interpretability thread](../paper-map.md) — the teal cluster in the paper map — is the satisfying ending of Act 1: the *mechanism* behind the reckoning. The key sc-FM finding ([Simon & Zou](../why-linear-baselines-win.md#cause-4-what-sc-fms-actually-encode)) is that single-cell FMs encode cell-type and pathway features but **minimal regulatory logic**.

That whole wave started on the protein side — [Adams et al. 2025 *PNAS*](../paper-map.md) applied SAEs to protein FMs first, and the sc-FM SAE papers followed. This review is the protein-side state of the art for the same toolkit:

- It is the **methods reference** for the interpretability cluster — what techniques exist, what they can and can't show.
- It is the **comparison baseline** — protein FMs are the most-studied biology FMs for interpretability, so "what works on protein LMs" sets expectations for what should work on sc-FMs.
- It reinforces the talk's point that interpretability is now a *family-spanning* research program, not a single-cell curiosity.

## Why it's adjacent, not core

A review, and protein-FM-focused rather than single-cell — so it is a resource page, not a paper-map node. But it is the right citation for anyone running the [Track 1 mechanistic-interpretability project](../../fm-to-virtual-cells-supplementary.md#c1-track-1-mechanistic-interpretability): it tells you which interpretability methods have a track record before you point them at a cancer sc-FM.

## Read more

- **[Hunklinger & Ferruz 2026 *Nat Mach Intell* — Towards the explainability of protein language models](https://doi.org/10.1038/s42256-026-01232-w)** — the paper.
- [Why do linear baselines win? — Cause 4](../why-linear-baselines-win.md#cause-4-what-sc-fms-actually-encode) — the sc-FM interpretability finding this mirrors.
- [The paper map — Pass 7](../paper-map.md) — the mechanistic-interpretability reading pass.

---

*Last updated 2026-05-14.*
