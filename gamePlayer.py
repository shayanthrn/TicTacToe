
from random import choice
from nn import NeuralNetwork
import numpy as np

class AIPlayer:
    def __init__(self,mark):
        self.mark = mark
    def think(self, ultimateBoard, activateMiniBoard):
        pass

class EasyAIPlayer(AIPlayer):
    def __init__(self,mark):
        super().__init__(mark)

    def think(self, ultimateBoard, activateMiniBoard):
        mini_i, mini_j = activateMiniBoard
        choices = self.findAvailableOptions(ultimateBoard[mini_i][mini_j])
        if choices:
            return choice(choices)
        return None
    
    def findAvailableOptions(self, board):
        choices = []
        for i in range(3):
            for j in range(3):
                if  board[i][j]== 0:
                    choices.append((i, j))
        return choices


class MediumAIPlayer(EasyAIPlayer):
    def __init__(self,mark):
        super().__init__(mark)

    def think(self, ultimateBoard, activateMiniBoard):
        mini_i, mini_j = activateMiniBoard
        board = ultimateBoard[mini_i][mini_j]
        choices = self.findAvailableOptions(board)
        winPositions = self.findWinPositions(board,choices)
        if winPositions:
            return choice(winPositions)
        elif choices:
            return choice(choices)
        return None

    def findWinPositions(self, board, choices):
        winPositions = []
        for i, j in choices:
            board[i][j] = self.mark
            from gameManager import getGameManager
            if getGameManager().checkMiniBoardWin(board):
                board[i][j] = 0
                winPositions.append((i, j)) 
            board[i][j] = 0 
        return winPositions

    
class HardAIPlayer(MediumAIPlayer):
    def __init__(self,mark):
        super().__init__(mark)
        self.nn = NeuralNetwork()

    def think(self, ultimateBoard, activateMiniBoard):
        mini_i, mini_j = activateMiniBoard
        board = ultimateBoard[mini_i][mini_j]
        choices = self.findAvailableOptions(board)
        winPositions = self.findWinPositions(board,choices)
        if winPositions:
            return choice(winPositions)
        else:
            safePositions = self.findSafePositions(ultimateBoard,choices)
            if safePositions:
                return choice(safePositions)
            elif choices:
                return choice(choices)
            return None

    def findSafePositions (self,ultimateBoard,choices):
        safePositions = []
        for i,j in choices:
            risky = False
            nextBoard = ultimateBoard[i][j]
            oppChoices = self.findAvailableOptions(nextBoard)
            for oi, oj in oppChoices:
                nextBoard[oi][oj] = self.mark.opposite()
                from gameManager import getGameManager
                if getGameManager().checkMiniBoardWin(nextBoard):
                    risky = True
                nextBoard[oi][oj] = 0
                if risky:
                    break
            if not risky:
                safePositions.append((i,j))

        return safePositions



