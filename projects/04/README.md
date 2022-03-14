# Project 4

**Handout:** https://www.nand2tetris.org/project04

## 1. Mult

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

## 2. Fill

The assembly code is self-explanatory.