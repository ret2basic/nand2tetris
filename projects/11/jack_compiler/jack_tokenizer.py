class JackTokenizer():
    def __init__(self, filename):
        self.filename = filename

        self.keywords = {
            'class',
            'constructor',
            'function',
            'method',
            'field',
            'static',
            'var',
            'int',
            'char',
            'boolean',
            'void',
            'true',
            'false',
            'null',
            'this',
            'let',
            'do',
            'if',
            'else',
            'while',
            'return',
        }
    
        self.symbols = {
            '{',
            '}',
            '(',
            ')',
            '[',
            ']',
            '.',
            ',',
            ';',
            '+',
            '-',
            '*',
            '/',
            '&',
            '|',
            '<',
            '>',
            '=',
            '~',
        }

        self.string_constant = {
            '"',
        }
    
        self.replace_lookup = {
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            '&': "&amp;",
        }

        self.replace_symbols = [
            '&',
            '"',
            "<",
            ">",
        ]

        self.current_token = ""
        self.tokens = []
        self.sep = '[' + ''.join(self.symbols) + ']'
        self.counter = 0
        filename_components = filename.split('/')
 
        self.code_to_tokens()
        self.max_length = len(self.tokens)

    def next_token(self):
        if self.counter < self.max_length:
            return self.tokens[self.counter]

    def code_to_tokens(self):
        """Jack source code => tokens."""
        # Handle both full filenames and base names
        if self.filename.endswith('.jack'):
            file_path = self.filename
        else:
            file_path = self.filename + '.jack'
        
        with open(file_path) as f:
            for line in f.readlines():
                data = line.split()
                # Skip whitespace
                if len(data) == 0:
                    pass
                # Skip all comments
                elif data[0] == '//':
                    pass
                elif data[0] == '/**' or data[0] == '*' or data[0] == '*/':
                    pass
                # Generate tokens
                else:
                    data = ' '.join(data)
                    # Skip in-line comments
                    data = data.split('//')[0]
                    result = self.parse_one_line(data)
                    self.tokens += result
    
    def parse_one_line(self, string):
        """One line of code => tokens."""
        result = []
        i = 0
        n = len(string)
        count = 0
        for j in range(n):
            if string[j] in self.string_constant:
                if count == 0:
                    i = j
                    count += 1
                else:
                    result.append(string[i: (j+1)])
                    count = 0
                    continue

            if string[j] == ' ' and count == 0:
                if (j > i):
                    result.append(string[i: j])
                i = j + 1
                    
            if string[j] in self.symbols:
                if (j > i and string[j-1] != '"'):
                    result.append(string[i: j])
                result.append(string[j])
                i = j + 1
        
        return result

    def _replace(self, word):
        """"""
        for i in word:
            if i in self.replace_symbols:
                word = word.replace(i, self.replace_lookup[i])
        return word

    def has_more_tokens(self):
        """Are there more tokens in the input?"""
        return self.counter < self.max_length

    def advance(self):
        """Gets the next token from the input, and makes it the current token.
        
        This method should be called only if `has_more_tokens` is True.
        Initially there is no current token.
        """
        if self.has_more_tokens():
            self.token = self.tokens[self.counter]
            self.counter += 1

    def token_type(self):
        """Returns the type of the current token, as a constant."""
        if self.token in self.keywords:
            return 'KEYWORD'
        elif self.token in self.symbols:
            return 'SYMBOL'
        elif self.token[0] == '"' and self.token[-1] == '"':
            return 'STRING_CONST'
        elif self.token.isdigit():
            return 'INT_CONST'
        else:
            return 'IDENTIFIER'

    def key_word(self):
        """Returns the keyword which is the current token, as a constant.
        
        This method should be called only if `token_type` is `KEYWORD`.
        """
        if self.token_type() == 'KEYWORD':
            return self.token
        else:
            print('Error in JackTokenizer.key_word().')
            exit()

    def symbol(self):
        """Returns the character which is the current token.
        
        Should be called only if `token_type` is `SYMBOL`.
        """
        if self.token_type() == 'SYMBOL':   
            self.token = self._replace(self.token)
            return self.token
        else:
            print('Error in JackTokenizer.symbol().')
            exit()

    def identifier(self):
        """Returns the string which is the current token.
        
        Should be called only if `token_type` is `IDENTIFIER`.
        """
        if self.token_type() == 'IDENTIFIER':
            return self.token
        else:
            print('Error in JackTokenizer.identifier().')
            exit()

    def int_val(self):
        """Returns the integer value of the the current token.
        
        Should be called only if `token_type` is `INT_CONST`.
        """
        if self.token_type() == 'INT_CONST':
            return int(self.token)
        else:
            print('Error in JackTokenizer.int_val().')
            exit()

    def string_val(self):
        """Returns the string value of the current token, without the opening and closing double quotes.
        
        Should be called only if `token_type` is `STRING_CONST`.
        """
        if self.token_type() == 'STRING_CONST':
            self.token = self._replace(self.token[1:-1])
            return self.token
        else:
            print('Error in JackTokenizer.string_val().')
            exit()

    def write_xml(self):
        """Tokens => XML"""
        current_line = ""
        xml_filename = self.filename + '_tokens.xml'

        with open(xml_filename, 'w+') as f:
            # Opening
            f.write('<tokens>\n')

            while self.has_more_tokens():
                self.advance()
                current_token_type = self.token_type()

                if current_token_type == 'KEYWORD':
                    current_line = '<keyword> ' + self.key_word() + ' </keyword>'
                elif current_token_type == "SYMBOL":
                    current_line = '<symbol> ' + self.symbol() + ' </symbol>'
                elif current_token_type == "INT_CONST":
                    current_line = '<integerConstant> ' + str(self.intVal()) + ' </integerConstant>'
                elif current_token_type == 'STRING_CONST':
                    current_line = '<stringConstant> ' + self.stringVal() + ' </stringConstant>'
                elif current_token_type == 'IDENTIFIER':
                    current_line = '<identifier> ' + self.identifier() + ' </identifier>'
                else:
                    print("Error in JackTokenizer.write_xml().")

                f.write(current_line + '\n')
            # Ending
            f.write('</tokens>\n')
