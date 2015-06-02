#!/usr/bin/python3
import re
import sys
import pickle
import global_defs
from global_defs import Rule, Symbol, Alternative

def analyze_grammar(file):
    grammar = open(file).read()
    grammar = re.sub("\/\*.*\*\/", "", grammar)
    grammar = grammar.replace("\n", "")
    grammar = grammar.split(" ;")
    global_defs.rules["AXIOM"] = Rule("AXIOM")
    global_defs.rules["AXIOM"].altrnatives = make_alternatives(grammar[0].split(' : ')[0])
    for r in grammar:
        if (r != ""):
            l_rule = r.split(' : ')
            rule = Rule(l_rule[0])
            rule.altrnatives = make_alternatives(l_rule[1])
            global_defs.rules[rule.name] = rule
    # print_table(rules)
    with open(file + '.pickle', 'wb') as f:
        pickle.dump(global_defs.rules, f)
    with open(file + '.lt.pickle', 'wb') as f:
        pickle.dump(global_defs.lt, f)
   
def make_alternatives(altrs):
    l_altrs = altrs.split(" |")
    altrnatives = []
    for altr in l_altrs:
        if (altr == ""):
            altrnatives.append(Alternative([Symbol("Empty", True)]))
        else:
            altrnatives.append(Alternative(make_symbol_list(altr)))
    return altrnatives
   
def make_symbol_list(altr):
    symbols_str = altr.split()
    symbol_list = []
    for sym in symbols_str:
        if (sym[0] == "'"):
            if ((ord(sym[1]) > 64) and (ord(sym[1]) < 91)) or ((ord(sym[1]) > 96) and (ord(sym[1]) < 123)):
                symbol_list.append(Symbol(global_defs.lt.add_keyword(sym.split("'")[1]), True))
            elif (len(sym.split("'")[1]) > 1):
                symbol_list.append(Symbol(global_defs.lt.add_mt_separator(sym.split("'")[1]), True))
            else:
                symbol_list.append(Symbol(ord(sym[1]), True))
        elif ((ord(sym[0]) > 64) and (ord(sym[0]) < 91)):
            symbol_list.append(Symbol(global_defs.lt.add_user_lexem(sym), True))
        else:
            symbol_list.append(Symbol(sym, False))
    return symbol_list

def print_table(rules):
    for rule in rules:
        rule_str = rule + " : "
        altrs = rules[rule].altrnatives
        for altr in altrs:
            for sym in altr.altrnative:
                rule_str += str(sym.name) + ' '
            if (altrs[len(altrs) - 1] != altr):
                rule_str += " | "
        rule_str += ";"
        print(rule_str)

        
