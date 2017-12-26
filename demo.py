from game import Game
from nn import NN
from alphago_zero_st import AZST

MAX_GAMES = 100
MAX_MOVES = 19 * 19 * 2

training_data = []


def demo_st():
    nn = NN()
    for i in range(MAX_GAMES):
        g = Game()
        azst = AZST(g, nn)
        game_data = []
        s = g.get_state()
        for _ in range(MAX_MOVES):
            pi, a = azst.play()
            g.step(a)
            game_data.append((s, pi))
            if g.done:
                for i, d in enumerate(game_data):
                    _s, _pi = d
                    training_data.append((_s, _pi,
                                          g.get_result(i % 2)))
                break
    nn.train(training_data)


if __name__ == '__main__':
    demo_st()
