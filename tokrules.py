import ply.lex as lex

# List of token names.   This is always required

keyword = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : 'DO',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'int' : 'INT',
    'double' : 'DOUBLE',
    'float' : 'FLOAT',
    'return' : 'RETURN',
    'char' : 'CHAR',
    'bool' : 'BOOL',
    'case' : 'CASE',
    'sizeof' : 'SIZEOF',
    'long' : 'LONG',
    'short' : 'SHORT',
    'typedef' : 'TYPEDEF',
    'switch' : 'SWITCH',
    'unsigned' : 'UNSIGNED',
    'void' : 'VOID',
    'static' : 'STATIC',
    'struct' : 'STRUCT',
    'goto' : 'GOTO',
    'printf' : 'PRINTF',
    'main' : 'MAIN'
}

operator = {
    'SUFFIX',
    'POSTFIX',
    'EQ',
    'NE',
    'LE',
    'GE',
    'OR',
    'AND',
    'ASSIGN',
    'LT',
    'GT',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV'
}

delimiter = {
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'PCOMMA'
}

tokens = [
    'DELIMITER',
    'OPERATOR',
    'IDENTIFIER',
    'KEYWORD',
    'STRING',
    'CHAR',
    'INTEGER',
    'REALNUMBER',
    'COMMENT'
] + list(keyword) + list(operator) + list(delimiter)


def MyLexer():
    # All Operators regular expressions
    t_SUFFIX = r'\++'
    t_POSTFIX = r'--' 
    t_EQ = r'==' 
    t_NE = r'!=' 
    t_LE = r'<=' 
    t_GE = r'>=' 
    t_OR = r'\/\/' 
    t_AND = r'&&' 
    t_ASSIGN = r'\=' 
    t_LT = r'<' 
    t_GT = r'>' 
    t_PLUS = r'\+'
    t_MINUS = r'-' 
    t_MULT = r'\*' 
    t_DIV = r'\/' 

    # All Operators regular expressions
    t_LBRACKET = r'\('
    t_RBRACKET = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_COMMA = r','
    t_PCOMMA = r';'

    # Ignore include
    def t_INCLUDE(t):
        r'\#.*'
        pass
        # No return value. Token discarded

    # Identifiers
    def t_IDENTIFIER(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = keyword.get(t.value,'IDENTIFIER')    # Check for reserved words
        return t

    # Real Numbers
    def t_REALNUMBER(t):
        r'\d(\d)*\.\d(\d)*'
        t.value = float(t.value)
        return t

    # Integers
    def t_INTEGER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Strings
    def t_STRING(t):
        r'\"([^\\\n]|(\\.))*?\"'
        return t

    # Char
    def t_CHAR(t):
        r'\'([^\\\n]|(\\.))*?\''
        return t

    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Ignore comments
    def t_COMMENT(t):
        r'(/\*(.|\n)*?\*/)|(//.*)'
        pass
        # No return value. Token discarded

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer from my environment and return it
    return lex.lex()