class puzzle():

    def __init__(self, stacks, goal):
        self.stacks = stacks
        self.goal = goal


    def copy(self):
        new_stacks = self.stacks.copy()
        for i in range(len(new_stacks)):
            new_stacks[i] = new_stacks[i].copy()

        return puzzle(new_stacks, self.goal)


    def move_block(self, pos, dest):
        if pos < 0 or pos >= len(self.stacks):
            print('invalid starting position')
            return
        if dest < 0 or dest >= len(self.stacks):
            print('invalid destination')
            return

        self.stacks[dest].append(self.stacks[pos].pop())


    def print_puzzle(self):
        print('Current:')
        for row in self.stacks:
            print(row)

        print('\nGoal:')
        for row in self.goal:
            print(row)


    def hash(self):
        return self.hash_item(self.stacks)

    
    def hash_item(self, item):
        hashable = []
        for e in item:
            hashable.append(tuple(e))
        return tuple(hashable)

    
    def is_solved(self):
        return self.hash_item(self.stacks) == self.hash_item(self.goal)

    