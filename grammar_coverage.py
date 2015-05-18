#!/usr/bin/python3
import sys
import pickle
from grammar_analyzer import analyze_grammar

def coverage(grm_file, test_file):
    analyze_grammar(grm_file)


    
if __name__ == "__main__":
    if len (sys.argv) > 2:
        coverage(sys.argv[1], sys.argv[2])
    else:
        coverage('Grammars/signal-part/signal-part.grm', 'signal-part-test-list.txt')
