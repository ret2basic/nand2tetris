# Project 9: High-Level Language

## Overview

The assembly and VM languages presented so far in this book are low-level, meaning that they are intended for controlling machines, not for developing applications. In this chapter we present a high-level language, called **Jack**, designed to enable programmers to write high-level programs. Jack is a simple object-based language. It has the basic features and flavor of mainstream languages like Java and C++, with a simpler syntax and no support for inheritance. Despite this simplicity, Jack is a general-purpose language that can be used to create numerous applications. In particular, it lends itself nicely to interactive games like Tetris, Snake, Pong, Space Invaders, and similar classics.

## Examples

### Example 1: Hello World

```
/** Prints "Hello World". File name: Main.jack */
class Main {
    function void main() {
        do Output.printString("Hello World");
        do Output.println(); // New line
        return; // The return statement is mandatory
    }
}
```

### Example 2: Procedural Programming and Array Handling

```
/** Inputs a sequence of integers, and computes their average. */
class Main {
    function void main() {
        var Array a; // Jack arrays are not typed
        var int length;
        var int i, sum;
        let i = 0;
        let sum = 0;
        let length = Keyboard.readInt("How many numbers? ");
        let a = Array.new(length); // Construct the array
        while (i < length) {
            let a[i] = Keyboard.readInt("Enter a number: ");
            let sum = sum + a[i];
            let i = i + 1;
        }
        do Output.printString("The average is: ");
        do Output.printInt(sum / length);
        do Output.println();
        return;
    }
}
```

### Example 3: Abstract Data Types

#### Using classes

```
/** Represents the Fraction type and related operations (class skeleton) */
class Fraction {

    /** Constructs a (reduced) fraction from x and y */
    constructor Fraction new(int x, int y)

    /** Returns the numerator of this fraction */
    method int getNumberator()

    /** Returns the denominator of this fraction */
    method int getDenominator()

    
}
```

#### Implementing classes

```
/** Represents the Fraction type and related operations. */

```


### Example 4: Linked List Implementation





## The Jack Language Specification






## Writing Jack Applications





## Project

In Project 9, we are going to implement the **Breakout** game. Specifically, we implement the following modules:

- `Ball.jack`
- `Brick.jack`
- `Paddle.jack`
- `Breakingoutgame.jack`
- `Main.jack`

### `Ball.jack`



### `Brick.jack`



### `Paddle.jack`



### `Breakingoutgame.jack`



### `Main.jack`


