# FMs → Virtual Cells

A talk-prep and knowledge-base site for AI foundation models, single-cell foundation models, perturbation prediction, and the **virtual cell** vision. v2 / extension of [awesome-virtual-cell](https://github.com/LiudengZhang/awesome-virtual-cell).

## What's here

- **[Talk Prep — FMs to Virtual Cells](talks/fm-to-virtual-cells.md)** — a 5-act talk page + long-form supplementary (11 model dossiers, 9 lanes, 9 tracks, compute matrix, ~110-reference reading list) + 8 explainers (incl. [the model glossary](talks/fm-to-virtual-cells/model-glossary.md) and [the paper map](talks/fm-to-virtual-cells/paper-map.md)) + ~12 interactive Plotly figures.
- **[Foundation Models index](foundation-models.md)** — cross-domain catalog: single-cell · DNA · pathology · protein · multimodal.
- **[Adjacent Methods catalog](talks/fm-to-virtual-cells/adjacent-methods/index.md)** — ~55 papers on perturbation, flow matching, learning beyond fine-tuning, genome LMs, protein-LM explainability, transformers vs. state-space.
- **[Resource Library](talks/fm-to-virtual-cells/resource-library.md)** — ~280-item filterable corpus: papers · tools · labs · datasets · events · money moves. YAML-driven; rerender adds tags automatically.
- **[Views — ranked dossiers](talks/fm-to-virtual-cells/views/index.md)** — top-10 people, top-10 institutes, top-10 themes auto-generated from the corpus by [resourcelib-views](https://github.com/Light-Kit/resourcelib-views).
- **[90-min Speed Read](speed-read.md)** — fastest path through the field for a non-specialist.

## How to use this site

1. **Time-constrained** — start at the [90-min Speed Read](speed-read.md).
2. **Talk preparation** — open [Talk Prep](talks/fm-to-virtual-cells.md) and [Supplementary](talks/fm-to-virtual-cells-supplementary.md) side-by-side; the figures are clickable Plotly.
3. **Field landscape** — [Views](talks/fm-to-virtual-cells/views/index.md) for who/where, [Foundation Models](foundation-models.md) for what.
4. **Paper hunt** — filter the [Resource Library](talks/fm-to-virtual-cells/resource-library.md) by tag (foundation-model · virtual-cell · perturbation-prediction · eval · clinical · pathology · multimodal · drug-design · agents).

## Why this exists

`awesome-virtual-cell` was a good curated link list, but the field has grown to a point where flat lists aren't enough: items need cross-cutting tags (who built it · which institute · which theme · what kind), and the right view depends on what question you're asking. A YAML schema + a renderer that emits ranked dossiers makes that possible while keeping the source of truth in one file.

This site is the result.
