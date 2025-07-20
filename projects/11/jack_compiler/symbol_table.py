"""
Symbol Table for Jack Compiler (Project 11)
Manages variable scoping and memory allocation for class and subroutine levels.
"""

class SymbolTable:
    def __init__(self):
        """Creates a new symbol table."""
        self.class_scope = {}  # Class-level symbols (static, field)
        self.subroutine_scope = {}  # Subroutine-level symbols (arg, var)
        self.counters = {
            'STATIC': 0,
            'FIELD': 0,
            'ARG': 0,
            'VAR': 0
        }
    
    def start_subroutine(self):
        """Starts a new subroutine scope (clears subroutine symbol table)."""
        self.subroutine_scope = {}
        self.counters['ARG'] = 0
        self.counters['VAR'] = 0
    
    def define(self, name, var_type, kind):
        """Defines a new identifier with name, type, and kind.
        Assigns it a running index in the kind's namespace.
        STATIC and FIELD are class scope, ARG and VAR are subroutine scope.
        """
        index = self.counters[kind]
        
        if kind in ['STATIC', 'FIELD']:
            self.class_scope[name] = {
                'type': var_type,
                'kind': kind,
                'index': index
            }
        else:  # ARG, VAR
            self.subroutine_scope[name] = {
                'type': var_type,
                'kind': kind,
                'index': index
            }
        
        self.counters[kind] += 1
    
    def var_count(self, kind):
        """Returns the number of variables of the given kind already defined."""
        return self.counters[kind]
    
    def kind_of(self, name):
        """Returns the kind of the named identifier.
        Returns None if the identifier is not found.
        """
        if name in self.subroutine_scope:
            return self.subroutine_scope[name]['kind']
        elif name in self.class_scope:
            return self.class_scope[name]['kind']
        else:
            return None
    
    def type_of(self, name):
        """Returns the type of the named identifier.
        Returns None if the identifier is not found.
        """
        if name in self.subroutine_scope:
            return self.subroutine_scope[name]['type']
        elif name in self.class_scope:
            return self.class_scope[name]['type']
        else:
            return None
    
    def index_of(self, name):
        """Returns the index of the named identifier.
        Returns None if the identifier is not found.
        """
        if name in self.subroutine_scope:
            return self.subroutine_scope[name]['index']
        elif name in self.class_scope:
            return self.class_scope[name]['index']
        else:
            return None
    
    def exists(self, name):
        """Returns True if the identifier exists in either scope."""
        return name in self.subroutine_scope or name in self.class_scope