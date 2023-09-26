from puzzle import Puzzle
from node import Node

import queue
import argparse, sys
import os

def read_file(filename):
    stacks = []
    goal = []
    file = open(filename, 'r')
    n_stacks = int(file.readline().split(' ')[0])
    for i in range(n_stacks):
        stacks.append([])
        goal.append([])

    file.readline()
    for i in range(n_stacks):
        line = file.readline()
        for label in line:
            if label != '\n': stacks[i].append(label) 

    file.readline()
    for i in range(n_stacks):
        line = file.readline()
        for label in line:
            if label != '\n': goal[i].append(label)

    file.close()
    state = Puzzle(stacks, goal)
    return Node(None, state)


def A_star(filename, summary):
    reached = {}
    frontier = queue.PriorityQueue()

    initial = read_file(f'probs/probs/{filename}')
    result = open(f'transcripts/{filename[:-4]}.transcript.txt', 'w+')
    frontier.put((initial.f, initial))
    reached[initial.state.hash()] = initial

    iters = 0
    maxq = 0

    while not frontier.empty():
        iters += 1
        maxq = max(frontier.qsize(), maxq)

        if iters > MAX_ITERS:
            result.close()
            return False

        _, node = frontier.get()
        if node.state.is_solved():
            stats = node.trace(result, iters, maxq, filename)
            summary.write(stats)
            result.close()
            return True
        
        children = node.expand()
        result.write(f'iter={iters}, pathcost={node.path_len}, heuristic={node.state.h()}, score={node.f}, children={len(children)}, Qsize={frontier.qsize()}\n')

        for child in children:
            state = child.state
            hashed = state.hash()
            if hashed not in reached or child.path_len < reached[hashed].path_len:
                reached[hashed] = child
                frontier.put((child.f, child))

    result.close()
    return False



parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-MAX_ITERS')
args = parser.parse_args()

MAX_ITERS = int(args.MAX_ITERS)

summary = open('results_stats.txt', 'w+')

# for running all tests
if args.filename == 'all':
    files = os.listdir('./probs/probs')
    for f in files:
        solved = A_star(f, summary)
        if not solved:
            print('Failure')

else:
    solved = A_star(args.filename, summary)
    if not solved:
        print('Failure')

summary.close()


