#!/usr/bin/python3
import re
import sys
import pickle

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
        self.user_lexems[lexem] = []

lt = LexTable()

def analyze_grammar(file):
    grammar = open(file).read()
    grammar = re.sub("\/\*.*\*\/", "", grammar)
    grammar = grammar.replace("\n", "")
    grammar = grammar.split(" ;")
    rules = {}
    for r in grammar:
        if (r != ""):
            l_rule = r.split(' : ')
            rule = Rule(l_rule[0])
            rule.altrnatives = make_alternatives(l_rule[1])
            rules[rule.name] = rule
    print_table(rules)
    with open(file + '.pickle', 'wb') as f:
        pickle.dump(rules, f)
    with open(file + '.lt.pickle', 'wb') as f:
        pickle.dump(lt, f)
   
def make_alternatives(altrs):
    l_altrs = altrs.split(" |")
    altrnatives = []
    for altr in l_altrs:
        if (altr == ""):
            altrnatives.append([Symbol("Empty", False)])
        else:
            altrnatives.append(make_symbol_list(altr))
    return altrnatives
   
def make_symbol_list(altr):
    symbols_str = altr.split()
    symbol_list = []
    for sym in symbols_str:
        if (sym[0] == "'"):
            if ((ord(sym[1]) > 64) and (ord(sym[1]) < 91)) or ((ord(sym[1]) > 96) and (ord(sym[1]) < 123)):
                symbol_list.append(Symbol(lt.add_keyword(sym.split("'")[1]), True))
            elif (len(sym.split("'")[1]) > 1):
                symbol_list.append(Symbol(lt.add_mt_separator(sym.split("'")[1]), True))
            else:
                symbol_list.append(Symbol(ord(sym[1]), True))
        else:
            symbol_list.append(Symbol(sym, False))
    return symbol_list

def print_table(rules):
    for rule in rules:
        rule_str = rule + " : "
        altrs = rules[rule].altrnatives
        for altr in altrs:
            for sym in altr:
                rule_str += str(sym.name) + ' '
            if (altrs[len(altrs) - 1] != altr):
                rule_str += " | "
        rule_str += ";"
        print(rule_str)

        
