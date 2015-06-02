#!/usr/bin/python3
import global_defs

cur_lex_list = []
rules = {}

def test_cover(axiom, lex_list):
    global cur_lex_list, rules 
    cur_lex_list = lex_list
    rules = global_defs.rules
    # cur_lex = cur_lex_list.pop()
    if (check_rule(axiom)):
        global_defs.rules = rules
        return True
    return False
    

def check_rule(rule_name):
    global cur_lex_list
    rule = rules[rule_name]
    for altr in rule.altrnatives:
        ch_altr = check_alternative(altr)
        if (ch_altr == 1):
            return 2
        elif (ch_altr == 0):
            return 0
    return 0

def check_alternative(altr):
    # for symbol in altr.altrnative:
    #     print("------",symbol.name)
    for symbol in altr.altrnative:
        ch_sym = check_symbol(symbol)
        if (ch_sym == 1):
            cur_lex_list.pop(0)
        elif (ch_sym == 0):
            if(symbol == altr.altrnative[0]):
                return 3
            else:
                return 0
    altr.visited += 1
    return 1

def check_symbol(symbol):
    # print ("Symbol = ", symbol.name, cur_lex_list[0], symbol.is_terminal)
    if (symbol.is_terminal):
        if (cur_lex_list[0] == symbol.name):
            return 1
        elif (symbol.name == "Empty"):
            return 2
        return 0
    else:
        return check_rule(symbol.name)
