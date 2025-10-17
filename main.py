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
    def __init__(self,width, height, xOffset=0, yOffset=0, id=0):
        self.id = id
        self.width = width
        self.height = height
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.x = None # will be set during drawing
        self.y = None # will be set during drawing

    def draw(self,screen,x,y):
        self.x = x + self.xOffset
        self.y = y + self.yOffset
        self._draw(screen)
        
    def _draw(self,screen):
        pass

    def handleEvent(self,event):
        pass

class UIImage(UIElement):
    def __init__(self,width, height, imagePath, xOffset=0, yOffset=0, id=0):
        super().__init__(width,height,xOffset,yOffset,id)
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, (width, height))

    def _draw(self,screen):
        screen.blit(self.image, (self.x, self.y))

class UILabel(UIElement):
    def __init__(self,width, height, text, fontType = None, fontSize=32, xOffset=0, yOffset=0, id=0):
        super().__init__(width,height,xOffset,yOffset,id)
        self.text = text
        self.font = pygame.font.Font(fontType, fontSize)

    def _draw(self,screen):
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.x, self.y))
        

class UIButton(UIElement):
    def __init__(self,width, height, image, hoverImage, xOffset=0, yOffset=0, id=0):
        super().__init__(width,height,xOffset,yOffset,id)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hoverImage = pygame.image.load(hoverImage)
        self.hoverImage = pygame.transform.scale(self.hoverImage, (width, height))

    def _draw(self,screen):
        mousePos = pygame.mouse.get_pos()
        if self.x <= mousePos[0] <= self.x + self.width and self.y <= mousePos[1] <= self.y + self.height:
            screen.blit(self.hoverImage, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))


class UILayout(UIElement):
    def __init__(self,width, height,xOffset=0,yOffset=0,id=0):
        super().__init__(width,height,xOffset,yOffset,id)
        self.elements = []

    def addElement(self,element):
        if(element.width > self.width or element.height > self.height):
            printError("Element exceeds layout bounds")
        self.elements.append(element)

    def handleEvent(self,event):
        for element in self.elements:
            element.handleEvent(event)


class UIVerticalLinearLayout(UILayout):
    def __init__(self,width, height,xOffset=0,yOffset=0,id=0):
        super().__init__(width,height,xOffset,yOffset,id)

    def _draw(self,screen):
        current_y = self.y
        for element in self.elements:
            if(current_y + element.height > self.y + self.height or element.width > self.width):
                printError("Element exceeds layout bounds")
            element.draw(screen,self.x,current_y)
            current_y += element.height + element.yOffset


class UIHorizontalLinearLayout(UILayout):
    def __init__(self,width, height,xOffset=0,yOffset=0,id=0):
        super().__init__(width,height,xOffset,yOffset,id)

    def _draw(self,screen):
        current_x = self.x
        for element in self.elements:
            if(current_x + element.width > self.x + self.width or element.height > self.height):
                printError("Element exceeds layout bounds")
            element.draw(screen,current_x,self.y)
            current_x += element.width + element.xOffset

def DescriptionLine(text, fontType = "./assets/Fonts/ethnocentric.ttf", fontSize=12):
    return UILabel(SCREEN_WIDTH, 20, text, fontType, fontSize,10)
def HeaderLine(text, fontType = "./assets/Fonts/ethnocentric.ttf", fontSize=48):
    return UILabel(SCREEN_WIDTH, 80, text, fontType, fontSize,10)
def Header2Line(text, fontType = "./assets/Fonts/ethnocentric.ttf", fontSize=34):
    return UILabel(SCREEN_WIDTH, 60, text, fontType, fontSize,10)
def Header3Line(text, fontType = "./assets/Fonts/ethnocentric.ttf", fontSize=20):
    return UILabel(SCREEN_WIDTH, 60, text, fontType, fontSize,10)

def GetWelComeAndRulesLayout():
    layout = UIVerticalLinearLayout(SCREEN_WIDTH,SCREEN_HEIGHT)
    layout.addElement(HeaderLine("Welcome to Tic Tac Toe!"))
    layout.addElement(Header2Line("Objective:"))
    layout.addElement(DescriptionLine("The goal of the game is to win any one mini-board by getting three marks in a row within"))
    layout.addElement(DescriptionLine("that mini-board."))
    layout.addElement(Header2Line("Setup:"))
    layout.addElement(DescriptionLine("1. The game consists of 9 mini Tic Tac Toe boards, arranged in a 3×3 grid."))
    layout.addElement(DescriptionLine("2. Each mini board is a standard 3×3 Tic Tac Toe board."))
    layout.addElement(DescriptionLine("3. Players take turns placing their mark (X or O) on the boards."))
    layout.addElement(DescriptionLine("4. The first move must be made on the center mini-board."))
    layout.addElement(Header2Line("Gameplay Rules:"))
    layout.addElement(DescriptionLine("1. On your turn, you must place your mark on the active mini-board."))
    layout.addElement(DescriptionLine("2. Wherever the previous player placed their mark within a mini-board determines the next "))
    layout.addElement(DescriptionLine("mini-board the opponent must play in."))
    layout.addElement(DescriptionLine("3. If the target mini-board is already full, the next player may choose any"))
    layout.addElement(DescriptionLine("available mini-board."))
    layout.addElement(DescriptionLine("4. Players alternate turns until one player wins a mini-board."))
    layout.addElement(Header2Line("Difficulties:"))
    layout.addElement(Header2Line("Easy:"))
    layout.addElement(DescriptionLine("Plays completely random moves within the allowed mini-board. No strategy is used."))
    layout.addElement(Header2Line("Medium:"))
    layout.addElement(DescriptionLine("Base strategy to block opponent wins and take wins when available."))
    layout.addElement(Header2Line("Hard:"))
    layout.addElement(DescriptionLine("Powered by a neural network trained with a genetic algorithm."))
    layout.addElement(DescriptionLine("If you manage to win against this AI, feel free to reject my job application. I’ll understand."))
    layout.addElement(UIButton(200, 75, "./assets/buttons/Rect/OkText/Default.png", "./assets/buttons/Rect/OkText/Hover.png", SCREEN_WIDTH/2 - 100))
    return layout


def GetMainMenuLayout():
    layout = UIVerticalLinearLayout(SCREEN_WIDTH,SCREEN_HEIGHT)
    layout.addElement(UILabel(HEADER_TEXT_WIDTH, HEADER_TEXT_HEIGHT, "Main Menu", "./assets/Fonts/ethnocentric.ttf", 48,SCREEN_WIDTH/2 - HEADER_TEXT_WIDTH/2))
    layout.addElement(UIImage(400,400,"./assets/images/board.png",SCREEN_WIDTH/2 - 200))
    layout.addElement(UILabel(DIFFICULTY_TEXT_WIDTH, DIFFICULTY_TEXT_HEIGHT, "Select The Difficulty", "./assets/Fonts/ethnocentric.ttf", 48,SCREEN_WIDTH/2 - DIFFICULTY_TEXT_WIDTH/2,50))
    layout.addElement(UIButton(200, 75, "./assets/buttons/Rect/PlayIcon/Default.png", "./assets/buttons/Rect/PlayIcon/Hover.png", SCREEN_WIDTH/2 - 100))
    
    return layout

def GetInGameLayout():
    layout = UIVerticalLinearLayout(300,300)
    layout.addElement(UIButton(100, 50, "./assets/buttons/Rect/PlayIcon/Default.png", "./assets/buttons/Rect/PlayIcon/Hover.png", 2))
    return layout

class GameState(Enum):
    WELCOME_AND_RULES = 0
    MAIN_MENU = 1
    IN_GAME = 2


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
HEADER_TEXT_HEIGHT = 100
HEADER_TEXT_WIDTH = 400
DIFFICULTY_TEXT_WIDTH = 800
DIFFICULTY_TEXT_HEIGHT = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

game_state = GameState.WELCOME_AND_RULES

clock = pygame.time.Clock()

welcomeLayout = GetWelComeAndRulesLayout()
mainMenuLayout = GetMainMenuLayout()
inGameLayout = GetInGameLayout()
while True:
    screen.fill((255, 255, 254))

    activeLayout = None

    if game_state == GameState.WELCOME_AND_RULES:
        activeLayout = welcomeLayout
    elif game_state == GameState.MAIN_MENU:
        activeLayout = mainMenuLayout
    elif game_state == GameState.IN_GAME:
        activeLayout = inGameLayout
    else:
        printError("Invalid game state")

    activeLayout.draw(screen,0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        activeLayout.handleEvent(event)
    pygame.display.flip()

    clock.tick(60)
