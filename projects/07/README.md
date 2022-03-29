# Chapter 7: Virtual Machine I Processing

## Overview

**Virtual Machine (VM)** is the intermediate layer between high-level source code and low-level machine language. For example, JVM. VM gives *cross-platform* compatibility: since the virtual machine may be realized with relative ease on many hardware platforms, the same VM code can run as is on any device equipped with such a VM implementation. The downside of this VM two-tier translation process is *reduced efficiency*.

Our VM model is *stack-based*: all the VM operations take their operands from, and store their results on, the stack. There is only one data type: a signed 16-bit integer. A VM program is a sequence of VM commands that fall into five categories:

- Comments and White Space
  - Lines beginning with `//` are considered comments and are ignored.
  - Blank lines are permitted and are ignored.
- Push/Pop Commands
  - `push segment index`: pushes the value of `segment[index]` onto the stack
  - `pop segment index`: pops the top stack value and stores it in `segment[index]`
- Arithmetic-Logical Commands
  - Arithmetic commands: `add`, `sub`, `neg`
  - Comparison commands: `eq`, `gt`, `lt`
  - Logical commands: `and`, `or`, `not`
- Branching Commands
- Function Commands

In this chapter we focus on the arithmetic-logical and push/pop commands.

## Project

**Handout:** https://www.nand2tetris.org/project07

In Project 7, we are going to implement the **VM Translator**. Specifically, we implement the following modules:

- `parser.py`
- `code_writer.py`
- `vm_translator.py`

### `parser.py`



### `code_writer.py`



### `vm_translator.py`

