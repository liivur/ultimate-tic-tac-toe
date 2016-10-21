import numpy as np

class BadPlayer:
    """docstring for BadPlayer."""
    def __init__(self, team):
        self.team = team

    def play(self, board, compulsory = None):
        """
         @arg board: 4-D numpy array of the current game state
         @arg compulsory: 2D Tuple, indicating wheere the next play should be made.
            If None, then there is no compulsory area.
         @return: 2-D tuple - ((board_coordinates), (box_coordinates))
        """

        # print(board)
        # print(compulsory)
        # res = []
        # while(len(res) != 4):
        #     res = [int(i)%3 for i in input().split(" ")]
        print('bad player compulsory', compulsory)
        res = self.getMove(board, compulsory)

        print((res[:2], res[2:]))
        return (res[:2], res[2:])

    def getMove(self, board, compulsory = None):
        # print(board)
        res, subBoard = self.getSubBoard(board, compulsory)

        for rowIndex in range(len(subBoard)):
            for columnIndex in range(len(subBoard[rowIndex])):
                if subBoard[rowIndex][columnIndex] == 0:
                    res.append(rowIndex)
                    res.append(columnIndex)
                    return res

    def getSubBoard(self, board, compulsory = None):
        res = []
        if compulsory == None:
            res.append(0)
            res.append(0)
        else:
            for i in compulsory:
                res.append(i)

        subBoard = board[res[0]][res[1]]
        if (isinstance(subBoard, np.ndarray)):
            return (res, subBoard)
        for i in range(3):
            for j in range(3):
                subBoard = board[i][j]
                if (isinstance(subBoard, np.ndarray)):
                    return ([i, j], subBoard)

        return ([], [])
