import sys

class CodeWriter():
    def __init__(self):
        """Opens an output file/stream and
        gets ready to write into it.
        """
        self.filename = sys.argv[1].split("/")[-1]
        self.file = open("".join(sys.argv[1].split(".vm")[0]) + ".asm", "w")
        self.count = 0

    def write_arithmetic(self, command):
        """Writes to the output file the assembly
        code that implements the given
        arithmetic-logical `command`
        """

        # Leave a comment
        self.file.write("// " + command + "\n")

        if command == "add":
            self.write_add()
        elif command == "sub":
            self.write_sub()
        elif command == "and":
            self.write_and()
        elif command == "or":
            self.write_or()
        elif command == "neg":
            self.write_neg()
        elif command == "not":
            self.write_not()
        elif command == "eq":
            self.write_eq()
            self.count += 1
        elif command == "gt":
            self.write_gt()
            self.count += 1
        elif command == "lt":
            self.write_lt()
            self.count += 1
        
        # End the current block
        self.file.write("\n")

    def write_push_pop(self, command, segment, index):
        """Writes to the output file the assembly
        code that implements the given push
        or pop `command
        """

        # Leave a comment
        self.file.write("// " + " ".join([command, segment, str(index)]) + "\n")
        
        if command == "push":
            self.write_push(command, segment, index)
        elif command == "pop":
            self.write_pop(command, segment, index)
        
        # End the current block
        self.file.write("\n")

    def close(self):
        """Closes the ouput file/stream."""
        self.file.close()

    def write_add(self):
        self.file.writelines([
            "@SP\n",
            "M=M-1\n",
            "@SP\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "M=M+D\n",
        ])

    def write_sub(self):
        self.file.writelines([
            "@SP\n",
            "M=M-1\n",
            "@SP\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "M=M-D\n",
        ])

    def write_and(self):
        self.file.writelines([
            "@SP\n",
            "M=M-1\n",
            "@SP\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "M=M&D\n",
        ])

    def write_or(self):
        self.file.writelines([
            "@SP\n",
            "M=M-1\n",
            "@SP\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "M=M|D\n",
        ])

    def write_neg(self):
        self.file.writelines([
            "@SP\n",
            "A=M-1\n",
            "M=-M\n"
        ])

    def write_not(self):
        self.file.writelines([
            "@SP\n",
            "A=M-1\n",
            "M=!M\n"
        ])

    def write_eq(self):
        self.file.writelines([
            "@SP\n",
            "AM=M-1\n",  # SP--, A=SP
            "D=M\n",     # D = stack[SP] (second operand)
            "A=A-1\n",   # A = SP-1
            "D=M-D\n",   # D = stack[SP-1] - stack[SP] (first - second)
            "M=0\n",     # Default to false
            "@SET" + str(self.count) + "\n",
            "D;JEQ\n",   # If D==0, jump to set true
            "@NEXT" + str(self.count) + "\n",
            "0;JMP\n",
            "(SET" + str(self.count) + ")\n",
            "@SP\n",
            "A=M-1\n",
            "M=-1\n",    # Set true
            "(NEXT" + str(self.count) + ")\n",
        ])
        self.count += 1

    def write_gt(self):
        self.file.writelines([
            "@SP\n",
            "AM=M-1\n",  # SP--, A=SP
            "D=M\n",     # D = stack[SP] (second operand)
            "A=A-1\n",   # A = SP-1
            "D=M-D\n",   # D = stack[SP-1] - stack[SP] (first - second)
            "M=0\n",     # Default to false
            "@SET" + str(self.count) + "\n",
            "D;JGT\n",   # If D>0, jump to set true
            "@NEXT" + str(self.count) + "\n",
            "0;JMP\n",
            "(SET" + str(self.count) + ")\n",
            "@SP\n",
            "A=M-1\n",
            "M=-1\n",    # Set true
            "(NEXT" + str(self.count) + ")\n",
        ])
        self.count += 1

    def write_lt(self):
        self.file.writelines([
            "@SP\n",
            "AM=M-1\n",  # SP--, A=SP
            "D=M\n",     # D = stack[SP] (second operand)
            "A=A-1\n",   # A = SP-1
            "D=M-D\n",   # D = stack[SP-1] - stack[SP] (first - second)
            "M=0\n",     # Default to false
            "@SET" + str(self.count) + "\n",
            "D;JLT\n",   # If D<0, jump to set true
            "@NEXT" + str(self.count) + "\n",
            "0;JMP\n",
            "(SET" + str(self.count) + ")\n",
            "@SP\n",
            "A=M-1\n",
            "M=-1\n",    # Set true
            "(NEXT" + str(self.count) + ")\n",
        ])
        self.count += 1

    def write_push(self, command, segment, index):

        if segment == "constant":
            self.file.writelines([
                "@" + str(index) + "\n",
                "D=A\n",
            ])
        
        elif segment == "local" or segment == "argument" or segment == "this" or segment == "that":
            self.file.writelines([
                "@" + str(index) + "\n",
                "D=A\n",
            ])

            if segment == "local":
                self.file.write("@LCL\n")
            elif segment == "argument":
                self.file.write("@ARG\n")
            elif segment == "this":
                self.file.write("@THIS\n")
            else:
                self.file.write("@THAT\n")
            
            self.file.writelines([
                "A=D+M\n",
                "D=M\n",
            ])

        elif segment == "temp":
            self.file.writelines([
                "@" + str(5 + index) + "\n",
                "D=M\n",
            ])
        
        elif segment == "pointer":
            if index == 0:
                self.file.write("@THIS\n")
            else:
                self.file.write("@THAT\n")
            self.file.write("D=M\n")

        elif segment == "static":
            self.file.writelines([
                "@" + self.filename + str(index) + "\n",
                "D=M\n",
            ])

        self.file.writelines([
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ])

    def write_pop(self, command, segment, index):

        self.file.writelines([
            "@SP\n",
            "M=M-1\n",
            "A=M\n",
            "D=M\n",
        ])

        if segment == "local" or segment == "argument" or segment == "this" or segment == "that":
            self.file.writelines([
                "@R13\n",
                "M=D\n",
                "@" + str(index) + "\n",
                "D=A\n",
            ])

            if segment == "local":
                self.file.write("@LCL\n")
            elif segment == "argument":
                self.file.write("@ARG\n")
            elif segment == "this":
                self.file.write("@THIS\n")
            else:
                self.file.write("@THAT\n")
            
            self.file.writelines([
                "D=D+M\n",
                "@R14\n",
                "M=D\n",
                "@R13\n",
                "D=M\n",
                "@R14\n",
                "A=M\n",
                "M=D\n",
            ])

        elif segment == "temp":
            self.file.writelines([
                "@" + str(5 + index) + "\n",
                "M=D\n",
            ])

        elif segment == "pointer":
            if index == 0:
                self.file.write("@THIS\n")
            elif index == 1:
                self.file.write("@THAT\n")
            self.file.write("M=D\n")

        elif segment == "static":
            self.file.writelines([
                "@" + self.filename + str(index) + "\n",
                "M=D\n",
            ])