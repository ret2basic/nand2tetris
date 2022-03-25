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
@SET1
D;JEQ
@NEXT1
0;JMP
(SET1)
@SP
A=M-1
M=-1
(NEXT1)

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
@SET2
D;JEQ
@NEXT2
0;JMP
(SET2)
@SP
A=M-1
M=-1
(NEXT2)

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
@SET3
D;JLT
@NEXT3
0;JMP
(SET3)
@SP
A=M-1
M=-1
(NEXT3)

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
@SET4
D;JLT
@NEXT4
0;JMP
(SET4)
@SP
A=M-1
M=-1
(NEXT4)

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
@SET5
D;JLT
@NEXT5
0;JMP
(SET5)
@SP
A=M-1
M=-1
(NEXT5)

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
@SET6
D;JGT
@NEXT6
0;JMP
(SET6)
@SP
A=M-1
M=-1
(NEXT6)

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
@SET7
D;JGT
@NEXT7
0;JMP
(SET7)
@SP
A=M-1
M=-1
(NEXT7)

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
@SET8
D;JGT
@NEXT8
0;JMP
(SET8)
@SP
A=M-1
M=-1
(NEXT8)

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
M=M+D

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

