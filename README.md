# nand2tetris

![nand2tetris](https://github.com/ret2basic/nand2tetris/blob/main/nand2tetris.png?raw=true)

**"nand2tetris" (From Nand to Tetris)** is a collection of projects that let student **build a computer from scratch**. It is a hands-on journey that starts with the most elementary logic gate, called **Nand**. and ends up, 12 projects later, with a **general-purpose computer system capable of running Tetris**. Specifically, the 12 projects are:

1. [Boolean Logic](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/01)
2. [Boolean Arithmetic](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/02)
3. [Memory](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/03)
4. [Machine Language](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/04)
5. [Computer Architecture](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/05)
6. [Assembler](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/06)
7. [Virtual Machine I: Processing](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/07)
8. [Virtual Machine II: Control](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/08)
9. [High-Level Language](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/09)
10. [Compiler I: Syntax Analysis](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/10)
11. [Compiler II: Code Generation](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/11)
12. [Opearting System](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/12)

# Part I: Hardware

Part I covers project 1 to 6. In this part, we are going to implement the hardware architecture for our Hack computer. In particular, we are going to build:

1. **Logical gates:** project 1
2. **ALU and memory devices:** project 2 and 3
3. **Hack machine language:** project 4
4. **CPU and RAM:** project 5
5. **Hack assembler:** project 6

# Chapter 1: Boolean Logic

## Course

We know that And gate, Or gate, and Not gate are the most fundamental logical gates of computer hardware. In fact, these three gates can be reduced to Nand gate, and we claim that **Nand gate is THE most fundamental logical gate**. We prove this claim informally:

- According to De Morgan's law, `x Or y = Not((Not a) And (Not y))`, so Or gate is reduced to Not gate and And gate.
- `Not(x) = Nand(x, x)`, so Not gate is reduced to Nand gate.
- `And(x, y) = Not(Nand(x, y))`, so And gate is reduced to Nand gate.

Based on these three observations, And gate, Or gate, and Not gate can be reduced to Nand gate. In nand2tetris, we are given a ready-to-go Nand chip (it is actually the only thing we have) and we are going to build a modern computer on top of it.

## Project

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

# Chapter 2: Boolean Arithmetic

## Course

Inside computers, **everything** is represented using binary codes. In this chapter, we are going to play with **binary addition** and **sign convertion**.

A pair of binary numbers can be added bitwise from right to left. For each pair of bits, binary addition produces two outputs: `sum` and `carry`. Note that the last carry bit is the overflow bit. For example, consider 1001 + 1001 = (1)0010 with word size 4. The very first step is adding the LSBs of both operands, that is, `1 + 1`. Here we get `sum = 0` and `carry = 1`. The very last step is adding the MSBs of both operands, that is, `1 + 1`. Again, here we get `sum = 0` and `carry = 1`, but this carry bit exceeds the word size hence is thrown away, so the final result is 0010 instead of 10010. This phenomenon is called **overflow**.

In order to represent negative numbers, we use **2's complement**. Suppose the word size is `n` and `x` is a negative number, then the 2's complement representation of `x` is `2**n - x`. This design is better than the naive "sign bit" design since there is no "positive 0" and "negative 0" issue. To compute the negative of a number, we convert this number to its binary representation, flip all bits, and then add 1 to it. For example, we are given number 4 and we want to compute -4 in 2's complement. The binary representation of 4 is 0100, flip all bits and we get 1011, then add 1 to it we get 1100. That is, -4 = 1100 in 2's complement.

## Project

In Project 2, we are going to implement:

- **HalfAdder:**
- **FullAdder:**
- **Add16:** Addition 16-bit version
- **Inc16:** Increment 16-bit version
- **ALU:** Arithmetic Logical Unit

# Chapter 3: Memory

## Course

### Combinational vs. Sequential

The chips that we built in Project 1 and Project 2 are **time-independent** (or **combinational**). In this chapter, we introduce the concept of **time** and move on to **time-dependent** (or **sequential**) logic.

### Clock Cycle

Time is a profound notion. In computer science, we have no way to model **continuous** time as what we are experience in real life. Instead, we divide time into small chunks so that it becomes **discrete**. Each chunk is called a **clock cycle**, and it is the smallest time interval that a computer can measure. The choice of clock cycle is not random. It must follow these two principles:

1. The clock cycle shouldn't be too small, because small clock cycle is not able to handle time delay properly and errors may occur. 
2. The clock cycle shouldn't be too large, because large clock cycle slows down the computer.

In order to balance out these two conditions, **we let clock cycle to be slightly larger than the maximal time delay in any chip in the system**.

### Data Flip-Flop (DFF)

With the notion of (discrete) time, we are ready to implement computer memory. Memory chips are designed to "remember", or store, information over time. The low-level devices that facilitate this storage abstraction are named **flip-flop gates**, of which there are several variants. In Nand to Tetris we use a variant named **data flip-flop**, or **DFF**. Like the Nand chip, DFF is given to us so we are not going to implement it. We are going to implement the following types of computer memory:

- Registers
- RAM
- Counter

Note that the "counter" mentioned here is the **Program Counter**.

## Project

In Project 3, we are going to implement:

- **Bit:**
- **Register:**
- **RAM8:** RAM 8-bit version
- **RAM64:** RAM 64-bit version
- **RAM512:** RAM 512-bit version
- **RAM4K:** RAM 4K-bit version
- **RAM16K:** RAM 16K-bit version
- **PC:** Program Counter

# Chapter 4: Machine Language

## Course

### A-instruction (@xxx)

The A-instruction sets the `A` register to some 15-bit value:

- Symbolic: `@xxx,  where `xxx` is a decimal value ranging from 0 to 32767, or a symbol bound to such a decimal value.
- Binary: `0vvvvvvvvvvvvvvv`, where `0` stands for A-instruction and `vvvvvvvvvvvvvvv` is the 15-bit value of `xxx`.

### C-instruction (dest = comp;jump)

The C-instruction answers three questions: what to compute (an ALU operation, denoted `comp`), where to store the computed value (`dest`), and what to do next (`jump`):

- Symbolic: `dest=comp;jump`,  where `comp` is mandatory. If `dest` is empty, the `=` is omitted; if `jump` is empty, the `;` is omitted.
- Binary: `111accccccdddjjj`, where `111` stands for C-instruction, `acccccc` refers to `comp`, `ddd` refers to `dest`, and `jjj` refers to `jump`. 

### Symbols

The symbols fall into three functional categories:

1. **Predefined Symbols:** representing special memory addresses.
2. **Label Symbols:** representing destinations of goto instructions.
3. **Variable Symbols:** representing variables.

In particular, predefined symbols include:

- **R0, R1, ... , R15:** These symbols are bound to the values 0 to 15.
- **SP, LCL, ARG, THIS, THAT:** These symbols are bound to the values 0, 1, 2, 3, and 4, respectively.
- **SCREEN, KBD:** SCREEN and KBD are bound, respectively, to the values 16384 and 24576 (in hexidecimal: 4000 and 6000), which are the agreed-upon base addresses of the screen memory map and the keyboard memory map.

## Project

In Project 4, we are going to implement:

- **Mult:**
- **Fill:**

# Chapter 5: Computer Architecture

## Course

The **von Neumann machine** is a practical model that informs the construction of almost all computer platforms today. At the heart of this architecture lies the **stored program** concept: the computer's memory stores not only the data that the computer manipulates but also the instructions that tell the computer what to do. A von Neumann machine contains the following components:

- **Memory (RAM)**
  - *Data memory:* stores data and allows reading/writing.
  - *Instruction memory:* stores the instructions of an executable.
- **Central Processing Unit (CPU)**
  - *Arithmetic Logic Unit (ALU):* handles fundamental computations such as addition and bitwise operations.
  - *Registers:* high-speed and expensive memory that prevents starvation.
    - data registers
    - address registers
    - program counter
    - instruction register
  - *Control Unit:* a binary decoder that decodes instructions into micro-codes.
- **Input and Output (I/O)**
  - *Memory-maped I/O:* create a binary emulation of the I/O device, making it appear to the CPU as if it were a regular linear memory segment.

## Project

In Project 5, we are going to implement:

- **Memory:**
- **CPU:**
- **Computer:**

# Chapter 6: Assembler

## Course

Suppose we are dealing with the assembly code `load R3, 7`.The **assembler** parses each assembly instruction into its underlying fields, for example, `load`, `R3`, and, `7`, translates each field into its equivalent binary code, and finally **assembles** the generated bits into binary instruction that can be executed by the hardware. Pictorially:

```
           Assembler
Assembly -------------> Binary
```

In this chapter we will build an assembler in **Python**.

## Project

In Project 6, we are going to implement:

- `parser.py`: parsing the input into instructions and instructions into fields.
- `code.py`: translating the fields (symbolic mnemonics) into binary codes.
- `hack_assembler.py`: drives the entire translation process.
- `symbol_table.py`: resolving symbols (labels in assembly language) into actual addresses.

# Part II: Software

Part II covers project 7 to 12. In this part, we are going to implement **Jack**, a *simple*, *Java-like*, *object-based* programming language. As with programming languages like Java and C#, the Jack compiler will be *two-tiered*:

1. The **Hack compiler** will generate interim **bytecode**, designed to run on an abstraction **virtual machine (VM)**.
2. The bytecode will then be compiled further by a separate **VM translator** into the **Hack machine language**.

Pictorially:

```
             Compiler            VM            Assembler
Source Code ---------> Bytecode ----> Assembly --------> Binary
```

The languaeg that we are going to implement, Jack, has the following syntax:

```
// First example in Programming 101
class Main {
  function void main() {
    do Output.printString("Hello World");
    return;
  }
}
```

In Part II, we are going to build:

1. **VM translator:** project 7-8
2. **BreakOut game written in Jack:** project 9
3. **Jack compiler:** project 10-11
4. **Operating system:** project 12

# Chapter 7: Virtual Machine I: Processing

## Course

**Virtual Machine (VM)** is the intermediate layer between high-level source code and low-level machine language. For example, JVM. VM gives *cross-platform* compatibility: since the virtual machine may be realized with relative ease on many hardware platforms, the same VM code can run as is on any device equipped with such a VM implementation. The downside of this VM two-tier translation process is *reduced efficiency*.

Our VM model is *stack-based*: all the VM operations take their operands from, and store their results on, the stack. There is only one data type: a signed 16-bit integer. A VM program is a sequence of VM commands that fall into five categories:

- Comments and White Space
  - Lines beginning with `//` are considered comments and are ignored.
  - Blank lines are permitted and are ignored.
- Push/Pop Commands
  - `push segment index`: pushes the value of `segment[index]` onto the stack
  - `pop segment index`: pops the top stack value and stores it in `segment[index]`
- Arithmetic-Logical Commands
  - Arithmetic commands: `add`, `sub`, `neg`
  - Comparison commands: `eq`, `gt`, `lt`
  - Logical commands: `and`, `or`, `not`
- Branching Commands
- Function Commands

In this chapter we focus on the arithmetic-logical and push/pop commands.

## Project

In Project 7, we are going to implement:

- `parser.py`
- `code_writer.py`
- `vm_translator.py`

# Chapter 8: Virtual Machine II: Control

## Course



## Project

In Project 8, we are going to implement:



# Chapter 9: High-Level Language

## Course



## Project

In Project 9, we are going to implement:



# Chapter 10: Compiler I: Syntax Analysis

## Overview

The previous chapter introduced Jack: a simple, object-based programming language with a Java-like syntax. In this chapter we start building a compiler for the Jack language.

> A **compiler** is a program that translates programs from a source language into a target machine.

The translation process, known as **compilation**, is conceptually based on two distinct tasks:

1. We have to understand the syntax of the source program => **syntax analysis**
2. From it, uncover the program's semantics => **code generation**

For example, the parsing of the code can reveal that the program seeks to declare an array or manipulate an object. Once we know the semantics, we can reexpress it using the syntax of the target language. The first task, typically called syntax analysis, is described in this chapter; the second task, code generation, is taken up in the next chapter.

## Background

Compilation consists of two main stages

1. **Syntax Analysis**
   1. Tokenizing: the grouping of input characters into language atoms called tokens
   2. Parsing: the grouping of tokens into structured statements that have a meaning
2. **Code Generation**

The tokenizing and parsing tasks are completely independent of the target language into which we seek to translate the source input. Since in this chapter we don't deal with code generation, we have chosen to **have the syntax analyzer output the parsed structure of the input program as an XML file**. This decision has two benefits:

1. The ouput file can be readily inspected, demonstrating that the syntax analyzer is parsing source programs correctly.
2. The requirement to output this file explicitly forces us to write the syntax analyzer in an architecture that can be later morphed into a full-scale compiler.

### Lexical Analysis

Each programming language specification includes the types of **tokens**, or words, that the language recognizes. In the Jack language, tokens fall into 5 categories:

1. Keywords: like `class` and `while`
2. Symbols: like `+` and `<`
3. Integer constants: like `17` and `314`
4. String constants: like `"FAQ"` and `"Frequently Asked Questions"`
5. Identifiers: the textual labels used for naming variables, classes, and subroutines

Taken together, the tokens defined by these lexical categories can be referred to as the language **lexicon**.

In its plaintext form, a computer program is a stream of characters stored in a text file. The first step in analyzing the program's syntax is grouping the characters into tokens, as defined by the language lexicon, while ignoring white space and comments. This task is called:

- **Lexical Analysis**
- **Scanning**
- **Tokenizing**

All meaning exactly the same thing.

Definition of the Jack lexicon:

- `keyword`
  - 'class'
  - 'constructor'
  - 'function'
  - 'method'
  - 'field'
  - 'static'
  - 'var'
  - 'int'
  - 'char'
  - 'boolean'
  - 'void'
  - 'true'
  - 'false'
  - 'null'
  - 'this'
  - 'let'
  - 'do'
  - 'if'
  - 'else'
  - 'while'
  - 'return'
- `symbol`:
  - '{'
  - '}'
  - '('
  - ')'
  - '['
  - ']'
  - '.'
  - ','
  - ';'
  - '+'
  - '-'
  - '*'
  - '/'
  - '&'
  - '|'
  - '<'
  - '>'
  - '='
  - '~'
- `integerConstant`: a decimal integer in the range 0...32767
- `stringConstant`: '"'a sequence of characters
- `identifier`: a sequence of letters, digits, and underscore (`_`), not starting with a digit.

### Grammars

Once we develop the ability to access a given text as a stream of tokens, or words, we can proceed to attempt grouping the words into valid sentences. A grammar is written in a **meta-language**: a language describing a language. Trying to keep things simple, in nand2tetris we view a grammar as a set of rules. **Each rule consists of a left side and a right side.**

The **left side** specifies the rule's name, which is not part of the language. Rather, it is made up by the person who describes the grammar, and thus it is not terribly important. For example, if we replace a rule's name with another name throughout the grammar, the grammar will be just as valid.

the rule's **right side** describes the lingual pattern that the rule specifies. This pattern is a left-to-right sequence consisting of three building blocks:

- Terminals: tokens, like `if`
- Nonterminals: names of other rules, like `expression`
- Qualifiers: `|`, `*`, `?`, `(`, `)`

For example, the rule `ifStatement: 'if' '(' expression ')' '{' statements '}'` stipulates that every valid instance of an `ifStatement` must:

- Begin with the token `if`
- Followed by the token `(`
- Followed by a valid instance of an `expression` (defined elsewhere in the grammar)
- Followed by the token `)`
- Followed by the token `{`
- Followed by a valid instance of `statements` (defined elsewhere in the grammar)
- Followed by the token `}`.

When there is more than one way to parse a pattern, we use the qualifier `|` to list the alternatives. The qualifier `*` is used to denote "0, 1, or more times". In a similar vein, the qualifier `?` is used to denote "0 or 1 times".

A subset of Jack grammar:

- `statements: statement*`
- `statement: letStatement | ifStatement | whileStatement`
- `letStatement: 'let' varName '=' expression ';'`
- `ifStatement: `if` '(' expression ')' '{' statements '}'`
- `whileStatement: 'while' '(' expression ')' '{' statements '}'`
- `expression: term(op term)?`
- `term: varName | constant`
- `varName: a string not beginning with a digit`
- `constant: a non-negative integer`
- `op: '+' | '-' | '=' | '>' | '<'`

### Parsing



### Parser



## Specification

This section consists of two parts. First, we specify the Jack language's grammar. Next, we specify a syntax analyzer designed to parse programs according to this grammar.

### The Jack Language Grammar



### A Syntax Analyzer for the Jack Language




## Project

In Project 10, we are going to implement the syntax analysis part of the Jack compiler. Specifically, we implement the following modules:

- `jack_tokenizer`: tokenizer
- `compilation_engine`: recursive top-down parser
- `jack_analyzer`: main program that sets up and invokes the other modules

Go to `projects/10` to learn more about the project:

https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/10

# Chapter 11: Compiler II: Code Generation

## Course



## Project

In Project 11, we are going to implement:



# Chapter 12: Operating System

## Course



## Project

In Project 12, we are going to implement:

