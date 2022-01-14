# Project 2

In this project, we are going to implement **ALU** based on the logical gates from Project 1. 

## 1. HalfAdder

`HalfAdder` is designed to add two bits. The result of this operation is a 2-bit number, and we call its right and left bits `sum` and `carry`. The truth table is:

| a | b | sum | carry |
|---|---|-----|-------|
| 0 | 0 | 0   | 0     |
| 0 | 1 | 1   | 0     |
| 1 | 0 | 1   | 0     |
| 1 | 1 | 0   | 1     |

Note that `sum` is the result of Xor gate and `carry` is the result of And gate.

## 2. FullAdder

`FullAdder` is designed to add three bits. Similar to `HalfAdder`, `FullAdder` outputs two bits. The truth table is:

| a | b | c | sum | carry |
|---|---|---|-----|-------|
| 0 | 0 | 0 | 0   | 0     |
| 0 | 0 | 1 | 0   | 1     |
| 0 | 1 | 0 | 0   | 1     |
| 0 | 1 | 1 | 1   | 0     |
| 1 | 0 | 0 | 0   | 1     |
| 1 | 0 | 1 | 1   | 0     |
| 1 | 1 | 0 | 1   | 0     |
| 1 | 1 | 1 | 1   | 1     |

Here we use HalfAdder twice. Informally, we do `HalfAdder(HalfAdder(a, b), c)`. Note that `HalfAdder(a, b)` gives a partial sum and `HalfAdder(HalfAdder(a, b), c)` gives the final sum directly. The carry bit is a bit tricky to think of: if `HalfAdder(a, b)` gives `carry=1` **or** `HalfAdder(HalfAdder(a, b), c)` gives `carry=1`, the final carry bit will be 1, so we use `Or` gate here.

## 3. Add16

First we use `HalfAdder(a[0], b[0])` for initialization since we only have two bits at this moment, and then loop `FullAdder(a[i], b[i], carry_bit_from_last_round)`.

## 4. Inc16

Just add 1 to the input. Here we use `b[1..15]=false, b[0]=true` to represent 1.

## 5. ALU

We implement the following things:

1. if (zx == 1) set x = 0        // 16-bit constant
2. if (nx == 1) set x = !x       // bitwise not
3. if (zy == 1) set y = 0        // 16-bit constant
4. if (ny == 1) set y = !y       // bitwise not
5. if (f == 1)  set out = x + y  // integer 2's complement addition
6. if (f == 0)  set out = x & y  // bitwise and
7. if (no == 1) set out = !out   // bitwise not
8. if (out == 0) set zr = 1
9. if (out < 0) set ng = 1

Step 1 to 7 are trivial to implement. At the end of step 7, we divide the output into 3 parts:

1. `out[15]` = sign bit = ng => step 9 solved
2. `out[8..15]` = first half of the output
3. `out[0..7]` = second half of the output

For step 8, we use `Or(Or8Way(out[0..7]), Or8Way(out[8..15]))` to find out if any bit is 1. If all bits are 0, then we set `zr=1`; otherwise, we set `zr=0`.