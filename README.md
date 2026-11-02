# ASIC Design for Beginners

An interactive book about ASIC design, built with [Sphinx](https://www.sphinx-doc.org/)
and the [Shibuya](https://shibuya.lepture.com/) theme.

> **Status:** boilerplate only. Every page is a placeholder marked `TODO`.

## Quick start

Requires [uv](https://docs.astral.sh/uv/). uv installs Python 3.13 for you.

```bash
uv sync          # create .venv and install pinned dependencies
make livehtml    # live-reloading preview at http://127.0.0.1:8000
```

Without `make`:

```bash
uv run sphinx-build -b html docs docs/_build/html
```

Other targets: `make html`, `make strict` (warnings are errors), `make linkcheck`, `make clean`.

Add a dependency with `uv add <pkg>` (or `uv add --dev <pkg>` for tooling).
Commit `pyproject.toml` and `uv.lock` together.

## Layout

```text
.
├── pyproject.toml / uv.lock   # dependencies (uv)
├── Makefile
└── docs/
    ├── conf.py                # Sphinx configuration
    ├── index.md               # landing page + toctrees
    ├── _static/               # custom.css, img/
    ├── _templates/
    │   ├── chapter_template.md
    │   └── AUTHORING.md       # syntax cheat-sheet
    ├── preface/
    ├── part1-foundations/
    ├── part2-rtl-design/
    ├── part3-verification/
    ├── part4-synthesis-timing/
    ├── part5-physical-design/
    ├── part6-tapeout/
    ├── projects/
    └── appendix/              # glossary, references, cheat sheets
```

## Interactive features

| Feature                              | Extension                              |
| ------------------------------------ | -------------------------------------- |
| Markdown pages (MyST)                | `myst-parser`                          |
| Cards, grids, tabs, dropdowns        | `sphinx-design`                        |
| Copy button on code blocks           | `sphinx-copybutton`                    |
| Collapsible admonitions              | `sphinx-togglebutton`                  |
| Timing diagrams                      | `sphinxcontrib-wavedrom`               |
| Block / flow diagrams                | `sphinxcontrib-mermaid`                |
| Multiple-choice / short-answer quiz  | `teachbooks-questions`                 |
| Draft TODO boxes                     | `sphinx.ext.todo`                      |

## Writing content

See [`docs/_templates/AUTHORING.md`](docs/_templates/AUTHORING.md) for the syntax
cheat-sheet, and copy `docs/_templates/chapter_template.md` to start a new chapter.
