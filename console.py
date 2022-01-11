from tokrules import MyLexer
from helpers import token_group

# Saving tokens values
data_tokens = []

# Getting source code
source_code = input('Introduzca código:\n')

# Using Lexer
lexer = MyLexer()

    # Input data into lexer
lexer.input(source_code)

    # Tokenize
print('\nTraduciendo su código...\n')
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