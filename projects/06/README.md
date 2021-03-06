# Chapter 6: Assembler

## Overview

Suppose we are dealing with the assembly code `load R3, 7`.The **assembler** parses each assembly instruction into its underlying fields, for example, `load`, `R3`, and, `7`, translates each field into its equivalent binary code, and finally **assembles** the generated bits into binary instruction that can be executed by the hardware. Pictorially:

```
           Assembler
Assembly -------------> Binary
```

In this chapter we will build the Jack assembler in **Python**.

## Project

**Handout:** https://www.nand2tetris.org/project06

In this project, we are going to implement the **Hack assembler** in Python. It translates assembly code into Hack machine language (binary code). The assembler is made of the following components:

- `parser.py`: parsing the input into instructions and instructions into fields.
- `code.py`: translating the fields (symbolic mnemonics) into binary codes.
- `hack_assembler.py`: drives the entire translation process.
- `symbol_table.py`: resolving symbols (labels in assembly language) into actual addresses.

## 1. `code.py`

This module provides services for translating symbolic Hack mnemonics into their binary codes.Specifically, it translates Hack mnemonics into their binary codes according to the language.

## 2. `symbol_table.py`

Since Hack instructions can contain symbolic references, the assembly process must resolve them into actual addresses. The asssembler deals with this task using a symbol table, designed to create and maintain the correspondence between symbols and their meaning.

## 3. `parser.py`

The Parser encapsulates access to the input assembly code. In particular, it provides a convenient means for advancing through the source code, skipping comments and white space, and breaking each symbolic instruction into its underlying components.

## 4. `hack_assembly.py`

This is the main program that drives the entire assembly process, using the services of the Parser and Code modules.
