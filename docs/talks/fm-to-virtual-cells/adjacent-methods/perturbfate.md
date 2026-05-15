# PerturbFate — mapping convergent regulators of drug resistance

> *[Adjacent methods](index.md) resource for the [FM-to-Virtual-Cells talk](../../fm-to-virtual-cells.md). Xu, Lu, Ugurbil et al., "Mapping convergent regulators of melanoma drug resistance by PerturbFate", [*Nature* 2026](https://doi.org/10.1038/s41586-026-10367-0).*

## What it is

PerturbFate is a perturbation-screening method that asks which gene perturbations *change a cell's fate* under drug pressure — specifically, which regulators drive melanoma cells into a drug-resistant state. It pairs a pooled genetic screen with a readout of cell state/fate, so the output is not just "this perturbation kills cells" but "this perturbation routes cells toward resistance." Applied to melanoma drug resistance, it surfaces a set of **convergent regulators** — distinct perturbations that funnel into the same resistant phenotype.

## How it connects to the talk

The talk's whole Act 1 is about one task: **perturbation prediction**. The 2025 reckoning is the finding that single-cell FMs do not yet beat linear baselines at predicting what a perturbation does. PerturbFate is the same question from the other side of the bench — a wet-lab + computational *measurement* method, not a model that predicts.

That makes it adjacent in three useful ways:

1. **It is the kind of data the FMs are supposed to learn from.** Convergent-regulator maps are exactly the causal structure the [reckoning](../evaluation-papers-catalog.md) says current sc-FMs fail to encode ([Simon & Zou's SAEs](../paper-map.md) find "minimal regulatory logic"). PerturbFate-style screens are a source of ground truth for that structure.
2. **"Convergent regulators" is a causal-transportability story.** Multiple perturbations reaching one resistant state is a statement about which causal pathways matter — the framing [Virtual Cells Need Context](../why-linear-baselines-win.md#the-theoretical-framing-causal-transportability) makes theoretically.
3. **It is a cancer paper.** For an AACR audience, it is a concrete oncology instance of the perturbation-prediction problem the talk argues FMs have not yet earned.

## Where it sits

Not an FM paper — there is no pretraining-once-adapt-many model here — so it is not in the [model glossary](../model-glossary.md) or the [paper map](../paper-map.md). It belongs on the shelf as the **assay-side counterpart** to the prediction-side reckoning: if you want to argue an sc-FM is good at perturbation prediction, PerturbFate-style maps are what you would validate against.

## Read more

- **[Xu et al. 2026 *Nature* — PerturbFate](https://doi.org/10.1038/s41586-026-10367-0)** — the paper.
- [Why do linear baselines win?](../why-linear-baselines-win.md) — the prediction-side problem PerturbFate measures the ground truth for.
- [The evaluation papers catalog](../evaluation-papers-catalog.md) — the reckoning corpus.

---

*Last updated 2026-05-14.*
