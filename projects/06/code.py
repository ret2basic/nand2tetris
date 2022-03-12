class Code():
    def __init__(self):
        pass
    
    def dest(self, mnemonic):
        """Maps `dest` to `ddd`"""
        lookup_table = {
            'null' : '000',
            'M' : '001',
            'D' : '010',
            'DM' : '011',
            'A' : '100',
            'AM' : '101',
            'AD' : '110',
            'ADM' : '111',
        }

        return lookup_table[mnemonic]

    def comp(self, mnemonic):
        """Maps `comp` to `a` and `cccccc`"""
        lookup_table = {
            '0' : ['0', '101010'],
            '1' : ['0', '111111'],
            '-1' : ['0', '111010'],
            'D' : ['0', '001100'],
            'A' : ['0', '110000'],
            '!D' : ['0', '001101'],
            '!A' : ['0', '110001'],
            '-D' : ['0', '001111'],
            '-A' : ['0', '110011'],
            'D+1' : ['0', '011111'],
            'A+1' : ['0', '110111'],
            'D-1' : ['0', '001110'],
            'A-1' : ['0', '110010'],
            'D+A' : ['0', '000010'],
            'D-A' : ['0', '010011'],
            'A-D' : ['0', '000111'],
            'D&A' : ['0', '000000'],
            'D|A' : ['0', '010101'],
            'M' : ['1', '110000'], 
            '!M' : ['1', '110001'], 
            '-M' : ['1', '110011'], 
            'M+1' : ['1', '110111'], 
            'M-1' : ['1', '110010'], 
            'D+M' : ['1', '000010'], 
            'D-M' : ['1', '010011'], 
            'M-D' : ['1', '000111'], 
            'D&M' : ['1', '000000'], 
            'D|M' : ['1', '010101'], 
            }

        return lookup_table[mnemonic][0] + lookup_table[mnemonic][1]

    def jump(self, mnemonic):
        """Maps `jump` to `jjj`"""
        lookup_table = {
            'null' : '000',
            'JGT' : '001',
            'JEQ' : '010',
            'JGE' : '011',
            'JLT' : '100',
            'JNE' : '101',
            'JLE' : '110',
            'JMP' : '111',
        }

        return lookup_table[mnemonic]