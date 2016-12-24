from UserInput import UserInput
class Play(UserInput):
    def play_game(self):
        print("You are playing X's and O's")
        self.print_board()
        print("This is the board, E repersents an empty space")
        print("use the words top, bottom, left, right, and middle to place you piece")
        self.game_setup()
        self.cycle_through_turns()
game = Play()
game.play_game()
