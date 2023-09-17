from puzzle import puzzle
from node import node
import queue

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

    state = puzzle(stacks, goal)
    return node(None, state)

def h():
    return 0

reached = set()
frontier = queue.PriorityQueue()

initial = read_file('probs/probs/probA03.bwp')
frontier.put((initial.f, initial))
reached.add(initial.state.hash())

while not frontier.empty():
    _, node = frontier.get()
    if node.state.is_solved():
        print('solved')
        break
    for child in node.expand():
        child.state.print_puzzle()


