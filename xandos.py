def drawOutBoard():
    board = []
    for i in range(3):
        board.append([])
    for i in range(len(board)):
        board[i] = ["E","E","E"]
    return board
def printOutBoard(board):
    for i in board:
        print i
def decideWhoGoesFirst():
    import random
    if random.randrange(2) == 0:
        print "O gets to go first"
        return "O"
    else:
        print "X gets to go first"
        return "X"
def playerTurn(board, player):
    if player =="O":
        otherPlayer = "X"
    else:
        otherPlayer = "O"
    print "It is ", player + "'s turn"
    placement = getUserInput()
    print placement
    for i in range(len(placement)):#start here I need to convert int to string
        placement[i] = int(placement[i])
    if board[placement[0]][placement[1]] == "E":
        board[placement[0]][placement[1]] = player
    return board
def boardFull(board):
    for i in board:
        for j in i:
            if i == "E" or j == "E":
                return False
    return True
def checkWinner(board):
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
def cycleThrouhTurns(board, player):
    while checkWinner(board)== False and boardFull(board) == False:
        playerTurn(board, player)
        printOutBoard(board)
        if player == "X":
            player = "O"
        else:
            player = "X"
def inputTestOne(placement):
    if len(placement) == 2:
        return True
def inputTestTwo(placement):
    for i in range(len(placement)):
        try:
            val = int(placement[i])
        except ValueError:
            return False
        placement[i] =int(placement[i])
    return placement
def inputTestThree(placement):
    for i in placement:
        if i < 0 or i > 2:
            return False
    return placement
def getUserInput():
    while True:
        placement = raw_input("Where do you want to go:")
        placement = placement.split(" ")#placement is where user wants to put pice:
        passTest = 0
        if inputTestOne(placement):
            passTest += 1
        if inputTestTwo(placement) != False:
            placement = inputTestTwo(placement)
            passTest += 1
        if inputTestThree(placement) != False:
            placement = inputTestThree(placement)
            passTest += 1
        if passTest == 3:
            break
        else:
            print "VALUE INPUT ERROR"
    return placement
def playGame():
    print "You are playing X's and O's"
    print "This is the board, E repersents an empty space"
    board = drawOutBoard()
    printOutBoard(board)
    print "Choose your position using numbers 0 to 2 separated by a space\nrow start at top then collum start at left"
    firstPlayer = decideWhoGoesFirst()
    cycleThrouhTurns(board, firstPlayer)
playGame()
'''
Possible winning combinations
[["E","E","E"],["X","X","X"],["E","E","E"]]
[["X","E","E"],["E","X","E"],["E","E","X"]]
[["X","E","E"],["X","E","E"],["X","E","E"]]
[["O","E","E"],["O","E","E"],["O","E","E"]]
'''
