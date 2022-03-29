# Chapter 3: Memory

## Overview



## Combinational vs. Sequential

The chips that we built in Project 1 and Project 2 are **time-independent** (or **combinational**). In this chapter, we introduce the concept of **time** and move on to **time-dependent** (or **sequential**) logic.

## Clock Cycle

Time is a profound notion. In computer science, we have no way to model **continuous** time as what we are experience in real life. Instead, we divide time into small chunks so that it becomes **discrete**. Each chunk is called a **clock cycle**, and it is the smallest time interval that a computer can measure. The choice of clock cycle is not random. It must follow these two principles:

1. The clock cycle shouldn't be too small, because small clock cycle is not able to handle time delay properly and errors may occur. 
2. The clock cycle shouldn't be too large, because large clock cycle slows down the computer.

In order to balance out these two conditions, **we let clock cycle to be slightly larger than the maximal time delay in any chip in the system**.

## Data Flip-Flop (DFF)

With the notion of (discrete) time, we are ready to implement computer memory. Memory chips are designed to "remember", or store, information over time. The low-level devices that facilitate this storage abstraction are named **flip-flop gates**, of which there are several variants. In Nand to Tetris we use a variant named **data flip-flop**, or **DFF**. Like the Nand chip, DFF is given to us so we are not going to implement it. We are going to implement the following types of computer memory:

- Registers
- RAM
- Counter

Note that the "counter" mentioned here is the **Program Counter (PC)**.

## Project

**Handout:** https://www.nand2tetris.org/project03

In Project 3, we are going to implement:

- **Bit:**
- **Register:**
- **RAM8:** RAM 8-bit version
- **RAM64:** RAM 64-bit version
- **RAM512:** RAM 512-bit version
- **RAM4K:** RAM 4K-bit version
- **RAM16K:** RAM 16K-bit version
- **PC:** Program Counter

**Note:** in HDL, bits are numbered from right to left, starting with 0. For example, we have address = abcdef, then:

- `address[0] = f`
- `address[1] = e`
- `address[2] = d`
- `address[3] = c`
- `address[4] = b`
- `address[5] = a`

### 1. Bit

We use `Mux` to select `out[t+1] = in[t]` or `out[t+1] = out[t]` based on the value of `load`, then use `DFF` to "shift" the output to the next clock cycle. Note that this chip is a loop: the output of `Mux` is the input of `DFF`, and the output of `DFF` is the input of `Mux`.

### 2. Register

Apply `Bit` to each bit of `in[16]`.

### 3. RAM8

1. Use `DMux8Way` to assign `load` for each register.
2. Use `Register` on each register.
3. Use `Mux8Way16` to select the correct register based on the given address. If `load==1`, then the value of this register is set to the value of `in[16]`.

### 4. RAM64

Note that `RAM64 = RAM8 * 8`. Here `address[0..2]` is for selecting one of the `RAM8` chips, and `address[3..5]` is for selecting one of the registers within the selected `RAM8`.

### 5. RAM512

Note that `RAM512 = RAM64 * 8`. Here `address[0..5]` is for selecting one of the `RAM64` chips, and `address[6..8]` is for selecting one of the registers within the selected `RAM64`.

### 6. RAM4K

Note that `RAM4K = RAM512 * 8`. Here `address[0..8]` is for selecting one of the `RAM512` chips, and `address[9..11]` is for selecting one of the registers within the selected `RAM512`.

### 7. RAM16K

Note that `RAM16K = RAM4K * 4`, so we use `DMux4Way` and `Mux4Way16` for this chip. Here `address[0..11]` is for selecting one of the `RAM4K` chips, and `address[12..13]` is for selecting one of the registers within the selected `RAM4K`.

### 8. PC

