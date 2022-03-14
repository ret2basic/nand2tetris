import sys

class CodeWriter():
    def __init__(self):
        # The relative pathname
        self.filename = sys.argv[1].split("/")[-1]
        # Output file handler, will be closed by the close() method.
        self.output_fhand = open(self.filename + ".asm", "w")

    def write_arithmetic(self):
        pass

    def write_push_pop(self):
        pass

    def close(self):
        """Closes the ouput file / stream."""
        self.file.close()