# Chapter 1: Boolean Logic

## Course

We know that And gate, Or gate, and Not gate are the most fundamental logical gates of computer hardware. In fact, these three gates can be reduced to Nand gate, and we claim that **Nand gate is THE most fundamental logical gate**. We prove this claim informally:

- According to De Morgan's law, `x Or y = Not((Not a) And (Not y))`, so Or gate is reduced to Not gate and And gate.
- `Not(x) = Nand(x, x)`, so Not gate is reduced to Nand gate.
- `And(x, y) = Not(Nand(x, y))`, so And gate is reduced to Nand gate.

Based on these three observations, And gate, Or gate, and Not gate can be reduced to Nand gate. In nand2tetris, we are given a ready-to-go Nand chip (it is actually the only thing we have) and we are going to build a modern computer on top of it.

## Project

**Handout:** https://www.nand2tetris.org/project01

In Project 1, we are going to implement:

- **Not:** Not gate 1-bit version
- **And:** And gate 1-bit version
- **Or:** Or gate 1-bit version
- **Xor:** Xor gate 1-bit version
- **Mux:** Multiplexer 1-bit version
- **DMux:** Demultiplexer 1-bit version
- **Not16:** Not gate 16-bit version
- **And16:** And gate 16-bit version
- **Or16:** Or gate 16-bit version
- **Mux16:** Multiplexer 16-bit version
- **Or8Way:**
- **Mux4Way16:**
- **Mux8Way16:**
- **DMux4Way:**
- **DMux8Way:**

**Note:** In HDL, bits are numbered from right to left, starting with 0. For example, we have sel = 110, then:

- `sel[0] = 0`
- `sel[1] = 1`
- `sel[2] = 1`

### 1. Not

Recall that `Not a = a Nand a`. This was shown when we were proving "any Boolean function can be represented by a Boolean expression containing only Nand operators".

### 2. And

Recall that **De Morgan's Law** gives `Not (a And b) = (Not a) Or (Not b)`, hence `a And b = Not ((Not a) Or (Not b))`.

### 3. Or

Again, recall that **De Morgan's Law** gives `Not (a Or b) = (Not a) And (Not b)`, hence `a Or b = Not ((Not a) And (Not b))`.

### 4. Xor

The truth table of `Xor` gate is:

| a | b | a Xor b |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The second row gives `(Not a) And b`, and the third row gives `a And (Not b)`, hence the disjunctive normal form (DNF) is `a Xor b = ((Not a) And b) Or (a And (Not b))`.

### 5. Mux

Mux stands for "multiplexer", which is essentially a **"selector"**. There are 2 cases:

| sel | out |
|---|---|
| 0 | a |
| 1 | b |

The first row gives `(Not sel) And a` and the second row gives `sel And b`, hence the DNF is `Mux(a, b, sel) = ((Not sel) And a) Or (sel And b)`.

### 6. Dmux

Dmux stands for "demultiplexer", which is the reverse version of a multiplexer. There are 2 cases:

| sel | a | b |
|---|---|---|
| 0 | in | 0 |
| 1 | 0 | in |

The first row gives `(Not sel) And a` and the second row gives `sel And b`, hence `a = (Not sel) And in and b = sel And b`.

### 7. Not16

Repeat `Not` for 16 times.

### 8. And16

Repeat `And` for 16 times.

### 9. Or16

Use **De Morgan's Law** together with `Not16` and `And16`.

### 10. Mux16

Repeat `Mux` for 16 times.

### 11. Or8Way

Repeat `Or` on each bit for 8 times.

### 12. Mux4Way16

There are 4 cases:

| sel | out |
|-----|-----|
| 00 | a |
| 01 | b |
| 10 | c |
| 11 | d |

Here we use `sel[0]` to "mux" out "ab" and "cd", and then use `sel[1]` to do the final selection.

### 13. Mux8Way16

Similarly, we use `sel[0]` to "mux" out "ab", "cd", "ef", and "gh", and then use `sel[1]` to do another round of selection, and then use `sel[2]` to do the final selection.

### 14. Dmux4Way

There are 4 cases:

| sel | a | b | c | d |
|-----|---|---|---|---|
| 00 | in | 0 | 0 | 0 |
| 01 | 0 | in | 0 | 0 |
| 10 | 0 | 0 | in | 0 |
| 11 | 0 | 0 | 0 | in |

Here we use `sel[1]` to "dmux" out "a or b" and "c or d", and then use `sel[0]` to do the final reversed selection.

### 15. Dmux8Way

Similarly, we use DMux4Way to "dmux" out "a or e", "b or f", "c or g", and "d or h, and then use `sel[2]` for the final reversed selection.
