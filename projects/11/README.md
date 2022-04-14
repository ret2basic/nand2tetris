# Project 11: Compiler II

## Overview

Most programmers take compilers for granted. But if you stop to think about it, the ability to translate a high-level program into binary code is almost like magic. In Nand to Tetris we devote four chapters (7-11) for demystifying this magic. Our hands-on methodology is based on two tiers:

1. A **virtual machine (VM)** back end that translates VM commands into machine language
2. A front end **compiler** that translates Jack programs into VM code.

Building a compiler is a challenging undertaking, so we divide it further into two conceptual modules:

1. A **syntax analyzer**, developed in chapter 10
2. A **code generator**, the subject of this chapter.

## Code Generation

Compilation example:

```
/** Represents a two-dimensional point.
    File name: Point.jack. */
class Point{
    // The coordinates of this point:
    field int x, y

    // The number of Point objects constructed so far:
    static int pointCount;

    /** Constructs a two-dimensional point and
        initializes it with the given coordinates. */
    constructor Point new(int ax, int ay){
        let x = ax;
        let y = ay;
        let pointCount = pointCount + 1;
        return this;
    }

    /** Returns the x coordinate of this point. */
    method int getx(){ return x; }

    /** Returns the y coordinate of this point. */
    method int gety(){ return y; }
    
    /** Returns the number of Point constructed so far. */
    function int getPointCount(){
        return pointCount;
    }

    /** Returns a point which is the point plus the other point. */
    method Point plus(Point other){
        return Point.new(x + other.getx(), y + other.gety());
    }

    /** Returns the Euclidean distance between
        this and the other point. */
    method int distance(Point other){
        var int dx, dy;
        let dx = x - other.getx();
        let dy = y - other.gety();
        return Math.sqrt((dx*dx) + (dy*dy));
    }

    /** Prints this point, as "(x, y)" */
    method void print(){
        do Output.printString("(");
        do Output.printInt(x);
        do Output.printString(",");
        do Output.printInt(y);
        do Output.printString(")");
        return;
    }
}
```

### Handling Variables




### 
