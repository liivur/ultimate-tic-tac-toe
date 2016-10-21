import numpy as np

class Board:
    """docstring for Board."""
    def __init__(self, level = 0, parent = None):
        self.level = level
        self.winner = 0
        self.nextSector = None
        self.parent = parent
        if not self.level:
            self.board = np.zeros((3, 3), dtype=np.uint8)
        else:
            self.board = np.array([[Board(parent = self), Board(parent = self), Board(parent = self)],
                        [Board(parent = self), Board(parent = self), Board(parent = self)],
                        [Board(parent = self), Board(parent = self), Board(parent = self)]])

    def get_board(self):
        board = np.ones_like(self.board)
        for i in range(3):
            for j in range(3):
                try:
                    board[i][j] = np.copy(self.board[i][j].board)
                except AttributeError:
                    board[i][j] = self.board[i][j]
        return board

    def childWon(self, child, winner):
        board = self.board.tolist()
        for row in board:
            if child in row:
                self.board[board.index(row)][row.index(child)] = winner
        self.getWinner()

    def checkWin(self):
        if [1, 1, 1] in self.board.tolist() or \
        [1, 1, 1] in self.board.T.tolist() or \
        [1, 1, 1] == self.board.diagonal().tolist() or \
        [1, 1, 1] == np.rot90(self.board).diagonal().tolist():
            self.winner = 1
            return 1
        if [2, 2, 2] in self.board.tolist() or \
        [2, 2, 2] in self.board.T.tolist() or \
        [2, 2, 2] == self.board.diagonal().tolist() or \
        [2, 2, 2] == np.rot90(self.board).diagonal().tolist():
            self.winner = 2
            return 2
        if self.level == 0 and np.count_nonzero(self.board) == 9:
            self.winner = 1 if list(self.board.flatten()).count(1) > 4 else 2
            return 3
        if self.level == 1 and len(list(filter(lambda x: isinstance(x, int), self.board.flatten().tolist()))) == 9:
            self.winner = 1 if list(self.board.flatten()).count(1) > 4 else 2
            return 4
        return 0

    def getWinner(self):
        self.checkWin()
        if self.winner:
            if self.parent:
                self.parent.childWon(self, self.winner)
        return(self.winner)

    def setNextSector(self, sector):
        if not self.level:
            return
        if self.board[sector[0]][sector[1]] == 1 or\
        self.board[sector[0]][sector[1]] == 2:
            self.nextSector = None
        else:
            self.nextSector = sector

    def getNextSector(self):
        if not self.level:
            return -1
        return self.nextSector

    def play(self, team, place, board = None):
        """
         @arg team: 1 or 2. 1 is "X", 2 is "O"
         @arg place: Which position on the 3x3 TicTacToe board to play
         @arg board: Which 3x3 TicTacToe board to play

         @return: Tuple
            If self is the ultimate board and board argument is specified, returns (1, subroutine())
            If self is the ultimate board and board argument is not correct, returns (0, 0)
            If self is the ultimate board and board argument is not specified, returns (-1, -1)
            If self is the sub board and self has already been won, returns (-1, winner) #Though might not ever get here.
            If self is the sub board and the position being played to has already been played, returns (0, played_value)
            If self is the sub board and the position being played to is empty, returns (1, played_value)
        """
        if not self.level:
            if not self.winner:
                if not self.board[place[0]][place[1]]:
                    self.board[place[0]][place[1]] = team
                    self.getWinner()
                    if self.parent:
                        self.parent.setNextSector(place)
                    return (1, team)

                return (0, self.board[place[0]][place[1]])
            return (-1, self.winner)

        if board != None:
            if (self.nextSector == None) or self.nextSector == board:
                if (type(self.board[board[0]][board[1]]) == type(Board())):
                    return (1, self.board[board[0]][board[1]].play(team, place))
            return(0)
        return(-1)
