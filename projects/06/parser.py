from code import Code

class Parser():
    def __init__(self, filename):

        self.parse(filename)

        # 
        self.address = 16
        # 
        self.line = 0
        # 
        self.MAX = len(self.text)
        # 
        self.command = ""

        self.comp = ""
        self.dest = ""
        self.jump = ""


    def parse(self, filename):
        """Parse the input file"""
        self.text = []
        with open(filename) as f:
            for line in f.readlines():
                chunks = line.split()
                # Skip empty lines
                if len(chunks) == 0:
                    continue
                # Skip comments
                elif chunks[0] == "//":
                    continue
                else:
                    # Delete whitespace
                    result = "".join(chunks)
                    # Delete comments
                    result = chunks.replace("//", " ")
                    result = chunks.split()[0]
                    
                self.text.append(result)"
    def hasMoreLines(self):
        """Are there more lines in the input?"""
        return self.i < self.MAX

    def advance(self):
        """Skips over white space and comments, if necessary.
        Reads the next instruction from the input, and makes it the current instruction.
        This routine should be called only if hasMoreLines is true.
        Initially there is no current instruction.
        """
        if self.hasMoreLines():
            self.command = self.text[self.i]
            self.i += 1
            if self.commandType() != "L":
                self.j += 1

    def instructionType(self):
        """Returns the type of the current instruction"
        A_INSTRUCTION for @xxx, where xxx is either a decimal number or a symbol.
        C_INSTRUCTION for dest=comp;jump.
        L_INSTRUCTION for (xxx), where xxx is a symbol.
        """
        pass

    def symbol(self):
        """If the current instruction is (xxx), returns the symbol xxx.
        If the current instruction is @xxx, returns the symbol or decimal xxx (as a string).
        Should be called only if instructionType is A_INSTRUCTION or L_INSTRUCTION.
        """
        pass

    def dest(self):
        """Returns the symbolic `dest` part of the current C-instruction (8 possibilities).
        Should be called only if instructionType is C_INSTRUCTION.
        """
        if self.commandType() == 'C':
            return Code.dest(self.dt)

    def comp(self):
        """Returns the symbolic `comp` part of the current C-instruction (28 possibilities).
        Should be called only if instructionType is C_INSTRUCTION.
        """
        pass

    def jump(self):
        """Returns the symbolic `jump` part of the current C-instruction (8 possibilities).
        Should be called only if instructionType is C_INSTRUCTION.
        """
        pass