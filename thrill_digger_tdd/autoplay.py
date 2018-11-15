from thrill_digger_tdd.board import Board


def single_random_game():
    play_area = Board()
    play_area.game_start()
    while not play_area.game_over:
        play_area.random_play()
    return play_area


def single_simple_game():
    play_area = Board()
    play_area.game_start()
    move_count = 0
    start = [(3, 1), (3, 3), (3, 5), (1, 1), (1, 3), (1, 5)]
    while not play_area.game_over:
        if move_count < 6:
            play_area.dig(start[move_count])
        else:
            play_area.random_play()
        move_count += 1
    return play_area

def autoplay(num_games, strategy='random'):
    gamelist = []
    for i in range(num_games):
        if strategy == 'random':
            gamelist.append(single_random_game())
        if strategy == 'simple':
            gamelist.append(single_simple_game())
    return gamelist
        
