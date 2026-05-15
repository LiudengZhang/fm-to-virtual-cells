# Adjacent methods — the catalog

> *Resource section for the [FM-to-Virtual-Cells talk](../../fm-to-virtual-cells.md). The talk is about foundation models, but the problems it cares about — perturbation prediction, generative cell modelling, evaluation, cheap model adaptation, the architecture debate — are also worked on by people **not** building FMs. This is the catalog of those papers: ~55 algorithm, benchmark, and methodology papers that sit next to the talk's argument without being FM papers, curated entirely from the talk's own [supplementary bibliography](../../fm-to-virtual-cells-supplementary.md#h3-recommended-reading-110-references) (§E, §H.3, §H.10) plus the lane and track dossiers (§B, §C).*

## How to read this catalog

- **It is the index, not the deep-dive.** Eight of these papers have full dossier pages — see the table below. The rest are one-liner entries here.
- **It deliberately excludes foundation models.** Those live in the [model glossary](../model-glossary.md) and the [paper map](../paper-map.md). This catalog is the methods *next door*.
- **Some entries also appear in the [paper map](../paper-map.md) or the [evaluation papers catalog](../evaluation-papers-catalog.md)** — where they do, the entry says so and points there for depth.
- **Grounding:** every entry is curated from the talk's existing bibliography. Where the source bibliography gives a direct link, it is reproduced; where it gives only a citation, the entry is text-only by design rather than inventing a URL.

## The dossier pages

The eight papers worth a full page — what the method is, how it connects, where to read more:

| Page | Paper | Theme |
|---|---|---|
| [PerturbFate](perturbfate.md) | Xu et al., *Nature* 2026 | Perturbation-prediction methods |
| [Flow matching in computational biology](flow-matching.md) | Morehead et al., *Nat Mach Intell* 2026 | Generative methods |
| [Learning beyond fine-tuning](learning-beyond-fine-tuning.md) | Zheng et al., *Nat Mach Intell* 2025 | Adaptation methodology |
| [Genome language models](genome-language-models.md) | Consens et al., *Nat Mach Intell* 2025 | Architecture reviews |
| [Protein-LM explainability](protein-lm-explainability.md) | Hunklinger & Ferruz, *Nat Mach Intell* 2026 | Mechanistic interpretability |
| [Transformers vs state-space models](transformers-vs-state-space.md) | Tiezzi et al., *Nat Mach Intell* 2025 | Architecture reviews |

---

## A. Perturbation-prediction & cell-modelling methods

Non-FM methods aimed directly at the talk's central task — predicting or mapping what a perturbation does to a cell.

- **CPA — Compositional Perturbation Autoencoder.** Lotfollahi et al. 2023 *Nat Cell Biol*. The autoencoder baseline the reckoning repeatedly tests FMs against; one of the six methods in [Ahlmann-Eltze & Huber](../evaluation-papers-catalog.md).
- **[GEARS](https://www.nature.com/articles/s41587-023-01905-6).** Roohani et al. 2024 *Nat Biotechnol*. Graph-based perturbation-effect prediction using a gene-gene knowledge graph — the pre-FM state of the art, and another standard reckoning baseline.
- **[PerturbFate](perturbfate.md).** Xu et al. 2026 *Nature*. Perturbation screening that maps convergent regulators of melanoma drug resistance — the assay-side counterpart to prediction. **→ [dossier](perturbfate.md).**
- **[TxPert](https://doi.org/10.1038/s41587-026-03113-4).** Wenkel et al. 2026 *Nat Biotech*. Multiple-knowledge-graph perturbation prediction — "the reckoning answering itself." Also a [paper-map](../paper-map.md) node.
- **[MAP — knowledge-driven framework](https://www.biorxiv.org/content/10.64898/2026.02.25.708091v1).** bioRxiv 2026.02. Zero-shot perturbation prediction for unprofiled drugs via biology-specific inductive bias (supplementary §C.4).
- **sc-FM Perturbation Adapter.** Maleki et al., ICLR 2026 LMRL workshop. A drug-conditional adapter (<1% trainable params) on a frozen FM backbone — generalises to unseen drugs where CPA / GEARS / scGen cannot (supplementary §B.2).
- **CINEMA-OT.** Optimal-transport perturbation-effect disentanglement, cited as a causal-objective exemplar in supplementary §C.2.
- **Lopez / Hsu 2025 *Nat Methods* — causal representation learning.** A causal-representation approach cited as the exemplar for new pretraining objectives that target causality (supplementary §C.2).

## B. Evaluation & critique — the reckoning corpus

The 2025–2026 evaluation papers are themselves non-FM method papers — benchmark designs and critiques. They have a [dedicated catalog](../evaluation-papers-catalog.md) and most are [paper-map](../paper-map.md) nodes; listed compactly here for completeness.

- **[Ahlmann-Eltze & Huber 2025 *Nat Methods*](https://www.nature.com/articles/s41592-025-02772-6)** — the canonical linear-baseline result.
- **[Kedzierska et al. 2025 *Genome Biology*](https://doi.org/10.1186/s13059-025-03574-x)** — extends it to the zero-shot setting.
- **[Wenkel et al. 2025 *Nat Methods*](https://pubmed.ncbi.nlm.nih.gov/41044630/)** — proposes the `latent-additive` baseline floor.
- **[Wu et al. 2026 *Nat Methods*](https://www.nature.com/articles/s41592-025-02980-0)** — 27 methods × 29 datasets × 6 metrics.
- **[Wu et al. 2025 *Genome Biology*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492631/)** — "no single scFM consistently outperforms."
- **[Liu et al. 2026 *Adv Sci* (scEval)](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)** — challenges the necessity of the FM paradigm.
- **[Parameter-free baseline 2026](https://www.biorxiv.org/content/10.64898/2026.02.11.705358v1)** — direct successor to Ahlmann-Eltze.
- **[PertEval-scFM, ICML 2025](https://icml.cc/virtual/2025/poster/43799)** — standardized perturbation-evaluation framework.
- **[CellBench-LS 2026](https://www.biorxiv.org/content/10.64898/2026.04.01.714123v1)** — stratified low-supervision benchmark.
- **[Han et al. 2026](https://www.biorxiv.org/content/10.64898/2026.04.17.719314v1)** — industry-grade real-world RNA-seq robustness.
- **[Cellular-dynamics zero-shot 2026](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)** — extends the critique to RNA velocity.
- **[Csendes scPerturBench 2024](https://www.biorxiv.org/content/10.1101/2024.09.30.615579)** — adversarial-split replication exposing leakage.
- **Boiarsky et al. 2023 NeurIPS workshop** — the earliest "linear baselines are competitive" warning.
- **[Foundation Models Improve Perturbation Response 2026](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** — the contrarian counter-evidence.

→ Full depth: **[the evaluation papers catalog](../evaluation-papers-catalog.md)**.

## C. Benchmarks & datasets

The substrates and leaderboards the methods above are trained and judged on.

- **Replogle et al. 2022 *Cell*** — whole-genome Perturb-seq; a standard perturbation test set.
- **Norman et al. 2019 *Science*** — combinatorial Perturb-seq; the substrate for compositional-generalization benchmarks (supplementary §C.3).
- **[Open Problems v2](https://openproblems.bio)** — the community single-cell benchmark suite.
- **[PerturBench](https://github.com/altoslabs/perturbench)** — Altos Labs perturbation-prediction benchmark.
- **[scPerturBench](https://bm2-lab.github.io/scPerturBench-reproducibility/)** — BM2-Lab benchmark with adversarial perturbation/cell-type splits.
- **[CZ Biohub Virtual Cell Challenge 2025](https://virtualcellchallenge.org/)** — the first community virtual-cell benchmark, $50k prize.
- **Roohani, Hsu et al. 2025 — Tahoe-100M** — the first large-scale perturbation atlas framed as virtual-cell training data.
- **Tabula Sapiens Consortium 2022 *Science*** — multi-organ human single-cell reference atlas.
- **CELLxGENE Census** — the aggregated single-cell corpus most sc-FMs pretrain on.
- **HuBMAP 2023 *Nature*** — the human tissue / spatial reference atlas.
- **HEST-1k** — the histology-with-spatial-transcriptomics benchmark dataset.
- **CASP15 / CAPRI** — the community structure- and complex-prediction assessments.
- **ProteinGym.** Notin et al. 2023 *NeurIPS* — the protein variant-effect benchmark.
- **Hetzel et al. 2024 NeurIPS LMRL** — compositional-generalization benchmark cited in supplementary §C.3.

## D. Generative & structure-prediction methods

The generative-modelling lineage behind generative virtual cells and protein design.

- **[Flow matching in computational biology](flow-matching.md).** Morehead et al. 2026 *Nat Mach Intell*. The generative technique under generative virtual cells. **→ [dossier](flow-matching.md).**
- **[AlphaFold 2](https://doi.org/10.1038/s41586-021-03819-2).** Jumper et al. 2021 *Nature*. The structure-prediction breakthrough the whole protein-modelling wave builds on.
- **[RFdiffusion](https://doi.org/10.1038/s41586-023-06415-8).** Watson et al. 2023 *Nature*. Diffusion-based de novo protein design — the generative-design exemplar.
- **[ProGen2](https://doi.org/10.1038/s41587-022-01618-2).** Madani et al. 2023 *Nat Biotechnol*. Generative protein-sequence modelling, pre-ESM-3.
- **scDiffusion.** A diffusion model for single-cell expression generation, cited as a Lane 8 data-augmentation exemplar (supplementary §B.8).

## E. Mechanistic interpretability methods

The toolkit for asking what a trained model actually encodes — the *mechanism* behind the reckoning.

- **[Adams et al. 2025 *PNAS*](https://www.pnas.org/doi/10.1073/pnas.2506316122)** — sparse autoencoders on protein language models; the paper that started the biology-FM interpretability wave.
- **[Simon & Zou 2026](https://arxiv.org/abs/2603.02952)** — SAEs reveal organized biology but minimal regulatory logic in sc-FMs; the mechanistic explanation of the reckoning. Also a [paper-map](../paper-map.md) node.
- **[SAEs Reveal Interpretable Features in Single-Cell FMs 2025](https://www.biorxiv.org/content/10.1101/2025.10.22.681631v2)** — independent SAE confirmation on scGPT.
- **[Hibou-LP SAE 2024](https://arxiv.org/abs/2407.10785)** — the first pathology-FM sparse autoencoder.
- **[What Do Biological Foundation Models Compute? 2026](https://www.biorxiv.org/content/10.64898/2026.03.04.709491v1)** — a cross-family synthesis of the interpretability wave.
- **[Protein-LM explainability](protein-lm-explainability.md).** Hunklinger & Ferruz 2026 *Nat Mach Intell*. A review of interpretability methods for protein FMs. **→ [dossier](protein-lm-explainability.md).**

## F. Adaptation & training methodology

How a pretrained model is adapted, and what the training run costs — the methods backbone of the small-lab lanes.

- **[Learning beyond fine-tuning](learning-beyond-fine-tuning.md).** Zheng et al. 2025 *Nat Mach Intell*. The landscape of model-adaptation paradigms past fine-tuning. **→ [dossier](learning-beyond-fine-tuning.md).**
- **[Hossain et al. — PEFT / LoRA recipe for sc-FMs](https://arxiv.org/abs/2412.13478).** *arXiv* 2412.13478. A concrete parameter-efficient fine-tuning recipe for single-cell FMs (Lane 2).
- **[Hoffmann et al. 2022 — Chinchilla](https://arxiv.org/abs/2203.15556)** — the compute-optimal scaling law behind every "is this model under- or over-trained" judgement.
- **[Epoch AI training-compute methodology](https://epoch.ai/blog/estimating-training-compute)** — the `FLOPs ≈ 6 × params × tokens` heuristic the talk's cost estimates rely on.
- **[Cottier, Rahman et al. 2024](https://arxiv.org/abs/2405.21015)** — "The Rising Costs of Training Frontier AI Models," the economic backdrop for the compute-disclosure argument.

## G. Architecture reviews

The architecture debate behind Cause 2 of the reckoning — "the transformer was borrowed from NLP."

- **[Genome language models](genome-language-models.md).** Consens et al. 2025 *Nat Mach Intell*. A review of transformer architectures for DNA. **→ [dossier](genome-language-models.md).**
- **[Transformers vs state-space models](transformers-vs-state-space.md).** Tiezzi et al. 2025 *Nat Mach Intell*. The transformer / recurrent / state-space crossroads. **→ [dossier](transformers-vs-state-space.md).**

## H. Uncertainty, causality & evaluation methodology

The methodological scaffolding behind the post-reckoning evaluation tracks (supplementary §C).

- **[Virtual Cells Need Context, Not Just Scale 2026](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1)** — frames the generalization failure as a causal-transportability problem (Pearl). Also a [paper-map](../paper-map.md) node.
- **[Beyond Alignment — Synergistic Information Score 2026](https://www.biorxiv.org/content/10.64898/2026.02.23.707420v3)** — Microsoft's metric for whether a multimodal FM extracts genuinely cross-modal information (supplementary §C.8).
- **Arjovsky et al. 2019 — Invariant Risk Minimization** — the causal-objective method cited as the basis for counterfactual pretraining (supplementary §C.2).
- **van Amersfoort et al. 2024 — deep deterministic UQ** — an uncertainty-quantification method for the clinical-grade-FM track (supplementary §C.5).
- **Angelopoulos & Bates 2023 — conformal prediction** — the distribution-free uncertainty method paired with the UQ track (supplementary §C.5).

---

## How this section relates to the rest of the talk prep

- The [model glossary](../model-glossary.md) and [paper map](../paper-map.md) cover the **foundation models** and the literature *about* them.
- The [evaluation papers catalog](../evaluation-papers-catalog.md) covers the **reckoning corpus** in depth (Theme B above is its index-level summary).
- This catalog covers **methods next door** — algorithm, benchmark, and methodology papers that inform the same problems without being FM papers.
- Anything here that turns out to be load-bearing for the argument graduates into the paper map; until then it lives here as a resource.

---

*Last updated 2026-05-14. ~55 papers, curated from supplementary §E / §H.3 / §H.10 / §B / §C.*
