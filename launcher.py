import pygame
import sys
from gameUI import SCREEN_HEIGHT, SCREEN_WIDTH, GetWelComeAndRulesLayout, GetMainMenuLayout, GetInGameLayout
from gameManager import GameManager, GameState
from utils import printError

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

gameManager = GameManager()

clock = pygame.time.Clock()

welcomeLayout = GetWelComeAndRulesLayout()
mainMenuLayout = GetMainMenuLayout()
inGameLayout = GetInGameLayout()

while True:
    screen.fill((255, 255, 254))

    activeLayout = None

    if gameManager.getGameState() == GameState.WELCOME_AND_RULES:
        activeLayout = welcomeLayout
    elif gameManager.getGameState() == GameState.MAIN_MENU:
        activeLayout = mainMenuLayout
    elif gameManager.getGameState() == GameState.IN_GAME:
        activeLayout = inGameLayout
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
