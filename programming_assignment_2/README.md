Before running the DPLL code, the knowledge base should be converted to CNF using the convCNF.py file. This can be done by entering the following command:
    python convCNF.py filename.kb -DIMACS > filename.cnf
Once the KB is converted to CNF form, the DPLL code can be run by entering the following command:
    python DPLL.py filename.cnf <*literals> +UCH
The filename should be the same as the one created in the previous step. Any facts that should be added to the knowledge base can be added to the command. Adding +UCH will also use the unit clause heuristic, which reduces the amount of DPLL calls made. Below is an example:
    python DPLL.py mapcolor.cnf QG VB +UCH > results_mapcolor_unsatisfiable.UCH.txt 
In this case, mapcolor.cnf is used for the knowledge base and QG and VB are added as initial facts. This also uses the unit clause heuristic due to the +UCH argument.

The program follows the DPLL pseudocode given in the textbook with some helper functions to clean up the code. The first of which, parse_input, reads the cnf file and breaks it down into independent clauses and a set of symbols that are contained within the clauses.
Another simple function, remove_negative, simply takes in a literal, removes the '-' indicating if its negated, and returns a dictionary of if the literal is negated and the symbol without the '-' sign.
The evaluate_clause function checks the truth value of a single clause by iterating through the literals and checking the model to see if one of the literals evaluates to true. If one of the literals is true, it means the clause is true so 1 is returned, indicating the clause is true. If all the clauses are false, -1 is returned to indicate that the clause is false. If there are still unbound variables so the truth value is undecided, it returns 0.
The find_unit_clause function follows the definition of a unit clause. It iterates through the clauses, looking for the first one that contains k-1 negative literals and 1 undefined value. If this is found, it is returned. If none are found, it returns None. Additionally, it returns None if the UCH is disabled.
The rest of the DPLL algorithm follows the book. One thing to note is that a set is used to keep track of the symbols, which means the symbols are not removed in the same order from run to run. This means different solutions can be found by running the exact same input multiple times. If this is not desired, the set can be converted into a list in the DPLL_SAT function and sorted to achieve the same result between runs.

The generate_queens.py script was used to create the KBs for the multiple queens problems. This can be ran entering:
    python generate_queens.py n_queens > filename.kb
This needs to be converted to CNF form like all other KBs before being run through the algorithm. The locations of the queens are 0 based.