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

(LOOP)
	@KBD // Check keyboard input
	D=M
	@WHITE // If no key pressed, set white
	D;JEQ
	
	// Key is pressed, set black
	@color
	M=-1
	@FILL
	0;JMP
	
(WHITE)
	@color
	M=0
	
(FILL)
	@8192 // Screen has 8192 words (512*256/16)
	D=A
	@n
	M=D
	
	@SCREEN
	D=A
	@addr
	M=D  // addr = screen base address
	
	@i
	M=0  // i = 0
	
(FILLLOOP)
	@i
	D=M
	@n
	D=D-M
	@LOOP  // Done filling, go back to main loop
	D;JGE
	
	@color
	D=M
	@addr
	A=M
	M=D  // Set pixel
	
	@addr
	M=M+1  // Next screen address
	@i
	M=M+1  // i++
	
	@FILLLOOP
	0;JMP