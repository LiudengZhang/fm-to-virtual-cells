# The paper map — how the literature connects, and how to read it

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). The talk cites ~110 papers; this page is the **map** — an interactive network of the ~50 load-bearing ones, colour-coded by category, with edges that say how each paper relates to the others. Below the map is a **systematic reading order**: the sequence to actually work through them in.*

## How to read the map

Every node is a paper. **Colour = what kind of paper it is.** **Edges = how papers relate**, and there are only four edge types:

- **builds on / lineage** (grey) — B is a descendant or successor of A.
- **evaluates / critiques** (red dashed) — B tested A and reported how it did.
- **responds to** (green) — B is a direct answer to A.
- **frames / explains** (purple dotted) — B gives A a theory, a mechanism, or a position.

The layout is not force-directed — it is deliberately arranged. **The reckoning sits at the centre** because almost everything else points at it: the model papers it critiqued, the responses it provoked, the theory that explains it. The other seven categories ring it. **Ahlmann-Eltze 2025 is the single hub node** — the paper the whole corpus orbits.

<iframe src="../../assets/fm-paper-network.html" width="100%" height="780" frameborder="0" loading="lazy" title="The FM-to-virtual-cells paper relationship network"></iframe>

*Interactive — hover any node for a one-line "why read this"; drag to pan, scroll to zoom. The dense red-dashed bundle in the middle is the visual thesis of the whole talk: ~13 independent evaluation papers all converging on the same handful of single-cell FMs.*

## The systematic reading order

Read the corpus in **seven passes**. Each pass is one region of the map. You do not need all ~50 — the **bold** papers in each pass are the minimum spine; the rest are depth.

### Pass 1 — Why the field exists (position / framing, purple)

Start with the ambition, so the reckoning lands as a disappointment rather than a curiosity.

1. **[Bunne et al. 2024 *Cell*](https://www.cell.com/cell/fulltext/S0092-8674(24)01332-1)** — "How to build the virtual cell with AI." The canonical thesis. Everything downstream is chasing this.
2. **[Roohani et al. 2025 *Cell*](https://www.cell.com/cell/fulltext/S0092-8674(25)00675-0)** — the Virtual Cell Challenge: what "success" is supposed to look like, operationalized as a Turing test.
3. Rood, Hupalowska & Regev 2024 *Cell* — Regev's reference-mapping framing of the same goal.
4. **[Rao et al. 2026 *Nat Biotech*](https://doi.org/10.1038/s41587-026-03064-w)** — "Generalist biological AI." The position paper that unifies all five FM families — read it to see why the other-family FMs (right side of the map) belong in this story at all.
5. [Li et al. 2026 *Nat Biotech*](https://doi.org/10.1038/s41587-026-03035-1) — agentic AI + in silico team science; the framing behind Pass 6.
6. Singh et al. 2025 *Exp Mol Med* — a clean orientation review if you want one survey before the primary literature.

### Pass 2 — What got built (single-cell FM model papers, blue)

The models the reckoning will later test. Read these for *architecture*, not results.

1. **[scGPT (Cui et al. 2024 *Nat Methods*)](https://doi.org/10.1038/s41592-024-02201-0)** — genes + cells as tokens; defined the category. This is the node the reckoning converges on — read it first and most carefully.
2. **[Geneformer (Theodoris et al. 2023 *Nature*)](https://doi.org/10.1038/s41586-023-06139-9)** — rank-based tokenization; the other universal reckoning target.
3. [UCE (Rosen et al. 2024)](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2) — cross-species, bridged through ESM-2 (note the grey edge to the protein-FM cluster).
4. [scFoundation](https://doi.org/10.1038/s41592-024-02305-7), [CellPLM](https://openreview.net/forum?id=BKXvPDekud), scBERT — the rest of the lineage; skim for how each varies the tokenization.
5. **[TranscriptFormer (Pearce et al. 2025 *Science*)](https://www.science.org/doi/10.1126/science.aec8514)** — the generative cross-species model; note it has a green edge — it is *also* a response (Pass 5).
6. STATE (Arc), Nicheformer (spatial) — read if perturbation/spatial is your angle.
7. [scPRINT (Kalfon et al. 2025 *Nat Commun*)](https://doi.org/10.1038/s41467-025-58699-1) and its successor [scPRINT-2 (bioRxiv 2025.12)](https://doi.org/10.64898/2025.12.11.693702) — a sc-FM line aimed at gene-network inference; scPRINT-2 ships its own benchmark suite, so it carries a green edge into the reckoning (Pass 3).

### Pass 3 — The reckoning (critique / benchmark, red — the centre)

This is the heart of the talk. Read in roughly this order — it *is* a chronological argument.

1. **[Ahlmann-Eltze & Huber 2025 *Nat Methods*](https://www.nature.com/articles/s41592-025-02772-6)** — THE paper. A one-line linear baseline beats every published sc-FM on perturbation prediction. Start here; everything else extends it.
2. Boiarsky 2023 + [Csendes scPerturBench](https://bm2-lab.github.io/scPerturBench-reproducibility/) — the earlier warnings Ahlmann-Eltze built on (grey edges *into* the hub).
3. **[Kedzierska et al. 2025 *Genome Biology*](https://doi.org/10.1186/s13059-025-03574-x)** — extends the result to the zero-shot setting.
4. **[Wenkel et al. 2025 *Nat Methods*](https://pubmed.ncbi.nlm.nih.gov/41044630/)** — proposes the stronger `latent-additive` baseline. Remember this name — it reappears in Pass 5.
5. [Wu *Nat Methods* 2026](https://www.nature.com/articles/s41592-025-02980-0), [Wu *Genome Biology* 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492631/), [Liu scEval 2026](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490) — the corpus broadens past perturbation to most cell-level tasks.
6. [Parameter-free baseline](https://www.biorxiv.org/content/10.64898/2026.02.11.705358v1), [PertEval-scFM](https://icml.cc/virtual/2025/poster/43799), [CellBench-LS](https://www.biorxiv.org/content/10.64898/2026.04.01.714123v1), [Han et al.](https://www.biorxiv.org/content/10.64898/2026.04.17.719314v1), [cellular-dynamics](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1) — the 2026 wave; each opens a new evaluation axis. Skim unless one matches your project.

→ The dedicated [evaluation papers catalog](evaluation-papers-catalog.md) is the deep version of this pass.

### Pass 4 — The pushback (contrarian + theory, orange)

The reckoning is not a settled consensus. Read these to hold the honest May-2026 position.

1. **[Foundation Models Improve Perturbation Response (2026)](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** — the contrarian voice: with enough data, FMs *do* improve. Note its green edges *into* the reckoning hub.
2. **[Virtual Cells Need Context, Not Just Scale (2026)](https://www.biorxiv.org/content/10.64898/2026.02.04.703804v1)** — names the theory: a causal-transportability problem in Pearl's sense. The purple "frames" edge.
3. [Beyond Alignment / SIS (Microsoft 2026)](https://www.biorxiv.org/content/10.64898/2026.02.23.707420v3) — a multimodal-FM evaluation metric nobody has applied broadly yet (a project lead).

### Pass 5 — The architectural response (green)

What the field is building *because of* the reckoning.

1. **[xVERSE (2026)](https://www.biorxiv.org/content/10.64898/2026.04.12.718016v1)** — transcriptomics-native architecture; first evidence the design choice is load-bearing.
2. **[TxPert (Wenkel et al. 2026 *Nat Biotech*)](https://doi.org/10.1038/s41587-026-03113-4)** — knowledge-graph-driven perturbation prediction. Follow its green edge to Wenkel 2025 in Pass 3: **the reckoning is answering itself** — the same author wrote the critique and the response.
3. [MAP (2026)](https://www.biorxiv.org/content/10.64898/2026.02.25.708091v1) — knowledge-driven zero-shot prediction for unprofiled drugs.

### Pass 6 — Agents built on the models (brown)

The 2026 convergence: agentic AI and FMs are complementary, not competing.

1. **rBio** — *reasons over* a virtual cell (trained on TranscriptFormer — follow the grey edge).
2. **[VCHarness (2026)](https://www.biorxiv.org/content/10.64898/2026.04.11.717183v1)** — *builds* virtual-cell models autonomously.
3. **[CellVoyager (2026 *Nat Methods*)](https://doi.org/10.1038/s41592-026-03029-6)** — *analyzes* single-cell data autonomously.

→ The [agentic-meets-foundation explainer](agentic-meets-foundation.md) is the deep version of this pass.

### Pass 7 — Why the models fail, mechanistically (interpretability, teal)

Optional, but it is the satisfying ending — the *mechanism* behind Pass 3.

1. **[Adams et al. 2025 *PNAS*](https://www.pnas.org/doi/10.1073/pnas.2506316122)** — the protein-FM SAE paper that started the interpretability wave.
2. **[Simon & Zou 2026](https://arxiv.org/abs/2603.02952)** — SAEs show sc-FMs encode cell-type and pathway features but *minimal regulatory logic*. Follow its purple edge to Ahlmann-Eltze: this is the mechanistic explanation of the reckoning.
3. [SAE-on-scGPT](https://www.biorxiv.org/content/10.1101/2025.10.22.681631v2), [SAE synthesis 2026](https://www.biorxiv.org/content/10.64898/2026.03.04.709491v1) — independent confirmation and the cross-family synthesis.

### Aside — the other four FM families (grey)

The talk is single-cell-centric, but it places sc-FMs against pathology, genomic, and protein FMs. Read **one representative each** if you want the full five-family picture: [AlphaGenome](https://doi.org/10.1038/s41586-025-10014-0) (genomic), [ESM-3](https://www.science.org/doi/10.1126/science.ads0018) (protein), [Virchow2](https://arxiv.org/abs/2408.00738) (pathology). They connect to the map through the generalist position paper (Rao 2026) and through UCE's ESM-2 bridge. The [model glossary](model-glossary.md) has one-liners for all of them.

## The shortest honest path

If you only read six papers, read the spine: **Bunne 2024** (the goal) → **scGPT** + **Geneformer** (what got built) → **Ahlmann-Eltze 2025** (the reckoning) → **FMs Improve Perturbation** (the pushback) → **xVERSE** (the response). That is the talk's Act 1 in six citations.

## Where to go next

- **[The main talk page Act 1 §1.3](../fm-to-virtual-cells.md#13-the-four-eras)** — the four eras these papers map onto.
- **[The evaluation papers catalog](evaluation-papers-catalog.md)** — Pass 3 in full depth.
- **[The model glossary](model-glossary.md)** — one-sentence descriptions of every model named above.
- **[How to read an FM paper critically](reading-an-fm-paper-critically.md)** — the checklist to apply as you work through the map.
- **[Supplementary §H.3](../fm-to-virtual-cells-supplementary.md#h3-recommended-reading-110-references)** — the full ~110-reference bibliography this map is curated from.

---

*Last updated 2026-05-14.*
