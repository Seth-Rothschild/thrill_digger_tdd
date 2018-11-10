import random

class Board():
    def __init__(self, height=5, width=8):
        self.height = height
        self.width = width
        self.size = self.height * self.width
        self.bombs = 0
        self.values = [[None for _ in range(self.width)]
                       for _ in range(self.height)]

    def set_bomb(self, pos):
        row, column = pos
        if self.values[row][column] != 'boom':
            self.values[row][column] = 'boom'
            self.bombs += 1

    def is_bomb(self, pos):
        row, column = pos
        return self.values[row][column] == 'boom'

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
        while self.bombs < 16:
            self.set_bomb(self.set_random(''))
        self.fill_board()
