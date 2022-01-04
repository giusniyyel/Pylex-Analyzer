#!/usr/bin/env python
# encoding: utf-8

tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ODD',
    'ASSIGN',
    'NE',
    'LT',
    'LTE',
    'GT',
    'GTE',
    'LPARENT',
    'RPARENT',
    'COMMA',
    'SEMMICOLOM',
    'DOT',
    'UPDATE'
]

reserved = {
    'begin':'BEGIN',
    'end':'END',
    'if':'IF',
    'then':'THEN',
    'while':'WHILE',
    'do':'DO',
    'call':'CALL',
    'const':'CONST',
    'int':'INT',
    'procedure':'PROCEDURE',
    'out':'OUT',
    'in':'IN',
    'else':'ELSE'
}