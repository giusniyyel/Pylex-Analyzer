# -----------------------------------------------------------------------------
# pylex-analyzer: constants.py
#
# Author: José Daniel Bautista Campos (Giusniyyel)
# Email: giusniyyel@gmail.com
# 
# All rights reserved.
# -----------------------------------------------------------------------------

keyword = {
    'if',
    'else',
    'while',
    'do',
    'break',
    'continue',
    'int',
    'double',
    'float',
    'return',
    'char',
    'bool',
    'case',
    'sizeof',
    'long',
    'short',
    'typedef',
    'switch',
    'unsigned',
    'void',
    'static',
    'struct',
    'goto',
    'printf',
    'main'
}

tokens = [
    'DELIMITER',    #0
    'OPERATOR',     #1
    'IDENTIFIER',   #2
    'KEYWORD',      #3
    'STRING',       #4
    'CHAR',         #5
    'INTEGER',      #6
    'REALNUMBER',   #7
    'COMMENT'       #8
]

group_number = [
    5,      #DELIMITER
    10,     #OPERATOR
    20,     #IDENTIFIER
    15,     #KEYWORD
    8,      #STRING
    16,     #CHAR
    30,     #INTEGER
    40      #REALNUMBER
]