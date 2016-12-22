class XsAndOsSetUp(object):
	def draw_out_board(self):
	    board = []
	    for i in range(3):
		board.append([])
	    for i in range(len(board)):
		board[i] = ["E","E","E"]
	    return board
	def print_out_board(self, board):
	    for i in board:
			print i
	def decide_who_goes_first(self):
	    import random
	    if random.randrange(2) == 0:
			print "O gets to go first"
			return "O"
	    else:
			print "X gets to go first"
			return "X"
	def player_turn(self, board, player):
	    if player =="O":
	        otherPlayer = "X"
	    else:
	        otherPlayer = "O"
	    print "It is ", player + "'s turn"
	    placement = self.get_user_input(board)
	    print placement
	    for i in range(len(placement)):#start here I need to convert int to string
	        placement[i] = int(placement[i])
	    if board[placement[0]][placement[1]] == "E":
	        board[placement[0]][placement[1]] = player
	    return board
	def get_user_input(self, board):
	    while True:
	        user_input =raw_input("Where do you want to go:")
	        while (user_input == ""):
	            print "Give a command dude"
	            user_input =raw_input("Where do you want to go:")
	        user_input = user_input.lower()
	        user_input = user_input.split(" ")
	        collum = "null"
	        row = "null"
	        if len(user_input) == 2:
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
		            if board[collum][row] == "E":
		                return [collum, row]
		                break
            else:
                print "incorrect placement"
	def board_full(self, board):
	    for i in board:
		for j in i:
		    if i == "E" or j == "E":
		        return False
	    return True
	def check_winner(self, board):
	    for i in ["X","O"]:
		for num in range(3):
		    if i == board[num][0] and i ==  board[num][1] and i == board[num][2]:
		        print i, "WINS"
		        return True
		    elif i == board[0][num] and i ==  board[1][num] and i == board[2][num]:
		        print i, "WINS"
		        return True
		    elif i == board[0][0] and i ==  board[1][1] and i == board[2][2]:
		        print i, "WINS"
		        return True
		    elif i == board[0][2] and i ==  board[1][1] and i == board[2][0]:
		        print i, "WINS"
		        return True
	    return False
	def cycle_through_turns(self, board, player):
	    while self.check_winner(board)== False and self.board_full(board) == False:
		self.player_turn(board, player)
		self.print_out_board(board)
		if player == "X":
		    player = "O"
		else:
		    player = "X"
	def input_test_one(self, placement):
	    if len(placement) == 2:
		return True
	def input_test_two(self, placement):
	    for i in range(len(placement)):
		try:
		    val = int(placement[i])
		except ValueError:
		    return False
		placement[i] =int(placement[i])
	    return placement
	def input_test_three(self, placement):
	    for i in placement:
		if i < 0 or i > 2:
		    return False
	    return placement
#class PlayXsAndOs(XsAndOsSetUp):
#    print "You are playing X's and O's"
#    print "This is the board, E repersents an empty space"
#    board = draw_out_board()
#    print_out_board(self.board)
#    print "use the words top, bottom, left, right, and middle to place you piece"
#    raw_input("choose who gets to go first then press enter")
#    self.firstPlayer = decide_who_goes_first()
#    cycle_through_turns(board, firstPlayer)
#PlayXsAndOs()

PlayGame = XsAndOsSetUp()
print "You are playing X's and O's"
print "This is the board, E repersents an empty space"
board = PlayGame.draw_out_board()
print board
PlayGame.print_out_board(board)
print "use the words top, bottom, left, right, and middle to place you piece"
raw_input("choose who is X and who is O and press enter: ")
firstPlayer = PlayGame.decide_who_goes_first()
PlayGame.cycle_through_turns(board, firstPlayer)
