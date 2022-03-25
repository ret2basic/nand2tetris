import sys

class CodeWriter():
    def __init__(self, filename):
        """Opens an output file/stream and
        gets ready to write into it.
        """
        self.filename = filename
        self.file = open(self.filename + ".asm", "w")
        self.count = 0

        self.tags = ["LCL", "ARG", "THIS", "THAT"]

        self.function_name = ""
        self.return_counter = 0

    def set_file_name(self, filename):
        self.filename = filename.split(".vm")[0]

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
            self.write_add()
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
            "M=M-1\n",
            "D=M\n",
            "@SP\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "D=M-D\n",
            "@SP\n",
            "A=M-1\n",
            "M=0\n",
            "@SET" + str(self.count) + "\n",
            "D;JEQ\n",
            "@NEXT" + str(self.count) + "\n",
            "0;JMP\n",
            "(SET" + str(self.count) + ")\n",
            "@SP\n",
            "A=M-1\n",
            "M=-1\n",
            "(NEXT" + str(self.count) + ")\n",
        ])

    def write_gt(self):
        self.file.writelines([
            "@SP\n",
            "M=M-1\n",
            "D=M\n",
            "@SP\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "D=M-D\n",
            "@SP\n",
            "A=M-1\n",
            "M=0\n",
            "@SET" + str(self.count) + "\n",
            "D;JGT\n",
            "@NEXT" + str(self.count) + "\n",
            "0;JMP\n",
            "(SET" + str(self.count) + ")\n",
            "@SP\n",
            "A=M-1\n",
            "M=-1\n",
            "(NEXT" + str(self.count) + ")\n",
        ])

    def write_lt(self):
        self.file.writelines([
            "@SP\n",
            "M=M-1\n",
            "D=M\n",
            "@SP\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "D=M-D\n",
            "@SP\n",
            "A=M-1\n",
            "M=0\n",
            "@SET" + str(self.count) + "\n",
            "D;JLT\n",
            "@NEXT" + str(self.count) + "\n",
            "0;JMP\n",
            "(SET" + str(self.count) + ")\n",
            "@SP\n",
            "A=M-1\n",
            "M=-1\n",
            "(NEXT" + str(self.count) + ")\n",
        ])

    def write_push(self, command, segment, index):
        if segment == "constant":
            self.file.write("@" + str(index) + "\n")
            self.file.write("D=A\n")
        elif segment == "local" or segment == "argument" or segment == "this" or segment == "that":
            self.file.write("@" + str(index) + "\n")
            self.file.write("D=A\n")
            if segment == "local":
                self.file.write("@LCL\n")
            elif segment == "argument":
                self.file.write("@ARG\n")
            elif segment == "this":
                self.file.write("@THIS\n")
            else:
                self.file.write("@THAT\n")
            self.file.write("A=D+M\n")
            self.file.write("D=M\n")
        elif segment == "temp":
            self.file.write("@" + str(5 + index) + "\n")
            self.file.write("D=M\n")
        elif segment == "pointer":
            if index == 0:
                self.file.write("@THIS\n")
            else:
                self.file.write("@THAT\n")
            self.file.write("D=M\n")
        elif segment == "static":
            self.file.write("@" + self.filename + str(index) + "\n")
            self.file.write("D=M\n")

        self.file.write("@SP\n")
        self.file.write("A=M\n")
        self.file.write("M=D\n")
        self.file.write("@SP\n")
        self.file.write("M=M+1\n")

    def write_pop(self, command, segment, index):
        self.file.write("@SP\n")
        self.file.write("M=M-1\n")
        self.file.write("A=M\n")
        self.file.write("D=M\n")
        
        if segment == "local" or segment == "argument" or segment == "this" or segment == "that":
            self.file.write("@R13\n")
            self.file.write("M=D\n")
            self.file.write("@" + str(index) + "\n")
            self.file.write("D=A\n")
            if segment == "local":
                self.file.write("@LCL\n")
            elif segment == "argument":
                self.file.write("@ARG\n")
            elif segment == "this":
                self.file.write("@THIS\n")
            else:
                self.file.write("@THAT\n")

            self.file.write("D=D+M\n")
            self.file.write("@R14\n")
            self.file.write("M=D\n")
            self.file.write("@R13\n")
            self.file.write("D=M\n")
            self.file.write("@R14\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
        elif segment == "temp":
            self.file.write("@" + str(5 + index) + "\n")
            self.file.write("M=D\n")
        elif segment == "pointer":
            if index == 0:
                self.file.write("@THIS\n")
            elif index == 1:
                self.file.write("@THAT\n")
            self.file.write("M=D\n")
        elif segment == "static":
            self.file.write("@" + self.filename + str(index) + "\n")
            self.file.write("M=D\n")
    
    def write_init(self):
        """Bootstrap code.
        Pseudocode:

        SP = 256
        call Sys.init
        """

        self.file.writelines([
            # Leave a comment
            "// Init\n",
            # SP = 256
            "@256\n",
            "D=A\n",
            "@SP\n",
            "M=D\n",
            # End the current block
            "\n",
        ])

        # call Sys.init
        self.function_name = "Sys.init"
        self.write_call("Sys.init", 0)
    
    def write_label(self, command, label):
        """Writes assembly code that effects the `label` command."""

        self.file.writelines([
            # Leave a comment
            "// " + command + " " + label + "\n",
            # (function_name$label)
            "(" + self.function_name + "$" + label + ")\n",
            # End the current block
            "\n",
        ])

    def write_goto(self, command, label):
        """Writes assembly code that effects the `goto` command."""

        self.file.writelines([
            # Leave a comment
            "// " + command + " " + label + "\n",
            # (function_name$label)
            "(" + self.function_name + "$" + label + ")\n",
            # Unconditional jump
            "0;JMP\n",
            # End the current block
            "\n",
        ])

    def write_if(self, command, label):
        """Writes assembly code that effects the `if` command."""

        self.file.writelines([
            # Leave a comment
            "// " + command + " " + label + "\n",
            "@SP\n",
            "M=M-1\n",
            "A=M\n",
            "D=M\n",
            "@0\n",
            "D=D-A\n",
            # @function_name$label
            "@" + self.function_name + "$" + label + "\n",
            # If A != D, jump to that label
            "D;JNE\n",
            # End the current block
            "\n",
        ])

    def write_function(self, function_name, n_vars):
        """Writes assembly code that effects the `function` command.
        Pseudocode:

        (f) // injects a function entry label into the code
            repeat n_vars times: // n_vars = number of local variables
            push 0 // initializes the local variables to 0
        """

        self.function_name = function_name

        self.file.writelines([
            # Leave a comment
            "//" + function_name + " " + str(n_vars) + "\n",
            # (f)
            "(" + function_name + ")\n",
        ])

        # repeat n_vars times: push 0
        for i in range(n_vars):
            self.file.writelines([
                # RAM[SP] = 0
                "@SP\n",
                "A=M\n",
                "M=0\n",
                # SP += 1
                "@SP\n",
                "M=M+1\n",
            ])

        # End the current block
        self.file.write("\n")

    def write_call(self, function_name, n_args):
        """Writes assembly code that effects the `call` command.
        Pseudocode:

        push return_address // generates a label and pushes it to the stack
        push LCL // saves LCL of the caller
        push ARG // saves ARG of the caller
        push THIS // saves THIS of the caller
        push THAT // saves THAT of the caller
        ARG = SP - 5 - n_args // repositions ARG
        LCL = SP // repositions LCL
        goto f // transfers control to the callee
        (return_address) // injects the return address label into the code
        """

        return_address_label = "return_address_" + str(self.return_counter)
        self.return_counter += 1

        self.file.writelines([
            # Leave a comment
            "//" + function_name + " " + str(n_args) + "\n",
            # push return_address
            "@" + return_address_label + "\n",
            "D=A\n",
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ])

        # push LCL
        # push ARG
        # push THIS
        # push THAT
        for tag in self.tags:
            self.file.writelines([
                "@" + tag + "\n",
                "D=M\n",
                "@SP\n",
                "A=M\n",
                "M=D\n",
                "@SP\n",
                "M=M+1\n",
            ])
            
        self.file.writelines([
            # ARG = SP - 5 - n_args
            "@SP\n",
            "D=M\n",
            "@" + str(n_args) + "\n",
            "D=D-A\n",
            "@5\n",
            "D=D-A\n",
            "@ARG\n",
            "M=D\n",
            # LCL = SP
            "@SP\n",
            "D=M\n",
            "@LCL\n",
            "M=D\n",
            # goto f
            "@" + function_name + "\n",
            "0;JMP\n",
            # (return_address)
            "(" + return_address_label + ")\n"
            # End the current block
            "\n",
        ])
        
    def write_return(self):
        """Writes assembly code that effects the `call` command.
        Pseudocode:

        frame = LCL // frame is a temporary variable
        return_address = *(frame - 5) // puts the return address in a temporary variable
        *ARG = pop() // repositions the return value for the caller
        SP = ARG + 1 // repositions SP for the caller
        THAT = *(frame - 1) // restores THAT for the caller
        THIS = *(frame - 2) // restores THIS for the caller
        ARG = *(frame - 3) // restores ARG for the caller
        LCL = *(frame - 4) // restores LCL for the caller
        goto return_address // go to the return address
        """

        self.file.writelines([
            # Leave a comment
            "// return\n",
            # frame = LCL
            "@LCL\n",
            "D=M\n",
            "@frame\n",
            "M=D\n",
            # return_address = *(frame – 5)
            "@5\n",
            "A=D-A\n",
            "D=M\n",
            "@RET\n",
            "M=D\n",
            # *ARG = pop()
            "@SP\n",
            "A=M-1\n",
            "D=M\n",
            "@ARG\n",
            "A=M\n",
            "M=D\n",
            # SP = ARG + 1
            "@ARG\n",
            "D=M\n",
            "@SP\n",
            "M=D+1\n",
        ])

        # THAT = *(frame - 1)
        # THIS = *(frame - 2)
        # ARG = *(frame - 3)
        # LCL = *(frame - 4)
        for i, tag in enumerate(self.tags):
            self.file.writelines([
                "@" + str(i + 1) + "\n",
                "D=A\n",
                "@frame\n",
                "A=M-D\n",
                "D=M\n",
                "@" + tag + "\n",
                "M=D\n",
            ])

        self.file.writelines([
            # goto return_address
            "@RET\n",
            "A=M\n",
            "0;JMP\n",
            # End the current block
            "\n",
        ])
