# Just some interfaces about game

class Game(object):
    def __init__(self, state=None):
        self.state = state
        self.player_just_moved = 2

    def evaluate(self):
        pass

    @property
    def done(self):
        return False

    def get_state(self):
        return

    def set_state(self, state):
        self.state = state

    def clone(self):
        return Game(self.get_state())

    def step(self, a):
        return self.state

    def get_result(self, i):
        return
