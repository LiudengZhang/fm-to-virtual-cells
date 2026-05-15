# FMs → Virtual Cells

Talk prep + knowledge base for AI foundation models, single-cell foundation models, perturbation prediction, and the virtual cell vision.

**This repo is the v2 / extension of [awesome-virtual-cell](https://github.com/LiudengZhang/awesome-virtual-cell).**

The original `awesome-virtual-cell` is a flat curated link list. This repo replaces that format with:

- A YAML-driven resource library (`data/resource-library/fm-to-virtual-cells.yaml`) carrying richer per-item metadata (people, institutes, themes, kind, papermap category).
- An MkDocs Material site that renders a filterable resource table, ranked dossier pages for top people / institutes / themes (via [resourcelib-views](https://github.com/Light-Kit/resourcelib-views)), a 5-act talk script, 8 explainers, a ~55-paper Adjacent Methods catalog, and ~12 interactive Plotly figures.
- A 90-min speed-read curriculum and a cross-vault Foundation Models index.

## Site

Built and deployed via `mkdocs gh-deploy`. The deployed site is password-gated using [mkdocs-encryptcontent-plugin](https://github.com/CoinK0in/mkdocs-encryptcontent-plugin). Pass the password via the `SITE_PASSWORD` env var at build time:

```bash
SITE_PASSWORD='your-password' mkdocs build --strict
SITE_PASSWORD='your-password' mkdocs gh-deploy --force
```

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
SITE_PASSWORD='your-password' mkdocs serve -a 127.0.0.1:8000
```

## Regenerating views

```bash
resourcelib-views generate data/resource-library/fm-to-virtual-cells.yaml \
  --out docs/talks/fm-to-virtual-cells/views/ \
  --top-people 10 --top-institutes 10 --top-themes 10
```

## Relationship to awesome-virtual-cell

| | awesome-virtual-cell (v1) | fm-to-virtual-cells (v2) |
|---|---|---|
| Content model | Markdown link list | YAML schema (resourcelib) |
| Site | Static awesome-list | MkDocs Material + ranked dossiers |
| Items per entry | URL + one-line description | + people, institutes, themes, kind, papermap category |
| Talk prep | None | 5-act script, supplementary, 8 explainers, 12 figures |
| Status | Archive | Active |

Items from `awesome-virtual-cell` have been ported into the YAML and re-rendered in the resource library here.
