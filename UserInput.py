from GameEngine import GameEngine
class UserInput(GameEngine):
    def game_setup(self):
        input("choose who gets to go first then press enter: ")
        self.turn = self.decide_who_goes_first()
    def get_user_input(self):
        #what this does is check take raw sting and convert it to a spot on the board
        #whis also checks if the spots on the board is available therefore only
        #returns a valid location someone can put their piece aka not 'E'
        #THIS NEEDS TO BE FIXED TO FIX THE ERROR
        self.print_board()
        print("it is " + self.turn + "'s turn and turn number " + str(self.turn_number))
        while True:
            test_user_input = False
            while (test_user_input == False):
                print("Give a command dude")
                user_input =input("Where do you want to go: ")
                user_input = user_input.lower()
                user_input = user_input.split(" ")
                if (user_input[0] == "log"):
                    self.save_game()
                if (user_input[0] == "undo"):
                    self.undo()
                if (user_input[0] == "redo"):
                    self.redo()
                if(len(user_input) == 2):
                    count = 0
                    for i in ["middle","left","right","top","bottom"]:
                        if i == user_input[0]:
                            count += 1
                    for i in ["middle","left","right","top","bottom"]:
                        if i == user_input[1]:
                            count += 1
                    if count == 2:
                        test_user_input = True
            collum = "null"
            row = "null"
            if user_input[0] == "middle" or user_input[1] == "middle":
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
                if self.board[collum][row] == "E":
                    return [collum, row]
                    break
                else:
                    print("incorrect placement")
    def cycle_through_turns(self):
        while (self.state == "play"):
            place = self.get_user_input()
            self.do_turn(place[0], place[1])
        print("The game has completed")
        if (self.state == "cats"):
            self.print_board()
            print("sorry cat's game")
        else:
            self.print_board()
            print(self.state)
        print("If you would like to save this game type 'yes'")
        if (input("type yes: ").lower() == "yes"):
            self.save_game(input("Type name of file here: "))
