import pygame
import sys
from random import randint

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

class VerticalLinearLayout:
    def __init__(self,x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.elements = []
    def draw(self,screen):
        current_y = self.y
        for element in self.elements:
            if(current_y + element.height > self.y + self.height or element.width > self.width):
                printError("Element exceeds layout bounds")
            element.draw(screen,self.x,current_y)
            current_y += element.height

def checkQuitEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Reimagined Tic Tac Toe")


clock = pygame.time.Clock()


while True:

    checkQuitEvent()
    screen.fill((255, 255, 255))
    
    # board = ticTacToeBoard()
    # board.drawBoard(50, 50)
    # board.drawBoard(250, 50)
    # board.drawBoard(450, 50)
    # board.drawBoard(50, 250)
    # board.drawBoard(250, 250)
    # board.drawBoard(450, 250)
    # board.drawBoard(50, 450)
    # board.drawBoard(250, 450)
    # board.drawBoard(450, 450)
    mainLayout = VerticalLinearLayout(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT)
    mainLayout.elements.append(UIElement(100,100,1))
    mainLayout.elements.append(UIElement(SCREEN_WIDTH,100,2))
    mainLayout.elements.append(UIElement(SCREEN_WIDTH,200,3))
    mainLayout.elements.append(UIElement(600,200,4))
    mainLayout.elements.append(UIElement(600,300,5))
    mainLayout.draw(screen)
    pygame.display.flip()

    clock.tick(60)
