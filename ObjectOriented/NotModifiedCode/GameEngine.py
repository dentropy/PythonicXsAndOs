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
