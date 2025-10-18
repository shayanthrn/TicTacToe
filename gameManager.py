from enum import Enum
import pygame

from gamePlayer import Player, EasyAIPlayer, MediumAIPlayer, HardAIPlayer

class GameState(Enum):
    WELCOME_AND_RULES = 0
    MAIN_MENU = 1
    IN_GAME = 2

class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

class GameManager:
    def __init__(self):
        self.difficulty = None
        self.gameState = GameState.WELCOME_AND_RULES
        self.bg_music_menu = "./assets/Musics/bg_menu.mp3"
        self.bg_music_ingame = "./assets/Musics/bg_ingame.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(self.bg_music_menu)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    def initGame(self):
        self.ultimateBoard = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append([[0 for _ in range(3)] for _ in range(3)])
            self.ultimateBoard.append(row)
        self.activateMiniBoard = (1,1)
        self.players = []
        self.players.append(Player())
        if self.difficulty == Difficulty.EASY:
            self.players.append(EasyAIPlayer())
        elif self.difficulty == Difficulty.MEDIUM:
            self.players.append(MediumAIPlayer())
        elif self.difficulty == Difficulty.HARD:
            self.players.append(HardAIPlayer())
        self.currentPlayer = 0

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

_game_manager_instance = GameManager()

def getGameManager():
    return _game_manager_instance