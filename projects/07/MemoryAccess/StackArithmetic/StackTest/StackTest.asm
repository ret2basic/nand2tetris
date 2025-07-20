// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET0
D;JEQ
@NEXT0
0;JMP
(SET0)
@SP
A=M-1
M=-1
(NEXT0)

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET2
D;JEQ
@NEXT2
0;JMP
(SET2)
@SP
A=M-1
M=-1
(NEXT2)

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET4
D;JEQ
@NEXT4
0;JMP
(SET4)
@SP
A=M-1
M=-1
(NEXT4)

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET6
D;JLT
@NEXT6
0;JMP
(SET6)
@SP
A=M-1
M=-1
(NEXT6)

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET8
D;JLT
@NEXT8
0;JMP
(SET8)
@SP
A=M-1
M=-1
(NEXT8)

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET10
D;JLT
@NEXT10
0;JMP
(SET10)
@SP
A=M-1
M=-1
(NEXT10)

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET12
D;JGT
@NEXT12
0;JMP
(SET12)
@SP
A=M-1
M=-1
(NEXT12)

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET14
D;JGT
@NEXT14
0;JMP
(SET14)
@SP
A=M-1
M=-1
(NEXT14)

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@SET16
D;JGT
@NEXT16
0;JMP
(SET16)
@SP
A=M-1
M=-1
(NEXT16)

// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53
@53
D=A
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

// push constant 112
@112
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

// neg
@SP
A=M-1
M=-M

// and
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M&D

// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M|D

// not
@SP
A=M-1
M=!M

