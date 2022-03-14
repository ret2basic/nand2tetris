import sys
from parser import Parser
from code_writer import CodeWriter

DEBUG = 1

class VMTranslator():
    def __init__(self):
        # Initialization
        parser = Parser()
        code_writer = CodeWriter()

        # The assembly code will be written to Prog.asm
        self.assembly_codes = []

    def main(self):
        # Pathname
        absolute_pathname = sys.argv[1].split("/")
        relative_pathname = absolute_pathname[1]
        relative_pathname_without_extension = relative_pathname.split(".")[0]

        name1 = "./" + "/".join(absolute_pathname)
        name2 = "./" + "/".join(absolute_pathname[:-1] + [relative_pathname_without_extension])

        self.vm_translate()
        self.write_to_file()

    def vm_translate(self):
        while self.parser.has_more_commands():
            self.parser.advance()
            command = self.parser.command[0]
            # Arithmetic commands
            if self.parser.command_type() == "C_ARITHMETIC":
                self.code_writer.write_arithmetic(command)
            # Push/Pop commands
            elif self.parser.command_type() == "C_PUSH" or self.parser.command_type() == "C_POP":
                segment = self.parser.arg1()
                index = self.parser.arg2()
                self.code_writer.write_push_pop(command, segment, index)
            
        self.code_writer.close()

        def write_to_file(self):
            """Write the assembly code to a file."""
            if DEBUG:
                print(f"{self.assembly_codes = }")

            with open(sys.argv[1].split(".")[0] + ".asm", "w") as f:
                for assembly_code in self.assembly_codes:
                    f.writelines(assembly_code + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 vm_translator.py Prog.vm')
        sys.exit(1)
    
    vm_translator = VMTranslator()
    vm_translator.main()
