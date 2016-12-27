from GameEngine import GameEngine
class UserInput(GameEngine):
    def game_setup(self):
        print("if you would like to import a save game type 'import' below'")
        if (input("choose who gets to go first then press enter: ") =="import"):
            while (True):
                print("type 'play' if you just want to play")
                file_name = input("imput the name of the file here: ")
                if (file_name == "play"):
                    break
                import json
                import os.path
                if(os.path.exists(file_name + '.json')):
                    f = open(file_name + '.json', 'r')
                    self.future_moves = json.loads(f.read())
                    f.close()
                    for i in range(len(self.future_moves)):
                        self.redo()
                        print(i)
                    break
                else:
                    print("File does not seem to exist please try again")
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
                    self.save_game(input("What do you want to call your save: "))
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
    def play_game(self):
        print("You are playing X's and O's")
        self.print_board()
        print("This is the board, E repersents an empty space")
        print("use the words top, bottom, left, right, and middle to place you piece")
        self.game_setup()
        self.cycle_through_turns()
