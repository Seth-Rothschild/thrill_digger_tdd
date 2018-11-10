import random

class Board():
    def __init__(self, height=5, width=8):
        self.height = height
        self.width = width
        self.size = self.height * self.width
        self.clear_board()

    def clear_board(self):
        self.bombs = 0
        self.score = 0
        self.game_over = False
        self.values = [[None for _ in range(self.width)]
                       for _ in range(self.height)]

    def fill_board(self):
        for i in range(self.height):
            for j in range(self.width):
                if not self.is_bomb((i, j)):
                    nbombs = self.find_adj_bombs((i, j))
                    self.set_value((i, j), self.color_code(nbombs))

    def game_start(self):
        self.clear_board()
        while self.bombs < 8:
            self.set_value(self.set_random(''), 'boom')
        while self.bombs < 16:
            self.set_value(self.set_random(''), 'rupoor')
        self.fill_board()

    def set_value(self, pos, value):
        row, column = pos
        lookup = self.values[row][column]
        if lookup in ['boom', 'rupoor']:
            self.bombs -= 1
        if value in ['boom', 'rupoor']:
            self.bombs += 1
        self.values[row][column] = value

    def is_bomb(self, pos):
        row, column = pos
        return self.values[row][column] in ['boom', 'rupoor']

    def find_adj_bombs(self, pos):
        row, column = pos
        add = [-1, 0, 1]
        lookup_rows = [row + i for i in add 
                       if row + i in range(self.height)]
        lookup_cols = [column + i for i in add 
                       if column + i in range(self.width)]
        adj_bombs = 0
        for i in lookup_rows:
            for j in lookup_cols:
                if self.is_bomb((i, j)) and ((i, j) != pos):
                    adj_bombs += 1
        return adj_bombs

    def color_code(self, num):
        rmap = {0: 'green',
                1: 'blue', 2: 'blue',
                3: 'red', 4: 'red',
                5: 'silver', 6: 'silver',
                7: 'gold', 8: 'gold'}
        return rmap[num]

    def score_code(self, color):
        smap = {'green': 1, 'blue': 5, 'red': 20,
                'silver': 100, 'gold': 300, 'boom': 0, 'rupoor': -10}
        return smap[color]

    def dig(self, pos):
        if self.game_over:
            return False

        row, column = pos
        result = self.values[row][column]
        self.set_value(pos, 'dug')
        if result == 'rupoor':
            self.bombs -= 1
        elif result == 'boom':
            self.bombs -= 1
            self.game_over = True

        if result != 'dug':
            self.score += self.score_code(result)
            self.score = max(self.score, 0)
            return result
        else:
            return None

    def get_random(self):
        row = random.randint(0, self.height - 1)
        col = random.randint(0, self.width - 1)
        return (row, col)

    def set_random(self, value):
        pos = self.get_random()
        self.set_value(pos, value)
        return pos

    def random_play(self):
        result = None
        while result is None:
            pos = self.get_random()
            result = self.dig(pos)
        return pos, result
