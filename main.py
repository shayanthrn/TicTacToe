import pygame
import sys
from random import randint
from enum import Enum

def printError(text):
    raise Exception(text)

class ticTacToeBoard:

    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.boardUI = pygame.image.load("./assets/board.png")
        self.boardUI = pygame.transform.scale(self.boardUI, (150, 150))

    def drawBoard(self,x,y):
        screen.blit(self.boardUI, (x, y))
        # for row in self.board:
        #     print(row)


class UIElement:
    def __init__(self,width, height, id=0):
        self.id = id
        self.width = width
        self.height = height
    def draw(self,screen,x,y):
        pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), (x, y, self.width, self.height))
        font = pygame.font.SysFont(None, 20)
        text = font.render(str(self.id), True, (0, 0, 0))
        screen.blit(text, (x + 5, y + 5))


class UILabel(UIElement):
    def __init__(self,width, height, text, fontType = None, fontSize=32, id=0):
        super().__init__(width,height,id)
        self.text = text
        self.font = pygame.font.Font(fontType, fontSize)

    def draw(self,screen,x,y):
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (x, y))

class UIButton(UIElement):
    def __init__(self,width, height, image, hoverImage, id=0):
        super().__init__(width,height,id)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hoverImage = pygame.image.load(hoverImage)
        self.hoverImage = pygame.transform.scale(self.hoverImage, (width, height))

    def draw(self,screen,x,y):
        mousePos = pygame.mouse.get_pos()
        if x <= mousePos[0] <= x + self.width and y <= mousePos[1] <= y + self.height:
            screen.blit(self.hoverImage, (x, y))
        else:
            screen.blit(self.image, (x, y))


class UILayout(UIElement):
    def __init__(self,width, height,id=0):
        super().__init__(width,height,id)
        self.elements = []

    def addElement(self,element):
        if(element.width > self.width or element.height > self.height):
            printError("Element exceeds layout bounds")
        self.elements.append(element)


class UIVerticalLinearLayout(UILayout):

    def __init__(self,width, height,id=0):
        super().__init__(width,height,id)

    def draw(self,screen,x,y):
        current_y = y
        for element in self.elements:
            if(current_y + element.height > y + self.height or element.width > self.width):
                printError("Element exceeds layout bounds")
            element.draw(screen,x,current_y)
            current_y += element.height


class UIHorizontalLinearLayout(UILayout):

    def __init__(self,width, height,id=0):
        super().__init__(width,height,id)
        
    def draw(self,screen,x,y):
        current_x = x
        for element in self.elements:
            if(current_x + element.width > x + self.width or element.height > self.height):
                printError("Element exceeds layout bounds")
            element.draw(screen,current_x,y)
            current_x += element.width


def GetMainMenuLayout():
    layout = UIVerticalLinearLayout(900,900)
    layout.addElement(UIButton(150, 50, "./assets/buttons/Rect/PlayIcon/Default.png", "./assets/buttons/Rect/PlayIcon/Hover.png", 1))
    layout.addElement(UILabel(200, 50, "Reimagined Tic Tac Toe", "./assets/Fonts/ethnocentric.ttf", 32, 2))
    layout.addElement(UIButton(50, 50, "./assets/Exit.png", "./assets/Exit.png", 1))
    return layout

def GetInGameLayout():
    layout = UIVerticalLinearLayout(300,300)
    layout.addElement(UIButton(100, 50, "./assets/buttons/Rect/PlayIcon/Default.png", "./assets/buttons/Rect/PlayIcon/Hover.png", 2))
    return layout

class GameState(Enum):
    MAIN_MENU = 1
    IN_GAME = 2


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Reimagined Tic Tac Toe")

game_state = GameState.MAIN_MENU

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    
    if game_state == GameState.MAIN_MENU:
        layout = GetMainMenuLayout()
    elif game_state == GameState.IN_GAME:
        layout = GetInGameLayout()
    else:
        printError("Invalid game state")

    layout.draw(screen,0,0)

    pygame.display.flip()

    clock.tick(60)
