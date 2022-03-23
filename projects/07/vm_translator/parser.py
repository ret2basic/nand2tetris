import sys

class Parser():
    def __init__(self, DEBUG):
        # DEBUG mode
        self.DEBUG = DEBUG
        # Current command
        self.command = ""
        # Lines of assembly code stored in a list
        self.text = []
        # Number of lines of assembly code
        self.total_lines = 0
        # Current line number
        self.i = 0

        self.parse(sys.argv[1])

    def parse(self, asm_file):
        """Opens the assembly code and stores the content in a list."""
        with open(asm_file, "r") as f:
            for line in f.readlines():
                # Skip white space
                if line == "\n":
                    pass
                # Skip comments
                elif line.startswith("//"):
                    pass
                else:
                    # A line of code => tokens
                    tokens = line.split()
                    self.text.append(tokens)

            self.total_lines = len(self.text)
            
            if self.DEBUG:        
                print(f"{self.text = }")

    def has_more_lines(self):
        """Are there more lines in the input?"""
        return self.i < self.total_lines

    def advance(self):
        """Reads the next command from the input and makes it the current command.
        This routine should be called only if has_more_lines() is true.
        Initially there is no current command.
        """
        if self.has_more_lines():
            self.command = self.text[self.i]
            self.i += 1

    def command_type(self):
        """Returns a constant representing the type of the current command.
        If the current command is an arithmetic-logical command, returns C_ARITHMETIC.
        """
        arithmetic_commands = ["add", "sub", "neg"]
        logical_commands = ['eq', 'gt', 'lt', 'and', 'or', 'not']
        other_commands = {
            "push" : "C_PUSH", "pop" : "C_POP", "label" : "C_LABEL",
            "goto" : "C_GOTO", "if-goto" : "C_IF",
            "function" : "C_FUNCTION", "call" : "C_RETURN",
        }

        if self.command[0] in arithmetic_commands + logical_commands:
            return "C_ARITHMETIC"
        elif self.command[0] in other_commands:
            return other_commands[self.command[0]]
        else:
            return "C_CALL"

    def arg1(self):
        """Returns the first argument of the current command.
        In the case of C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
        Should not be called if the current command is C_RETURN.
        """
        if self.command_type() == "C_RETURN":
            return None
        elif self.command_type() == "C_ARITHMETIC":
            return self.command[0]
        else:
            return self.command[1]
    
    def arg2(self):
        """Returns the second argument of the current command.
        Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
        """
        function_commands = ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]
        if self.command_type() in function_commands:
            return int(self.command[-1])
        else:
            return None