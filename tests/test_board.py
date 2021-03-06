import pytest
from thrill_digger_tdd.board import Board


@pytest.fixture
def new():
    new = Board(5, 8)
    new.set_value((0, 0), 'boom')
    new.set_value((2, 2), 'boom')
    new.set_value((4, 7), 'boom')
    new.set_value((4, 6), 'boom')
    new.set_value((4, 5), 'boom')
    new.set_value((3, 7), 'boom')
    new.set_value((3, 5), 'boom')
    new.set_value((2, 7), 'boom')
    new.set_value((3, 3), 'rupoor')
    new.fill_board()
    return new


def test_board_default_shape():
    default = Board()
    assert default.height == 5
    assert default.width == 8
    assert default.size == 40


def test_set_random():
    new = Board(5, 8)
    pos = new.set_random('boom')
    assert new.is_bomb((pos[0], pos[1]))


def test_set_value():
    fake = Board(5, 8)
    fake.set_value((1, 1), 'blue')
    fake.set_value((1, 2), 'green')
    fake.set_value((2, 2), 'silver')
    assert fake.values[1][1] == 'blue'
    assert fake.values[1][2] == 'green'
    assert fake.values[2][2] == 'silver'


def test_values(new):
    assert len(new.values) == new.height
    assert len(new.values[0]) == new.width


def test_is_bomb(new):
    assert new.is_bomb((0, 0))
    assert new.is_bomb((2, 2))
    assert new.is_bomb((4, 7))


def test_find_adj_bombs(new):
    assert new.find_adj_bombs((1, 1)) == 2
    assert new.find_adj_bombs((0, 1)) == 1
    assert new.find_adj_bombs((0, 2)) == 0
    assert new.find_adj_bombs((0, 0)) == 0


def test_color_code():
    new = Board()
    assert new.color_code(0) == 'green'
    assert new.color_code(1) == 'blue'
    assert new.color_code(2) == 'blue'
    assert new.color_code(3) == 'red'
    assert new.color_code(4) == 'red'
    assert new.color_code(5) == 'silver'
    assert new.color_code(6) == 'silver'
    assert new.color_code(7) == 'gold'
    assert new.color_code(8) == 'gold'


def test_fill_board(new):
    assert new.values[1][1] == 'blue'
    assert new.values[0][1] == 'blue'
    assert new.values[0][2] == 'green'
    assert new.values[0][0] == 'boom'


def test_game_start():
    new = Board()
    new.game_start(booms=5, rupoors=4)
    assert new.bombs == 9
    values_list = []

    for row in new.values:
        values_list += row
        for col in row:
            assert col is not None
    assert values_list.count('boom') == 5
    assert values_list.count('rupoor') == 4

    new.dig((0, 0))
    new.game_start()
    assert not new.game_over


def test_dig(new):
    assert new.dig((1, 1)) == 'blue'
    assert new.values[1][1] == 'dug'
    assert new.dig((0, 3)) == 'green'
    assert new.dig((3, 6)) == 'silver'
    assert new.score == 106
    new.dig((0, 0))
    assert new.bombs == 8
    assert len(new.moves) == 4


def test_score_code():
    new = Board()
    assert new.score_code('green') == 1
    assert new.score_code('blue') == 5
    assert new.score_code('red') == 20
    assert new.score_code('silver') == 100
    assert new.score_code('gold') == 300
    assert new.score_code('boom') == 0


def test_rupoor():
    new = Board(2, 2)
    new.set_value((0, 0), 'rupoor')
    new.fill_board()
    new.dig((0, 1))

    assert new.bombs == 1
    assert new.dig((0, 0)) == 'rupoor'
    assert new.score == 0
    assert new.values[1][1] == 'blue'
    assert new.bombs == 0


def test_game_end(new):
    assert not new.game_over
    new.dig((0, 0))
    assert new.game_over


def test_random_play(new):
    pos, result = new.random_play()
    row, column = pos
    assert new.values[row][column] == 'dug'
    for i in range(10):
        assert new.random_play()[1] != 'dug'


def test_list_adj(new):
    assert len(new.list_adj((0, 0))) == 3
    assert len(new.list_adj((0, 1))) == 5
    assert len(new.list_adj((1, 1))) == 8


def test_game_win():
    small_board = Board(2, 2)
    small_board.set_value((0, 0), 'boom')
    small_board.set_value((0, 1), 'boom')
    small_board.set_value((1, 0), 'boom')
    small_board.fill_board()
    small_board.dig((1, 1))
    assert small_board.game_over is True
    assert small_board.game_won is True


def test_valid_start():
    failed_start = Board(2, 2)
    try:
        failed_start.game_start()
        assert False

    except AssertionError:
        assert failed_start.values[0][0] is None
    try:
        failed_start.game_start(2, 2)
        assert False

    except AssertionError:
        assert failed_start.values[0][0] is None


def test_ruplist(new):
    new.dig((1, 1))
    new.dig((0, 3))

    new.dig((3, 6))
    new.dig((3, 6))

    new.dig((0, 0))
    new.dig((0, 0))
    true_results = ['blue', 'green', 'silver', 'boom']
    for i, result in enumerate(true_results):
        assert new.ruplist[i] == result
    assert len(new.ruplist) == len(new.moves)
