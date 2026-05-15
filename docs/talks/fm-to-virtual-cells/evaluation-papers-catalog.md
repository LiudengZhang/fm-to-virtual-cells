# 2025–2026 evaluation papers catalog

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). The full reckoning canon, organized by what each paper evaluated and what axis it covered. As of May 2026, Lane 4 (replication / critique) is the most-published lane of 2025–2026 by a wide margin — eleven evaluation papers + one contrarian. This page is the directory.*

## The canon at a glance

| # | Paper | Venue | Date | Models evaluated | Headline |
|---|---|---|---|---|---|
| 1 | **Ahlmann-Eltze & Huber** | *Nature Methods* | Aug 2025 | 6 sc-FMs (scGPT, Geneformer, scFoundation, GEARS, CPA) + UCE | None beats `mean-of-training-perturbations` linear baseline |
| 2 | **Kedzierska et al.** | *Genome Biology* 26:101 | Apr 2025 | scGPT, Geneformer, UCE, scFoundation | scFMs lose to PCA + kNN zero-shot |
| 3 | **Wenkel et al.** | *Nature Methods* | Jul 2025 | sc-FMs vs `latent-additive` | Latent-additive + scGPT-embeddings = new baseline floor |
| 4 | **Wu et al.** | *Nature Methods* | Jan 2026 | 27 methods × 29 datasets × 6 metrics | Axis-by-axis failure decomposition |
| 5 | **Wu et al.** | *Genome Biology* | Oct 2025 | 6 scFMs (Geneformer, scGPT, UCE, scFoundation, LangCell, scCello) | "No single scFM consistently outperforms others" |
| 6 | **Liu et al. (scEval)** | *Advanced Science* | Jan 2026 | 10 scFMs × 8 tasks | "Challenges the necessity of developing FMs for single-cell" |
| 7 | **Parameter-free baseline** | bioRxiv 2026.02.11 | Feb 2026 | sc-FMs vs parameter-free reps | Parameter-free wins on downstream benchmarks |
| 8 | **PertEval-scFM** | ICML 2025 | Jul 2025 | scFM embeddings (standardized framework) | Most don't beat baselines on strong/atypical perturbations |
| 9 | **CellBench-LS** | bioRxiv 2026.04.01 | Apr 2026 | 7 scFMs + PCA / UMAP / scVI | Stratified low-supervision: FMs lead cell-type, classical leads gene-expression |
| 10 | **Han et al. (real-world)** | bioRxiv 2026.04.17 | Apr 2026 | scFMs in pharma deployment | Industry-grade robustness gaps exposed |
| 11 | **Cellular-dynamics zero-shot** | bioRxiv 2026.03.10 | Mar 2026 | zero-shot scFM on RNA velocity | scFMs fail to recover cellular dynamics |
| 12 | **Csendes scPerturBench** | BM2 Lab | 2024 | scGPT replication | Original split was leaky; cleaner splits expose failure |
| **+contrarian** | **FMs Improve Perturbation** | bioRxiv 2026.02.18 | Feb 2026 | sc-FMs with sufficient data | **FMs DO improve perturbation prediction with enough data** |

<iframe src="../../assets/fm-eval-catalog-timeline.html" width="100%" height="470" frameborder="0" loading="lazy" title="The reckoning corpus by venue tier"></iframe>

*Interactive — the same 13 papers placed by publication date (x) and venue tier (y): six landed in peer-reviewed journals — Nature Methods ×3, Genome Biology, Advanced Science — so the corpus isn't one lab's grievance, it cleared review across venues. Colour marks the evaluation axis; the green ✕ is the contrarian voice. Hover for the headline.*

## The catalog organized by what's covered

### Axis 1: Perturbation prediction (the original reckoning)

The 2025 critique trio + Wu et al. *Nat Methods* established that current sc-FMs don't beat linear baselines on perturbation prediction as originally defined.

- **[Ahlmann-Eltze & Huber 2025 *Nat Methods*](https://www.nature.com/articles/s41592-025-02772-6)** — THE canonical paper. Pure inference on 6 published FMs + a one-line linear baseline. **<$2k compute. Retired the entire sc-FM perturbation-prediction leaderboard.**
- **[Kedzierska et al. 2025 *Genome Biology*](https://doi.org/10.1186/s13059-025-03574-x)** — Extended the result to UCE and the zero-shot setting. Cambridge + Broad.
- **[Wenkel et al. 2025 *Nat Methods*](https://pubmed.ncbi.nlm.nih.gov/41044630/)** — Proposed `latent-additive + scGPT-embeddings` as the new baseline floor. Current FMs still don't beat it consistently.
- **[Wu et al. 2025 *Nat Methods*](https://www.nature.com/articles/s41592-025-02980-0)** — 27 methods × 29 datasets × 6 metrics. The first axis-by-axis failure decomposition — some FMs are stronger on combinatorial perturbations, none on out-of-distribution cell types.
- **[Parameter-free baseline (bioRxiv 2026.02)](https://www.biorxiv.org/content/10.64898/2026.02.11.705358v1)** — Direct successor to Ahlmann-Eltze; cleanest post-reckoning headline.
- **[PertEval-scFM ICML 2025](https://icml.cc/virtual/2025/poster/43799)** — Formal venue stamp.

### Axis 2: Beyond perturbation — most cell-level tasks

The 2026 evaluation wave broadened the critique past perturbation-only.

- **[Liu et al. 2026 *Adv Sci* — scEval](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)** — 10 scFMs × 8 tasks. **Headline**: *"single-cell foundation models may not consistently outperform task-specific methods in all tasks, which challenges the necessity of developing foundation models for single-cell analysis."* The strongest "is the FM paradigm worth it?" framing.
- **[Wu et al. 2025 *Genome Biology* (Oct 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492631/)** — 6 scFMs (Geneformer, scGPT, UCE, scFoundation, LangCell, scCello) on gene-level + cell-level with cell-ontology-grounded metrics. **Headline**: *"no single scFM consistently outperforms others across all tasks."* (Distinct from Wu *Nat Methods* — different authors despite shared surname.)
- **[CellBench-LS (bioRxiv 2026.04)](https://www.biorxiv.org/content/10.64898/2026.04.01.714123v1)** — 7 scFMs (scGPT, Geneformer, LangCell, CellPLM, scMulan, scFoundation, Nicheformer) + PCA / UMAP / scVI baselines, in low-supervision scenarios. FMs lead on cell-type recognition; classical methods stay competitive on gene-expression quantification.

### Axis 3: New evaluation dimensions

The 2026 wave opened new axes the original reckoning hadn't covered.

- **[Han et al. — Real-world RNA-seq data integration (bioRxiv 2026.04)](https://www.biorxiv.org/content/10.64898/2026.04.17.719314v1)** — Industry-authored (Mansi et al.); pharma-relevant deployment-grade evaluation. Robustness gaps in real-world data integration.
- **[Cellular-dynamics zero-shot (bioRxiv 2026.03)](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)** — Extends the critique to **RNA-velocity / dynamics reconstruction**, a new axis beyond perturbation prediction. zero-shot scFM embeddings fail to recover cellular dynamics.

### Axis 4: Replication + clean splits

- **[Csendes scPerturBench (BM2 Lab)](https://bm2-lab.github.io/scPerturBench-reproducibility/)** — Independent scGPT replication on a benchmark with adversarial perturbation/cell-type splits. Found the original scGPT train/test split was leaky.

### The contrarian voice

- **[Foundation Models Improve Perturbation Response Prediction (bioRxiv 2026.02.18)](https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1)** — Claims that **with sufficient data**, FMs *do* significantly improve genetic + chemical perturbation predictions and approach fundamental performance limits. **Directly opposes** Ahlmann-Eltze, Liu, parameter-free, and the Wu papers. **Whether this paper holds up determines whether the reckoning is a permanent verdict or a temporary state.**

## Uncovered axes — what's still open

Across these 12 papers, five evaluation axes are not yet systematically covered. Each is wide-open for a 2026 Lane 4 paper at <$2k compute. **These are the differentiating angles for a new critique paper today.**

| Uncovered axis | Why it matters | What's needed |
|---|---|---|
| **Donor-split benchmarks** | Cross-donor generalization barely measured because the data substrate is donor-skewed (Tahoe-100M = 50 cell lines, no patient-derived) | A held-out-donor benchmark on HTAN or HCA real-world cohorts |
| **Cross-tissue transfer** | Pretraining on tissue A, evaluating on tissue B — almost never tested. Even UCE's cross-species tests are within healthy tissue. | A formal cross-tissue split using a tissue-stratified scRNA atlas |
| **Time-resolved perturbation** | Most evals are steady-state. What about 0h vs 6h vs 24h post-perturbation? | A perturb-seq dataset with multiple timepoints + a temporal-split protocol |
| **Cancer-cell-line → primary-tumor transfer** | The donor-split applied to cancer specifically. If sc-FMs can't transfer K562 → patient tumor, they can't help oncology. | Paired K562/RPE1 + matched primary-tumor scRNA cohorts |
| **Rare-cohort robustness** | How does FM performance degrade with <100 cells per class? The xVERSE paper hints at this (resolves rare types with 4 cells) but doesn't formalize the curve. | A systematic degradation-vs-cohort-size benchmark across sc-FMs |

The first paper that lands any of these owns the citation for the 2026–2028 cycle. **<$2k compute. *Nat Methods* / *Genome Biology* / *Adv Sci* will take it.**

## How to use this catalog for project selection

**If you want to write a critique paper (Lane 4)**:
1. Pick an uncovered axis from the table above.
2. Verify the axis isn't covered by checking the 12 papers above.
3. Choose your test set: Replogle (Cell 2022), Norman (Science 2019), Tahoe-100M, Open Problems v2, scPerturBench.
4. Implement at least the Ahlmann-Eltze + Wenkel baselines as your floor.
5. Cite the contrarian (FMs Improve Perturbation) and engage with whether your finding supports or contradicts it.
6. See [reading an FM paper critically](reading-an-fm-paper-critically.md) for the checklist you'd want your own paper to pass.

**If you want to write a methods paper (Track 1–9)**:
- Tracks 3, 6, 8, 9 are the post-reckoning evaluation frontier.
- [Track 9 (causal transportability)](../fm-to-virtual-cells-supplementary.md#c9-track-9-causal-transportability-benchmarks-new-2026) is the most open, because Virtual Cells Need Context (2026) named the framework but didn't operationalize it into a benchmark suite.
- [Track 8 (Synergistic Information Score)](../fm-to-virtual-cells-supplementary.md#c8-track-8-synergistic-information-evaluation-of-multimodal-fms-new-2026) is the most concrete — Microsoft published the metric in Feb 2026 and no one has applied it across the multimodal FM zoo yet.

## The narrative arc

The 12 papers tell one story when read in chronological order:

- **2024 → early 2025**: scattered warnings (Boiarsky NeurIPS workshop, Csendes scPerturBench preprint).
- **Aug 2025**: Ahlmann-Eltze *Nat Methods* lands the canonical blow — linear baseline beats every published sc-FM on perturbation prediction.
- **Apr–Oct 2025**: Kedzierska, Wenkel, Wu *Nat Methods*, Wu *Genome Biology* — the reckoning becomes a corpus.
- **Jan–Apr 2026**: Liu *Adv Sci*, parameter-free, CellBench-LS, Han et al., cellular-dynamics — the reckoning generalizes past perturbation prediction to most cell-level tasks. **By Apr 2026, it's a discipline-wide consensus.**
- **Feb 2026**: The contrarian voice arrives (FMs Improve Perturbation). The reckoning becomes contested again.
- **Feb 2026**: Virtual Cells Need Context names the *theoretical* framing (causal transportability).
- **May 2026**: the field's honest position is *four-part* — reckoning + contrarian + theoretical underpinning + architectural response (xVERSE, compositional FMs, TranscriptFormer).

This is the arc the talk's Act 1 walks through.

## Where to go next

- **[The main talk page Act 1 §1.3](../fm-to-virtual-cells.md#13-the-four-eras)** — the four eras: paradigm → ambition → reckoning → response.
- **[The paper map](paper-map.md)** — this catalog placed in the wider literature network, with a systematic reading order.
- **[Why do linear baselines win?](why-linear-baselines-win.md)** — the mechanism behind the catalog.
- **[How to read an FM paper critically](reading-an-fm-paper-critically.md)** — the 8-item checklist.
- **[Supplementary §E — the full evaluation catalog with methodology details](../fm-to-virtual-cells-supplementary.md#e-20252026-evaluation-papers-catalog)** — even more depth.

---

*Last updated 2026-05-13.*
