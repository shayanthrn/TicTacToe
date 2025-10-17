from utils import printError
import pygame

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

    def handleEvent(self,event, gameManager):
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
    def __init__(self,width, height, image, hoverImage, onClick, xOffset=0, yOffset=0, id=0):
        super().__init__(width,height,xOffset,yOffset,id)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hoverImage = pygame.image.load(hoverImage)
        self.hoverImage = pygame.transform.scale(self.hoverImage, (width, height))
        self.onClick = onClick

    def _draw(self,screen):
        mousePos = pygame.mouse.get_pos()
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if rect.collidepoint(mousePos):
            screen.blit(self.hoverImage, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))
    
    def handleEvent(self,event, gameManager):
        mousePos = pygame.mouse.get_pos()
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect.collidepoint(mousePos):
                if self.onClick:
                    self.onClick(gameManager)


class UILayout(UIElement):
    def __init__(self,width, height,xOffset=0,yOffset=0,id=0):
        super().__init__(width,height,xOffset,yOffset,id)
        self.elements = []

    def addElement(self,element):
        self.elements.append(element)

    def handleEvent(self,event, gameManager):
        for element in self.elements:
            element.handleEvent(event, gameManager)


class UIVerticalLinearLayout(UILayout):
    def __init__(self,width, height,xOffset=0,yOffset=0,id=0):
        super().__init__(width,height,xOffset,yOffset,id)

    def _draw(self,screen):
        current_y = self.y
        for element in self.elements:
            if(current_y + element.height > self.y + self.height or element.width > self.width):
                printError(f"Element exceeds layout bounds, {current_y + element.height} > {self.y + self.height} or {element.width} > {self.width}")
            element.draw(screen,self.x,current_y)
            current_y += element.height + element.yOffset


class UIHorizontalLinearLayout(UILayout):
    def __init__(self,width, height,xOffset=0,yOffset=0,id=0):
        super().__init__(width,height,xOffset,yOffset,id)

    def _draw(self,screen):
        current_x = self.x
        for element in self.elements:
            if(current_x + element.width > self.x + self.width or element.height > self.height):
                printError(f"Element exceeds layout bounds, {current_x + element.width} > {self.x + self.width} or {element.height} > {self.height}")
            element.draw(screen,current_x,self.y)
            current_x += element.width + element.xOffset