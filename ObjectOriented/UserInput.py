from GameEngine import GameEngine
class UserInput(GameEngine):
    def get_user_input(self):
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
