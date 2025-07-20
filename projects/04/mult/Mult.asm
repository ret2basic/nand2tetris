// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Pseudocode:
//
// i = 1;
// sum = 0;
//
// while (i < RAM[1])
// {
//     sum += RAM[0];
//     i++;
// }
// 
// RAM[2] = sum;
//
// return 0;

// i = 1;
@i // select variable "i"
M=1 // i = 1

// sum = 0;
@sum // select variable "sum"
M=0 // sum = 0


// while (i < RAM[1])
// {
//     sum += RAM[0];
//     i++;
// }
(LOOP)
	@i // select variable "i"
	D=M // D = i
	@R1 // A = 1
	D=D-M // D = D - RAM[1]
	@STOP // select label SsTOP
	D;JGE	// if D >= 0, jump to label STOP

	@sum // select variable "sum"
	D=M // D = sum
	@R0 // A = 0
	D=D+M  // D += RAM[0]
    @sum
    M=D

	@i // select variable "i"
	M=M+1 // i++

	@LOOP // select label LOOP
	0;JMP // jump to LOOP

// RAM[2] = sum;
(STOP)
    @sum // select variable "sum"
    D=M // D = sum
    @R2 // A = 2
    M=D // RAM[2] = D

// return 0;
(END)
    @END // select label END
    0;JMP // This is just a convention. 0 is a placeholder.