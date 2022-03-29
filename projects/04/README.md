# Chapter 4: Machine Language

## Overview



## A-instruction (@xxx)

The A-instruction sets the `A` register to some 15-bit value:

- Symbolic: `@xxx,  where `xxx` is a decimal value ranging from 0 to 32767, or a symbol bound to such a decimal value.
- Binary: `0vvvvvvvvvvvvvvv`, where `0` stands for A-instruction and `vvvvvvvvvvvvvvv` is the 15-bit value of `xxx`.

## C-instruction (dest = comp;jump)

The C-instruction answers three questions: what to compute (an ALU operation, denoted `comp`), where to store the computed value (`dest`), and what to do next (`jump`):

- Symbolic: `dest=comp;jump`,  where `comp` is mandatory. If `dest` is empty, the `=` is omitted; if `jump` is empty, the `;` is omitted.
- Binary: `111accccccdddjjj`, where `111` stands for C-instruction, `acccccc` refers to `comp`, `ddd` refers to `dest`, and `jjj` refers to `jump`. 

## Symbols

The symbols fall into three functional categories:

1. **Predefined Symbols:** representing special memory addresses.
2. **Label Symbols:** representing destinations of goto instructions.
3. **Variable Symbols:** representing variables.

In particular, predefined symbols include:

- **R0, R1, ... , R15:** These symbols are bound to the values 0 to 15.
- **SP, LCL, ARG, THIS, THAT:** These symbols are bound to the values 0, 1, 2, 3, and 4, respectively.
- **SCREEN, KBD:** SCREEN and KBD are bound, respectively, to the values 16384 and 24576 (in hexidecimal: 4000 and 6000), which are the agreed-upon base addresses of the screen memory map and the keyboard memory map.

## Project

**Handout:** https://www.nand2tetris.org/project04

In Project 4, we are going to implement:

- **Mult:**
- **Fill:**

### 1. Mult

Recall that multiplication is the same as adding a number repeatly. For example, 3 * 5 means 3 + 3 + 3 + 3 + 3 or 5 + 5 + 5.

Pseudocode:

```c
i = 1;
sum = 0;

while (i < RAM[1])
{
    sum += RAM[0];
    i++;
}
 
RAM[2] = sum;

return 0;
```

The assembly code is self-explanatory.

### 2. Fill

The assembly code is self-explanatory.