
from random import choice

class AIPlayer:
    def __init__(self):
        pass
    def think(self, ultimateBoard, activateMiniBoard):
        pass

class EasyAIPlayer(AIPlayer):
    def __init__(self):
        super().__init__()

    def think(self, ultimateBoard, activateMiniBoard):
        mini_i, mini_j = activateMiniBoard
        choices = []
        for i in range(3):
            for j in range(3):
                if ultimateBoard[mini_i][mini_j][i][j] == 0:
                    choices.append((i, j))
        if choices:
            return choice(choices)
        return None

class MediumAIPlayer(AIPlayer):
    def __init__(self):
        super().__init__()

    def think(self, ultimateBoard, activateMiniBoard):
        mini_i, mini_j = activateMiniBoard
        board = ultimateBoard[mini_i][mini_j]
        choices = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    choices.append((i, j))
                    board[i][j] = 1 # check for blocking
                    from gameManager import getGameManager
                    if getGameManager().checkMiniBoardWin(board):
                        board[i][j] = 0
                        return (i, j)
                    board[i][j] = 2 # check win self
                    if getGameManager().checkMiniBoardWin(board):
                        board[i][j] = 0
                        return (i, j)
                    board[i][j] = 0          
        if choices:
            return choice(choices)
        return None


    
class HardAIPlayer(AIPlayer):
    def __init__(self):
        super().__init__()

    def think(self, ultimateBoard, activateMiniBoard):
        pass
