from enum import Enum
import pygame

from gamePlayer import EasyAIPlayer, MediumAIPlayer, HardAIPlayer

class PlayerType(Enum):
    HUMAN = 0
    AI = 1

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
    def __init__(self, enableMusic=True):
        self.difficulty = None
        self.gameState = GameState.WELCOME_AND_RULES
        self.bg_music_menu = "./assets/Musics/bg_menu.mp3"
        self.bg_music_ingame = "./assets/Musics/bg_ingame.mp3"
        self.gameStarted = False
        if enableMusic:
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
            self.AI = EasyAIPlayer()
        elif self.difficulty == Difficulty.MEDIUM:
            self.AI = MediumAIPlayer()
        elif self.difficulty == Difficulty.HARD:
            self.AI = HardAIPlayer()
        self.playerTurn = PlayerType.HUMAN
        self.gameStarted = True

    def initGameAIvsAI(self):
        self.playerTurn = 1

    def getGameState(self):
        return self.gameState
    
    def setplayerTurn(self, playerType):
        self.playerTurn = playerType
    
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
                return True
        for j in range(3):
            if board[0][j] != 0 and board[0][j] == board[1][j] == board[2][j]:
                return True
        if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
            return True
        if board[0][2] != 0 and board[0][2] == board[1][1] == board[2][0]:
            return True
        return False
    
    def toggleMute(self):
        self.isMuted = not self.isMuted

        if self.isMuted:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(0.1)

    def terminateGame(self, winnerType):
        self.gameStarted = False
        self.activateMiniBoard = (-1,-1)
        if winnerType == PlayerType.HUMAN:
            self.setGameState(GameState.WINNER_HUMAN)
        else:
            self.setGameState(GameState.WINNER_AI)

    def makeMove(self, cell_i, cell_j, playerType):
        mini_i, mini_j = self.activateMiniBoard
        if self.ultimateBoard[mini_i][mini_j][cell_i][cell_j] != 0:
            return False
        if playerType == PlayerType.HUMAN:
            self.ultimateBoard[mini_i][mini_j][cell_i][cell_j] = 1
            self.setplayerTurn(PlayerType.AI)
        else:
            self.ultimateBoard[mini_i][mini_j][cell_i][cell_j] = 2
            self.setplayerTurn(PlayerType.HUMAN)

        if(self.checkMiniBoardWin(self.ultimateBoard[mini_i][mini_j])):
            self.terminateGame(playerType)
        else:
            if not self.isActiveBoardFull(cell_i, cell_j):
                self.activateMiniBoard = (cell_i, cell_j)
            else:
                self.activateMiniBoard = self.findNextActiveBoard()
        return True
    
    def makeMoveAIvsAI(self, cell_i, cell_j, playerTurn):
        mini_i, mini_j = self.activateMiniBoard
        if self.ultimateBoard[mini_i][mini_j][cell_i][cell_j] != 0:
            return False
        self.ultimateBoard[mini_i][mini_j][cell_i][cell_j] = playerTurn

        if(self.checkMiniBoardWin(self.ultimateBoard[mini_i][mini_j])):
            return {'winner' : playerTurn}
        else:
            if not self.isActiveBoardFull(cell_i, cell_j):
                self.activateMiniBoard = (cell_i, cell_j)
            else:
                self.activateMiniBoard = self.findNextActiveBoard()

        if playerTurn == 1:
            self.playerTurn = 2
        else:
            self.playerTurn = 1
        return True
    
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
        if self.gameState == GameState.IN_GAME and self.gameStarted and self.playerTurn == PlayerType.AI:
            move = self.AI.think(self.ultimateBoard, self.activateMiniBoard,2)
            self.makeMove(*move, PlayerType.AI)


_game_manager_instance = GameManager()

def getGameManager():
    return _game_manager_instance