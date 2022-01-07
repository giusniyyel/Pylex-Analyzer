from tokrules import MyLexer
from helpers import token_group

# Saving tokens values
data_tokens = []

# Opening source code file
f = open('test/examples/helloworld.cpp','r')

# Adding data to a variable
data = f.read()

# Using Lexer
lexer = MyLexer()

    # Input data into lexer
lexer.input(data)

    # Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    tok_group = token_group(tok.type)
    data_tokens.append(tok_group)
    print('[',tok_group,', ',tok,']')

# Print all the tokens
print('TOKEN: ',data_tokens)

# Closing the source code file
f.close()