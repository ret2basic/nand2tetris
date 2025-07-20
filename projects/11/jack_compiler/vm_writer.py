"""
VM Writer for Jack Compiler (Project 11)
Generates VM commands for the Jack language.
"""

class VMWriter:
    def __init__(self, output_file):
        """Creates a new VM writer that writes to the specified output file."""
        self.file = open(output_file, 'w')
    
    def write_push(self, segment, index):
        """Writes a VM push command."""
        self.file.write(f"push {segment} {index}\n")
    
    def write_pop(self, segment, index):
        """Writes a VM pop command."""
        self.file.write(f"pop {segment} {index}\n")
    
    def write_arithmetic(self, command):
        """Writes a VM arithmetic/logical command.
        Commands: add, sub, neg, eq, gt, lt, and, or, not
        """
        self.file.write(f"{command}\n")
    
    def write_label(self, label):
        """Writes a VM label command."""
        self.file.write(f"label {label}\n")
    
    def write_goto(self, label):
        """Writes a VM goto command."""
        self.file.write(f"goto {label}\n")
    
    def write_if(self, label):
        """Writes a VM if-goto command."""
        self.file.write(f"if-goto {label}\n")
    
    def write_call(self, name, n_args):
        """Writes a VM call command."""
        self.file.write(f"call {name} {n_args}\n")
    
    def write_function(self, name, n_locals):
        """Writes a VM function command."""
        self.file.write(f"function {name} {n_locals}\n")
    
    def write_return(self):
        """Writes a VM return command."""
        self.file.write("return\n")
    
    def close(self):
        """Closes the output file."""
        self.file.close()
    
    def write_comment(self, comment):
        """Writes a comment to the VM file (for debugging)."""
        self.file.write(f"// {comment}\n")