# Authoring cheat-sheet

Quick syntax reference for writing chapters in this book (MyST Markdown).
Start new chapters from [`chapter_template.md`](chapter_template.md).

## Admonitions

```markdown
:::{note}
Body text.
:::

:::{admonition} Custom title
:class: tip
Body text.
:::
```

Available types: `note`, `tip`, `hint`, `important`, `warning`, `caution`,
`attention`, `danger`, `error`, `seealso`, and `todo` (shown only while
`todo_include_todos = True` in `conf.py`).

## Questions (teachbooks-questions)

```markdown
:::{question} Q1
:type: multiple-choice
:variant: single-select
:showanswer:

Question stem.

---
[ ] Wrong option
> Feedback shown when this option is picked.
[x] Correct option
> Feedback for the correct option.
& Feedback shown only when "show answer" is clicked.
---
:::
```

- Options go between two `---` lines.
- `[x]` marks a correct option, `[ ]` a wrong one.
- `> ` after an option is per-option feedback.
- `& ` after an option is feedback shown only on "show answer".
- For `:variant: multiple-select`, a `^^^` line starts general feedback for
  the whole question.
- `:type: short-answer` is also available for free-text answers.

Full docs: <https://gh.ali360.cloudns.ch/TeachBooks/TeachBooks-Questions>

## Dropdown answers (no grading)

```markdown
:::{dropdown} Question text
Answer text.
:::

:::{admonition} Solution
:class: dropdown
Hidden until clicked.
:::
```

## Tabs (HDL variants)

````markdown
::::{tab-set}
:::{tab-item} Verilog
```verilog
module m; endmodule
```
:::
:::{tab-item} VHDL
```vhdl
entity e is end entity;
```
:::
::::
````

## Timing diagrams (WaveDrom)

````markdown
```{wavedrom}
{ "signal": [
  { "name": "clk", "wave": "p...." },
  { "name": "q",   "wave": "01.0." }
]}
```
````

Try diagrams interactively in the editor: <https://wavedrom.com/editor.html>

## Diagrams (Mermaid)

````markdown
```{mermaid}
flowchart LR
    A[RTL] --> B[Synthesis] --> C[Place & Route]
```
````

## Math

```markdown
Inline: $t_{setup} + t_{cq} \le T_{clk}$

$$
f_{max} = \frac{1}{t_{cq} + t_{logic} + t_{setup}}
$$
```

## Cross-references and labels

```markdown
(part2-rtl-design-fsm)=
# Finite State Machines

See {ref}`part2-rtl-design-fsm` or {doc}`../part2-rtl-design/fsm`.
```

Chapter labels follow `<part-dir>-<slug>`.

## Glossary terms

Define terms in `appendix/glossary.md`:

````markdown
```{glossary}
Flip-flop
  A clocked storage element.
```
````

Reference them anywhere with ``{term}`Flip-flop` ``.

## Figures

Put images in `docs/_static/img/`:

````markdown
```{figure} /_static/img/example.png
:alt: Description
:width: 80%

Caption text.
```
````
