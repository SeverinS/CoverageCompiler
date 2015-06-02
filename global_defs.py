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

class Alternative:
    visited = 0
    def __init__(self, altrnative):
        self.altrnative = altrnative
                
class LexTable:
    num_mt_sep = 301
    mt_separators = {}
    num_keywords = 401
    keywords = {}
    num_user_lexem = 1000
    user_lexems = {}
    def add_mt_separator(self, sep):
        if sep in self.mt_separators:
            return self.mt_separators[sep]
        self.mt_separators[sep] = self.num_mt_sep
        self.num_mt_sep += 1
        return self.num_mt_sep - 1
    def add_keyword(self, keyword):
        if keyword in self.keywords:
            return self.keywords[keyword]
        self.keywords[keyword] = self.num_keywords
        self.num_keywords += 1
        return self.num_keywords - 1
    def add_user_lexem(self, lexem):
        if lexem in self.user_lexems:
            return self.user_lexems[lexem]
        self.user_lexems[lexem] = self.num_user_lexem
        self.num_user_lexem += 1
        return self.num_user_lexem - 1

lt = LexTable()
rules = {}
