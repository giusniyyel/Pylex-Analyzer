# This version simplifies all types by groups and assign to it a number to identify the group
from typing import TYPE_CHECKING
import ply.lex as lex

# List of token names.   This is always required
from constants import tokens, keyword

def MyLexer():
    # Delimiters
    t_DELIMITER = r'(\()|(\))|(\{)|(\})|(,)|(;)'

    # Operators
    t_OPERATOR = r'(\++)|(--)|(==)|(!=)|(<=)|(>=)|(\|\|)|(\|)|(&&)|(&)|(\=)|(<)|(>)|(\+)|(-)|(\*)|(\/)|(\%)'

    # Strings
    t_STRING = r'\"([^\\\n]|(\\.))*?\"'

    # Char
    t_CHAR = r'\'([^\\\n]|(\\.))*?\''

    # Ignore include
    def t_INCLUDE(t):
        r'\#.*'
        pass
        # No return value. Token discarded

    # Identifiers
    def t_IDENTIFIER(t):
        r'[a-zA-Z_]+[a-zA-Z0-9_]*'
        if t.value in keyword:
            t.type = 'KEYWORD'
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