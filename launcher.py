import pygame
import sys
from gameLayout import *
from gameManager import GameState, getGameManager
from utils import printError

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

gameManager = getGameManager()

clock = pygame.time.Clock()
welcomeLayout = GetWelComeAndRulesLayout()
mainMenuLayout = GetMainMenuLayout()
inGameLayout = GetInGameLayout()
winnerLayout = GetWinnerLayout()
loserLayout = GetLoserLayout()
while True:
    screen.fill((255, 255, 254))

    activeLayout = None

    if gameManager.getGameState() == GameState.WELCOME_AND_RULES:
        activeLayout = welcomeLayout
    elif gameManager.getGameState() == GameState.MAIN_MENU:
        activeLayout = mainMenuLayout
    elif gameManager.getGameState() == GameState.IN_GAME:
        gameManager.tick()
        activeLayout = inGameLayout
    elif gameManager.getGameState() == GameState.WINNER_HUMAN:
        activeLayout = winnerLayout
    elif gameManager.getGameState() == GameState.WINNER_AI:
        activeLayout = loserLayout
    else:
        printError("Invalid game state")
    
    activeLayout.draw(screen,0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        activeLayout.handleEvent(event, gameManager)

    pygame.display.flip()
    clock.tick(60)
