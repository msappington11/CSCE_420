Before running the DPLL code, the knowledge base should be converted to CNF using the convCNF.py file. This can be done by entering the following command:
    python convCNF.py filename.kb -DIMACS > filename.cnf
Once the KB is converted to CNF form, the DPLL code can be run by entering the following command:
    python DPLL.py filename.cnf <*literals> +UCH
The filename should be the same as the one created in the previous step. Any facts that should be added to the knowledge base can be added to the command. Adding +UCH will also use the unit clause heuristic, which reduces the amount of DPLL calls made. Below is an example:
    python DPLL.py mapcolor.cnf QG VB +UCH > results_mapcolor_unsatisfiable.UCH.txt 
In this case, mapcolor.cnf is used for the knowledge base and QG and VB are added as initial facts. This also uses the unit clause heuristic due to the +UCH argument.