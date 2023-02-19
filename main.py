class tictactoe:
    def __init__(self, gameBoard, side):
        self.gameBoard = gameBoard
        self.side = side

    def playerMove(self):
        loc = int(input("Where to place? (0,8): "))
        if self.side == 0:
            playerMark = 'X'
        else:
            playerMark = 'O'
        match loc:
            case 0:
                self.gameBoard[0] = playerMark
            case 1:
                self.gameBoard[1] = playerMark
            case 2:
                self.gameBoard[2] = playerMark
            case 3:
                self.gameBoard[3] = playerMark
            case 4:
                self.gameBoard[4] = playerMark
            case 5:
                self.gameBoard[5] = playerMark
            case 6:
                self.gameBoard[6] = playerMark
            case 7:
                self.gameBoard[7] = playerMark
            case 8:
                self.gameBoard[8] = playerMark

    def boardCheck(self, gameBoard):
        xwin = "XXX"
        owin = "OOO"
        # win check
        if (gameBoard[0] + gameBoard[1] + gameBoard[2]) == xwin or (
                gameBoard[3] + gameBoard[4] + gameBoard[5]) == xwin or (
                gameBoard[6] + gameBoard[7] + gameBoard[8]) == xwin or (
                gameBoard[0] + gameBoard[3] + gameBoard[6]) == xwin or (
                gameBoard[1] + gameBoard[4] + gameBoard[7]) == xwin or (
                gameBoard[2] + gameBoard[5] + gameBoard[8]) == xwin or (
                gameBoard[0] + gameBoard[4] + gameBoard[8]) == xwin or (
                gameBoard[2] + gameBoard[4] + gameBoard[6]) == xwin:
            return 2
        # lose check
        if (gameBoard[0] + gameBoard[1] + gameBoard[2]) == owin or (
                gameBoard[3] + gameBoard[4] + gameBoard[5]) == owin or (
                gameBoard[6] + gameBoard[7] + gameBoard[8]) == owin or (
                gameBoard[0] + gameBoard[3] + gameBoard[6]) == owin or (
                gameBoard[1] + gameBoard[4] + gameBoard[7]) == owin or (
                gameBoard[2] + gameBoard[5] + gameBoard[8]) == owin or (
                gameBoard[0] + gameBoard[4] + gameBoard[8]) == owin or (
                gameBoard[2] + gameBoard[4] + gameBoard[6]) == owin:
            return 3
        # draw check
        if gameBoard.count('-') == 0:
            return 1
        return 0

    def aiMove(self):
        boards = []
        if self.side == 1:
            aiMark = 'X'
        else:
            aiMark = 'O'
        for x in range(len(self.gameBoard)):
            if self.gameBoard[x] == '-':
                boards.append(nextMoveBoard(self.gameBoard, x, aiMark, True, True))
        maxVal = boards[0].pathValue()
        for x in boards:
            if x.pathValue() > maxVal:
                maxVal = x.pathValue()
        for x in boards:
            if x.pathValue() == maxVal:
                self.gameBoard[x.firstMove] = aiMark


    def printBoard(self):
        for x in range(0, 8, 3):
            print(self.gameBoard[x] + self.gameBoard[x+1] + self.gameBoard[x+2])

class nextMoveBoard:
    def __init__(self, board, firstMoveIndex, side, turn, first):
        self.board = board.copy()
        self.firstMove = firstMoveIndex
        self.side = side
        self.turn = turn
        self.value = 0
        self.depth = 1
        self.done = False
        self.innerBoards = []
        self.firstBoard = first
        self.board[self.firstMove] = side
        if tictactoe.boardCheck(self.board) == 0:
            print('continue')
            if turn is True:
                for x in range(len(self.board)):
                    if self.board[x] == '-':
                        innerBoard = nextMoveBoard(self.board, x, self.side, False, False)
                        innerBoard.depth = self.depth + 1
                        print(innerBoard.board)
                        self.innerBoards.append(innerBoard)
            elif turn is False:
                if side == 'X':
                    playerMark = 'O'
                else:
                    playerMark = 'X'
                for x in range(len(self.board)):
                    if self.board[x] == '-':
                        innerBoard = nextMoveBoard(self.board, x, playerMark, True, False)
                        innerBoard.depth = self.depth + 1
                        print(innerBoard.board)
                        self.innerBoards.append(innerBoard)
        elif tictactoe.boardCheck(self.board) == 1:
            self.value = 0
        elif tictactoe.boardCheck(self.board) == 3:
            self.value = 1
        elif tictactoe.boardCheck(self.board) == 2:
            self.value = -1
    def pathValue(self):
        valueSum = self.value
        for inner_board in self.innerBoards:
            inner_board_value = inner_board.pathValue()
            if inner_board_value != 0:
                valueSum += inner_board_value
        return valueSum


board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
n = int(input("First(0) or Second(1) "))

playerF = True
if n == 0:
    tictactoe = tictactoe(board, 0)
    while tictactoe.boardCheck(tictactoe.gameBoard) == 0:
        tictactoe.playerMove()
        tictactoe.printBoard()
        tictactoe.aiMove()
        tictactoe.printBoard()

elif n == 1:
    playerF = False
    tictactoe = tictactoe(board, 1)
    while tictactoe.boardCheck(tictactoe.gameBoard) == 0:
        tictactoe.aiMove()
        tictactoe.printBoard()
        tictactoe.playerMove()
        tictactoe.printBoard()
