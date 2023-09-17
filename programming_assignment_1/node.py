from puzzle import puzzle

class node():

    def __init__(self, parent, state):
        self.parent = parent
        self.state = state
        self.path_len = self.parent.path_len + 1 if parent else 0
        self.f = self.path_len + self.h()

    def h(self):
        return 0

    def expand(self):
        children = []
        for i in range(len(self.state.stacks)):
            for j in range(len(self.state.stacks)):
                if i == j: continue
                new_state = self.state.copy().move_block(i, j)
                children.append(new_state)
        print(children)
        return children
