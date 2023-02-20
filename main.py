class tictactoe:
    def __init__(self, gameBoard, side):
        self.gameBoard = gameBoard
        self.side = side

    def playerMove(self):
        loc = int(input("Where to place? (1,9): "))
        if self.side == 0:
            playerMark = 'X'
        else:
            playerMark = 'O'
        match loc:
            case 1:
                self.gameBoard[0] = playerMark
            case 2:
                self.gameBoard[1] = playerMark
            case 3:
                self.gameBoard[2] = playerMark
            case 4:
                self.gameBoard[3] = playerMark
            case 5:
                self.gameBoard[4] = playerMark
            case 6:
                self.gameBoard[5] = playerMark
            case 7:
                self.gameBoard[6] = playerMark
            case 8:
                self.gameBoard[7] = playerMark
            case 9:
                self.gameBoard[8] = playerMark

    def miniMax(self, board, side, minMax):
        if side == 1:
            aiMark = 'X'
            pMark = 'O'
        elif side == 0:
            aiMark = 'O'
            pMark = 'X'
        if minMax == 1:
            if boardCheck(board) == 1:
                return 0
            elif boardCheck(board) == 2 and side == 1:
                return 1
            elif boardCheck(board) == 3 and side == 0:
                return 1
            else:
                availableBoards = []
                for index in range(len(self.gameBoard)):
                    if self.gameBoard[index] == '-':
                        newBoard = self.gameBoard.copy()
                        newBoard[index] = aiMark
                        availableBoards.append(newBoard)
                for nextBoard in availableBoards:
                    self.miniMax(nextBoard, self.side, 0)
        elif minMax == 0:
            if boardCheck(board) == 1:
                return 0
            elif boardCheck(board) == 3 and side == 1:
                return -1
            elif boardCheck(board) == 2 and side == 0:
                return -1
            else:
                availableBoards = []
                for index in range(len(self.gameBoard)):
                    if self.gameBoard[index] == '-':
                        newBoard = self.gameBoard.copy()
                        newBoard[index] = aiMark
                        availableBoards.append(newBoard)
                for nextBoard in availableBoards:
                    self.miniMax(nextBoard, self.side, 1)

    def aiMove(self):
        if self.side == 1:
            aiMark = 'X'
        elif self.side == 0:
            aiMark = 'O'
        availableBoards = []
        for i in range(len(self.gameBoard)):
            if self.gameBoard[i] == '-':
                newBoard = self.gameBoard.copy()
                newBoard[i] = aiMark
                availableBoards.append(newBoard)
        # creates a new board for all legal possibilities
        scores = []
        for board in availableBoards:
            scores.append(self.miniMax(board, self.side, self.side))
        for i in range(len(scores)):
            if scores[i] == max(scores):
                self.gameBoard = availableBoards[i]


        #for x in range(len(self.gameBoard)):
        #    if self.gameBoard[x] == '-':
        #        minimax
                #boards.append(nextMoveBoard(self.gameBoard, x, aiMark, True, True))
       #if boardCheck(self.gameBoard) == 0:
       #    maxVal = boards[0].pathValue()
       #    print(boards[0].pathValue())
       #    for x in boards:
       #        if x.pathValue() > maxVal:
       #            maxVal = x.pathValue()
       #    for x in boards:
       #        if x.pathValue() == maxVal:
       #            self.gameBoard[x.firstMove] = aiMark
       #            break

    def printBoard(self):
        for x in range(0, 8, 3):
            print(self.gameBoard[x] + self.gameBoard[x+1] + self.gameBoard[x+2])
        print('\n')

#class nextMoveBoard:
#
#    def __init__(self, board, firstMoveIndex, side, turn, first):
#        self.board = board.copy()
#        self.firstMove = firstMoveIndex
#        self.side = side
#        self.turn = turn
    #    self.first = first
    #    self.aiValue = 0
    #    self.playerValue = 0
    #    self.depth = 1
    #    self.innerBoards = []
    #    self.playerInnerBoards = []
    #    self.board[self.firstMove] = side
    #    if boardCheck(self.board) == 0:
    #        if turn is True:
    #            for nextMove in range(len(self.board)):
    #                if self.board[nextMove] == '-':
    #                    innerBoard = nextMoveBoard(self.board, nextMove, self.side, False, False)
    #                    innerBoard.depth = self.depth + 1
    #                    self.innerBoards.append(innerBoard)
    #        elif turn is False:
    #            if side == 'X':
    #                playerMark = 'O'
    #            else:
    #                playerMark = 'X'
    #            for nextMove in range(len(self.board)):
    #                if self.board[nextMove] == '-':
    #                    innerBoard = nextMoveBoard(self.board, nextMove, playerMark, True, False)
    #                    innerBoard.depth = self.depth + 1
    #                    self.innerBoards.append(innerBoard)
    #    else:
    #        if self.side == 'O':
    #            if boardCheck(self.board) == 1:
    #                self.aiValue = 0
    #            elif boardCheck(self.board) == 3:
    #                self.aiValue = 1
    #            elif boardCheck(self.board) == 2:
    #                self.aiValue = -1
    #        if self.side == 'X':
    #            if boardCheck(self.board) == 1:
    #                self.aiValue = 0
    #            elif boardCheck(self.board) == 2:
    #                self.aiValue = 1
    #            elif boardCheck(self.board) == 3:
    #                self.aiValue = -1

    #def pathValue(self):
    #    valueSum = self.aiValue
    #    for inner_board in self.innerBoards:
    #        inner_board_value = inner_board.pathValue()
    #        if inner_board_value != 0:
    #            valueSum += inner_board_value
    #    return valueSum
def boardCheck(board):
    xwin = "XXX"
    owin = "OOO"
    # x win
    if (board[0] + board[1] + board[2]) == xwin or (
            board[3] + board[4] + board[5]) == xwin or (
            board[6] + board[7] + board[8]) == xwin or (
            board[0] + board[3] + board[6]) == xwin or (
            board[1] + board[4] + board[7]) == xwin or (
            board[2] + board[5] + board[8]) == xwin or (
            board[0] + board[4] + board[8]) == xwin or (
            board[2] + board[4] + board[6]) == xwin:
        return 2
    # o win
    if (board[0] + board[1] + board[2]) == owin or (
            board[3] + board[4] + board[5]) == owin or (
            board[6] + board[7] + board[8]) == owin or (
            board[0] + board[3] + board[6]) == owin or (
            board[1] + board[4] + board[7]) == owin or (
            board[2] + board[5] + board[8]) == owin or (
            board[0] + board[4] + board[8]) == owin or (
            board[2] + board[4] + board[6]) == owin:
        return 3
    # draw check
    if board.count('-') == 0:
        return 1
    return 0

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
userInput = int(input("First(0) or Second(1) "))

playerF = True
if userInput == 0:
    tictactoe = tictactoe(board, 0)
    while boardCheck(tictactoe.gameBoard) == 0:
        tictactoe.playerMove()
        tictactoe.printBoard()
        tictactoe.aiMove()
        tictactoe.printBoard()

elif userInput == 1:
    playerF = False
    tictactoe = tictactoe(board, 1)
    while boardCheck(tictactoe.gameBoard) == 0:
        tictactoe.aiMove()
        tictactoe.printBoard()
        tictactoe.playerMove()
        tictactoe.printBoard()
