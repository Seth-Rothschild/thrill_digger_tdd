import click
import thrill_digger_tdd
from thrill_digger_tdd.board import Board


def interactive_start():
    print('Welcome to Thrill Digger! (version: {})'.format(
        thrill_digger_tdd.__version__))
    print('Choose difficulty: (beginner, intermediate, expert)')
    game_type = input()
    if game_type == 'beginner':
        play_area = Board(4, 5)
        play_area.game_start(booms=4, rupoors=0)

    elif game_type == 'intermediate':
        play_area = Board(5, 6)
        play_area.game_start(booms=4, rupoors=4)

    elif game_type == 'expert':
        play_area = Board(5, 8)
        play_area.game_start(booms=8, rupoors=8)

    elif game_type == 'q':
        print('Quitting')
    else:
        interactive_start()

    digs = [['   ' for _ in row] for row in play_area.values]
    print_board(play_area, digs)
    return play_area, digs


def interactive_dig(board, digs):
    print('Dig where?')
    loc_str = input('row, col: ')
    if loc_str == 'q':
        print('Quitting!')
        return None
    try:
        loc = (int(loc_str[0]) - 1, int(loc_str[3]) - 1)
        result = board.dig(loc)
    except Exception:
        interactive_dig(board, digs)

    digs[loc[0]][loc[1]] = 'dug'
    print_board(board, digs)
    print('Got a {}!'.format(result))

    if not board.game_over:
        interactive_dig(board, digs)
    elif board.game_over:
        print('Game over!')


def print_board(board, digs):
    print('   {}'.format(['  {}'.format(i + 1) for i in range(board.width)]))
    for j, row in enumerate(digs):
        print('{}: {}'.format(j + 1, row))
    print('Score: {}'.format(board.score))


@click.command()
def play():
    play_area, digs = interactive_start()
    interactive_dig(play_area, digs)

if __name__ == '__main__':
    play()
