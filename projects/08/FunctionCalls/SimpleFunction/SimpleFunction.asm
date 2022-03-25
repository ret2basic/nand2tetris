//SimpleFunction.test 2
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1

// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M+D

// not
@SP
A=M-1
M=!M

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

// add
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M+D

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

