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

// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

//Main.fibonacci 1
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
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(return_address_1)

// label WHILE
(Sys.init$WHILE)

// goto WHILE
(Sys.init$WHILE)
0;JMP

//Main.fibonacci 0
(Main.fibonacci)

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

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
D=M
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@SP
A=M-1
M=0
@SET0
D;JLT
@NEXT0
0;JMP
(SET0)
@SP
A=M-1
M=-1
(NEXT0)

// if-goto IF_TRUE
@SP
M=M-1
A=M
D=M
@0
D=D-A
@Main.fibonacci$IF_TRUE
D;JNE

// goto IF_FALSE
(Main.fibonacci$IF_FALSE)
0;JMP

// label IF_TRUE
(Main.fibonacci$IF_TRUE)

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

// label IF_FALSE
(Main.fibonacci$IF_FALSE)

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

// push constant 2
@2
D=A
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

//Main.fibonacci 1
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
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(return_address_2)

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

// push constant 1
@1
D=A
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

//Main.fibonacci 1
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
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(return_address_3)

// add
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M+D

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

