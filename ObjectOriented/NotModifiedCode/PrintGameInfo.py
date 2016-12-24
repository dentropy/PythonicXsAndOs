class print_game_info:
    def draw_out_board(self):
        board = []
        for i in range(3):
            board.append([])
        for i in range(len(board)):
            board[i] = ["E","E","E"]
        return board
    def print_out_board(self, board):
        for i in board:
            print(i)
