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


def test_single_game_params():
    beg_game1 = autoplay.single_random_game(board='beginner')
    beg_game2 = autoplay.single_simple_game(board='beginner')
    int_game1 = autoplay.single_random_game(board='intermediate')
    int_game2 = autoplay.single_simple_game(board='intermediate')
    exp_game1 = autoplay.single_simple_game(board='expert')
    exp_game2 = autoplay.single_simple_game(board='expert')

    for game in [beg_game1, beg_game2]:
        assert game.height == 4
        assert game.width == 5
        assert game.bombs == 4 - game.ruplist.count('boom')

    for game in [int_game1, int_game2]:
        dug_bombs = game.ruplist.count('boom') + game.ruplist.count('rupoor')
        assert game.height == 5
        assert game.width == 6
        assert game.bombs == 8 - dug_bombs

    for game in [exp_game1, exp_game2]:
        dug_bombs = game.ruplist.count('boom') + game.ruplist.count('rupoor')
        assert game.height == 5
        assert game.width == 8
        assert game.bombs == 16 - dug_bombs
