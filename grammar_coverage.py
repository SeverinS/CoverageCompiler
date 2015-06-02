#!/usr/bin/python3
import sys
import pickle
import global_defs
from grammar_analyzer import analyze_grammar
from grammar_analyzer import print_table
# from grammar_analyzer import LexTable
from test_coverage import test_cover
import test

def coverage_count():
    covered = 0
    all = 0
    for rule in global_defs.rules:
        altrs = global_defs.rules[rule].altrnatives
        for altr in altrs:
            all += 1
            if (altr.visited > 0):
                covered += 1
            else:
                print ("Uncovered alternative: rule ", rule, " : ", altrnative_str(altr))
    print ("All = ", all)
    print ("Covered = ", covered)
    print ("Test Coverage = ", round(covered*100 / all, 1))
    
def altrnative_str(altr):
    str_al = ""
    for symbol in altr.altrnative:
        str_al += str(symbol.name) + " "
    return str_al
def coverage(grm_file, test_file):
    analyze_grammar(grm_file)
    with open(grm_file + '.pickle', 'rb') as f:
        global_defs.rules = pickle.load(f)
    with open(grm_file + '.lt.pickle', 'rb') as f:
        lt = pickle.load(f)
    # print("-----------------------------------------")
    # print_table(rules)
    # lexer
# test.sig
# ((401 1) (1001 1) (40 1) (1002 1) (44 1) (1003 1) (44 1) (1004 1) (41 1) (59 1)
#  (401 2) (1005 2) (40 2) (1006 2) (44 2) (1007 2) (41 2) (59 2) (401 4)
#  (1008 4) (40 4) (1009 4) (41 4) (59 4) (401 6) (1010 6) (40 6) (1011 6) (44 6)
#  (1012 6) (44 6) (1013 6) (41 6) (59 6) (402 8) (1005 9) (40 9) (501 9) (44 9)
#  (502 9) (41 9) (59 9) (1005 10) (40 10) (503 10) (44 10) (504 10) (41 10)
#  (59 10) (1010 11) (40 11) (505 11) (44 11) (506 11) (44 11) (507 11) (41 11)
#  (59 11) (404 12) (59 12) (403 13) (59 13))

# test2.sig
# ((401 1) (1001 1) (40 1) (1002 1) (44 1) (1003 1) (44 1) (1004 1) (41 1) (59 1)
#  (401 2) (1005 2) (40 2) (1006 2) (44 2) (1007 2) (41 2) (59 2) (401 3)
#  (1008 3) (40 3) (1009 3) (44 3) (1014 3) (44 3) (1011 3) (41 3) (59 3) (401 4)
#  (1015 4) (40 4) (1009 4) (41 4) (59 4) (402 5) (1005 6) (40 6) (508 6) (44 6)
#  (509 6) (41 6) (59 6) (1015 7) (40 7) (510 7) (41 7) (59 7) (404 8) (59 8)
#  (403 9) (59 9))

    
    lex_l = [401, 1001, 40, 1001, 44, 1001, 44, 1001, 41, 59, 401, 1001, 40, 1001, 44, 1001, 41, 59, 401, 1001, 40, 1001, 44, 1001, 44, 1001, 41, 59, 402, 1001, 40, 1000, 44, 1000, 41, 59, 1001, 40, 1000, 44, 1000, 41, 59, 1001, 40, 1000, 44, 1000, 44, 1000, 44, 1000, 41, 59, 404, 59, 403, 59]

    lex_l2 = [401, 1001, 40, 1001, 44, 1001, 44, 1001, 41, 59, 401,1001,40, 1001, 44, 1001, 41, 59, 401, 1001, 40, 1001, 44, 1001, 44, 1001, 41, 59, 401,1001, 40, 1001, 41, 59, 402, 1001, 40, 1000, 44, 1000, 41, 59, 1001, 40, 1000, 41, 59, 404, 59, 403, 59,]

    # test_result = test_cover("AXIOM", lex_l)
    if (test_cover("AXIOM", lex_l)):
        print ("=============== OK ================")
    else:
        print ("=============== NO ================")
        print ("Test Failure!!")
    coverage_count()

    
if __name__ == "__main__":
    if len (sys.argv) > 2:
        coverage(sys.argv[1], sys.argv[2])
    else:
        coverage('Grammars/signal-part/signal-part.grm', 'signal-part-test-list.txt')


