class Turn:
    PLAYER_1 = 0
    PLAYER_2 = 1
    PLAYER_3 = 2
    PLAYER_4 = 3
    ENEMIES = 4
    ACTIONCARD = 5
    GET_RESOURCES = 6
    GET_GRAIN = 7
    END = 8

    @staticmethod
    def isPlayerTurn(turn):
        return turn >= Turn.PLAYER_1 and turn <= Turn.PLAYER_4
    @staticmethod
    def turnToPlayerIndex(turn):
        return turn - Turn.PLAYER_1