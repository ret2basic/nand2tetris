import sys
import os
from collections import deque
from parser import Parser
from code_writer import CodeWriter

class VMTranslator():
    def __init__(self):
        self.DEBUG = 1

        # The assembly code will be written to Prog.asm
        self.assembly_codes = []

    def vm_translate(self, parser, code_writer):

        while parser.has_more_lines():
            parser.advance()
            command = parser.command[0]
            if self.DEBUG:
                print(f"{command = }")
            # Handle arithmetic commands
            if parser.command_type() == "C_ARITHMETIC":
                code_writer.write_arithmetic(command)
            # Handle push/Pop commands
            elif parser.command_type() == "C_PUSH" or parser.command_type() == "C_POP":
                segment = parser.arg1()
                index = parser.arg2()
                code_writer.write_push_pop(command, segment, index)
            # Handle label commands
            elif parser.command_type() == "C_LABEL":
                label = parser.arg1()
                code_writer.write_label(command, label)
            # Handle goto commands
            elif parser.command_type() == "C_GOTO":
                label = parser.arg1()
                code_writer.write_goto(command, label)
            # Handle if commands
            elif parser.command_type() == "C_IF":
                label = parser.arg1()
                code_writer.write_if(command, label)
            # Handle function commands
            elif parser.command_type() == "C_FUNCTION":
                function_name = parser.arg1()
                n_vars = int(parser.arg2())
                code_writer.write_function(function_name, n_vars)
            # Handle call commands
            elif parser.command_type() == "C_CALL":
                function_name = parser.arg1()
                n_args = int(parser.arg2())
                code_writer.write_call(function_name, n_args)
            else:
                code_writer.write_return()

    def vm_translate_for_file(self, is_directory):
        """Handle the case when a file is given as input."""
        parser = Parser(sys.argv[1], self.DEBUG)
        code_writer = CodeWriter(sys.argv[1].split(".vm")[0] + ".asm", is_directory)
        self.vm_translate(parser, code_writer)
        code_writer.close()

    def vm_translate_for_directory(self, is_directory):
        """Handle the case when a directory is given as input."""

        # Initialize a queue and parse the files inside the directory
        files = deque()
        directory = os.listdir(sys.argv[1])
        print(directory)

        for file in directory:
            filename_tokens = file.split(".")
            # If the extension is ".vm", add this file to the queue
            if filename_tokens[-1] == "vm":
                files.append(filename_tokens[0])

        # If "Sys" is in the queue, move it to the front of the queue
        if "Sys" in files:
            files.remove("Sys")
            files.appendleft("Sys")

        filename_tokens = sys.argv[1].split("/")
        print(f"{filename_tokens = }")
        if filename_tokens[-1]:
            code_writer = CodeWriter(sys.argv[1] + filename_tokens[-1] + ".asm", is_directory)
        else:
            code_writer = CodeWriter(sys.argv[1] + filename_tokens[-2] + ".asm", is_directory)

        for filename in files:
            print(f"{filename = }")
            parser = Parser(sys.argv[1] + "/" + filename + ".vm", self.DEBUG)
            self.vm_translate(parser, code_writer)

        code_writer.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 VMTranslator.py <vm_file/directory>')
        sys.exit(1)

    is_directory = False
    if ".vm" not in sys.argv[1]:
        is_directory = True
    
    vm_translator = VMTranslator()

    # name = Name[0]
    # file = './' + '/'.join(data + [name])
    # print(f"{file = }")

    if is_directory:
        vm_translator.vm_translate_for_directory(is_directory)
    else:
        vm_translator.vm_translate_for_file(is_directory)
