import argparse
from convCNF import convCNF

count = 0

def parse_input(filename): # append command line stuff
    file = open(filename, 'r')
    clauses = []
    symbols = set()
    for line in file.readlines():
        line = line.replace('\n', '') # remove endline chars
        if len(line) == 0 or line[0] == '#': # pass over comments and blank lines
            continue
        clauses.append(line) # add clause
        for c in line.split(' '): # for each symbol in the clause
            symbols.add(c.replace('-', '')) # add symbol without negation

    return clauses, symbols


# return if the symbol has negation and the variable without the negation
def remove_neg(symbol):
    return { 'is_neg': symbol[0] == '-', 'value': symbol.replace('-', '') }


# return 1 if at least 1 symbol true, -1 if all false, 0 if undecided
def evaluate_clause(clause, model):
    false_count = 0
    for symbol in clause.split(' '):
        symbol = remove_neg(symbol)
        # if value true, return 1
        if (symbol['is_neg'] and symbol['value'] == -1) or (not symbol['is_neg'] and symbol['value'] == 1):
            return 1
        # if value false, add to count
        if (symbol['is_neg'] and symbol['value'] == 1) or (not symbol['is_neg'] and symbol['value'] == -1):
            false_count += 1
    # if number of false == length of clause, return -1        
    if false_count == len(clause.split(' ')):
        return -1
    
    # else unknown, return 0
    return 0


# find clauses where all but 1 literal is false and last is unknown
def find_unit_clause(clauses, model):
    for clause in clauses: # for each clause
        false_count = 0 # should be 1 less than the amount of literals
        unknown = None # should be the 1 unknown literal
        for p in clause.split(' '):
            var = remove_neg(p)
            if var['is_neg'] and model[var['value']] == 1:
                false_count += 1
            elif not var['is_neg'] and model[var['value']] == -1:
                false_count += 1

            # if unknown, fill with symbol and the assignment needed for clause to be true
            elif model[var['value']] == 0: 
                # if its negative, needs false value to be true
                assign = 1
                if var['is_neg']:
                    assign = -1
                unknown = ( var['value'], assign )

        if false_count == len(clause.split(' ')) - 1 and unknown is not None:
            return unknown
    return ( None, None )


def DPLL_SAT(filename, literals, uch): # filename contains the sentence
    clauses, symbols = parse_input(filename)
    model = {}
    for symbol in symbols:
        model[symbol] = 0
    for literal in literals:
        model[literal] = 1 # set negated version to false?

    DPLL(clauses, symbols, model, uch)


def DPLL(clauses, symbols, model, uch):
    print(count)
    count += 1
    print(model)
    # evaluate each clause with values in model, if all true, return true
    all_true = True
    for clause in clauses:
        truth = evaluate_clause(clause, model)
        if truth == -1: # if there is a clause thats false, return false
            return False
        all_true = all_true and truth == 1 # if the truth of a clause is false or unknown, all_true will be false
    if all_true: # if all clauses true, return true
        return True
    
    P, value = find_unit_clause(clauses, model)
    if P is not None:
        # might be messed up since messing with shared memory
        symbols.remove(P)
        return DPLL(clauses, symbols, model | {P: value}, uch)
    
    P = next(iter(symbols))
    symbols.remove(P) # might be bad
    return DPLL(clauses, symbols, model | {P: True}, uch) or DPLL(clauses, symbols, model | {P: False}, uch)
    

            


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input filename")
parser.add_argument("literals", nargs="*", help="Literals")
parser.add_argument("UCH", action="store_true", help="Use UCH option")
args = parser.parse_args()

DPLL_SAT(args.filename, args.literals, args.UCH)
