import argparse
from convCNF import convCNF

count = 0

# remove initial facts from symbols set
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
        if (symbol['is_neg'] and model[symbol['value']] == -1) or (not symbol['is_neg'] and model[symbol['value']] == 1):
            return 1
        # if value false, add to count
        if (symbol['is_neg'] and model[symbol['value']] == 1) or (not symbol['is_neg'] and model[symbol['value']] == -1):
            false_count += 1
    # if number of false == length of clause, return -1        
    if false_count == len(clause.split(' ')):
        return -1
    
    # else unknown, return 0
    return 0


# find clauses where all but 1 literal is false and last is unknown
def find_unit_clause(clauses, model, uch):
    if not uch: # if disabled, return
        return ( None, None )
    
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
        literal = remove_neg(literal)
        if literal['is_neg']:
            model[literal['value']] = -1 # set literals to false if fact is negative
        else:
            model[literal['value']] = 1 # set literal to true if fact is positive

        symbols.remove(literal['value']) # remove from symbols list so they dont get overriden

    return DPLL(clauses, symbols, model, uch)


def DPLL(clauses, symbols, model, uch):
    print(model)
    global count
    count += 1
    # evaluate each clause with values in model, if all true, return true
    all_true = True
    for clause in clauses:
        truth = evaluate_clause(clause, model)
        if truth == -1: # if there is a clause thats false, return false
            print('Backtracking')
            return False
        all_true = all_true and truth == 1 # if the truth of a clause is false or unknown, all_true will be false
    if all_true: # if all clauses true, return true
        return model
    
    P, value = find_unit_clause(clauses, model, uch)
    if P is not None:
        symbols_copy = set(symbols)
        symbols_copy.remove(P)
        print(f'Forced assignment from UCH: {P}={value}')
        return DPLL(clauses, symbols_copy, dict(model | {P: value}), uch)
    
    # take random P from set
    P = next(iter(symbols))
    symbols_copy = set(symbols)
    symbols_copy.remove(P)

    print(f'Guessing assignment: {P}=1')
    left = DPLL(clauses, symbols_copy, dict(model | {P: 1}), uch)
    if not left:
        print(f'Guessing assignment: {P}=-1')
        right = DPLL(clauses, symbols_copy, dict(model | {P: -1}), uch)
    return left or right    

            


parser = argparse.ArgumentParser(prefix_chars='+')
parser.add_argument("filename", help="Input filename")
parser.add_argument("literals", nargs="*", help="Literals")
parser.add_argument("+UCH", action="store_true", help="Use UCH option")
args = parser.parse_args()

print('filename:', args.filename)
print('literals:', args.literals)
print('UCH:', args.UCH)

solved = DPLL_SAT(args.filename, args.literals, args.UCH)
if solved:
    print('\nSolved with model:\n', solved)
    print('True values: ', end='')
    for key in solved.keys():
        if solved[key] == 1:
            print(key, end=' ')
    print()
else:
    print('\nUnsatisfiable')
print('DPLL Calls:', count)
print('UCH:', args.UCH)