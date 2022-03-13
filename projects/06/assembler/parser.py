import sys
from code import Code
from symbol_table import SymbolTable

DEBUG = 1

class Parser():
    def __init__(self, DEBUG):
        # DEBUG mode
        self.DEBUG = DEBUG
        # Current line of code
        self.line = ""
        # Lines of assembly code stored in a list
        self.lines = []
        # Number of lines of assembly code
        self.total_lines = 0

        # The symbol `i` starts at address 16
        self.base_address = 16
        self.i = 0
        self.j = 0

        # The `comp`, `dest`, and `jump` components in a C-instruction
        self._comp = ""
        self._dest = ""
        self._jump = ""

        self.parse(sys.argv[1])

    def parse(self, asm_file):
        """Opens the assembly code and stores the content in a list."""
        with open(asm_file, "r") as f:
            for line in f.readlines():
                tokens = line.split()
                # Skip white space
                if len(tokens) == 0:
                    pass
                # Skip comments
                elif tokens[0] == "//":
                    pass
                else:
                    # Tokens => string
                    parsed = "".join(tokens)
                    # Delete in-line comments
                    parsed = parsed.split("//")[0]
                    # Add this parsed line of code to self.lines
                    self.lines.append(parsed)

            self.total_lines = len(self.lines)
            
            if self.DEBUG:        
                print(f"{self.lines = }")

    def has_more_lines(self):
        """Are there more lines in the input?"""
        return self.i < self.total_lines

    def advance(self):
        """Skips over white space and comments, if necessary.
        Reads the next instruction from the input, and makes it the current instruction.
        This routine should be called only if has_more_lines() is true.
        Initially there is no current instruction.
        """
        if self.has_more_lines():
            self.line = self.lines[self.i]
            self.i += 1
            if self.instruction_type() != "L":
                self.j += 1

    def instruction_type(self):
        """Returns the type of the current instruction"
        A_INSTRUCTION for @xxx, where xxx is either a decimal number or a symbol.
        C_INSTRUCTION for dest=comp;jump.
        L_INSTRUCTION for (xxx), where xxx is a symbol.
        """
        # A-instruction: @xxx
        if self.line.startswith("@"):
            return "A"
        # L-instruction: (xxx)
        elif self.line.startswith("(") and self.line.endswith(")"):
            return "L"
        # C-instruction: dest=comp;jump
        else:
            # find() returns -1 if the argument is not found
            index_1 = self.line.find("=")
            index_2 = self.line.find(";")
            # Both "=" and ";" exists in the line: dest=comp;jump
            if index_1 != -1 and index_2 != -1:
                self._comp = self.line[index_1+1: index_2]
                self._dest = self.line[:index_1]
                self._jump = self.line[index_2+1:]
            # Only ";" exists in the line: comp;jump
            elif index_1 == -1:
                self._comp = self.line[:index_2]
                self._dest = ""
                self._jump = self.line[index_2+1:]
            # Only "=" exists in the line: dest=comp
            elif index_2 == -1:
                self._comp = self.line[index_1+1:]
                self._dest = self.line[:index_1]
                self._jump = ""
                
            return "C"

    def symbol(self, symbol_table):
        """If the current instruction is (xxx), returns the symbol xxx.
        If the current instruction is @xxx, returns the symbol or decimal xxx (as a string).
        Should be called only if instruction_type is A_INSTRUCTION or L_INSTRUCTION.
        """
        # A-instruction
        if self.instruction_type() == "A":
            symbol = self.line[1:]

            if symbol.isdigit():
                return int(symbol)
            else:
                if not symbol_table.contains(symbol):
                    symbol_table.add_entry(symbol, self.base_address)
                    self.base_address += 1

                return symbol_table.get_address(symbol)

        # L-instruction
        elif self.instruction_type() == "L":
            symbol = self.line[1: -1]

            if not symbol_table.contains(symbol):
                symbol_table.add_entry(symbol, self.j)
                
            return symbol_table.get_address(symbol)

    def dest(self, code):
        """Returns the symbolic `dest` part of the current C-instruction (8 possibilities).
        Should be called only if instruction_type is C_INSTRUCTION.
        """
        if self.instruction_type() == "C":
            return code.dest(self._dest)

    def comp(self, code):
        """Returns the symbolic `comp` part of the current C-instruction (28 possibilities).
        Should be called only if instruction_type is C_INSTRUCTION.
        """
        if self.instruction_type() == "C":
            return code.comp(self._comp)

    def jump(self, code):
        """Returns the symbolic `jump` part of the current C-instruction (8 possibilities).
        Should be called only if instruction_type is C_INSTRUCTION.
        """
        if self.instruction_type() == "C":
            return code.jump(self._jump)