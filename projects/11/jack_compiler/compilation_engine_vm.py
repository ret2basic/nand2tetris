"""
Compilation Engine for Jack Compiler (Project 11)
Generates VM code instead of XML output.
"""

from jack_tokenizer import JackTokenizer
from symbol_table import SymbolTable
from vm_writer import VMWriter

class CompilationEngine:
    def __init__(self, input_file, output_file):
        """Creates a new compilation engine with the given input and output."""
        self.tokenizer = JackTokenizer(input_file)
        self.vm_writer = VMWriter(output_file)
        self.symbol_table = SymbolTable()
        
        # Class-level information
        self.class_name = ""
        self.subroutine_type = ""  # constructor, function, method
        self.subroutine_name = ""
        
        # Label counters for control structures
        self.label_counter = 0
        
    def get_next_label(self, prefix="LABEL"):
        """Generates a unique label."""
        label = f"{prefix}_{self.label_counter}"
        self.label_counter += 1
        return label
    
    def compile_class(self):
        """Compiles a complete class."""
        # class
        self.tokenizer.advance()
        
        # className
        self.class_name = self.tokenizer.identifier()
        self.tokenizer.advance()
        
        # {
        self.tokenizer.advance()
        
        # classVarDec*
        while self.tokenizer.token in ['static', 'field']:
            self.compile_class_var_dec()
        
        # subroutineDec*
        while self.tokenizer.token in ['constructor', 'function', 'method']:
            self.compile_subroutine()
        
        # }
        self.tokenizer.advance()
        
        self.vm_writer.close()
    
    def compile_class_var_dec(self):
        """Compiles a static or field declaration."""
        # static|field
        kind = self.tokenizer.key_word().upper()
        self.tokenizer.advance()
        
        # type
        var_type = self.get_type()
        
        # varName (, varName)*
        while True:
            var_name = self.tokenizer.identifier()
            self.symbol_table.define(var_name, var_type, kind)
            self.tokenizer.advance()
            
            if self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == ',':
                self.tokenizer.advance()  # skip comma
            else:
                break
        
        # ;
        self.tokenizer.advance()
    
    def compile_subroutine(self):
        """Compiles a complete method, function, or constructor."""
        # Start new subroutine scope
        self.symbol_table.start_subroutine()
        
        # constructor|function|method
        self.subroutine_type = self.tokenizer.key_word()
        self.tokenizer.advance()
        
        # void|type
        return_type = self.get_type()
        
        # subroutineName
        self.subroutine_name = self.tokenizer.identifier()
        self.tokenizer.advance()
        
        # If method, add 'this' as first argument
        if self.subroutine_type == 'method':
            self.symbol_table.define('this', self.class_name, 'ARG')
        
        # (
        self.tokenizer.advance()
        
        # parameterList
        self.compile_parameter_list()
        
        # )
        self.tokenizer.advance()
        
        # subroutineBody
        self.compile_subroutine_body()
    
    def compile_parameter_list(self):
        """Compiles a parameter list."""
        if self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == ')':
            return  # Empty parameter list
        
        while True:
            # type
            param_type = self.get_type()
            
            # varName
            param_name = self.tokenizer.identifier()
            self.symbol_table.define(param_name, param_type, 'ARG')
            self.tokenizer.advance()
            
            if self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == ',':
                self.tokenizer.advance()  # skip comma
            else:
                break
    
    def compile_subroutine_body(self):
        """Compiles a subroutine body."""
        # {
        self.tokenizer.advance()
        
        # varDec*
        while self.tokenizer.token == 'var':
            self.compile_var_dec()
        
        # Write function declaration
        n_locals = self.symbol_table.var_count('VAR')
        function_name = f"{self.class_name}.{self.subroutine_name}"
        self.vm_writer.write_function(function_name, n_locals)
        
        # Handle constructor/method setup
        if self.subroutine_type == 'constructor':
            # Allocate memory for object
            n_fields = self.symbol_table.var_count('FIELD')
            self.vm_writer.write_push('constant', n_fields)
            self.vm_writer.write_call('Memory.alloc', 1)
            self.vm_writer.write_pop('pointer', 0)  # Set THIS
        elif self.subroutine_type == 'method':
            # Set THIS to first argument
            self.vm_writer.write_push('argument', 0)
            self.vm_writer.write_pop('pointer', 0)
        
        # statements
        self.compile_statements()
        
        # }
        self.tokenizer.advance()
    
    def compile_var_dec(self):
        """Compiles a var declaration."""
        # var
        self.tokenizer.advance()
        
        # type
        var_type = self.get_type()
        
        # varName (, varName)*
        while True:
            var_name = self.tokenizer.identifier()
            self.symbol_table.define(var_name, var_type, 'VAR')
            self.tokenizer.advance()
            
            if self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == ',':
                self.tokenizer.advance()  # skip comma
            else:
                break
        
        # ;
        self.tokenizer.advance()
    
    def compile_statements(self):
        """Compiles a sequence of statements."""
        while self.tokenizer.token in ['let', 'if', 'while', 'do', 'return']:
            if self.tokenizer.token == 'let':
                self.compile_let()
            elif self.tokenizer.token == 'if':
                self.compile_if()
            elif self.tokenizer.token == 'while':
                self.compile_while()
            elif self.tokenizer.token == 'do':
                self.compile_do()
            elif self.tokenizer.token == 'return':
                self.compile_return()
    
    def compile_let(self):
        """Compiles a let statement."""
        # let
        self.tokenizer.advance()
        
        # varName
        var_name = self.tokenizer.identifier()
        self.tokenizer.advance()
        
        # Check for array access
        is_array = False
        if self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == '[':
            is_array = True
            # Push array base address
            self.push_variable(var_name)
            
            # [
            self.tokenizer.advance()
            
            # expression (index)
            self.compile_expression()
            
            # ]
            self.tokenizer.advance()
            
            # Calculate array[index] address
            self.vm_writer.write_arithmetic('add')
        
        # =
        self.tokenizer.advance()
        
        # expression
        self.compile_expression()
        
        # ;
        self.tokenizer.advance()
        
        # Store value
        if is_array:
            # Store in array element
            self.vm_writer.write_pop('temp', 0)  # Store value temporarily
            self.vm_writer.write_pop('pointer', 1)  # Set THAT to array[index]
            self.vm_writer.write_push('temp', 0)  # Push value back
            self.vm_writer.write_pop('that', 0)  # Store in array[index]
        else:
            # Store in variable
            self.pop_variable(var_name)
    
    def compile_if(self):
        """Compiles an if statement."""
        else_label = self.get_next_label("IF_ELSE")
        end_label = self.get_next_label("IF_END")
        
        # if
        self.tokenizer.advance()
        
        # (
        self.tokenizer.advance()
        
        # expression
        self.compile_expression()
        
        # )
        self.tokenizer.advance()
        
        # Jump to else if condition is false
        self.vm_writer.write_arithmetic('not')
        self.vm_writer.write_if(else_label)
        
        # {
        self.tokenizer.advance()
        
        # statements
        self.compile_statements()
        
        # }
        self.tokenizer.advance()
        
        # Jump to end (skip else)
        self.vm_writer.write_goto(end_label)
        
        # else label
        self.vm_writer.write_label(else_label)
        
        # Check for else clause
        if self.tokenizer.token == 'else':
            # else
            self.tokenizer.advance()
            
            # {
            self.tokenizer.advance()
            
            # statements
            self.compile_statements()
            
            # }
            self.tokenizer.advance()
        
        # end label
        self.vm_writer.write_label(end_label)
    
    def compile_while(self):
        """Compiles a while statement."""
        loop_label = self.get_next_label("WHILE_LOOP")
        end_label = self.get_next_label("WHILE_END")
        
        # Loop label
        self.vm_writer.write_label(loop_label)
        
        # while
        self.tokenizer.advance()
        
        # (
        self.tokenizer.advance()
        
        # expression
        self.compile_expression()
        
        # )
        self.tokenizer.advance()
        
        # Jump to end if condition is false
        self.vm_writer.write_arithmetic('not')
        self.vm_writer.write_if(end_label)
        
        # {
        self.tokenizer.advance()
        
        # statements
        self.compile_statements()
        
        # }
        self.tokenizer.advance()
        
        # Jump back to loop
        self.vm_writer.write_goto(loop_label)
        
        # End label
        self.vm_writer.write_label(end_label)
    
    def compile_do(self):
        """Compiles a do statement."""
        # do
        self.tokenizer.advance()
        
        # subroutineCall
        self.compile_subroutine_call()
        
        # ;
        self.tokenizer.advance()
        
        # Discard return value
        self.vm_writer.write_pop('temp', 0)
    
    def compile_return(self):
        """Compiles a return statement."""
        # return
        self.tokenizer.advance()
        
        # Check for return expression
        if not (self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == ';'):
            self.compile_expression()
        else:
            # Void function - push 0
            self.vm_writer.write_push('constant', 0)
        
        # ;
        self.tokenizer.advance()
        
        self.vm_writer.write_return()
    
    def compile_expression(self):
        """Compiles an expression."""
        # term
        self.compile_term()
        
        # (op term)*
        while self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
            op = self.tokenizer.symbol()
            self.tokenizer.advance()
            
            self.compile_term()
            
            # Generate VM command for operation
            if op == '+':
                self.vm_writer.write_arithmetic('add')
            elif op == '-':
                self.vm_writer.write_arithmetic('sub')
            elif op == '*':
                self.vm_writer.write_call('Math.multiply', 2)
            elif op == '/':
                self.vm_writer.write_call('Math.divide', 2)
            elif op == '&':
                self.vm_writer.write_arithmetic('and')
            elif op == '|':
                self.vm_writer.write_arithmetic('or')
            elif op == '<':
                self.vm_writer.write_arithmetic('lt')
            elif op == '>':
                self.vm_writer.write_arithmetic('gt')
            elif op == '=':
                self.vm_writer.write_arithmetic('eq')
    
    def compile_term(self):
        """Compiles a term."""
        if self.tokenizer.token_type() == 'INT_CONST':
            # integerConstant
            value = self.tokenizer.int_val()
            self.vm_writer.write_push('constant', value)
            self.tokenizer.advance()
            
        elif self.tokenizer.token_type() == 'STRING_CONST':
            # stringConstant
            string_val = self.tokenizer.string_val()
            # Create string
            self.vm_writer.write_push('constant', len(string_val))
            self.vm_writer.write_call('String.new', 1)
            for char in string_val:
                self.vm_writer.write_push('constant', ord(char))
                self.vm_writer.write_call('String.appendChar', 2)
            self.tokenizer.advance()
            
        elif self.tokenizer.token in ['true', 'false', 'null', 'this']:
            # keywordConstant
            keyword = self.tokenizer.key_word()
            if keyword == 'true':
                self.vm_writer.write_push('constant', 1)
                self.vm_writer.write_arithmetic('neg')
            elif keyword == 'false' or keyword == 'null':
                self.vm_writer.write_push('constant', 0)
            elif keyword == 'this':
                self.vm_writer.write_push('pointer', 0)
            self.tokenizer.advance()
            
        elif self.tokenizer.token_type() == 'IDENTIFIER':
            # Variable, array element, or subroutine call
            identifier = self.tokenizer.identifier()
            self.tokenizer.advance()
            
            if self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == '[':
                # Array access
                self.push_variable(identifier)
                
                # [
                self.tokenizer.advance()
                
                # expression
                self.compile_expression()
                
                # ]
                self.tokenizer.advance()
                
                # Get array element
                self.vm_writer.write_arithmetic('add')
                self.vm_writer.write_pop('pointer', 1)
                self.vm_writer.write_push('that', 0)
                
            elif self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() in ['(', '.']:
                # Subroutine call - handle inline
                self.compile_subroutine_call_with_name(identifier)
                
            else:
                # Variable
                self.push_variable(identifier)
                
        elif self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == '(':
            # (expression)
            self.tokenizer.advance()
            self.compile_expression()
            self.tokenizer.advance()
            
        elif self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() in ['-', '~']:
            # unaryOp term
            op = self.tokenizer.symbol()
            self.tokenizer.advance()
            self.compile_term()
            
            if op == '-':
                self.vm_writer.write_arithmetic('neg')
            elif op == '~':
                self.vm_writer.write_arithmetic('not')
    
    def compile_subroutine_call(self):
        """Compiles a subroutine call."""
        # subroutineName | className | varName
        name = self.tokenizer.identifier()
        self.tokenizer.advance()
        self.compile_subroutine_call_with_name(name)
    
    def compile_subroutine_call_with_name(self, name):
        """Compiles a subroutine call when the name is already known."""
        n_args = 0
        
        if self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == '.':
            # Method or function call
            self.tokenizer.advance()
            
            # Check if name is a variable (object method call)
            if self.symbol_table.exists(name):
                # Object method call
                self.push_variable(name)  # Push object reference
                class_name = self.symbol_table.type_of(name)
                n_args = 1
            else:
                # Static function call
                class_name = name
                n_args = 0
            
            # subroutineName
            method_name = self.tokenizer.identifier()
            self.tokenizer.advance()
            
            function_name = f"{class_name}.{method_name}"
        else:
            # Method call on current object
            self.vm_writer.write_push('pointer', 0)  # Push this
            function_name = f"{self.class_name}.{name}"
            n_args = 1
        
        # (
        self.tokenizer.advance()
        
        # expressionList
        n_args += self.compile_expression_list()
        
        # )
        self.tokenizer.advance()
        
        self.vm_writer.write_call(function_name, n_args)
    
    def compile_expression_list(self):
        """Compiles an expression list. Returns the number of expressions."""
        n_expressions = 0
        
        if not (self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == ')'):
            self.compile_expression()
            n_expressions = 1
            
            while self.tokenizer.token_type() == 'SYMBOL' and self.tokenizer.symbol() == ',':
                self.tokenizer.advance()
                self.compile_expression()
                n_expressions += 1
        
        return n_expressions
    
    def get_type(self):
        """Gets the current type (int, char, boolean, or className)."""
        if self.tokenizer.token_type() == 'KEYWORD':
            type_name = self.tokenizer.key_word()
        else:
            type_name = self.tokenizer.identifier()
        
        self.tokenizer.advance()
        return type_name
    
    def push_variable(self, var_name):
        """Pushes a variable onto the stack."""
        kind = self.symbol_table.kind_of(var_name)
        index = self.symbol_table.index_of(var_name)
        
        if kind == 'STATIC':
            self.vm_writer.write_push('static', index)
        elif kind == 'FIELD':
            self.vm_writer.write_push('this', index)
        elif kind == 'ARG':
            self.vm_writer.write_push('argument', index)
        elif kind == 'VAR':
            self.vm_writer.write_push('local', index)
    
    def pop_variable(self, var_name):
        """Pops the stack top into a variable."""
        kind = self.symbol_table.kind_of(var_name)
        index = self.symbol_table.index_of(var_name)
        
        if kind == 'STATIC':
            self.vm_writer.write_pop('static', index)
        elif kind == 'FIELD':
            self.vm_writer.write_pop('this', index)
        elif kind == 'ARG':
            self.vm_writer.write_pop('argument', index)
        elif kind == 'VAR':
            self.vm_writer.write_pop('local', index)