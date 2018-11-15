from thrill_digger_tdd.board import Board
from thrill_digger_tdd import autoplay

def test_single_random_game():
    game = autoplay.single_random_game()
    assert len(game.moves) >= 1
    assert game.ruplist[-1] == 'boom' or game.game_won


def test_single_simple_game():
    game = autoplay.single_simple_game()
    moves = game.moves
    start = [(3, 1), (3, 3), (3, 5), (1, 1), (1, 3), (1, 5)]
    for i, loc in enumerate(moves[:5]):
        assert start[i][0] == loc[0]
        assert start[i][1] == loc[1]
    assert game.ruplist[-1] == 'boom' or game.game_won


def test_autoplay():
    gamelist = autoplay.autoplay(10)
    assert len(gamelist) == 10
    for game in gamelist:
        assert game.ruplist[-1] == 'boom' or game.game_won


def test_strategy_kwarg():
    gamelist = autoplay.autoplay(3, strategy='simple')
    start = [(3, 1), (3, 3), (3, 5), (1, 1), (1, 3), (1, 5)]
    for game in gamelist:
        for i, loc in enumerate(game.moves[:5]):
            assert start[i][0] == loc[0]
            assert start[i][1] == loc[1]
        assert game.ruplist[-1] == 'boom' or game.game_won
