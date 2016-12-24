from Board import Board
class GameEngine(Board):
    def __init__(self):
        import random
        if random.randrange(2) == 0:
            print("O gets to go first")
            self.turn = "O"
        else:
            print("X gets to go first")
            self.turn = "X"
    def check_winner(self):
        for i in ["X","O"]:
            for num in range(3):
                if i == board[num][0] and i ==  board[num][1] and i == board[num][2]:
                    #print(i, "WINS")
                    self.state = i + " WINS"
                elif i == board[0][num] and i ==  board[1][num] and i == board[2][num]:
                    print(i, "WINS")
                    self.state = i + " WINS"
                elif i == board[0][0] and i ==  board[1][1] and i == board[2][2]:
                    #print(i, "WINS")
                    self.state = i + " WINS"
                elif i == board[0][2] and i ==  board[1][1] and i == board[2][0]:
                    #print(i, "WINS")
                    self.state = i + " WINS"
        print(self.game_state)
        return False
    def check_cats(self):
        count = 0
        for j in range(3):
            for k in range(3):
                count += 1
        if (count == 0):
            self.state = "cats"
    def do_turn(self, player, yPos, xpos):#remember down then accrsoss
        self.check_cats()
        self.check_winner()
        if (self.state == "X" or "O"):
            print("It is " + self.turn + "'s turn")
            if self.board[yPos][xPos] == "E":
                self.board[yPos][xPos] = player
        else:
            return("GAME OVER, please reset")
