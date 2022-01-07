from constants import tokens

def token_group(tok):
    group = 0
    if tok == tokens[0]:        #DELIMITER
        group = 5
    elif tok == tokens[1]:      #OPERATOR
        group = 10
    elif tok == tokens[2]:      #IDENTIFIER
        group = 20
    elif tok == tokens[3]:      #KEYWORD
        group = 15
    elif tok == tokens[4]:      #STRING
        group = 8
    elif tok == tokens[5]:      #CHAR
        group = 16
    elif tok == tokens[6]:      #INTEGER
        group = 30
    elif tok == tokens[7]:      #REALNUMBER
        group = 40
    else:                       #AVOID NONE ERROR
        group = 0
    return group
