from jack_tokenizer import JackTokenizer

class CompilationEngine():
    def __init__(self, filename, flag=1):
        """Creates a new compilation engine with the given input and output.
        
        The next routine called (by the `JackAnalyzer` module) must be `compile_class`.
        """
        self.filename = filename
        self.tokenizer = JackTokenizer(filename)
        if flag == 1:
            self.output = self.filename + "X.xml"
        else:
            self.output = self.filename + ".xml"
        self.file = open(self.output, "w+")
        
    def compile_class(self):
        """Compiles a complete class."""

        # <class>
        s = "<class>\n"
        self.file.write(s)
        # class
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # className
        s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # {
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()

        # Determine whether the next item is `classVarDec` or not.
        while self.tokenizer.token in ['static', 'field']:
            # classVarDec*
            self.compile_class_var_dec()
        while self.tokenizer.token in ['constructor', 'function', 'method']:
            # subroutineDec
            self.compile_subroutine()
        # }
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # </class>
        s = "</class>\n"
        self.file.write(s)
        
    def compile_class_var_dec(self):
        """Compiles a static variable declaration, or a field declaration."""

        # <classVarDec>
        s = "<classVarDec>\n"
        self.file.write(s)
        # static,field
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # type
        self.compile_type()
        # varName
        s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
        self.file.write(s)
        # , varName
        self.tokenizer.advance()
        while self.tokenizer.token == ',':
            # ','
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # varName
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # ;
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # </classVarDec>
        s = "</classVarDec>\n"
        self.file.write(s)
    
    def compile_subroutine(self):
        """Compiles a complete method, function, or constructor."""

        # <subroutineDec>
        s = "<subroutineDec>\n"
        self.file.write(s)
        # constructor, function, method
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # void, int, char, boolean, className
        if self.tokenizer.token in ['int', 'char', 'boolean', 'void']:
            s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
            self.file.write(s)
        else:
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
        self.tokenizer.advance()
        # subroutineName
        s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # (
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # parameterlist
        self.compile_parameter_list()
        # )
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # subroutineBody
        self.compile_subroutine_body()
        # </subroutineDec>
        s = "</subroutineDec>\n"
        self.file.write(s)

    def compile_parameter_list(self):
        """Compiles a (possibly empty) parameter list.
        
        Does not handle the enclosing parentheses tokens `(` and `)`.
        """

        # <parameterList>
        s = "<parameterList>\n"
        self.file.write(s)
        # type
        if self.tokenizer.token in ['int', 'char', 'boolean'] or self.tokenizer.token_type == "IDENTIFIER":
            # type
            self.compile_type()
            # varName
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # ,
            while self.tokenizer.token == ",":
                s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
                self.file.write(s)
                self.tokenizer.advance()
                # type
                self.compile_type()
                # varName
                s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
                self.file.write(s)
                self.tokenizer.advance()
        
        # </parameterList>
        s = "</parameterList>\n"
        self.file.write(s)   

    def compile_subroutine_body(self):
        """Compiles a subroutine's body."""

        # <subroutineBody>
        s = "<subroutineBody>\n"
        self.file.write(s)
        # {
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # varDec
        while self.tokenizer.token == "var":
            self.compile_var_dec()
        # statements
        self.compile_statements()
        # }
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # </subroutineBody>
        s = "</subroutineBody>\n"
        self.file.write(s)
    
    def compile_type(self):
        """"""
        if self.tokenizer.token in ['int', 'char', 'boolean']:
            s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
            self.file.write(s)
            self.tokenizer.advance()
        else:
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
            self.tokenizer.advance()
    
    def compile_var_dec(self):
        """Compiles a `var` declaration."""

        # <varDec>
        s = "<varDec>\n"
        self.file.write(s)
        # var
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # type
        self.compile_type()
        # varName
        s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # ,
        while self.tokenizer.token == ",":
            # ,
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # varName
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # ;
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # </varDec>
        s = "</varDec>\n"
        self.file.write(s)
        
    def compile_statement(self):
        """Compiles one statement.
        
        Helper function for `self.compile_statements()`.
        """

        if self.tokenizer.token == "let":
            self.compile_let()
        elif self.tokenizer.token == "if":
            self.compile_if()
        elif self.tokenizer.token == "while":
            self.compile_while()
        elif self.tokenizer.token == "do":
            self.compile_do()
        elif self.tokenizer.token == "return":
            self.compile_return()
    
    def compile_statements(self):
        """Compiles a sequence of statements.
        
        Does not handle the enclosing curly bracket tokens `{` and `}`.
        """

        # <statements>
        s = "<statements>\n"
        self.file.write(s)
        while self.tokenizer.token in ["let", "if", "while", "do", "return"]:
            self.compile_statement()
        # </statements>
        s = "</statements>\n"
        self.file.write(s)

    def compile_let(self):
        """Compiles a `let` statement."""

        # <letStatement>
        s = "<letStatement>\n"
        self.file.write(s)
        # let
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # varName
        s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # [
        if self.tokenizer.token == "[":
            # [
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # expression
            self.compile_expression()
            # ]
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # =
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # expression
        self.compile_expression();
        # ;
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # </letStatement>
        s = "</letStatement>\n"
        self.file.write(s)

    def compile_if(self):
        """Compiles an `if` statement, possibly with a trailing `else` clause."""

        # <ifStatement>
        s = "<ifStatement>\n"
        self.file.write(s)
        # if
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # (
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # expression
        self.compile_expression()
        # )
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # {
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # statements
        self.compile_statements()
        # }
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # else
        if self.tokenizer.token == "else":
            # else
            s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # {
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # statements
            self.compile_statements()
            # }
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # </ifStatement>
        s = "</ifStatement>\n"
        self.file.write(s)
    
    def compile_while(self):
        """Compiles a `while` statement."""

        # <whileStatement>
        s = "<whileStatement>\n"
        self.file.write(s)
        #while
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        #(
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        #expression
        self.compile_expression()
        #)
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        #{
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        #statements
        self.compile_statements()
        #}
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        #</whileStatement>
        s = "</whileStatement>\n"
        self.file.write(s)

    def compile_do(self):
        """Compiles a `do` statement."""

        # <doStatement>
        s = "<doStatement>\n"
        self.file.write(s)
        # do
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # subroutine_call
        self.compile_subroutine_call()
        #;
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # </doStatement>
        s = "</doStatement>\n"
        self.file.write(s)
   
    def compile_return(self):
        """Compiles a `return` statement."""

        # <returnStatement>
        s = "<returnStatement>\n"
        self.file.write(s)
        # return
        s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
        self.file.write(s)
        self.tokenizer.advance()
        if self.tokenizer.token != ';':
            self.compile_expression()
        # ;
        s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
        self.file.write(s)
        self.tokenizer.advance()
        # </returnStatement>
        s = "</returnStatement>\n"
        self.file.write(s)

    def compile_expression(self):
        """Compiles an expression."""

        # <expression>
        s = "<expression>\n"
        self.file.write(s)
        self.compile_term()
        # Determine whether the current token is an operator or not.
        while self.tokenizer.token in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
            # op
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # term
            self.compile_term()
        # </expression>
        s = "</expression>\n"
        self.file.write(s)
    
    def compile_term(self):
        """Compiles a `term`.
        
        If the current token is an `identifier`, the routine must resolve it into
        a `variable`, an `array element`, or a `subroutine call`.
        A single lookahead token, which may be `[`, `(`, or `.`,
        suffices to distinguish between the possibilities.
        Any other token is not part of this term and should not be advanced over.
        """

        # <term>
        s = "<term>\n"
        self.file.write(s)
        # integerConstant
        if self.tokenizer.token_type() == "INT_CONST":
            s = "<integerConstant> " + str(self.tokenizer.int_val()) + " </integerConstant>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # stringConstant
        elif self.tokenizer.token_type() == "STRING_CONST":
            s = "<stringConstant> " + self.tokenizer.string_val() + " </stringConstant>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # keywordConstant
        elif self.tokenizer.token_type() == "KEYWORD" and self.tokenizer.token in ['true', 'false', 'null', 'this']:
            s = "<keyword> " + self.tokenizer.key_word() + " </keyword>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # varName[], varName, subroutineCall
        elif self.tokenizer.token_type() == "IDENTIFIER":
            # a[]
            if self.tokenizer.next_token() == "[":
                # varName
                s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
                self.file.write(s)
                self.tokenizer.advance()
                # [
                s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
                self.file.write(s)
                self.tokenizer.advance()
                # expression
                self.compile_expression()
                # ]
                s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
                self.file.write(s)
                self.tokenizer.advance()
            # subroutineCall
            elif self.tokenizer.next_token() in ["(", "."]:
                self.compile_subroutine_call()
            else:
                # varName
                s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
                self.file.write(s)
                self.tokenizer.advance()
        # (expression)
        elif self.tokenizer.token == "(":
            # (
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # expression
            self.compile_expression()
            # )
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
        # unaryOp term
        elif self.tokenizer.token in ['-', '~']:
            # unaryOp
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # term
            self.compile_term()
        # </term>
        s = "</term>\n"
        self.file.write(s)
    
    def is_expression(self):
        """Determine if the current token is an expression.
        
        Helper function for ``.
        """
        # integerConstant
        if self.tokenizer.token_type() == "INT_CONST":
            return True
        # stringConstant
        elif self.tokenizer.token_type() == "STRING_CONST":
            return True
        # keywordConstant
        elif self.tokenizer.token_type() == "KEYWORD" and self.tokenizer.token in ['true', 'false', 'null', 'this']:
            return True
        # varName[], varName, subroutineCall
        elif self.tokenizer.token_type() == "IDENTIFIER":
            return True
        # (expression)
        elif self.tokenizer.token == "(":
            return True
        # unaryOp term
        elif self.tokenizer.token in ['-', '~']:
            return True
        # subroutineCall
        else:
            return False
    
    def compile_expression_list(self):
        """Compiles a (possibly empty) comma-separated list of expressions.
        
        Returns the number of expressions in the list.
        """

        # <expressionList>
        s = "<expressionList>\n"
        self.file.write(s)
        if self.is_expression():
            self.compile_expression()
            while self.tokenizer.token == ",":
                # ,
                s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
                self.file.write(s)
                self.tokenizer.advance()
                # expression
                self.compile_expression()
        # </expressionList>
        s = "</expressionList>\n"
        self.file.write(s)

    def compile_subroutine_call(self):
        """Compiles a subroutine call."""

        if self.tokenizer.next_token() == "(":
            # subroutineName
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # (
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # expressionList
            self.compile_expression_list()
            # )
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
        else:
            # className|varName
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # .
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # subroutineName
            s = "<identifier> " + self.tokenizer.identifier() + " </identifier>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # (
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
            # expressionList
            self.compile_expression_list()
            # )
            s = "<symbol> " + self.tokenizer.symbol() + " </symbol>\n"
            self.file.write(s)
            self.tokenizer.advance()
