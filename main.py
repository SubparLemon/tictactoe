class tictactoe:
    turn = 0
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
                boards.append(nextMoveBoard(self.gameBoard, x, aiMark, True))
        maxVal = boards[0].pathValue()
        index = 0
        for x in boards:
            if x.pathValue() > maxVal:
                index += 1
                maxVal = x.pathValue()
        self.gameBoard[index] = aiMark
    def printBoard(self):
        for x in range(0, 8, 3):
            print(self.gameBoard[x] + self.gameBoard[x+1] + self.gameBoard[x+2])

class nextMoveBoard:
    def __init__(self, board, firstMoveIndex, side, turn):
        self.board = board
        self.firstMove = firstMoveIndex
        self.side = side
        self.turn = turn
        self.value = 0
        self.depth = 1
        self.done = False
        self.innerBoards = []
        board[self.firstMove] = side
        if tictactoe.boardCheck(self.board) == 0:
            if turn is True:
                for x in range(len(self.board)):
                    if self.board[x] == '-':
                        innerBoard = nextMoveBoard(self.board, x, self.side, False)
                        innerBoard.depth = self.depth + 1
                        self.innerBoards.append(innerBoard)
            elif turn is False:
                if side == 'X':
                    playerMark = 'O'
                else:
                    playerMark = 'X'
                for x in range(len(self.board)):
                    if self.board[x] == '-':
                        innerBoard = nextMoveBoard(self.board, x, playerMark, True)
                        innerBoard.depth = self.depth + 1
                        self.innerBoards.append(innerBoard)
        elif tictactoe.boardCheck(self.board) == 1:
            self.value = 0
        elif tictactoe.boardCheck(self.board) == 2:
            self.value = 1
        elif tictactoe.boardCheck(self.board) == 3:
            self.value = -1
    def pathValue(self):
        valueSum = self.value
        for inner_board in self.innerBoards:
            if inner_board.depth > 1:
                valueSum += inner_board.pathValue()
            else:
                valueSum += inner_board.value
            if len(inner_board.innerBoards) > 0:
                valueSum += inner_board.pathValue()
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
