import argparse
from convCNF import convCNF

def parse_input(filename): # append command line stuff
    file = open(filename, 'r')
    clauses = []
    symbols = set()
    for line in file.readlines():
        line = line.replace('\n', '')
        if len(line) == 0 or line[0] == '#':
            continue
        clauses.append(line)
        for c in line.split(' '):
            symbols.add(c)

    return clauses, symbols

def find_unit_clause(clauses, model):
    for clause in clauses:
        
        for p in clause:


def DPLL_SAT(filename, literals, uch): # filename contains the sentence
    clauses, symbols = parse_input(filename)
    model = {}
    for symbol in symbols:
        model[symbol] = 0
    for literal in literals:
        model[literal] = 1 # set negated version to false?

    DPLL(clauses, symbols, model, uch)


def DPLL(clauses, symbols, model, uch):
    # all clauses
    all_true = True
    for clause in clauses:
        if model.get(clause, None) == -1: # if clause in model false, return false
            return False
        if model.get(clause, None) == None: # if clause not in model ?
            all_true = False
    if all_true: # if all clauses true in model, return true
        return True
    
    P, value = find_unit_clause(clauses, model)
    

            


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input filename")
parser.add_argument("literals", nargs="*", help="Literals")
parser.add_argument("UCH", action="store_true", help="Use UCH option")
args = parser.parse_args()

DPLL_SAT(args.filename, args.literals, args.UCH)
