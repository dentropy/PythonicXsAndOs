from UserInput import UserInput
class Test(UserInput):
    def test_Board(self):
        print("Testing Board")
        print(self.board)
        print(self.turn)
        print(self.state)
        self.print_board()
    def test_GameEngine(self):
        print("Testing GameEngine")
        print(self.board)
        print(self.turn)
        print(self.state)
        self.print_board()
        print("self.turn = " + self.turn)
        self.decide_who_goes_first()
        print("self.turn = " + self.turn)
    def test_UserInput(self):
        print("Testing GameEngine")
        self.game_setup()
        self.cycle_through_turns()
game = Test()
game.test_Board()
game.test_GameEngine()
game.test_UserInput()
