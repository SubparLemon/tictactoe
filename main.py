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

    def boardCheck(self):
        xwin = "XXX"
        owin = "OOO"
        # win check
        if (self.gameBoard[0] + self.gameBoard[1] + self.gameBoard[2]) == xwin or (
                self.gameBoard[3] + self.gameBoard[4] + self.gameBoard[5]) == xwin or (
                self.gameBoard[6] + self.gameBoard[7] + self.gameBoard[8]) == xwin or (
                self.gameBoard[0] + self.gameBoard[3] + self.gameBoard[6]) == xwin or (
                self.gameBoard[1] + self.gameBoard[4] + self.gameBoard[7]) == xwin or (
                self.gameBoard[2] + self.gameBoard[5] + self.gameBoard[8]) == xwin or (
                self.gameBoard[0] + self.gameBoard[4] + self.gameBoard[8]) == xwin or (
                self.gameBoard[2] + self.gameBoard[4] + self.gameBoard[6]) == xwin:
            return 2
        # lose check
        if (self.gameBoard[0] + self.gameBoard[1] + self.gameBoard[2]) == owin or (
                self.gameBoard[3] + self.gameBoard[4] + self.gameBoard[5]) == owin or (
                self.gameBoard[6] + self.gameBoard[7] + self.gameBoard[8]) == owin or (
                self.gameBoard[0] + self.gameBoard[3] + self.gameBoard[6]) == owin or (
                self.gameBoard[1] + self.gameBoard[4] + self.gameBoard[7]) == owin or (
                self.gameBoard[2] + self.gameBoard[5] + self.gameBoard[8]) == owin or (
                self.gameBoard[0] + self.gameBoard[4] + self.gameBoard[8]) == owin or (
                self.gameBoard[2] + self.gameBoard[4] + self.gameBoard[6]) == owin:
            return 3
        # draw check
        if self.gameBoard.count('-') == 0:
            return 1
        return 0

    def aiMove(self):
        moves = []
        if self.side == 1:
            aiMark = 'X'
        else:
            aiMark = 'O'
        score = 0
        if self.turn == 0:
            self.gameBoard[0] = aiMark
            self.turn += 1
        else:
            x

    def printBoard(self):
        for x in range(0, 8, 3):
            print(self.gameBoard[x] + self.gameBoard[x+1] + self.gameBoard[x+1])


board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
n = int(input("First(0) or Second(1)"))

playerF = True
if n == 0:
    tictactoe = tictactoe(board, 0)
    while True:
        tictactoe.playerMove()
        tictactoe.printBoard()
        tictactoe.aiMove()

elif n == 1:
    playerF = False
    tictactoe = tictactoe(board, 1)
    while True:
        tictactoe.aiMove()
        tictactoe.printBoard()
        tictactoe.playerMove()
