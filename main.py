from tokrules import MyLexer

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
    print(tok)

# Closing the source code file
f.close()