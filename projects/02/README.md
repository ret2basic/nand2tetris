# Chapter 2: Boolean Arithmetic

## Overview

Inside computers, **everything** is represented using binary codes. In this chapter, we are going to play with **binary addition** and **sign convertion**.

A pair of binary numbers can be added bitwise from right to left. For each pair of bits, binary addition produces two outputs: `sum` and `carry`. Note that the last carry bit is the overflow bit. For example, consider 1001 + 1001 = (1)0010 with word size 4. The very first step is adding the LSBs of both operands, that is, `1 + 1`. Here we get `sum = 0` and `carry = 1`. The very last step is adding the MSBs of both operands, that is, `1 + 1`. Again, here we get `sum = 0` and `carry = 1`, but this carry bit exceeds the word size hence is thrown away, so the final result is 0010 instead of 10010. This phenomenon is called **overflow**.

In order to represent negative numbers, we use **2's complement**. Suppose the word size is `n` and `x` is a negative number, then the 2's complement representation of `x` is `2**n - x`. This design is better than the naive "sign bit" design since there is no "positive 0" and "negative 0" issue. To compute the negative of a number, we convert this number to its binary representation, flip all bits, and then add 1 to it. For example, we are given number 4 and we want to compute -4 in 2's complement. The binary representation of 4 is 0100, flip all bits and we get 1011, then add 1 to it we get 1100. That is, -4 = 1100 in 2's complement.

## Project

**Handout:** https://www.nand2tetris.org/project02

In Project 2, we are going to implement:

- **HalfAdder:**
- **FullAdder:**
- **Add16:** Addition 16-bit version
- **Inc16:** Increment 16-bit version
- **ALU:** Arithmetic Logical Unit

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

First we use `HalfAdder(a[0], b[0])` since we don't have any carry bit at this moment, and then loop `FullAdder(a[i], b[i], carry_bit_from_last_round)`.

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