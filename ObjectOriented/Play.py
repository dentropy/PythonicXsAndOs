from UserInput import UserInput
class Play(UserInput):
    def __init__(self):
        print(self.board)
    def play_game(self):
        print("You are playing X's and O's")
        print("This is the board, E repersents an empty space")
        #self.print_board()
        #print(self.board)
        print("use the words top, bottom, left, right, and middle to place you piece")
        input("choose who gets to go first then press enter: ")
        firstPlayer = self.decide_who_goes_first()
        self.cycle_through_turns(board, firstPlayer)
game001 = Play()
print("run object below")
game001.play_game()
