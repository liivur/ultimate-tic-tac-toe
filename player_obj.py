import numpy as np
from enum import Enum
from math import inf

class Scenario(Enum): # Kasutame Enum klassi, et eristada hinnanguid
    best_case = 5 # Võit
    next_best = 4 # Varsti võit
    mehh_case = 3 # Ei midagi erilist
    stal_case = 2 # Viik
    next_wrst = 1 # Varsti kaotus
    wrst_case = 0 # Kaotus
    
def check(thing, board): # Funktsioon tagastab boolean väärtuse, sellest kas "thing" esineb numpy massiivis "board"
    return(thing in np.sort(board).tolist() or \
           thing in np.sort(board.T).tolist() or \
           thing == np.sort(board.diagonal()).tolist() or \
           thing == np.sort(np.rot90(board).diagonal()).tolist())

def hinnang(team, board, depth):
    one, two = check([1, 1, 1], board), check([2, 2, 2], board)
    if one and two:
        return None

    if team == 1:
        if two:
            return -9000-depth
        if one:
            return 9000+depth

    if team == 2:
        if one:
            return -9000-depth
        if two:
            return 9000+depth

    value = 0
    opponent = 3-team

    checkList = np.sort(board).tolist()
    checkList.extend(np.sort(board.T).tolist())
    # checkList.append(np.sort(board.diagonal()).tolist())
    # checkList.append(np.sort(np.rot90(board).diagonal()).tolist())

    for i in checkList:
        if i == [0, team, team]:
            value += 5
        elif i == [0, opponent, opponent]:
            value -= 5

        if i == [0, 0, team]:
            value += 2
        elif i == [0, 0, opponent]:
            value -= 2

    return value
        
    #otsi võitu/kaotust.
    # one, two = check([1, 1, 1], board), check([2, 2, 2], board)
    # if one and two:
    #     return None

    # if team == 1:
    #     if two:
    #         return -depth
    #     if one:
    #         return depth

    # if team == 2:
    #     if one:
    #         return -depth
    #     if two:
    #         return depth
    
    # return 0


# def hinnang(team, board):
#     case = Scenario.mehh_case

#     #otsi võitu/kaotust.
#     if check([1, 1, 1], board):
#         if team == 1:
#             case = Scenario.best_case
#         else:
#             case = Scenario.wrst_case
#         return case
#     if check([2, 2, 2], board):
#         if team == 2:
#             case = Scenario.best_case
#         else:
#             case = Scenario.wrst_case
#         return case

#     #otsi peatset võitu/kaotust
#     if check([0, 1, 1], board):
#         if team == 1:
#             case = Scenario.next_best
#         else:
#             case = Scenario.next_wrst
#     if check([0, 2, 2], board):
#         if team == 2:
#             if case != Scenario.mehh_case:
#                 case = Scenario.stal_case
#             else:
#                 case = Scenario.next_best
#         else:
#             if case != Scenario.mehh_case:
#                 case = Scenario.stal_case
#             else:
#                 case = Scenario.next_wrst

#     return case

def compile_possibilities(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j]:
                yield (i, j)

def make_move(team, board, move):
    i, j = move
    if not board[i][j]:
        board[i][j] = team
    return board

# def maximiser(team, depth, board, alpha = Scenario.wrst_case, beta = Scenario.best_case):
#     if depth == 0:
#         return (None, None)
#     h = hinnang(team, board)
#     if h == Scenario.best_case or h == Scenario.wrst_case or np.count_nonzero(board) == 9:
#         return (h, None)
    
#     val = alpha
#     best = None
#     for pos in compile_possibilities(board):
#         board[pos[0]][pos[1]] = team
#         scen, p = minimiser(team, depth-1, board, val, beta)
#         board[pos[0]][pos[1]] = 0
#         if scen == None:
#             continue
#         if scen.value >= val.value:
#             val = scen
#             best = pos
#         if val.value > beta.value:
#             break
            
#     return (val, best)

# def minimiser(team, depth, board, alpha = Scenario.wrst_case, beta = Scenario.best_case):
#     if depth == 0:
#         return (None, None)
#     h = hinnang(team, board)
#     if h == Scenario.best_case or h == Scenario.wrst_case or np.count_nonzero(board) == 9:
#         return (h, None)
    
#     val = beta
#     best = None
#     for pos in compile_possibilities(board):
#         board[pos[0]][pos[1]] = 3 - team
#         scen, p = maximiser(team, depth-1, board, alpha, val)
#         board[pos[0]][pos[1]] = 0
#         if scen == None:
#             continue
#         if scen.value <= val.value:
#             val = scen
#             best = pos
#         if val.value < alpha.value:
#             break
            
#     return (val, best)

# def maximiser(team, depth, board, alpha = -10000, beta = 10000):
#     if depth == 0:
#         return (None, None)
#     h = hinnang(team, board, depth)
#     if h == None:
#         return (None, None)
#     if np.count_nonzero(board) == 9:
#         return (h, None)
    
#     val = alpha
#     best = None
#     for pos in compile_possibilities(board):
#         if not best:
#             best = pos
#         board[pos[0]][pos[1]] = team
#         scen, p = minimiser(team, depth-1, board, val, beta)
#         board[pos[0]][pos[1]] = 0
#         if scen == None:
#             continue
#         if scen >= val:
#             val = scen
#             best = pos
#         if val > beta:
#             break
#     return (val, best)

# def minimiser(team, depth, board, alpha = -10000, beta = 10000):
#     if depth == 0:
#         return (None, None)
#     h = hinnang(team, board, depth)
#     if h == None:
#         return (None, None)
#     if np.count_nonzero(board) == 9:
#         return (h, None)
    
#     val = beta
#     best = None
#     for pos in compile_possibilities(board):
#         if not best:
#             best = pos
#         board[pos[0]][pos[1]] = 3 - team
#         scen, p = maximiser(team, depth-1, board, alpha, val)
#         board[pos[0]][pos[1]] = 0
#         if scen == None:
#             continue
#         if scen <= val:
#             val = scen
#             best = pos
#         if val < alpha:
#             break
#     return (val, best)



class Player:
    """docstring for Player."""
    def __init__(self, team):
        self.team = team
        self.hinnangud = np.array([[0,0,0],[0,0,0],[0,0,0]])
        self.kolmReas = [
            [ 0, 1, 2 ],
            [ 3, 4, 5 ],
            [ 6, 7, 8 ],
            [ 0, 3, 6 ],
            [ 1, 4, 7 ],
            [ 2, 5, 8 ],
            [ 0, 4, 8 ],
            [ 2, 4, 6 ]
        ];
        self.vaartused = [
            [     0,   -10,  -100, -1000 ],
            [    10,     0,     0,     0 ],
            [   100,     0,     0,     0 ],
            [  1000,     0,     0,     0 ]
        ];

    def compile_possibilities(self, board, compulsory = None):
        # data = []
        if (compulsory == None):
            for i in range(3):
                for j in range(3):
                    if isinstance(board[i][j], np.ndarray):
                        # yield self.compile_possibilities(board, (i, j))
                        subBoard = board[i][j]
                        for k in range(3):
                            for l in range(3):
                                # data.append(((i, j), (k, l)))
                                if not subBoard[i][j]:
                                    yield ((i, j), (k, l))

        else:
            subBoard = board[compulsory[0]][compulsory[1]]
            for i in range(3):
                for j in range(3):
                    if not subBoard[i][j]:
                        # data.append((compulsory, (i, j)))
                        yield (compulsory, (i, j))

        # return data

    def hinnang(self, board, depth = 0):
        hinnang = 0
        myBoard = np.array([[0,0,0],[0,0,0],[0,0,0]])
        for i in range(len(board)):
            for j in range(len(board[i])):
                if isinstance(board[i][j], np.ndarray):
                    subBoard = board[i][j]
                    if np.count_nonzero(subBoard) == 9:
                        countTeam = np.count_nonzero(subBoard == self.team)
                        if countTeam > 4:
                            myBoard[i][j] = 1
                        else:
                            myBoard[i][j] = 0
                    else:
                        hinnang += self.subHinnang(subBoard)
                else:
                    myBoard[i][j] = board[i][j]

        hinnang += self.subHinnang(myBoard)*10
        return hinnang

    def subHinnang(self, board):
        opponent = 3 - self.team;
        t = 0
        tempBoard = board.flatten()
        if np.count_nonzero(tempBoard) < 1:
            return 0

        for i in range(8):
            players = others = 0
            for j in range(3):
                piece = tempBoard[self.kolmReas[i][j]]
                if piece == self.team:
                    players += 1
                elif piece == opponent:
                    others += 1
            t += self.vaartused[players][others]

        totalPlayers = np.count_nonzero(tempBoard == self.team)
        totalOthers = np.count_nonzero(tempBoard == opponent)
        difference = totalPlayers - totalOthers
        if abs(difference) > 1:
            t += 10*difference

        return t

    def maximiser(self, depth, board, compulsory, alpha = -inf, beta = inf):
        h = self.hinnang(board, depth)
        if depth == 0:
            return (h, None)
        val = alpha
        best = None
        debug = []
        # for pos in self.compile_possibilities(board, compulsory):
        #     debug.append(pos)
        # print('debug', compulsory, debug)
        # print(board)
        # for pos in debug:
        for pos in self.compile_possibilities(board, compulsory):
            if board[pos[0][0]][pos[0][1]][pos[1][0]][pos[1][1]] != 0:
                continue
            if not best:
                best = pos
            subBoard = board[pos[0][0]][pos[0][1]]
            if subBoard[pos[1][0]][pos[1][1]] != 0:
                print('given not open position', board, pos)
                exit()
            subBoard[pos[1][0]][pos[1][1]] = self.team
            scen, p = self.minimiser(depth-1, board, pos[0])
            # scen, p = self.minimiser(depth-1, board, pos[0], val, beta)
            subBoard[pos[1][0]][pos[1][1]] = 0
            if scen >= val:
                val = scen
                best = pos
            # if val > beta:
            #     break
        # print('maxi', val, best)
        return (val, best)

    def minimiser(self, depth, board, compulsory, alpha = -inf, beta = inf):
        h = self.hinnang(board, depth)
        if depth == 0:
            return (h, None)
        
        val = beta
        best = None
        for pos in self.compile_possibilities(board, compulsory):
            if not best:
                best = pos
            subBoard = board[pos[0][0]][pos[0][1]]
            subBoard[pos[1][0]][pos[1][1]] = 3 - self.team
            scen, p = self.maximiser(depth-1, board, pos[0])
            # scen, p = self.maximiser(depth-1, board, pos[0], alpha, val)
            subBoard[pos[1][0]][pos[1][1]] = 0
            if scen <= val:
                val = scen
                best = pos
            # if val < alpha:
            #     break
        # print('mini', val, best)
        return (val, best)

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
        # print(list(suur_compile_possibilities(board, compulsory)))
        # print('player compulsory', compulsory)
        # res = self.getMove(board, compulsory)
        val, res = self.maximiser(4, board, compulsory)
        print('player play', compulsory, val, res)
        # print('player move', res[0], res[1])
        # print(board)
        return (res[0], res[1])

    def getMove(self, board, compulsory = None):
        # print(board)
        res, subBoard = self.getSubBoard(board, compulsory)

        value, move = maximiser(self.team, 10, subBoard)
        if move:
            res.append(move[0])
            res.append(move[1])
        else:
            print('board', board)
            print(subBoard)
        return res
        # for rowIndex in range(len(subBoard)):
        #     for columnIndex in range(len(subBoard[rowIndex])):
        #         if subBoard[rowIndex][columnIndex] == 0:
        #             res.append(rowIndex)
        #             res.append(columnIndex)
        #             return res

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

        return (None, None)

def kiire_hinnang(team, board, depth = 0):
    kolmReas = [
        [ 0, 1, 2 ],
        [ 3, 4, 5 ],
        [ 6, 7, 8 ],
        [ 0, 3, 6 ],
        [ 1, 4, 7 ],
        [ 2, 5, 8 ],
        [ 0, 4, 8 ],
        [ 2, 4, 6 ]
    ];
    vaartused = [
        [     0,   -10,  -100, -1000 ],
        [    10,     0,     0,     0 ],
        [   100,     0,     0,     0 ],
        [  1000,     0,     0,     0 ]
    ];
    opponent = 3 - team;
    totalPlayers = 0
    totalOthers = 0
    t = 0
    tempBoard = board.flatten()
    if [0,0,0,0,0,0,0,0,0] in tempBoard:
        return 0

    for i in range(8):
        players = others = 0
        for j in range(3):
            piece = tempBoard[kolmReas[i][j]]
            if piece == team:
                players += 1
            elif piece == opponent:
                others += 1
        t += vaartused[players][others]

        totalPlayers += players
        totalOthers += others


    difference = totalPlayers - totalOthers
    if difference > 1:
        t += 10000*difference
    elif difference < -1:
        t -= -10000*difference
    return t

def maximiser(team, depth, board):
    h = kiire_hinnang(team, board, depth)
    if depth == 0 or np.count_nonzero(board) == 9:
        return (h, None)
    
    val = -inf
    best = None
    for pos in compile_possibilities(board):
        if not best:
            best = pos
        board[pos[0]][pos[1]] = team
        scen, p = minimiser(team, depth-1, board)
        # print('scen max', team, scen, h)
        board[pos[0]][pos[1]] = 0
        if scen == None:
            continue
        if scen > val:
            # print('bigger', scen, val)
            val = scen
            best = pos

    # print('max', team, val, best)
    return (val, best)

def minimiser(team, depth, board):
    h = kiire_hinnang(team, board, depth)
    if depth == 0 or np.count_nonzero(board) == 9:
        return (h, None)
    
    val = inf
    best = None
    for pos in compile_possibilities(board):
        if not best:
            best = pos
        board[pos[0]][pos[1]] = 3 - team
        scen, p = maximiser(team, depth-1, board)
        # print('scen min', team, scen, h)
        board[pos[0]][pos[1]] = 0
        if scen == None:
            continue
        if scen < val:
            # print('smaller', scen, val)
            val = scen
            best = pos
        
    # print('min', team, val, best)
    return (val, best)
    

# asd = np.array([[0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]])

asd = np.array([[0, 0, 0],
       [0, 0, 2],
       [2, 2, 1]])

# asd = np.array([[0, 0, 0],
#  [2, 1, 2],
#  [1, 2, 1]])

# asd = np.array([[0, 0, 0],
#  [0, 2, 0],
#  [1, 2, 1]])

# over = False
# team = 1
# count = 0
# while not over:
#     value, move = maximiser(team, 4, asd)
#     print('final move', team, value, move)
#     asd[move[0]][move[1]] = team
#     print(asd)
#     countTeam = np.count_nonzero(asd == team)
#     print(countTeam)
#     over = check([team, team, team], asd) or np.count_nonzero(asd) == 9
#     if team == 1:
#         team = 2
#     else:
#         team = 1
#     count += 1
#     # if count > 4:
#     #     break
