import random


board = ["-", "-", "-","-",
        "-", "-", "-","-",
        "-", "-", "-","-",
        "-","-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(" "+board[0] + " | " + board[1] + " | " + board[2]+" | "+board[3])
    print("----------------")
    print(" "+board[4] + " | " + board[5] + " | " + board[6]+" | "+board[7])
    print("---------------")
    print(" "+board[8] + " | " + board[9] + " | " + board[10]+" | "+board[11])
    print("---------------")
    print(" "+board[12] + " | " + board[13] + " | " + board[14]+" | "+board[15])


# take player input
def playerInput(board):
    inp = int(input("Select a spot 1-16: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] == board[3] and board[0] != "-":
        winner = board[0]
        print("horizontal")
        return True
    elif board[4] == board[5] == board[6] == board[7] and board[4] != "-":
        winner = board[4]
        print("horizontal")
        return True
    elif board[8] == board[9] == board[10] == board[11] and board[8] != "-":
        winner = board[8]
        print("horizontal")
        return True
    elif board[12] == board[13] == board[14] == board[15] and board[12] != "-":
        winner = board[12]
        print("horizontal")
        return True

def checkRow(board):
    global winner
    if board[0] == board[4] == board[8] == board[12] and board[0] != "-":
        winner = board[0]
        print("Row")
        return True
    elif board[1] == board[5] == board[9] == board[13] and board[1] != "-":
        winner = board[1]
        print("Row")
        return True
    elif board[2] == board[6] == board[10] == board[14] and board[2] != "-":
        winner = board[2]
        print("Row")
        return True
    elif board[3] == board[7] == board[11] == board[15] and board[3] != "-":
        winner = board[3]
        print("Row")
        return True


def checkDiag(board):
    global winner
    if board[0] == board[5] == board[10] == board[15] and board[0] != "-":
        winner = board[0]
        print("diag")
        return True
        print("diag")
    elif board[3] == board[6] == board[9] == board[12] and board[3] != "-":
        winner = board[2]
        print("diag")
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 15)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
