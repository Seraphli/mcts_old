# AlphaGo Zero like MCTS, single thread
from node import Node

MAX_ITER = 1600


class AZST(object):
    def __init__(self, game, nn):
        self.game = game
        self.nn = nn

    def play(self):
        self.tree = Node(self.game, self.nn)
        for _ in range(MAX_ITER):
            node = self.tree
            game = self.game.clone()
            while node.children != []:
                node = self.tree.select()
                game.step(node.action)
            self.tree.expand()
            self.tree.update(1)
        return sorted(self.tree.children, key=lambda c: c.N)[-1].action
