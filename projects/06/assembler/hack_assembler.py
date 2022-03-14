from code import Code
from symbol_table import SymbolTable
from parser import Parser
import sys

DEBUG = 0

class HackAssembler():
    def __init__(self):
        # Initialization
        self.code = Code()
        self.symbol_table = SymbolTable()
        self.parser = Parser(DEBUG)
        # The binary code that will be written to Prog.hack
        self.binary_strings = []

    def main(self):
        """Drives the entire translation process."""
        # First pass: builds a symbol table, adds all the label symbols to the table, and generates no code.
        self.first_pass()
        # Second pass: handles the variable symbols and generates binary code, using the symbol table.
        self.second_pass()
        # Write the binary code to Prog.hack
        self.write_to_file()

    def first_pass(self):
        """The assembler goes through the entire assembly program,line by line,
        keeping track of the line number.
        This number starts at 0 and is incremented by 1
        whenever an A-instruction or a C-instruction is encountered,
        but does not change when a comment or a label declaration is encountered.
        Each time a label declaration (xxx) is encountered,
        the assembler adds a new entry to the symbol table,
        associating the symbol xxx with the current line number plus 1.
        """
        while self.parser.has_more_lines():
            self.parser.advance()
            # Add all the label symbols to the symbol table
            if self.parser.instruction_type() == "L":
                symbol = self.parser.line[1:-1]
                address = self.parser.j
                self.symbol_table.add_entry(symbol, address)

    def second_pass(self):
        """The assembler goes again through the entire program and parses each line
        as follows. Each time an A-instruction with a symbolic reference is encountered, namely,
        @xxx, where xxx is a symbol and not a number, the assembler looks up xxx in the symbol
        table. If the symbol is found, the assembler replaces it with its numeric value and completes
        the instruction's translation. If the symbol is not found, then it must represent a new variable.
        To handle it, the assembler (i) adds the entry <xxx,value> to the symbol table, where `value`
        is the next available address in the RAM space designated for variables, and (ii) completes
        the instruction's translation, using this address.
        """

        # Reset parse.i and parse.j
        self.parser.i, self.parser.j = 0, 0

        while self.parser.has_more_lines():
            self.parser.advance()
            binary_string = ""
            # A-instruction
            if self.parser.instruction_type() == "A":
                num = self.parser.symbol(self.symbol_table)
                binary = bin(num)[2:]
                binary_string = binary.rjust(16, "0")
                self.binary_strings.append(binary_string)
            # C-instruction
            elif self.parser.instruction_type() == "C":
                if DEBUG:
                    print(f"{self.parser.line = }")
                dest_in_binary = self.parser.dest(self.code)
                comp_in_binary = self.parser.comp(self.code)
                jump_in_binary = self.parser.jump(self.code)
                
                binary_string = "111" + comp_in_binary + dest_in_binary + jump_in_binary
                self.binary_strings.append(binary_string)

    def write_to_file(self):
        """Write the binary code to a file."""
        if DEBUG:
            print(f"{self.binary_strings = }")

        with open(sys.argv[1].split(".")[0] + ".hack", "w") as f:
            for binary_string in self.binary_strings:
                f.writelines(binary_string + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
            print('Usage: python3 hack_assembler.py Prog.asm')
            sys.exit(1)

    hack_assembler = HackAssembler()
    hack_assembler.main()