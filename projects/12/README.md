# Project 12: Operating System

## Overview

In chapters 1-6 we described and built a general-purpose hardware architecture. In chapters 7-11 we developed a software hierarchy that makes the hardware usable, culminating in the construction of a modern, object-based language. Other high-level programming languages can be specified and implemented on top of the hardware platform, each requiring its own compiler.

The last major piece missing in this puzzle is an operating system. The OS is designed to close gaps between the computer's hardware and software, making the computer system more accessible to programmers, compilers, and users. For example, to display the text `Hello World` on the screen, several hundred pixels must be drawn aat specific screen location. This can be done by consulting the hardware specification and writing code that turns bits on and off in selected RAM locations. Clearly, high-level programmers expect a better interface. They want to write `print("Hello World")` and let someone else worry about the details. That's where the operating system enters the picture.

## Background

###

## The Jack OS Specification


## Implementation

**Handout:** https://www.nand2tetris.org/project12

### Init functions

Some OS classes use data structures that support the implementation of some of their subroutines. For each such `OSClass`, these data structures can be declared statically at the class level and initialized by a function which, by convention, we call `OSClass.init`. The `init` functions are for internal purposes and are not documented in the OS API.

### Math

- multiply
- divide
- sqrt

### String

- intValue, setInt
- newLine, backSpace, doubleQuote
  
### Array

- `new`
  - In spite of its name, this subroutine is not a constructor but rather a function. Therefore, the implementation of this function must allocate memory space for the new array by explicitly calling the OS function `Memory.alloc`.
- `dispose`
  - This void method is called by statements like `do arr.dispose()`. The `dispose` implementation deallocates the array by calling the OS function `Memory.deAlloc`.
  
### Memory

- `peek`, `poke`
  - `Memory.peak(addr)` returns the value of the RAM at address `addr`.
  - `Memory.poke(addr, value)` sets the word in RAM address `addr` to `value`.
- `alloc`, `dealloc`
- `drawPixel`
- `drawLine`
- `drawCircle`

### Output



- `printChar`
- `printString`
- `printInt`

### Keyboard

The Hack computer memory organization specifies that the keyboard memory map is a single 16-bit memory register located at address 24576.

- `keyPressed`
- `readChar, readString`
- `readInt`

### Sys

- `wait`
  - This function is supposed to wait a given number of milliseconds and return. It can be implemented by writing a loop that runs approximately `duration` milliseconds before terminating.
  - You will have to time your specific computer to obtain a one millisecond wait, as this constant varies from one CPU to another.
  - As a result, your `Sys.wait()` function will not be portable.
  - The function can be made portable by running yet another configuration function that sets various constants reflecting the hardware specifications of the host platform, but for Nand to Tetris this is not needed.
- `halt`
  - Can be implemented by entering an infinite loop.
- `init`
  - According to the Jack language specification, a Jack program is a set of one or more classes. One class must be named `Main`, and this class must include a function named `main`.
  - To start running a program, the `Main.main` function should be called.
  - With that in mind, `Sys.init` should do two things: call all the `init` functions of the other OS classes, and then call `Main.main`.
