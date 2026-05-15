# Theme — perturbation-prediction

**Items in corpus:** 39

### Papers

- **[scPerturBench replication](https://www.biorxiv.org/content/10.1101/2024.09.30.615579)** — Csendes et al., BM2 Lab preprint, 2024   
  _Showed the original scGPT split was leaky._
- **[Deep-learning predictions of gene expression don't generalize](https://www.nature.com/articles/s41592-025-02772-6)** — Ahlmann-Eltze & Huber, Nature Methods, 2025   
  _THE canonical reckoning paper — start here._
- **[latent-additive is the new baseline floor](https://pubmed.ncbi.nlm.nih.gov/41044630/)** — Wenkel et al., Nature Methods, 2025   
  _Proposed the stronger baseline current FMs still don't beat._
- **[PertEval-scFM — standardised evaluation framework](https://icml.cc/virtual/2025/poster/43799)** — ICML, 2025   
  _Formal venue stamp on the perturbation critique._
- **[Foundation Models Improve Perturbation Response](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** — bioRxiv, 2026   
  _Contrarian voice — FMs DO improve with enough data._
- **sc-FM Perturbation Adapter** — Maleki et al., ICLR LMRL workshop, 2026   
  _Drug-conditional adapter (<1% trainable params) on a frozen FM — generalises where CPA/GEARS/scGen don't._
- **Causal representation learning (Lopez/Hsu)** — Nature Methods, 2025   
  _Causal-rep exemplar for pretraining objectives that target causality._
- **[X-Cell — Scaling Causal Perturbation Prediction via Diffusion Language Models](https://doi.org/10.64898/2026.03.18.712807)** — Wang, Karimzadeh, Ravindra et al. (Bo Wang group), bioRxiv 2026.03.18.712807, 2026   
  _Diffusion LM for perturbation — direct rival to State / scGPT-perturb framing._
- **CellFluxRL — Biologically-Constrained Virtual Cell Modeling via RL** — Wu, Su, Zhang, Sui, Lundberg, Fox, Yeung-Levy, preprint, 2026   
  _RL-driven virtual-cell modelling with biological constraints — Stanford/CZI/Lundberg axis._
- **SCALE — Scalable Conditional Atlas-Level Endpoint transport for virtual-cell perturbation** — preprint, 2026   
  _Optimal-transport / endpoint framing of perturbation prediction at atlas scale._
- **[TxGNN — knowledge-graph FM for therapeutics](https://www.nature.com/articles/s41591-024-03233-x)** — Zitnik et al., Nature Medicine, 2024   
  _Graph FM bridging gene-level and patient-level AI._
- **[Evaluating single-cell perturbation response models is far from straightforward](https://www.biorxiv.org/content/10.64898/2026.02.14.705879v1)** — Heidari, Karimpour, Srivatsa & Montazeri, bioRxiv, 2026   
  _Second front in the perturbation-evaluation reckoning — Wasserstein/Energy distances mislead in high-dim gene space._
- **[VCWorld — biological world model for virtual cell simulation](https://arxiv.org/abs/2512.00306)** — Shuangjia Zheng lab et al., arXiv, 2025   
  _White-box LLM-driven simulator: stepwise mechanistic reasoning, SOTA on drug-perturbation benchmarks. Anti-black-box alternative._

### Tools

- **scGPT** — Cui et al., Nature Methods, 2024   
  _Defined the category — genes + cells as tokens. The reckoning's main target._
- **scFoundation** — Hao et al., Nature Methods, 2024   
  _Read-depth-aware attention; one of the four reckoning regulars._
- **STATE (Arc Institute)** — bioRxiv, 2025   
  _First production virtual cell at Tahoe-100M scale._
- **xVERSE — transcriptomics-native sc-FM** — bioRxiv, 2026   
  _First evidence the architectural choice is load-bearing (+17.9% over LM-derived sc-FMs)._
- **[TxPert — multiple-knowledge-graph perturbation prediction](https://doi.org/10.1038/s41587-026-03113-4)** — Wenkel et al., Nature Biotechnology, 2026   
  _The reckoning answering itself — Wenkel co-authored both critique and response._
- **[MAP — knowledge-driven perturbation framework](https://www.biorxiv.org/content/10.64898/2026.02.25.708091v1)** — bioRxiv, 2026   
  _Zero-shot perturbation prediction for unprofiled drugs._
- **CPA — Compositional Perturbation Autoencoder** — Lotfollahi et al., Nature Cell Biology, 2023   
  _Autoencoder baseline the reckoning repeatedly tests FMs against._
- **[GEARS](https://www.nature.com/articles/s41587-023-01905-6)** — Roohani et al., Nature Biotechnology, 2024   
  _Graph-based perturbation-effect prediction with a gene-gene KG — the pre-FM SOTA._
- **CINEMA-OT**   
  _Optimal-transport perturbation-effect disentanglement._
- **PerturbHD** — Stanford   
  _Stanford perturbation method — only a name so far._
- **CellFluxV2**   
  _Successor to CellFluxRL — name only._
- **CRADLE-VAE — compositional active learning** — Bunne et al.   
  _Closed-loop virtual-cell active learning prototype._
- **scPoli — single-cell policy learning** — Lotfollahi et al.   
  _Policy-based perturbation prediction; the scArches lineage._
- **[Pertpy — end-to-end framework for perturbation analysis](https://github.com/scverse/pertpy)** — Heumos, Ji, May, Theis et al., Nature Methods, 2025   
  _scverse-blessed perturbation toolbox — distances, perturbation spaces, harmonisation. The canonical analysis layer._
- **scpFormer**   
  _scpFormer — name only; transformer for single-cell perturbation, no paper yet._

### Benchmarks

- **[PerturBench](https://github.com/altoslabs/perturbench)** — Altos Labs   
  _Altos Labs perturbation-prediction benchmark._
- **[scPerturBench](https://bm2-lab.github.io/scPerturBench-reproducibility/)** — BM2-Lab   
  _Benchmark with adversarial perturbation/cell-type splits._
- **Compositional-generalisation benchmark (Hetzel et al.)** — NeurIPS LMRL, 2024   
  _Compositional generalisation benchmark referenced in supplementary §C.3._

### Datasets

- **Replogle whole-genome Perturb-seq** — Replogle et al., Cell, 2022   
  _Standard perturbation test set._
- **Norman combinatorial Perturb-seq** — Norman et al., Science, 2019   
  _Substrate for compositional-generalisation benchmarks._

### Organisations

- **[Bo Wang Lab (U. Toronto / Vector / UHN)](https://wanglab.ai/)** — Bo Wang   
  _Defined the sc-FM category (scGPT); agentic-AI pivot 2026 (X-Cell)._

### People

- **[Mohammad Lotfollahi](https://lotfollahi.com/research/)** — Wellcome Sanger   
  _scArches, scPoli, CPA, CRADLE-VAE — the perturbation-and-adaptation stack._
- **[Constantin Ahlmann-Eltze](https://const-ae.name/)** — Isomorphic Labs (ex-EMBL)   
  _Linear-baseline-2025 first author; recently moved to Isomorphic._

### Competition

- **[CZ Biohub Virtual Cell Challenge 2025](https://virtualcellchallenge.org/)**   
  _First community virtual-cell benchmark, $50k prize._
- **Echoes of Silenced Genes — Myllia Biotechnology cell challenge** — Myllia, 2026   
  _Biotech-run challenge focused on perturbation prediction._

### Move

- **Turbine raises $25M** — 2026   
  _Validates commercial market for VC-style perturbation simulators._

---

_Regenerated 2026-05-15 from a 277-item corpus by [resourcelib-views](https://github.com/Light-Kit/resourcelib-views)._
