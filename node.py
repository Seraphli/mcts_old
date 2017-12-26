from math import *
import parameter


class Node(object):
    """A node in the search tree."""

    def __init__(self, game, nn,
                 action=None, parent=None):
        self.game = game
        self.nn = nn
        self.state = game.get_state()
        # the action of this node - "None" for the root node
        self.action = action
        # "None" for the root node
        self.parent = parent
        self.children = []
        self.N = 0
        self.W = 0
        self.P = self.nn.evaluate(self.state, self.action)
        # the only part of the state that the Node needs later
        self.player_just_moved = game.player_just_moved

    def select(self):
        """Use the UCB1 formula to select a children node."""
        a = sorted(self.children, key=lambda c: c.Q + c.U)[-1]
        return a

    def expand(self):
        for a in self.game.get_actions():
            n = Node(self.game, self.nn, action=a, parent=self)
            self.children.append(n)

    @property
    def total_n(self):
        return sum([c.N for c in self.children])

    @property
    def Q(self):
        if self.N == 0:
            return 0
        return self.W / self.N

    @property
    def U(self):
        return parameter.c_PUCT * self.P * \
               sqrt(self.parent.total_n) / (1 + self.N)

    def update(self, v):
        """Update this node."""
        self.N += 1
        self.W += v

    def __repr__(self):
        return "[A:" + str(self.action) + " Q:" + str(self.Q) + \
               " U:" + str(self.U) + "]"

    def tree_to_string(self, indent):
        s = self.indent_string(indent) + str(self)
        for c in self.children:
            s += c.tree_to_string(indent + 1)
        return s

    def indent_string(self, indent):
        s = "\n"
        for i in range(1, indent + 1):
            s += "| "
        return s

    def children_to_string(self):
        s = ""
        for c in self.children:
            s += str(c) + "\n"
        return s
