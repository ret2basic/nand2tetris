from code import Code
from symbol_table import SymbolTable
from parser import Parser
import sys

class HackAssembler():

    def __init__(self):
        pass

    def main(self, name, result):
        """"""
        # Parse command line argument
        if len(sys.argv) != 2:
            print("Usage: python3 hack_assembler.py Prog.asm")
            sys.exit(1)  
        filename = sys.argv[1]

        # Main logic
        self.initialization(filename)
        self.first_pass()
        self.second_pass()

        # Store the result in a file
        with open(name + ".hack", "w+") as f:
            for i in result:
                f.writelines(i + "\n")

    def initialization(self, filename):
        """The assembler creates a symbol table and initializes it with
        all the pre-defined symbols and their pre-allocated values.
        """
        code = Code()
        symboltable = SymbolTable()
        parser = Parser(filename)

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
        pass

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
        pass

if __name__ == "__main__":
    hack_assembler = HackAssembler()
    hack_assembler.main()