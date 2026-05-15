# Theme — eval

**Items in corpus:** 48

### Papers

- **Virtual Cell Challenge — a Turing test for the virtual cell** — CZI / Roohani / Hsu et al., Cell, 2025   
  _What success is supposed to look like, operationalised._
- **Earliest 'linear baselines are competitive' warning** — Boiarsky et al., NeurIPS workshop, 2023   
  _First warning shot — read it to see how early the signal was._
- **[scPerturBench replication](https://www.biorxiv.org/content/10.1101/2024.09.30.615579)** — Csendes et al., BM2 Lab preprint, 2024   
  _Showed the original scGPT split was leaky._
- **[Deep-learning predictions of gene expression don't generalize](https://www.nature.com/articles/s41592-025-02772-6)** — Ahlmann-Eltze & Huber, Nature Methods, 2025   
  _THE canonical reckoning paper — start here._
- **[Limits of zero-shot foundation models in single-cell biology](https://doi.org/10.1186/s13059-025-03574-x)** — Kedzierska et al., Genome Biology, 2025   
  _Extends the result to UCE and the zero-shot setting._
- **[latent-additive is the new baseline floor](https://pubmed.ncbi.nlm.nih.gov/41044630/)** — Wenkel et al., Nature Methods, 2025   
  _Proposed the stronger baseline current FMs still don't beat._
- **[27 methods × 29 datasets × 6 metrics](https://www.nature.com/articles/s41592-025-02980-0)** — Wu et al., Nature Methods, 2026   
  _First axis-by-axis failure decomposition._
- **[No single scFM consistently outperforms](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492631/)** — Wu et al., Genome Biology, 2025   
  _6 scFMs, cell-ontology-grounded metrics._
- **[scEval — challenges the necessity of sc-FMs](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)** — Liu et al., Advanced Science, 2026   
  _Strongest 'is the paradigm worth it' framing._
- **[Parameter-free baseline beats sc-FMs](https://www.biorxiv.org/content/10.64898/2026.02.11.705358v1)** — bioRxiv, 2026   
  _Cleanest post-reckoning headline; direct Ahlmann successor._
- **[PertEval-scFM — standardised evaluation framework](https://icml.cc/virtual/2025/poster/43799)** — ICML, 2025   
  _Formal venue stamp on the perturbation critique._
- **[CellBench-LS — stratified low-supervision benchmark](https://www.biorxiv.org/content/10.64898/2026.04.01.714123v1)** — bioRxiv, 2026   
  _FMs lead cell-type ID; classical methods win gene-expression._
- **[Real-world RNA-seq integration](https://www.biorxiv.org/content/10.64898/2026.04.17.719314v1)** — Han et al., bioRxiv, 2026   
  _Industry-authored — deployment-grade robustness gaps._
- **[Zero-shot scFMs fail to recover cellular dynamics](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)** — bioRxiv, 2026   
  _Extends the critique to RNA-velocity / dynamics._
- **[Foundation Models Improve Perturbation Response](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** — bioRxiv, 2026   
  _Contrarian voice — FMs DO improve with enough data._
- **[Beyond Alignment — Synergistic Information Score](https://www.biorxiv.org/content/10.64898/2026.02.23.707420v3)** — bioRxiv (Microsoft), 2026   
  _Microsoft's metric for whether a multimodal FM extracts genuinely cross-modal information._
- **Deep deterministic UQ** — van Amersfoort et al., 2024   
  _Uncertainty-quantification method for the clinical-grade-FM track._
- **Conformal prediction** — Angelopoulos & Bates, 2023   
  _Distribution-free uncertainty paired with the UQ track._
- **Sukumaran et al. — clinical-decision-support evaluation** — JCO Precision Oncology, 2025   
  _Framework for clinical AI evaluation._
- **[Evaluating single-cell perturbation response models is far from straightforward](https://www.biorxiv.org/content/10.64898/2026.02.14.705879v1)** — Heidari, Karimpour, Srivatsa & Montazeri, bioRxiv, 2026   
  _Second front in the perturbation-evaluation reckoning — Wasserstein/Energy distances mislead in high-dim gene space._

### Tools

- **scPRINT-2** — Kalfon, Peyré & Cantini, bioRxiv, 2025   
  _Next-gen cell FM AND benchmark suite in one preprint._
- **MedAgentGym**   
  _Agentic environment / benchmark for training and evaluating medical AI agents._
- **[Pertpy — end-to-end framework for perturbation analysis](https://github.com/scverse/pertpy)** — Heumos, Ji, May, Theis et al., Nature Methods, 2025   
  _scverse-blessed perturbation toolbox — distances, perturbation spaces, harmonisation. The canonical analysis layer._

### Benchmarks

- **[Open Problems v2](https://openproblems.bio)**   
  _Community single-cell benchmark suite._
- **[PerturBench](https://github.com/altoslabs/perturbench)** — Altos Labs   
  _Altos Labs perturbation-prediction benchmark._
- **[scPerturBench](https://bm2-lab.github.io/scPerturBench-reproducibility/)** — BM2-Lab   
  _Benchmark with adversarial perturbation/cell-type splits._
- **CASP15 / CAPRI**   
  _Community structure- and complex-prediction assessments._
- **ProteinGym** — Notin et al., NeurIPS, 2023   
  _Protein variant-effect benchmark._
- **Compositional-generalisation benchmark (Hetzel et al.)** — NeurIPS LMRL, 2024   
  _Compositional generalisation benchmark referenced in supplementary §C.3._
- **VCBench** — arXiv   
  _Named benchmark for virtual cells — details still being chased down._
- **[Campanella et al. clinical-grade pathology panel](https://www.nature.com/articles/s41467-025-58245-z)** — Campanella et al., Nature Communications, 2025   
  _Multi-task pathology benchmark for FM evaluation._
- **[Polaris Hub — drug-discovery ML benchmark community](https://polarishub.io/)**   
  _Public leaderboard for drug-discovery models._
- **[Therapeutics Data Commons (TDC-2)](https://tdcommons.ai/)** — Marinka Zitnik   
  _Therapeutic ML benchmark suite._
- **[CZI Virtual Cells Platform Benchmarks](https://virtualcellmodels.cziscience.com/benchmarks)**   
  _Official virtual-cell evaluation suite hosted by CZI._
- **sc-Arena — single-cell benchmark suite**   
  _Third-party-maintained sc-FM benchmark._
- **[Virtual Cell Challenge](https://www.kaggle.com/competitions/open-problems-single-cell-perturbations)** — Cell, 2025   
  _Arc Institute competition with 5,000+ teams; most of 300+ submissions scored worse than mean baseline on MAE, and the winning approach was a hybrid using protein embeddings plus classical features (Cell, 2025)._
- **[Perturbation Prediction vs Baselines](https://doi.org/10.1038/s41592-025-02772-6)** — Nature Methods, 2025   
  _Independent evaluation showing linear models match or beat scGPT and GEARS on held-out perturbations (Nature Methods, 2025)._
- **[BioLLM](https://github.com/BGIResearch/BioLLM)**   
  _Standardized benchmarking framework running scBERT, Geneformer, scGPT, and scFoundation through unified APIs for fair comparison._

### Organisations

- **[Ahlmann-Eltze / Huber (EMBL Heidelberg)](https://const-ae.name/)**   
  _Authored the 2025 reckoning paper; Ahlmann-Eltze now at Isomorphic Labs._

### People

- **[Constantin Ahlmann-Eltze](https://const-ae.name/)** — Isomorphic Labs (ex-EMBL)   
  _Linear-baseline-2025 first author; recently moved to Isomorphic._
- **[Wolfgang Huber](https://www.huber.embl.de/)** — EMBL   
  _Bioconductor + genomics-statistics elder; co-author of the reckoning paper._
- **[Kasia Z. Kedzierska](https://scholar.google.com/citations?user=lvJpQGUAAAAJ)** — Oxford / MSR   
  _Zero-shot-critique first author._
- **[Qi Liu](https://bm2-lab.github.io/)** — Tongji University   
  _BM2 Lab — CausCell, STAMP, scPerturBench. Methods-critique + tooling powerhouse from China._

### Competition

- **[CZ Biohub Virtual Cell Challenge 2025](https://virtualcellchallenge.org/)**   
  _First community virtual-cell benchmark, $50k prize._
- **Echoes of Silenced Genes — Myllia Biotechnology cell challenge** — Myllia, 2026   
  _Biotech-run challenge focused on perturbation prediction._
- **AI Proteomics Competition (AIPC)** — Westlake University   
  _Westlake-run AI-proteomics challenge — bridges AIVC and mass-spec ML._

### Event

- **Virtual Cell Challenge 2025 — first round** — CZI / Biohub, 2025   
  _The annual benchmark cycle whose 2025 launch crystallised the field._
- **[Arc Virtual Cell Challenge 2025](https://virtualcellchallenge.org/)**   
  _Community benchmark with $50k prize; first formal VC evaluation._

---

_Regenerated 2026-05-15 from a 304-item corpus by [resourcelib-views](https://github.com/Light-Kit/resourcelib-views)._
