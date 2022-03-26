// Init
@256
D=A
@SP
M=D

//Sys.init 0
@return_address_0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(return_address_0)

//Sys.init 0
(Sys.init)

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

//Class1.set 2
@return_address_1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(return_address_1)

// pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D

// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

//Class2.set 2
@return_address_2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(return_address_2)

// pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D

//Class1.get 0
@return_address_3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(return_address_3)

//Class2.get 0
@return_address_4
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(return_address_4)

// label WHILE
(Sys.init$WHILE)

// goto WHILE
@Sys.init$WHILE
0;JMP

//Class2.set 0
(Class2.set)

// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 0
@SP
M=M-1
A=M
D=M
@StaticsTest.asm0
M=D

// push argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 1
@SP
M=M-1
A=M
D=M
@StaticsTest.asm1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// return
@LCL
D=M
@frame
M=D
@5
A=D-A
D=M
@RET
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@frame
A=M-D
D=M
@LCL
M=D
@2
D=A
@frame
A=M-D
D=M
@ARG
M=D
@3
D=A
@frame
A=M-D
D=M
@THIS
M=D
@4
D=A
@frame
A=M-D
D=M
@THAT
M=D
@RET
A=M
0;JMP

//Class2.get 0
(Class2.get)

// push static 0
@StaticsTest.asm0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@StaticsTest.asm1
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M-D

// return
@LCL
D=M
@frame
M=D
@5
A=D-A
D=M
@RET
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@frame
A=M-D
D=M
@LCL
M=D
@2
D=A
@frame
A=M-D
D=M
@ARG
M=D
@3
D=A
@frame
A=M-D
D=M
@THIS
M=D
@4
D=A
@frame
A=M-D
D=M
@THAT
M=D
@RET
A=M
0;JMP

//Class1.set 0
(Class1.set)

// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 0
@SP
M=M-1
A=M
D=M
@StaticsTest.asm0
M=D

// push argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 1
@SP
M=M-1
A=M
D=M
@StaticsTest.asm1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// return
@LCL
D=M
@frame
M=D
@5
A=D-A
D=M
@RET
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@frame
A=M-D
D=M
@LCL
M=D
@2
D=A
@frame
A=M-D
D=M
@ARG
M=D
@3
D=A
@frame
A=M-D
D=M
@THIS
M=D
@4
D=A
@frame
A=M-D
D=M
@THAT
M=D
@RET
A=M
0;JMP

//Class1.get 0
(Class1.get)

// push static 0
@StaticsTest.asm0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@StaticsTest.asm1
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M-D

// return
@LCL
D=M
@frame
M=D
@5
A=D-A
D=M
@RET
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@frame
A=M-D
D=M
@LCL
M=D
@2
D=A
@frame
A=M-D
D=M
@ARG
M=D
@3
D=A
@frame
A=M-D
D=M
@THIS
M=D
@4
D=A
@frame
A=M-D
D=M
@THAT
M=D
@RET
A=M
0;JMP

