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

    def set_bomb(self, pos, btype='boom'):
        row, column = pos
        assert btype in ['boom', 'rupoor']
        lookup = self.values[row][column]
        if lookup not in ['boom', 'rupoor']:
            self.bombs += 1
        self.values[row][column] = btype

    def is_bomb(self, pos):
        row, column = pos
        return self.values[row][column] in ['boom', 'rupoor']

    def set_value(self, pos, value):
        self.values[pos[0]][pos[1]] = value

    def set_random(self, value):
        row = random.randint(0, self.height - 1)
        col = random.randint(0, self.width - 1)
        self.set_value((row, col), value)
        return (row, col)

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

    def fill_board(self):
        for i in range(self.height):
            for j in range(self.width):
                if not self.is_bomb((i, j)):
                    bombs = self.find_adj_bombs((i, j))
                    self.values[i][j] = self.color_code(bombs)

    def game_start(self):
        self.clear_board()
        while self.bombs < 8:
            self.set_bomb(self.set_random(''))
        while self.bombs < 16:
            self.set_bomb(self.set_random(''), btype='rupoor')
        self.fill_board()

    def dig(self, pos):
        if self.game_over:
            return False

        row, column = pos
        result = self.values[row][column]
        self.values[row][column] = 'dug'
        if result == 'rupoor':
            self.bombs -= 1
        elif result == 'boom':
            self.bombs -= 1
            self.game_over = True

        if result != 'dug':
            self.score += self.score_code(result)
            return result
        else:
            return None

    def score_code(self, color):
        smap = {'green': 1, 'blue': 5, 'red': 20,
                'silver': 100, 'gold': 300, 'boom': 0, 'rupoor': -10}
        return smap[color]

    def random_play(self):
        result = None
        while result is None:
            row = random.randint(0, self.height - 1)
            column = random.randint(0, self.width - 1)
            result = self.dig((row, column))
        return (row, column), result
