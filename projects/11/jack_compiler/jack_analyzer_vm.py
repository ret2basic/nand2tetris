"""
Jack Analyzer for VM Code Generation (Project 11)
Coordinates the compilation of Jack files to VM code.
"""

from compilation_engine_vm import CompilationEngine
import sys
import os

class JackAnalyzer:
    def __init__(self):
        """Creates a new Jack analyzer."""
        pass

    def analyze_file(self, input_file):
        """Analyzes a single Jack file and generates VM code."""
        # Create output file name
        if input_file.endswith('.jack'):
            output_file = input_file[:-5] + '.vm'
        else:
            output_file = input_file + '.vm'
        
        # Create compilation engine and compile
        compiler = CompilationEngine(input_file, output_file)
        compiler.tokenizer.advance()  # Prime the tokenizer
        compiler.compile_class()
        
        print(f"Compiled {input_file} -> {output_file}")

    def analyze(self, path):
        """Analyzes Jack file(s) and generates VM code."""
        if os.path.isfile(path):
            # Single file
            if path.endswith('.jack'):
                self.analyze_file(path)
            else:
                print(f"Error: {path} is not a .jack file")
                sys.exit(1)
        elif os.path.isdir(path):
            # Directory - find all .jack files
            jack_files = []
            for file in os.listdir(path):
                if file.endswith('.jack'):
                    jack_files.append(os.path.join(path, file))
            
            if not jack_files:
                print(f"Error: No .jack files found in {path}")
                sys.exit(1)
            
            for jack_file in jack_files:
                self.analyze_file(jack_file)
        else:
            print(f"Error: {path} is not a valid file or directory")
            sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 jack_analyzer_vm.py <jack_file_or_directory>')
        sys.exit(1)
    
    analyzer = JackAnalyzer()
    analyzer.analyze(sys.argv[1])
    print("Compilation completed successfully!")

if __name__ == '__main__':
    main()