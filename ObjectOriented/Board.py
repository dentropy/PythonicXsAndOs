class Board:
    def __init__(self):
        self.board = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        self.turn = "unknown"
        self.state = "unknown"
    def print_board (self):
        for i in self.board:
            print(i)
