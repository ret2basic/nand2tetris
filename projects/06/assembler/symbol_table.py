class SymbolTable():
    def __init__(self):
        self.symbol_table = {
            'R0' : 0, 'R1' : 1, 'R2' : 2, 'R3' : 3, 'R4' : 4,
            'R5' : 5, 'R6' : 6, 'R7' : 7, 'R8' : 8, 'R9' : 9,
            'R10' : 10, 'R11' : 11, 'R12' : 12, 'R13' : 13,
            'R14' : 14, 'R15' : 15, 'SCREEN' : 16384, 'KBD' : 24576,
            'SP' : 0, 'LCL' : 1, 'ARG' : 2, 'THIS' : 3, 'THAT' : 4,
        }

    def contains(self, symbol):
        """Does the symbol table contain the given `symbol`?"""
        return symbol in self.symbol_table
    
    def add_entry(self, symbol, address):
        """Adds `<symbol,address> to the table."""
        if symbol not in self.symbol_table:
            self.symbol_table[symbol] = address
        else:
            pass
            
    def get_address(self, symbol):
        """Return the address associated with the `symbol`"""
        return self.symbol_table[symbol]