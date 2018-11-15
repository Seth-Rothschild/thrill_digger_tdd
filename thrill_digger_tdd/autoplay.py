from thrill_digger_tdd.board import Board


def gen_game(game_type):
    if game_type == 'beginner':
        game = Board(4, 5)
        game.game_start(4, 0)
    if game_type == 'intermediate':
        game = Board(5, 6)
        game.game_start(4, 4)
    if game_type == 'expert':
        game = Board(5, 8)
        game.game_start(8, 8)
    return game


def single_random_game(board='expert'):
    play_area = gen_game(board)
    while not play_area.game_over:
        play_area.random_play()
    return play_area


def single_simple_game(board='expert'):
    play_area = gen_game(board)
    move_count = 0
    if board == 'expert':
        start = [(3, 1), (3, 3), (3, 5), (1, 1), (1, 3), (1, 5)]

        while not play_area.game_over:
            if move_count < 6:
                play_area.dig(start[move_count])
            else:
                play_area.random_play()
            move_count += 1
    else:
        play_area = single_random_game(board)
    return play_area


def autoplay(num_games, strategy='random', board='expert'):
    gamelist = []
    for i in range(num_games):
        if strategy == 'random':
            gamelist.append(single_random_game(board))
        if strategy == 'simple':
            gamelist.append(single_simple_game(board))
    return gamelist
