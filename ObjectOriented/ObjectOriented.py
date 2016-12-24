class user_input:
    def get_user_input(self, board):
        while True:
            test_user_input = False
            while (test_user_input == False):
                print("Give a command dude")
                user_input =input("Where do you want to go:")
                user_input = user_input.lower()
                user_input = user_input.split(" ")
                if(len(user_input) == 2):
                    test_user_input = True
            collum = "null"
            row = "null"
            if len(user_input) != 2:
                print("Use only one space in your answer")
            elif user_input[0] == "middle" or user_input[1] == "middle":
                    collum = 1
                    row = 1
            if user_input[0] == "top" or user_input[1] == "top":
                collum = 0
            elif user_input[0] == "bottom" or user_input[1] == "bottom":
                collum = 2
            if user_input[0] == "left" or user_input[1] == "left":
                row = 0
            elif user_input[0] == "right" or user_input[1] == "right":
                row = 2
            if type(collum) == int or type(row) == int:
                if board[collum][row] == "E":
                    return [collum, row]
                    break
                else:
                    print("incorrect placement")
    def cycle_through_turns(self, board, player):
        while check_winner(board)== False and board_full(board) == False:
            player_turn(board, player)
            print_out_board(board)
            if player == "X":
                player = "O"
            else:
                player = "X"
class game_engine:
    def player_turn(self, board, player):
        if player =="O":
            otherPlayer = "X"
        else:
            otherPlayer = "O"
        print("It is ", player + "'s turn")
        placement = get_user_input(board)
        print(placement)
        for i in range(len(placement)):#start here I need to convert int to string
            placement[i] = int(placement[i])
        if board[placement[0]][placement[1]] == "E":
            board[placement[0]][placement[1]] = player
        return board
    def check_winner(self, board):
        for i in ["X","O"]:
            for num in range(3):
                if i == board[num][0] and i ==  board[num][1] and i == board[num][2]:
                    print(i, "WINS")
                    return True
                elif i == board[0][num] and i ==  board[1][num] and i == board[2][num]:
                    print(i, "WINS")
                    return True
                elif i == board[0][0] and i ==  board[1][1] and i == board[2][2]:
                    print(i, "WINS")
                    return True
                elif i == board[0][2] and i ==  board[1][1] and i == board[2][0]:
                    print(i, "WINS")
                    return True
        return False
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
def play_game():
    print("You are playing X's and O's")
    print("This is the board, E repersents an empty space")
    board = draw_out_board()
    print_out_board(board)
    print("use the words top, bottom, left, right, and middle to place you piece")
    input("choose who gets to go first then press enter: ")
    firstPlayer = decide_who_goes_first()
    cycle_through_turns(board, firstPlayer)
play_game()
