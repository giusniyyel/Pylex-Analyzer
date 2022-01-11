# -----------------------------------------------------------------------------
# pylex-analyzer: main.py
#
# Author: José Daniel Bautista Campos (Giusniyyel)
# Email: giusniyyel@gmail.com
# 
# All rights reserved.
# -----------------------------------------------------------------------------

from tokrules import MyLexer
from helpers import token_group, choose_example_file

# Saving tokens values
data_tokens = []

# Choosing source code file
source_code = 'test/examples/'+choose_example_file()

# Opening source code file
f = open(source_code,'r')

# Adding data to a variable
data = f.read()

# Using Lexer
lexer = MyLexer()

# Input data into lexer
lexer.input(data)

# Tokenize
print('\nTraduciendo '+source_code+'...\n')
print('{:>5} | {:<10} | {:<64}'.format('Token','Lexema','Valor'))
print('{:>5} | {:<10} | {:<64}'.format('_____','__________','__________'))
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    tok_group = token_group(tok.type)
    data_tokens.append(tok_group)
    print('{:>5} | {:<10} | {:<64}'.format(tok_group,tok.type,tok.value))

# Print all the tokens
print('\nTOKEN: ',data_tokens)

# Closing the source code file
f.close()