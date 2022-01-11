import os
from constants import tokens, group_number

def token_group(tok):
    group = 0
    if tok == tokens[0]:        #DELIMITER
        group = group_number[0]
    elif tok == tokens[1]:      #OPERATOR
        group = group_number[1]
    elif tok == tokens[2]:      #IDENTIFIER
        group = group_number[2]
    elif tok == tokens[3]:      #KEYWORD
        group = group_number[3]
    elif tok == tokens[4]:      #STRING
        group = group_number[4]
    elif tok == tokens[5]:      #CHAR
        group = group_number[5]
    elif tok == tokens[6]:      #INTEGER
        group = group_number[6]
    elif tok == tokens[7]:      #REALNUMBER
        group = group_number[7]
    else:                       #AVOID NONE ERROR
        group = 0
    return group

def group_table():
    print("{:>8}    {:<12}".format('Token','Lexema'))
    print("{:>8}    {:<12}".format('--------','-----------'))
    for i in range(len(group_number)):
        print("{:>8}    {:<12}".format(str(group_number[i]),tokens[i]))

def example_files():
    examples_dir = './test/examples'
    content = os.listdir(examples_dir)
    return content

def choose_example_file():
    options = {}
    examples = example_files()
    print('Bienvenido estos son los archivos disponibles:')
    for i in range(len(examples)):
        print("{:>2}. {:<25}".format(i+1,examples[i]))
        options[i+1] = examples[i]
    option = int(input('¿Qué archivo desea abrir? '))
    return options.get(option)