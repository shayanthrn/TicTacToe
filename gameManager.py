from enum import Enum
import pygame
from utils import printError
from gamePlayer import EasyAIPlayer, MediumAIPlayer, HardAIPlayer

class PlayerMark(Enum):
    O = 1
    X = 2

    def opposite(self):
        return PlayerMark.O if self == PlayerMark.X else PlayerMark.X

class GameState(Enum):
    WELCOME_AND_RULES = 0
    MAIN_MENU = 1
    IN_GAME = 2
    WINNER_HUMAN = 3
    WINNER_AI = 4

class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

class GameManager:
    def __init__(self, isSimulation = False):
        self.difficulty = None
        self.gameState = GameState.WELCOME_AND_RULES
        self.bg_music_menu = "./assets/Musics/bg_menu.mp3"
        self.bg_music_ingame = "./assets/Musics/bg_ingame.mp3"
        self.gameStarted = False
        self.isSimulation = isSimulation
        if not isSimulation:
            pygame.mixer.init()
            pygame.mixer.music.load(self.bg_music_menu)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
        self.isMuted = False

    def initGame(self):
        self.ultimateBoard = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append([[0 for _ in range(3)] for _ in range(3)])
            self.ultimateBoard.append(row)
        self.activateMiniBoard = (1,1)
        self.AI = None
        if self.difficulty == Difficulty.EASY:
            self.AI = EasyAIPlayer(PlayerMark.X)
        elif self.difficulty == Difficulty.MEDIUM:
            self.AI = MediumAIPlayer(PlayerMark.X)
        elif self.difficulty == Difficulty.HARD:
            self.AI = HardAIPlayer(PlayerMark.X)
        self.markToPlayNow = PlayerMark.O
        self.gameStarted = True

    def getGameState(self):
        return self.gameState
    
    def setGameState(self, state):
        self.gameState = state
        self.updateBackgroundMusic()
    
    def setDifficultyAndStart(self, difficulty):
        self.difficulty = difficulty
        self.setGameState(GameState.IN_GAME)
        self.initGame()

    def updateBackgroundMusic(self):
        if self.gameState in [GameState.WELCOME_AND_RULES, GameState.MAIN_MENU]:
            pygame.mixer.music.load(self.bg_music_menu)
            pygame.mixer.music.play(-1)

        elif self.gameState == GameState.IN_GAME:
            pygame.mixer.music.load(self.bg_music_ingame)
            pygame.mixer.music.play(-1)

    def checkMiniBoardWin(self, board):
        for i in range(3):
            if board[i][0] != 0 and board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
        for j in range(3):
            if board[0][j] != 0 and board[0][j] == board[1][j] == board[2][j]:
                return board[0][j]
        if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] != 0 and board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        return 0
    
    def toggleMute(self):
        self.isMuted = not self.isMuted

        if self.isMuted:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(0.1)

    def terminateGame(self, winnerType):
        self.gameStarted = False
        self.activateMiniBoard = (-1,-1)
        if self.isSimulation:
            return winnerType
        if winnerType == PlayerMark.O:
            self.setGameState(GameState.WINNER_HUMAN)
        else:
            self.setGameState(GameState.WINNER_AI)

    def makeMove(self, cell_i, cell_j):
        mini_i, mini_j = self.activateMiniBoard
        if self.ultimateBoard[mini_i][mini_j][cell_i][cell_j] != 0:
            printError("Request to make move for invalid position")
        self.ultimateBoard[mini_i][mini_j][cell_i][cell_j] = self.markToPlayNow
        winner = self.checkMiniBoardWin(self.ultimateBoard[mini_i][mini_j])
        if(winner):
            return self.terminateGame(winner)
        else:
            if not self.isActiveBoardFull(cell_i, cell_j):
                self.activateMiniBoard = (cell_i, cell_j)
            else:
                self.activateMiniBoard = self.findNextActiveBoard()
        self.markToPlayNow = self.markToPlayNow.opposite()
        return 0
    
    def isActiveBoardFull(self, mini_i, mini_j):
        board = self.ultimateBoard[mini_i][mini_j]
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return False
        return True
    
    def findNextActiveBoard(self):
        for i in range(3):
            for j in range(3):
                if not self.isActiveBoardFull(i, j):
                    return (i, j)
        return (-1,-1)
    
    def tick(self):
        if self.gameState == GameState.IN_GAME and self.gameStarted and self.markToPlayNow == PlayerMark.X:
            move = self.AI.think(self.ultimateBoard, self.activateMiniBoard)
            self.makeMove(*move)


_game_manager_instance = GameManager()

def getGameManager():
    return _game_manager_instance