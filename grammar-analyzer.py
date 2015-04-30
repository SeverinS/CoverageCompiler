#!/usr/bin/python3

class Rule:
    def __init__(self, name):
        altrnatives = []
        self.name = name

class Symbol:
    visited = 0;
    def __init__(self, name, is_terminal):
        self.name = name
        self.is_terminal = is_terminal
                
class LexTable:
    num_mt_sep = 301
    mt_separators = {}
    num_keywords = 401
    keywords = {}
    num_constants = 501
    constants = {}
    num_ident = 1001
    identifiers = {}
    def add_mt_separator(self, sep):
        self.mt_separators[self.num_mt_sep] = sep
        self.num_mt_sep += 1
    def add_keyword(self, keyword):
        self.keywords[self.num_keywords] = keyword
        self.num_keywords += 1
    def add_constant(self, constant):
        self.constants[self.num_constants] = constant
        self.num_constants += 1
    def add_identifier(self, identifier):
        self.identifiers[num_ident] = identifier
        self.num_ident += 1
        

        
