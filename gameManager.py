from enum import Enum
import pygame

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
        pygame.mixer.music.load(self.bg_music_menu)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    def getGameState(self):
        return self.gameState
    
    def setGameState(self, state):
        self.gameState = state
        self.updateBackgroundMusic()
    
    def setDifficultyAndStart(self, difficulty):
        self.difficulty = difficulty
        self.setGameState(GameState.IN_GAME)

    def updateBackgroundMusic(self):
        if self.gameState in [GameState.WELCOME_AND_RULES, GameState.MAIN_MENU]:
            pygame.mixer.music.load(self.bg_music_menu)
            pygame.mixer.music.play(-1)

        elif self.gameState == GameState.IN_GAME:
            pygame.mixer.music.load(self.bg_music_ingame)
            pygame.mixer.music.play(-1)