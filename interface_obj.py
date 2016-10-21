import board_obj as bo

class Interface:
    """docstring for Interface."""
    def __init__(self, player_1, player_2):
        self.board = bo.Board(1, self)
        self.winner = 0
        self.game_over = False
        self.player_1 = player_1
        self.player_2 = player_2

    def childWon(self, child, winner):
        print('board', self.board.get_board())
        self.game_over = True
        print("Winner: Player", winner)
        exit(0)

    def player_plays(self, player):
        board = self.board.get_board()
        retval = (0, 0)
        while(retval != (1, (1, player.team))):
            # print('before', board)
            play = [(i%3, j%3) for i, j in player.play(board, self.board.nextSector)]
            retval = self.board.play(player.team, play[1], play[0])
            # print('board', player.team, play)
            # print(retval)
            print('after', board)

    def game(self):
        while not self.game_over:
            self.player_plays(self.player_1)
            self.player_plays(self.player_2)
            # Player one plays once, then player two.

        print('board', self.board.get_board())
        print("Winner: Player", self.winner)
