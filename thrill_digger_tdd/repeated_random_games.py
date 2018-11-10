from thrill_digger_tdd.board import Board

def play(num_games):
    play_area = Board(5, 8)
    scores = []
    moveslist = []
    winlist = []
    for i in range(num_games):
        play_area.game_start()
        while not play_area.game_over:
            play_area.random_play()
        scores.append(play_area.score)
        moveslist.append(play_area.moves)
        winlist.append(play_area.game_won)
    return moveslist, scores, winlist
