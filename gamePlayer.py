
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
        
    
class HardAIPlayer(AIPlayer):
    def __init__(self):
        super().__init__()

    def think(self, ultimateBoard, activateMiniBoard):
        pass
