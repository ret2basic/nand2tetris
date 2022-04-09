from compilation_engine import CompilationEngine
import sys
import os

class JackAnalyzer:
    def __init__(self):
        self.filename = ''

    def analyze_one_file(self):
        """"""
        jack_compiler = CompilationEngine(self.filename, 2)
        jack_compiler.tokenizer.advance()
        jack_compiler.compile_class()
        jack_compiler.file.close()

    def analyze(self):
        """"""
        path = sys.argv[-1]
        data = path.split('/')
        file = data[-1]
        filename_components = file.split('.')

        # If the input is a single file
        if len(filename_components) == 2:
            self.filename = path
            self.analyze_one_file()
        # If the input is a directory
        else:
            files = os.listdir(path)
            for f in files:
                if f.split(".")[-1] == 'jack':
                    self.filename = path + '/' + f
                    self.analyze_one_file()
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 jack_analyzer <jack_file/directory>')
        sys.exit(1)
    
    jack_analyzer = JackAnalyzer()
    jack_analyzer.analyze()
