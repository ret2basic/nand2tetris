# Project 4

In this project, we are going to implement **Multiplication** and **I/O handling** in **Hack assembly language**. Specifically:

- **Multiplication** (`Mult.asm`)
  - The inputs of this program are the values stored in `R0` and `R1` (`RAM[0]` and `RAM[1]`). The program computes the product `R0 * R1` and stores the result in `R2`.
  - Assume that `R0 >= 0`, `R1 >= 0`, and `R0 * R1 < 32768` (your program need not test these assertions).
  - THe supplied `Mult.tst` and `Mult.cmp` scripts are designed to test your program on representative data values.
- **I/O handling** (`Fill.asm`)
  - This program runs an infinite loop that listens to the keyboard.
  - When a key is pressed (any key), the program blackens the screen by writing black in every pixel.
  - When no key is pressed, the program clears the screen by writing white in every pixel.
  - You may choose to blacken and clear the screen in any spatial pattern, as long as pressing a key continuously for long enough will result in a fully blackened screen, and not pressing any key for long enough will result in a cleared screen.
  - This program has a test script (`Fill.tst`) but no compare file--it should be checked by visibly inspecting the simulated screen in the CPU emulator.

## Mult

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

## Fill

Pseudocode:

```c

```

The assembly code is self-explanatory.