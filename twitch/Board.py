from copy import deepcopy

MAX_COL = 4
MAX_ROW = 4

class Board:
    """ Models the board for our game"""

    def __init__(self):
        self.goal = [[" 1", " 2", " 3", " 4"], 
                     [" 5", " 6", " 7", " 8"], 
                     [" 9", "10", "11", "12"], 
                     ["13", "14", "15", "__"]]
        
        self.board = deepcopy(self.goal)

        self.empty_loc = [MAX_ROW - 1, MAX_COL - 1]

    def __repr__(self):
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                print(self.board[i][j], end=" ")
            print()

        # __repr__ MUST return something
        return ""