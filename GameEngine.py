class GameEngine(object):
    def __init__(self):
        #create a 2D array which repersents the board
        self.board = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        #the turn variable remembers who turn it is as a string "X" or "O"
        self.turn = "unknown"
        #the stste variable records state of game "win", "cats", or "play"
        self.state = "unknown"
    def print_board (self):
        for i in self.board:
            print(i)
    def decide_who_goes_first(self):
        #randomly decide who gies first
        import random
        if random.randrange(2) == 0:
            self.turn = "O"
        else:
            self.turn = "X"
        self.state = "play"
        return self.turn
    def check_winner(self):
        for i in ["X","O"]:
            for num in range(3):
                if i == self.board[num][0] and i ==  self.board[num][1] and i == self.board[num][2]:
                    self.state = i + " WINS"
                elif i == self.board[0][num] and i ==  self.board[1][num] and i == self.board[2][num]:
                    print(i, "WINS")
                    self.state = i + " WINS"
                elif i == self.board[0][0] and i ==  self.board[1][1] and i == self.board[2][2]:
                    self.state = i + " WINS"
                elif i == self.board[0][2] and i ==  self.board[1][1] and i == self.board[2][0]:
                    self.state = i + " WINS"
        return False
    def check_cats(self):
        count = 0
        for j in range(3):
            for k in range(3):
                if self.board[j][k] == "E":
                    count += 1
        if (count == 0):
            self.state = "cats"
    def do_turn(self, yPos, xPos):
        #remember down then accrsoss to navigate the board
        if (self.state == "play"):
            if self.board[yPos][xPos] == "E":
                self.board[yPos][xPos] = self.turn
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"
        else:
            return(False)
        self.check_cats()
        self.check_winner()
