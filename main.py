import math


def printBoard(boardState, playerLetter, computerLetter):
    for i in range(3):
        row = boardState[i * 3:i * 3 + 3]
        rowString = []
        for val in row:
            if val == -1:
                rowString.append(playerLetter)
            elif val == 1:
                rowString.append(computerLetter)
            elif val == 0:
                rowString.append('-')
            else:
                rowString.append(str(val))
        print(" ".join(rowString))


def isFull(boardState):
    return EMPTYSLOT not in boardState


def getWinner(boardState):
    # Check rows
    for i in range(0, 9, 3):
        if boardState[i] == boardState[i + 1] == boardState[i + 2] and boardState[i] != EMPTYSLOT:
            return boardState[i]
    # Check columns
    for i in range(3):
        if boardState[i] == boardState[i + 3] == boardState[i + 6] and boardState[i] != EMPTYSLOT:
            return boardState[i]
    # Check diagonals
    if boardState[0] == boardState[4] == boardState[8] and boardState[0] != EMPTYSLOT:
        return boardState[0]
    if boardState[2] == boardState[4] == boardState[6] and boardState[2] != EMPTYSLOT:
        return boardState[2]
    # No winner
    return None


def getAvailableMoves(boardState):
    # returns indices of empty slots by iteratively checking if the boardstate is an empty slot
    return [i for i in range(len(boardState)) if boardState[i] == EMPTYSLOT]


def evaluate(boardState):
    winner = getWinner(boardState)
    if winner == COMPUTERPLAYER:
        return 1
    elif winner == HUMANPLAYER:
        return -1
    else:
        return 0

def getOtherPlayer(player):
    if player == -1:
        return 1
    else:
        return -1

def minimax(boardState, depth, player):
    # maximize
    if player == COMPUTERPLAYER:
        bestScore = -math.inf
    else:
        bestScore = math.inf
    best_move = None
    # minimize
    best_move = None
    for move in getAvailableMoves(boardState):
        newBoardState = boardState.copy()
        newBoardState[move] = player
        score = minimax(newBoardState, depth + 1, getOtherPlayer(player))
        if player == HUMANPLAYER and score < bestScore:
            bestScore = score
            best_move = move
        elif player == COMPUTERPLAYER and score > bestScore:
            bestScore = score
            best_move = move
    if best_move is None:
        return evaluate(boardState)
    if depth == 0:
        return best_move
    return bestScore


def main():
    # copys the board
    boardState = initialBoardState.copy()
    # input to determine who goes first
    currentPlayer = HUMANPLAYER if input("Do you want to go first? (y/n): ").lower() == "y" else COMPUTERPLAYER
    # sets variables for printing board
    playerLetter = 'X' if currentPlayer == HUMANPLAYER else 'O'
    computerLetter = '0' if playerLetter == 'X' else 'X'
    # repeats until board is full
    while not isFull(boardState):
        printBoard(boardState, playerLetter, computerLetter)
        # player turn
        if currentPlayer == HUMANPLAYER:
            move = int(input("Enter your move (1-9): "))-1
            if boardState[move] != EMPTYSLOT:
                print("Invalid move")
                continue
            boardState[move] = HUMANPLAYER
        # computer turn
        else:
            print("Computer is thinking...")
            move = minimax(boardState, 0, COMPUTERPLAYER)
            boardState[move] = COMPUTERPLAYER

        winner = getWinner(boardState)
        if winner is not None:
            printBoard(boardState, playerLetter, computerLetter)
            if winner == HUMANPLAYER:
                print("Cheater")
            elif winner == COMPUTERPLAYER:
                print("Idiot")
            else:
                print("It's a draw. Who could've guessed")
            return

        currentPlayer = -currentPlayer

    printBoard(boardState, playerLetter, computerLetter)
    print("It's a draw. Who could've guessed")

# sets constant values for different states of a board space
HUMANPLAYER = -1
COMPUTERPLAYER = 1
EMPTYSLOT = 0

# creates a list of 9 0 elements
initialBoardState = [0] * 9

# runs the main game loop
main()
