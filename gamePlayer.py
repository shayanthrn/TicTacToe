
from random import choice
from NN import NeuralNetwork
import numpy as np
class AIPlayer:
    def __init__(self):
        pass
    def think(self, ultimateBoard, activateMiniBoard):
        pass

class EasyAIPlayer(AIPlayer):
    def __init__(self):
        super().__init__()

    def think(self, ultimateBoard, activateMiniBoard,selfMark):
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

    def think(self, ultimateBoard, activateMiniBoard,selfMark):
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
        self.nn = NeuralNetwork([85,20,9])


    def think(self, ultimateBoard, activateMiniBoard,selfMark): #selfMark 1 -> O 2 -> X
        boardFlat = []
        for mini_i in range(3):
            for mini_j in range(3):
                for cell_i in range(3):
                    for cell_j in range(3):
                        val = ultimateBoard[mini_i][mini_j][cell_i][cell_j]
                        if val == 0:
                            boardFlat.append(0)
                        elif val == selfMark:
                            boardFlat.append(1)
                        else:
                            boardFlat.append(-1)

        mini_i, mini_j = activateMiniBoard
        pos_index = mini_i * 3 + mini_j
        oneHot = [int(b) for b in format(pos_index, '04b')]
        inputN = np.array(boardFlat+oneHot).reshape(85,1)
        result = self.nn.forward(inputN).flatten()
        moves = [(result[i*3 + j], (i,j)) for i in range(3) for j in range(3)]
        moves.sort(reverse=True)
        for prob, (i,j) in moves:
            if ultimateBoard[mini_i][mini_j][i][j] == 0:
                return (i,j)
        return (0,0)
