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
            
        code_writer.close()

    def vm_translate_for_file(self):
        """Handle the case when a file is given as input."""
        parser = Parser(sys.argv[1], self.DEBUG)
        code_writer = CodeWriter(sys.argv[1].split(".vm")[0])
        self.vm_translate(parser, code_writer)

    def vm_translate_for_directory(self):
        """Handle the case when a directory is given as input."""

        code_writer = CodeWriter(sys.argv[1])
        code_writer.write_init()

        # Initialize a queue and parse the files inside the directory
        files = deque()
        directory = os.listdir(sys.argv[1])

        for file in directory:
            filename_tokens = file.split(".")
            # If the extension is ".vm", add this file to the queue
            if filename_tokens[-1] == "vm":
                files.append(sys.argv[1] + "/" + file)

        # If "Sys" is in the queue, move it to the front of the queue
        if "Sys" in files:
            files.remove("Sys")
            files.appendleft("Sys")

        for filename in files:
            parser = Parser(filename, self.DEBUG)
            self.vm_translate(parser, code_writer)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 VMTranslator.py Prog.vm')
        sys.exit(1)

    is_directory = True
    if len(sys.argv[1].split(".")) == 2:
        is_directory = False
    
    data = sys.argv[1].split("/")
    Name = data[-1].split(".")
    name = Name[0]
    filename = './' + '/'.join(data + [name])
    
    vm_translator = VMTranslator()

    if is_directory:
        vm_translator.vm_translate_for_directory()
    else:
        vm_translator.vm_translate_for_file()
