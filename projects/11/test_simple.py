#!/usr/bin/env python3

from jack_compiler.jack_tokenizer import JackTokenizer

# Simple test of tokenizer
tokenizer = JackTokenizer('/root/nand2tetris/projects/11/Seven/Main.jack')

print("Testing tokenizer...")
tokenizer.advance()

count = 0
while tokenizer.has_more_tokens() and count < 20:
    print(f"Token: '{tokenizer.token}', Type: {tokenizer.token_type()}")
    if tokenizer.token_type() == 'SYMBOL':
        print(f"  Symbol: '{tokenizer.symbol()}'")
    elif tokenizer.token_type() == 'KEYWORD':
        print(f"  Keyword: '{tokenizer.key_word()}'")
    elif tokenizer.token_type() == 'IDENTIFIER':
        print(f"  Identifier: '{tokenizer.identifier()}'")
    
    tokenizer.advance()
    count += 1

print("Tokenizer test completed.")