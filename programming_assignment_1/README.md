The program can be run by entering the following command:
    python blocksworld.py <filename> -MAX_ITERS <int>

The filename should be the name of the test file without any folders (probA03.bwp)
'all' can also be entered as the filename, which will run all tests and output the stats in the results_stats.txt file
The specified test file, or all test files if 'all' is entered, will have their trace added to the transcripts folder with the same name

MAX_ITERS stops the program after a certain number of iterations has been reached. In my testing, I used a value of 1,000,000 and was able to run all the tests successfully.

I did not run into any limitations of the program. There are no hard coded constraints in the code and all test cases were able to run. There are no known limitations, but large puzzles will likely not finish due to the MAX_ITERS constraint. 