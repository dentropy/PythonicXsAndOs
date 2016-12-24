from UserInput import UserInput
class Play(UserInput):
    def __init__(self):
        print(self.board)
    def play_game(self):
        print("You are playing X's and O's")
        print("This is the board, E repersents an empty space")
        print("use the words top, bottom, left, right, and middle to place you piece")
        self.cycle_through_turns(self.turn)
game = Play()
print("run object below")
game.play_game()
