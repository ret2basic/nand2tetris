// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Pseducode:
//
//
//
//
//
//
//
//
//
//

@i // select variable "i"
M=1 // i = 1
@8192 // A = 8192
D=A // D = 8192
@n // select variable "n"
M=D	// n = 8192
@color // select variable "color"
M=0 // color = 0

(LOOP1)
	@SCREEN
	D=A
	@addr
	M=D			// addr = 16384
	@i
	M=1			//i=1
	@color
	M=0

	@KBD
	D=M 		//获取键盘
	@BLACKEN		//如果键盘有输入，则将颜色变为黑色
	D;JGT		
	
	(LOOP2)		//循环填充屏幕
		@i
		D=M
		@n
		D=D-M	
		@LOOP1	//i>n goto LOOP1
		D;JGT
		
		@color
		D=M		//获得颜色
		
		@addr
		A=M
		M=D 	//RAM[addr]=D
		
		@i
		M=M+1
		@addr
		M=M+1
		@LOOP2
		0;JMP
	
(BLACKEN)
	@color
	M=-1
	@LOOP2
	0;JMP