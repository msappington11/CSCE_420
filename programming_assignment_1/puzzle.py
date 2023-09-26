from copy import deepcopy

class Puzzle():

    def __init__(self, stacks, goal):
        self.stacks = stacks
        self.goal = goal


    def copy(self):
        new_stacks = [stack for stack in self.stacks]
        for i in range(len(new_stacks)):
            new_stacks[i] = [item for item in new_stacks[i]]

        return Puzzle(new_stacks, self.goal)


    def move_block(self, pos, dest):
        if pos < 0 or pos >= len(self.stacks):
            print('invalid starting position')
            return
        if dest < 0 or dest >= len(self.stacks):
            print('invalid destination')
            return

        if len(self.stacks[pos]) > 0:
            self.stacks[dest].append(self.stacks[pos].pop())


    def h(self):
        h = 0
        for i in range(len(self.stacks)):
            j = 0
            while j < len(self.goal[i]) and j < len(self.stacks[i]) and self.stacks[i][j] == self.goal[i][j]:
                j += 1
            h += len(self.stacks[i]) - j
        return h
    # start from bottom of each stack and continue up until you find a block out of place
    # once found, count the number of blocks on top
    

    def is_solved(self):
        return self.hash_item(self.stacks) == self.hash_item(self.goal)
    
    
    def hash(self):
        return self.hash_item(self.stacks)
    
    
    def hash_item(self, item):
        hashable = []
        for e in item:
            hashable.append(tuple(e))
        return tuple(hashable)
    
    
    def print_puzzle(self):
        for row in self.stacks:
            print(row)

    