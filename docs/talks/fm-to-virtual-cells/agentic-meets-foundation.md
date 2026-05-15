# How do agentic AI and foundation models meet?

> *Explainer page for the [FM-to-Virtual-Cells talk](../fm-to-virtual-cells.md). Answers the question someone asks during Act 1 or Act 4: "what's the relationship between LLM agents and biology FMs?" The short answer: it's bidirectional. The longer answer matters for project selection because Lane 9 — the most commercially fundable lane in the 2026 menu — sits exactly at this intersection.*

## The headline

Agentic AI and biology FMs are **complementary, not competing**. There are four load-bearing patterns at the intersection:

1. **Agents that use FMs as tools** — LLM agent calls a biology FM (frozen) the way it would call a calculator. PathChat-DX, BioAgents, MedAgentGym.
2. **Agents that build FMs** — LLM agent + AI coding agent autonomously designs and trains a virtual-cell architecture. VCHarness (BioMap, 2026).
3. **Agents that reason over FMs** — LLM post-trained with reinforcement learning where a biology FM serves as the *verifier* of biological plausibility. rBio (CZ Biohub, 2025).
4. **Agents that analyze data with FMs as substrate** — autonomous comp-bio agent that runs a full analysis and generates new biological insight. CellVoyager (*Nat Methods* 2026).

All four exist as public 2025–2026 systems. The intersection is no longer vapor — and the [Li et al. 2026 *Nat Biotech* position paper "Agentic AI and the rise of in silico team science"](https://doi.org/10.1038/s41587-026-03035-1) is the first venue-level framing of the whole intersection as a *team-science* shift, not just a tooling shift.

<iframe src="../../assets/agentic-fm-patterns.html" width="100%" height="580" frameborder="0" loading="lazy" title="Agentic AI × foundation models — the four patterns"></iframe>

*Interactive — the four patterns don't form an orthogonal 2×2; the public 2024–2026 systems run along one diagonal, from FM-consumers (bottom-left) to FM-producers (top-right). Hover any bubble for the canonical exemplar.*

## Pattern 1: Agents using FMs as tools

**The structure**: an LLM (Claude / GPT / open Llama / Qwen) sits at the top of the stack. It receives a user query in natural language ("Stage this tumor"; "Predict expression after CRISPRi on Gene X"). It decides which downstream tool to call, calls a biology FM (pathology / single-cell / genomic) as a remote function, then reasons over the FM's output to produce a final answer.

**Canonical exemplars**:

- **[PathChat / PathChat-DX](https://www.nature.com/articles/s41586-024-07618-3)** (Mahmood Lab, *Nature* 2024) — multimodal conversational pathology model. The LLM-side handles the natural-language interface; pathology-FM-side (UNI / CONCH) handles the slide encoding. **PathChat-DX is the first generative-AI pathology tool with FDA Breakthrough Designation (Jan 2025)** — the regulatory template for this pattern.
- **[MedAgentGym](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/medagentgym/)** (ICLR 2026, AACR-relevant) — 72k-task sandboxed code-exec gym with Med-Copilot-7B orchestrating biomedical analyses. The agent writes code to call scikit-learn, run scanpy, query databases. **The substrate for training agents that use bio-FMs as tools.**
- **[Owkin Pathology Explorer in Anthropic's Claude HCLS environment](https://owkin.com)** (2026) — agent that uses Owkin's pathology FMs inside a Claude-based clinical workflow. The agentic interface for FM-driven pathology analysis.

**Why this pattern matters**: it makes biology FMs *accessible* to clinicians and biologists who can't write PyTorch. The interface layer is the LLM; the heavy lift is the biology FM. **The agent doesn't fix the FM's accuracy problems — but it makes them tractable in a clinical workflow.**

## Pattern 2: Agents building FMs

**The structure**: an LLM agent + AI coding agent (think Claude Code or Cursor on biology) autonomously **designs and trains** a virtual-cell architecture from scratch. The agent reads the dataset, proposes an architecture, writes training code, runs the training loop, evaluates the result, and iterates. The output is a *trained model*, not a *predicted answer*.

**Canonical exemplar**:

- **[VCHarness (Cheng et al., bioRxiv 2026.04.11)](https://www.biorxiv.org/content/10.64898/2026.04.11.717183v1)** — BioMap Research + MBZUAI (Le Song + Eric Xing). Combines an AI coding agent with multimodal biological FMs to construct perturbation-response models. **Identifies architectures that outperform expert designs; reduces development time months → days.**

**Why this pattern matters**: it changes who can build a virtual cell. A lab without ML engineering capacity can describe what they want and let the agent prototype. The pattern is early — VCHarness is one paper from one lab as of April 2026 — but it's the agentic ↔ virtual-cell *builder* direction made concrete. **Pairs with the rBio reasoning direction** (Pattern 3): rBio reasons over an existing virtual cell; VCHarness builds new ones.

## Pattern 3: Agents reasoning over FMs

**The structure**: an LLM is post-trained with reinforcement learning. The reward signal comes from a **biology FM serving as a verifier** of biological plausibility — not from RLHF on human preferences, not from text-based correctness, but from "does the biology FM agree this is true?"

**Canonical exemplar**:

- **[rBio v1 (CZ Biohub, 2025)](https://virtualcellmodels.cziscience.com/model/rbio)** — Qwen2.5-3B-Instruct post-trained via GRPO (Group Relative Policy Optimization) using **TranscriptFormer as a soft-supervision verifier**. **First reasoning model trained on virtual-cell simulations.** Answers questions like *"Would suppressing gene A increase activity of gene B?"* with biological grounding from a sc-FM rather than from web text.

**Why this pattern matters**: it inverts the standard LLM tool-use direction. Instead of *the LLM asks the FM for an answer*, here *the LLM is shaped by the FM during training*. The output is an LLM whose reasoning reflects the FM's encoded biology. This is the **virtual-cell reasoning model** the field had been asking for since the 2024 Bunne *Cell* perspective.

**Caveat**: rBio is post-trained on Qwen2.5-3B — a small LLM. Performance is limited by both the LLM's capacity and the verifier's accuracy. If the verifier (TranscriptFormer) is wrong on a query, rBio learns to be confidently wrong. This is the same risk profile as RLHF-with-bad-rewards, transposed to biology.

## Pattern 4: Agents analyzing data with FMs as substrate

**The structure**: an autonomous comp-bio agent receives a dataset and a loose goal ("find what's interesting here"). It runs a full analysis pipeline — QC, clustering, differential expression, pathway enrichment — calling FMs and classical tools as needed, and surfaces *new biological insight* rather than a single predicted value. This is the agent as a *junior computational biologist*, not as a calculator.

**Canonical exemplar**:

- **[CellVoyager (Alber et al., *Nat Methods* 2026)](https://doi.org/10.1038/s41592-026-03029-6)** — "AI CompBio agent generates new insights by autonomously analyzing biological data." Where VCHarness *builds* a model and rBio *reasons* over one, CellVoyager *does the analysis* — autonomously, end-to-end, on real single-cell data.

**Why this pattern matters**: it's the pattern closest to a working scientist's daily loop. The other three patterns produce *models* or *answers*; CellVoyager produces *analyses* — the actual unit of comp-bio work. For a small lab, this is the pattern that most directly threatens-or-augments the bottleneck (analyst bandwidth). The [Li et al. 2026 *Nat Biotech* "in silico team science"](https://doi.org/10.1038/s41587-026-03035-1) framing is essentially "what happens to a lab when Pattern 4 is reliable."

**Caveat**: an autonomous analysis agent that surfaces "insights" inherits the multiple-comparisons problem at machine speed. CellVoyager-style outputs need the same statistical hygiene a human analyst's would — and arguably more, because the agent can generate a hundred plausible-looking findings before a human would notice it's p-hacking.

## The 2026 commercial frame

The intersection is where pharma + AI-native biotechs spend money:

- **JPM 2026 Day 2**: AstraZeneca acquires **Modella AI** — multimodal pathology FMs + agentic AI capabilities in one stack. The agent-uses-FM-as-tool pattern at acquisition scale.
- **JPM 2026 Day 1**: Lilly + NVIDIA $1B AI Co-Innovation Lab — infrastructure commitment that pre-supposes agentic interfaces on FMs.
- **2026**: Owkin launches Pathology Explorer inside Claude — agent ↔ FM as the commercial interface.

The **AACR 2026 AT02 session "Agentic AI as the Cancer Researcher"** + the **4/22 "Agentic AI as the Oncologist" session** are the field's first conference-level commitment to this intersection on a clinical-AI stage.

## What this means for academic project selection

**[Lane 9 (FM-aided experimental design / active learning)](../fm-to-virtual-cells.md#31-the-9-application-lanes-budget-tier-overview)** is the lane that sits at this intersection. It uses the FM-as-tool pattern (Pattern 1) in a closed loop with wet-lab experiments. The buyer is AI-native biotech (Recursion, Insitro, Latent Labs, Vevo) — they actively pay for this work.

**Concrete project shape**: partner with a wet-lab running CRISPRi or drug-perturb screens. Implement an LLM-orchestrated FM-guided selection loop (Pattern 1 — FM-as-tool). Compare to literature-prior baseline. Output: methods paper in *Nat Methods* / *Cell Systems* + a clinical-relevance paper.

**The next-step research questions** that the four patterns expose:

- **Pattern 1 (FM-as-tool)**: how does an agent decide *which* biology FM to call for a given query? Tool-routing for biology is unsolved.
- **Pattern 2 (FM-builder)**: VCHarness designs architectures but not pretraining objectives. Can an agent design a *better objective* than next-gene-prediction? See [Track 2 in the supplementary](../fm-to-virtual-cells-supplementary.md#c-track-dossiers-the-9-small-lab-innovation-tracks).
- **Pattern 3 (FM-as-verifier)**: rBio uses one verifier (TranscriptFormer). Can a reasoning agent use *multiple* verifiers (TranscriptFormer + pathology FM + AlphaGenome) for cross-modality biological reasoning? This is the open follow-up — and the first paper to do it owns the citation.
- **Pattern 4 (FM-as-analysis-substrate)**: CellVoyager produces autonomous analyses — but who audits them? A statistical-hygiene layer for agentic comp-bio outputs (multiple-comparisons control, automated sensitivity analysis) does not exist. That layer is itself a publishable small-lab project.

## Common misconceptions

**"Agentic AI is replacing FMs."** False. Agents need FMs as substrates. Without the biology FM, the agent has nothing to call.

**"Agentic AI fixes the linear-baseline reckoning."** No. The reckoning is about the FMs themselves; agents make those FMs accessible but don't improve their underlying accuracy. If scGPT loses to a linear baseline on perturbation prediction, an agent calling scGPT will also lose to that baseline.

**"Agents need GPT-4-class capacity."** Not necessarily. rBio is built on Qwen2.5-3B (small open model). MedAgentGym's Med-Copilot is 7B params. The bottleneck for biology agents is the *verifier accuracy* and *tool quality*, not the LLM size.

**"This is too early to be a project area."** False as of May 2026. VCHarness, rBio, MedAgentGym, PathChat-DX, Owkin Pathology Explorer are all 2024–2026 public systems. The agentic ↔ FM intersection has tools, papers, and commercial signals. It just doesn't have a settled taxonomy yet — which is the small-lab opportunity.

## Where to go next

- **[The main talk page](../fm-to-virtual-cells.md)** — full 5-act outline.
- **[Supplementary §B.9 — Lane 9 detail (FM-aided experimental design / active learning)](../fm-to-virtual-cells-supplementary.md#b9-lane-9-fm-aided-experimental-design-active-learning-1k10k-fm-side-new-2026)** — the application lane at this intersection.
- **[AACR 2026 AT02 session](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/sessions/2026-04-21-at02-agentic-ai-cancer-researcher/)** — "Agentic AI as the Cancer Researcher."
- **[AACR 2026 4/22 Oncologist session](https://liudengzhang.github.io/conference-vaults/conferences/aacr-2026/sessions/2026-04-22-agentic-ai-as-the-oncologist/)** — clinical-AI-as-agent angle.
- **[ICLR 2026 MedAgentGym dossier](https://liudengzhang.github.io/conference-vaults/conferences/iclr-2026/tools/medagentgym/)** — the agent-substrate for biomedical analyses.
- **[rBio model card on CZI Virtual Cells Platform](https://virtualcellmodels.cziscience.com/model/rbio)** — first public reasoning model trained on virtual-cell simulations.

---

*Last updated 2026-05-13.*
