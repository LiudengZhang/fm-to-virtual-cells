# Theme — single-cell

**Items in corpus:** 87

### Papers

- **The future of automated single-cell analysis** — Rood, Regev et al., Cell, 2024   
  _Regev's reference-mapping framing of the same ambition._
- **Earliest 'linear baselines are competitive' warning** — Boiarsky et al., NeurIPS workshop, 2023   
  _First warning shot — read it to see how early the signal was._
- **[Limits of zero-shot foundation models in single-cell biology](https://doi.org/10.1186/s13059-025-03574-x)** — Kedzierska et al., Genome Biology, 2025   
  _Extends the result to UCE and the zero-shot setting._
- **[27 methods × 29 datasets × 6 metrics](https://www.nature.com/articles/s41592-025-02980-0)** — Wu et al., Nature Methods, 2026   
  _First axis-by-axis failure decomposition._
- **[No single scFM consistently outperforms](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492631/)** — Wu et al., Genome Biology, 2025   
  _6 scFMs, cell-ontology-grounded metrics._
- **[scEval — challenges the necessity of sc-FMs](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)** — Liu et al., Advanced Science, 2026   
  _Strongest 'is the paradigm worth it' framing._
- **[CellBench-LS — stratified low-supervision benchmark](https://www.biorxiv.org/content/10.64898/2026.04.01.714123v1)** — bioRxiv, 2026   
  _FMs lead cell-type ID; classical methods win gene-expression._
- **[Real-world RNA-seq integration](https://www.biorxiv.org/content/10.64898/2026.04.17.719314v1)** — Han et al., bioRxiv, 2026   
  _Industry-authored — deployment-grade robustness gaps._
- **[Zero-shot scFMs fail to recover cellular dynamics](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)** — bioRxiv, 2026   
  _Extends the critique to RNA-velocity / dynamics._
- **[SAEs reveal organized biology but minimal regulatory logic](https://arxiv.org/abs/2603.02952)** — Simon & Zou, arXiv, 2026   
  _Mechanistic explanation of the reckoning, on Geneformer + scGPT._
- **[SAEs reveal interpretable features in single-cell FMs](https://www.biorxiv.org/content/10.1101/2025.10.22.681631v2)** — bioRxiv, 2025   
  _Independent confirmation on scGPT._
- **Causal representation learning (Lopez/Hsu)** — Nature Methods, 2025   
  _Causal-rep exemplar for pretraining objectives that target causality._
- **[PEFT / LoRA recipe for sc-FMs](https://arxiv.org/abs/2412.13478)** — Hossain et al., arXiv 2412.13478, 2024   
  _Concrete PEFT recipe for single-cell FMs (Lane 2)._
- **[OmniCell — multimodal spatial FM](https://www.biorxiv.org/content/10.64898/2025.12.29.696804v1)** — bioRxiv, 2025   
  _Multimodal spatial-transcriptomics FM._
- **[CLM-X — spatial-temporal cell-language model](https://www.biorxiv.org/content/10.64898/2026.02.17.704943v1)** — bioRxiv, 2026   
  _Spatial + temporal context for cell language modelling._
- **[CELLama — cell language model](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202513210)** — Advanced Science, 2026   
  _Alternative transformer-based cell FM._
- **[CancerFoundation](https://www.biorxiv.org/content/10.1101/2024.11.01.621087v1)** — bioRxiv, 2024   
  _Cancer-domain-specific single-cell FM._
- **[scPEFT — parameter-efficient fine-tuning for single-cell LLMs](https://www.nature.com/articles/s42256-025-01170-z)** — He et al., Nature Machine Intelligence, 2025   
  _Adapter-style PEFT cuts scLLM fine-tuning to <4% params and beats zero-shot — practical answer to the reckoning._
- **[UNAGI — generative model for cellular dynamics + in-silico drug discovery](https://www.nature.com/articles/s41551-025-01423-7)** — Ding lab et al., Nature Biomedical Engineering, 2025   
  _Time-series scRNA generative model used as a virtual-disease simulator for in-silico perturbation screens._
- **[Evaluating single-cell perturbation response models is far from straightforward](https://www.biorxiv.org/content/10.64898/2026.02.14.705879v1)** — Heidari, Karimpour, Srivatsa & Montazeri, bioRxiv, 2026   
  _Second front in the perturbation-evaluation reckoning — Wasserstein/Energy distances mislead in high-dim gene space._
- **[scTranslator — transcriptome→proteome generative model](https://www.nature.com/articles/s41551-025-01528-z)** — Jianhua Yao et al., Nature Biomedical Engineering, 2025   
  _Tencent AI Lab — align-free scRNA→protein generation pretrained on 2M cells + 18k bulk samples._
- **[CausCell — causal disentanglement + counterfactual single-cell generation](https://www.nature.com/articles/s41467-025-62008-1)** — Qi Liu lab (Tongji) et al., Nature Communications, 2025   
  _Structural causal model + diffusion → interpretable cellular representations with explicit cDAGs. Counter-position to black-box scLLMs._
- **[STAMP — single-cell transcriptomics + multimodal profiling through imaging](https://www.cell.com/cell/fulltext/S0092-8674(25)00577-X)** — Qi Liu lab et al., Cell, 2025   
  _Turns Xenium/CosMx/MERSCOPE/PhenoCycler into scalable single-cell profilers — wet-lab counterpart to virtual spatial proteomics._
- **[MERCI — mitochondrial-receiver cell detection in tumours](https://www.cell.com/cell-metabolism/fulltext/S1550-4131(23)00468-0)** — Cell Metabolism   
  _Computational method spotting cells with mitochondrial-transfer signatures — used as motivation in AIVM commentary._

### Reviews

- **Single-cell foundation models — bringing AI into cell biology** — Singh et al., Experimental & Molecular Medicine, 2025   
  _Clean mid-2025 review — the orientation read._
- **Eleven grand challenges in single-cell data science** — Lähnemann et al., Genome Biology, 2020   
  _Pre-FM landscape framing — what needed solving before the wave hit._

### Tools

- **scBERT** — Yang et al., Nature Machine Intelligence, 2022   
  _BERT-style precursor that pre-dated the 2023 sc-FM wave._
- **scGPT** — Cui et al., Nature Methods, 2024   
  _Defined the category — genes + cells as tokens. The reckoning's main target._
- **Geneformer / Geneformer V2** — Theodoris et al., Nature, 2023   
  _First atlas-pretrained transformer; rank-based tokenisation. V2 (Dec 2024) matched 316M at ⅓ the compute._
- **Universal Cell Embedding (UCE)** — Rosen et al., Nature Methods, 2024   
  _Cross-species sc-FM — bridges through ESM2 protein embeddings (8 species)._
- **scFoundation** — Hao et al., Nature Methods, 2024   
  _Read-depth-aware attention; one of the four reckoning regulars._
- **CellPLM** — Wen et al., ICLR, 2024   
  _Cell-as-token sc-FM; beats scGPT/Geneformer on cell-typing cheaply._
- **STATE (Arc Institute)** — bioRxiv, 2025   
  _First production virtual cell at Tahoe-100M scale._
- **TranscriptFormer** — Pearce et al., Science, 2025   
  _First generative cross-species sc-FM; CZ Biohub flagship (112M cells, 12 species)._
- **Nicheformer** — Theis lab, Nature Methods, 2025   
  _Spatial-omics sc-FM with a niche-aware objective._
- **scMulan**   
  _Multitask single-cell language model; benchmarked in CellBench-LS._
- **GenePT / scELMo**   
  _NOT trained sc-FMs — frozen LLM embeddings of gene names + LR head (~$200) matching scGPT zero-shot._
- **CellFM** — Zhang et al., Nature Communications, 2025   
  _Another sc-FM from the 2025 wave._
- **scPRINT** — Kalfon et al., Nature Communications, 2025   
  _50M-cell pretraining aimed at robust zero-shot gene-network inference._
- **scPRINT-2** — Kalfon, Peyré & Cantini, bioRxiv, 2025   
  _Next-gen cell FM AND benchmark suite in one preprint._
- **xVERSE — transcriptomics-native sc-FM** — bioRxiv, 2026   
  _First evidence the architectural choice is load-bearing (+17.9% over LM-derived sc-FMs)._
- **CellVoyager — autonomous comp-bio agent** — Nature Methods, 2026   
  _Agent that ANALYSES single-cell data with the FM as substrate._
- **scDiffusion**   
  _Diffusion model for single-cell expression generation._
- **Flex v2** — Broad Institute   
  _Broad's Flex v2 single-cell platform — currently a name._
- **ProPer-seq**   
  _ProPer-seq assay — name only._
- **CellTRIP**   
  _CellTRIP — name only._
- **LangCell / LangStem**   
  _LLM-based cell annotation tool._
- **GET — gene expression toolkit**   
  _sc-FM-based gene-expression analysis toolkit._
- **[CytoVerse — browser-native sc-FM via ONNX](https://www.biorxiv.org/content/10.64898/2026.01.29.702554v1)** — bioRxiv, 2026   
  _In-browser sc-FM inference; pushes inference to where the data is._
- **scPoli — single-cell policy learning** — Lotfollahi et al.   
  _Policy-based perturbation prediction; the scArches lineage._
- **[scvi-tools](https://scvi-tools.org/)** — Theis Lab   
  _Single-cell methodology reference framework underpinning much of the field._
- **scverse ecosystem (Scanpy / AnnData / squidpy / scvi-tools)**   
  _Community standards for single-cell Python tools._
- **signifinder — sc-FM wrapper for Bioconductor** — Calura lab, U Padua   
  _Bioconductor interface to sc-FMs._
- **mia / miaTime / miaViz** — Borman, U Turku   
  _Scverse-adjacent tools for single-cell analysis._
- **SpatialData — unified spatial-omics data framework** — Marconato, Palla et al. (Theis + Stegle)   
  _Standard for spatial transcriptomics data representation._
- **scones**   
  _Single-cell analysis utility._
- **[Pertpy — end-to-end framework for perturbation analysis](https://github.com/scverse/pertpy)** — Heumos, Ji, May, Theis et al., Nature Methods, 2025   
  _scverse-blessed perturbation toolbox — distances, perturbation spaces, harmonisation. The canonical analysis layer._
- **scpFormer**   
  _scpFormer — name only; transformer for single-cell perturbation, no paper yet._
- **scFOCAL**   
  _scFOCAL — name only._
- **SC-pSILAC** — Zilu Ye   
  _Single-cell pSILAC variant — Zilu Ye attribution from talk notes, not yet citable._

### Benchmarks

- **[Open Problems v2](https://openproblems.bio)**   
  _Community single-cell benchmark suite._
- **sc-Arena — single-cell benchmark suite**   
  _Third-party-maintained sc-FM benchmark._

### Datasets

- **Tabula Sapiens** — Science, 2022   
  _Multi-organ human single-cell reference atlas._
- **CELLxGENE Census**   
  _Aggregated single-cell corpus most sc-FMs pretrain on._

### Organisations

- **Jian Ma's Virtual Bio Center** — Carnegie Mellon   
  _New CMU center anchored around Jian Ma's lab as a US academic hub for virtual biology._
- **IBS — Park Jong-eun (human digital twin)** — Institute for Basic Science, Korea   
  _Korean national lab investing in human-digital-twin programme around single-cell data._
- **[CZ Biohub](https://chanzuckerberg.com/science/programs-resources/virtual-cells-initiative/)** — Theofanis Karaletsos, Steve Quake, Angela Pisco   
  _Substrate + model shipper (TranscriptFormer, rBio); breaks substrate-only stereotype._
- **[Theodoris Lab (Gladstone / UCSF)](https://www.theodorislab.gladstone.org/)** — Christina Theodoris   
  _Only sc-FM lab with full compute disclosure (NVIDIA BioNeMo)._
- **[Bo Wang Lab (U. Toronto / Vector / UHN)](https://wanglab.ai/)** — Bo Wang   
  _Defined the sc-FM category (scGPT); agentic-AI pivot 2026 (X-Cell)._
- **[Leskovec + Quake (Stanford / SNAP)](https://snap.stanford.edu/)** — Jure Leskovec & Steve Quake   
  _Cross-species sc-FM (UCE) — 8 species via ESM2 bridge._
- **[Ahlmann-Eltze / Huber (EMBL Heidelberg)](https://const-ae.name/)**   
  _Authored the 2025 reckoning paper; Ahlmann-Eltze now at Isomorphic Labs._
- **[Theis Lab (Helmholtz Munich)](https://www.helmholtz-munich.de/en/icb/pi/fabian-theis)** — Fabian Theis   
  _Methodological reference class; author of 2026 compositional-FM perspective._
- **Cellarity**   
  _Cell-state engineering company._

### People

- **[Aviv Regev](https://www.gene.com/scientists/our-scientists/aviv-regev)** — Genentech   
  _Agenda-setter for causal foundation models in cell biology._
- **[Christina Theodoris](https://www.theodorislab.gladstone.org/)** — Gladstone Institutes   
  _Geneformer creator; one of the few sc-FM PIs with full compute disclosure._
- **[Bo Wang](https://wanglab.ai/)** — U. Toronto / Vector   
  _scGPT PI; 2026 pivot to agentic AI (X-Cell)._
- **[Mohammad Lotfollahi](https://lotfollahi.com/research/)** — Wellcome Sanger   
  _scArches, scPoli, CPA, CRADLE-VAE — the perturbation-and-adaptation stack._
- **[Jure Leskovec](https://cs.stanford.edu/people/jure/)** — Stanford   
  _UCE co-PI; graph + sc-FM bridge._
- **[Sara Mostafavi](http://saramostafavi.github.io/)** — UW Allen School   
  _Gene-expression modelling expert._
- **[Wolfgang Huber](https://www.huber.embl.de/)** — EMBL   
  _Bioconductor + genomics-statistics elder; co-author of the reckoning paper._
- **[Kasia Z. Kedzierska](https://scholar.google.com/citations?user=lvJpQGUAAAAJ)** — Oxford / MSR   
  _Zero-shot-critique first author._
- **[Hani Goodarzi](https://arcinstitute.org/labs/goodarzilab)** — Arc Institute   
  _STATE co-lead._
- **[Fabian Theis](https://www.helmholtz-munich.de/en/icb/pi/fabian-theis)** — Helmholtz Munich   
  _Compositional-FM Perspective author; scvi-tools / Nicheformer._
- **[Jianhua Yao](https://scholar.google.com/citations?user=3bQwlCQAAAAJ)** — Tencent AI Lab   
  _scTranslator PI, AIMBE fellow — Tencent's bio-FM lead._
- **[Qi Liu](https://bm2-lab.github.io/)** — Tongji University   
  _BM2 Lab — CausCell, STAMP, scPerturBench. Methods-critique + tooling powerhouse from China._

### Commentary

- **[CZ Biohub Data Science blog](https://ds.czbiohub.org/blog)**   
  _Blog on Tabula, CELLxGENE, virtual cells, from the inside._
- **[preLights — preprint commentary](https://prelights.biologists.com/)** — Company of Biologists   
  _Community preprint commentary on bio papers._

---

_Regenerated 2026-05-15 from a 277-item corpus by [resourcelib-views](https://github.com/Light-Kit/resourcelib-views)._
