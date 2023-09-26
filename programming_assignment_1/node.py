from puzzle import Puzzle

class Node():

    def __init__(self, parent, state):
        self.parent = parent
        self.state = state
        self.path_len = self.parent.path_len + 1 if parent else 0
        self.f = self.path_len + self.state.h()


    def expand(self):
        children = []
        for i in range(len(self.state.stacks)):
            for j in range(len(self.state.stacks)):
                if i == j: continue
                new_state = self.state.copy()
                new_state.move_block(i, j)
                children.append(Node(self, new_state))

        return children
    

    def __lt__(self, other): # override because the priority queue compares node objects in the event of a priority tie
        return 0
    

    def trace(self, result, iters, maxq, filename):
        # make a stack to go back up to the top
        stack = []
        node = self
        while node:
            stack.append(node)
            node = node.parent

        # pop off stack to go back down
        move = 0
        result.write('\n\nSolution path:\n')
        while len(stack) > 0:
            node = stack.pop(-1)
            result.write(f'move {move}, pathcost={node.path_len}, heuristic={node.state.h()}, f(n)={node.f}\n')
            for row in node.state.stacks:
                result.write(f'{row}\n')
            move += 1

        result.write(f'\n\nstatistics: planlen: {move-1}\t iters: {iters}\t maxq: {maxq}\n')
        return f'statistics: {filename} planlen: {move-1}\t iters: {iters}\t maxq: {maxq}\n'


    def print(self):
        print('Parent:', self.parent)
        print('State:', self.state.print_puzzle())
        print('Path length:', self.path_len)
        print('f:', self.f)
