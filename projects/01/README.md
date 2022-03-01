# Project 1

In this project, we are going to implement many commonly-used chips from scratch, starting with the built-in **Nand** chip.

## 1. Not

Recall that `Not a = a Nand a`. This was shown when we were proving "any Boolean function can be represented by a Boolean expression containing only Nand operators".

## 2. And

Recall that **De Morgan's Law** gives `Not (a And b) = (Not a) Or (Not b)`, hence `a And b = Not ((Not a) Or (Not b))`.

## 3. Or

Again, recall that **De Morgan's Law** gives `Not (a Or b) = (Not a) And (Not b)`, hence `a Or b = Not ((Not a) And (Not b))`.

## 4. Xor

The truth table of `Xor` gate is:

| a | b | a Xor b |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The second row gives `(Not a) And b`, and the third row gives `a And (Not b)`, hence the disjunctive normal form (DNF) is `a Xor b = ((Not a) And b) Or (a And (Not b))`.

## 5. Mux

Mux stands for "multiplexer", which is essentially a **"selector"**. There are 2 cases:

| sel | out |
|---|---|
| 0 | a |
| 1 | b |

The first row gives `(Not sel) And a` and the second row gives `sel And b`, hence the DNF is `Mux(a, b, sel) = ((Not sel) And a) Or (sel And b)`.

## 6. Dmux

Dmux stands for "demultiplexer", which is the reverse version of a multiplexer. There are 2 cases:

| sel | a | b |
|---|---|---|
| 0 | in | 0 |
| 1 | 0 | in |

The first row gives `(Not sel) And a` and the second row gives `sel And b`, hence `a = (Not sel) And in and b = sel And b`.

## 7. Not16

Repeat `Not` for 16 times.

## 8. And16

Repeat `And` for 16 times.

## 9. Or16

Use **De Morgan's Law** together with `Not16` and `And16`.

## 10. Mux16

Repeat `Mux` for 16 times.

## 11. Or8Way

Repeat `Or` on each bit for 8 times.

## 12. Mux4Way16

There are 4 cases:

| sel | out |
|---|---|
| 00 | a |
| 01 | b |
| 10 | c |
| 11 | d |

Here we use `sel[0]` to "mux" out "ab" and "cd", and then use `sel[1]` to do the final selection.

## 13. Mux8Way16

Similarly, we use `sel[0]` to "mux" out "ab", "cd", "ef", and "gh", and then use `sel[1]` to do another round of selection, and then use `sel[2]` to do the final selection.

## 14. Dmux4Way

There are 4 cases:

| sel | a | b | c | d |
|---|---|---|---|---|
| 00 | in | 0 | 0 | 0 |
| 01 | 0 | in | 0 | 0 |
| 10 | 0 | 0 | in | 0 |
| 11 | 0 | 0 | 0 | in |

Here we use `sel[1]` to "dmux" out "a or b" and "c or d", and then use `sel[0]` to do the final reversed selection.

## 15. Dmux8Way

Similarly, we use DMux4Way to "dmux" out "a or e", "b or f", "c or g", and "d or h, and then use `sel[2]` for the final reversed selection.