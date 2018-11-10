import pytest
from thrill_digger_tdd.board import Board


@pytest.fixture
def new():
    new = Board(5, 8)
    new.set_bomb((0, 0))
    new.set_bomb((2, 2))
    new.set_bomb((4, 7))
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


def test_set_bomb(new):
    assert new.is_bomb((0, 0))
    assert new.is_bomb((2, 2))
    assert new.is_bomb((4, 7))


def test_bomb_count(new):
    assert new.bombs == 3


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
    new.fill_board()
    assert new.values[1][1] == 'blue'
    assert new.values[0][1] == 'blue'
    assert new.values[0][2] == 'green'
    assert new.values[0][0] == 'boom'


def test_game_start():
    new = Board()
    new.game_start()
    assert new.bombs == 16
    for row in new.values:
        for col in row:
            assert col is not None
