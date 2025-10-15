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


class Layout(UIElement):
    def __init__(self,width, height,id=0):
        super().__init__(width,height)
        self.elements = []

    def addElement(self,element):
        if(element.width > self.width or element.height > self.height):
            printError("Element exceeds layout bounds")
        self.elements.append(element)


class VerticalLinearLayout(Layout):

    def __init__(self,width, height,id=0):
        super().__init__(width,height,id)

    def draw(self,screen,x,y):
        current_y = y
        for element in self.elements:
            if(current_y + element.height > y + self.height or element.width > self.width):
                printError("Element exceeds layout bounds")
            element.draw(screen,x,current_y)
            current_y += element.height


class HorizantalLinearLayout(Layout):

    def __init__(self,width, height,id=0):
        super().__init__(width,height,id)
        
    def draw(self,screen,x,y):
        current_x = x
        for element in self.elements:
            if(current_x + element.width > x + self.width or element.height > self.height):
                printError("Element exceeds layout bounds")
            element.draw(screen,current_x,y)
            current_x += element.width

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




    # mainLayout = VerticalLinearLayout(SCREEN_WIDTH, SCREEN_HEIGHT)
    # header = UIElement(SCREEN_WIDTH,50,1)
    # mainLayout.addElement(header)
    # midSection = HorizantalLinearLayout(SCREEN_WIDTH, 800)
    # ele1 = UIElement(200,800,4)
    # ele2 = UIElement(200,800,5)
    # ele3 = UIElement(200,800,6)
    # ele4 = UIElement(200,800,7)
    # ele5 = UIElement(200,800,8)
    # midSection.addElement(ele1)
    # midSection.addElement(ele2)
    # midSection.addElement(ele3)
    # midSection.addElement(ele4)
    # midSection.addElement(ele5)
    # mainLayout.addElement(midSection)
    # footer = UIElement(SCREEN_WIDTH,50,3)
    # mainLayout.addElement(footer)
    # mainLayout.draw(screen,0,0)



    mainLayout = Layout(400, 400)
    mainLayout.draw(screen,0,0)

    pygame.display.flip()

    clock.tick(60)
