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