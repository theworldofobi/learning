---
myst:
  html_meta:
    description: "TODO: one-sentence summary of this chapter."
---

(part4-synthesis-timing-sta)=
# Static Timing Analysis

:::{admonition} Learning objectives
:class: tip
By the end of this chapter you will be able to:

- TODO: objective 1
- TODO: objective 2
- TODO: objective 3
:::

:::{admonition} Prerequisites
:class: note
- TODO: link earlier chapters, e.g. ``{ref}`part1-foundations-digital-logic` ``
:::

:::{todo}
Draft the content for "Static Timing Analysis".
:::

## Introduction

TODO: motivate the topic.

## Concepts

### TODO: Concept 1

TODO

### TODO: Concept 2

TODO

## Worked example

TODO: walk through an example.

::::{tab-set}

:::{tab-item} Verilog
```verilog
// TODO: Verilog example
module todo_module (
    input  wire clk,
    input  wire rst_n
);
    // TODO
endmodule
```
:::

:::{tab-item} SystemVerilog
```systemverilog
// TODO: SystemVerilog example
module todo_module (
    input  logic clk,
    input  logic rst_n
);
    // TODO
endmodule
```
:::

:::{tab-item} VHDL
```vhdl
-- TODO: VHDL example
library ieee;
use ieee.std_logic_1164.all;

entity todo_entity is
    port (
        clk   : in std_logic;
        rst_n : in std_logic
    );
end entity todo_entity;

architecture rtl of todo_entity is
begin
    -- TODO
end architecture rtl;
```
:::

::::

### Timing diagram

```{wavedrom}
{ "signal": [
  { "name": "clk",  "wave": "p......" },
  { "name": "TODO", "wave": "0.1..0." }
]}
```

### Block diagram

```{mermaid}
flowchart LR
    A[TODO: input] --> B[TODO: logic] --> C[TODO: output]
```

## Check your understanding

:::{question} Q1
:type: multiple-choice
:variant: single-select
:showanswer:

TODO: single-answer question stem.

---
[ ] TODO: option A
> TODO: feedback for A
[x] TODO: option B (correct)
> TODO: feedback for B
[ ] TODO: option C
> TODO: feedback for C
---
:::

:::{question} Q2
:type: multiple-choice
:variant: multiple-select
:showanswer:

TODO: multiple-answer question stem.

---
[x] TODO: option A (correct)
[ ] TODO: option B
[x] TODO: option C (correct)
---
:::

:::{dropdown} Quick check (no grading): TODO question
TODO: answer.
:::

## Exercises

1. TODO: exercise.

:::{admonition} Solution
:class: dropdown
TODO: solution.
:::

## Summary

- TODO: key takeaway 1
- TODO: key takeaway 2

## Further reading

- TODO: reference
