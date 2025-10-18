from UIFramework import *
from gameManager import Difficulty, PlayerType, getGameManager

class UIBoard(UIElement):
    def __init__(self, width, height, index_i,index_j, xOffset=0, yOffset=0, id=0):
        super().__init__(width, height, xOffset, yOffset, id)
        self.boardImage = UIImage(self.width, self.height, "./assets/images/board.png")
        self.isActiveLabel = UILabel(self.width, 20, "Active", "./assets/Fonts/ethnocentric.ttf", 16)
        self.naughtImage = UIImage(self.width//3, self.height//3, "./assets/images/naught.png")
        self.crossImage = UIImage(self.width//3, self.height//3, "./assets/images/cross.png")
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = UIButton(self.width // 3 -30, self.height // 3-30, "./assets/Images/empty.png", "./assets/Images/hover.png", lambda i=i, j=j: getGameManager().makeMove(i, j, PlayerType.HUMAN), 20, 20)
                row.append(button)
            self.buttons.append(row)
        self.index_i = index_i
        self.index_j = index_j

    def _draw(self, screen):
        gm = getGameManager()
        self.boardImage.draw(screen, self.x, self.y)
        isActive = (self.index_i,self.index_j) == gm.activateMiniBoard
        isUserTurn = gm.playerTurn == PlayerType.HUMAN
        if isActive:
            self.isActiveLabel.draw(screen, self.x + 50, self.y + self.height + 20)
        cellWidth = self.width // 3
        cellHeight = self.height // 3
        board = gm.ultimateBoard[self.index_i][self.index_j]
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0 and isActive and isUserTurn:
                    self.buttons[i][j].draw(screen, self.x + j * cellWidth, self.y + i * cellHeight)
                if board[i][j] == 1:
                    self.naughtImage.draw(screen, self.x + j * cellWidth, self.y + i * cellHeight)
                if board[i][j] == 2:
                    self.crossImage.draw(screen, self.x + j * cellWidth, self.y + i * cellHeight)

    def handleEvent(self, event):
        gm = getGameManager()
        isActive = (self.index_i,self.index_j) == gm.activateMiniBoard
        isUserTurn = gm.playerTurn == PlayerType.HUMAN
        if isActive and isUserTurn:
            for row in self.buttons:
                for button in row:
                    button.handleEvent(event)


class DifficultyLabel(UIElement):
    def __init__(self,width, height, fontType = None, fontSize=32, xOffset=0, yOffset=0, id=0):
        super().__init__(width, height, xOffset, yOffset, id)
        self.font = pygame.font.Font(fontType, fontSize)

    def _draw(self, screen):
        gm = getGameManager()
        text = ""
        if gm.difficulty == Difficulty.EASY:
            text = "Difficulty: Easy"
        elif gm.difficulty == Difficulty.MEDIUM:
            text = "Difficulty: Medium"
        elif gm.difficulty == Difficulty.HARD:
            text = "Difficulty: Hard"
        text_surface = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (self.x, self.y))

class TurnLabel(UIElement):
    def __init__(self,width, height, fontType = None, fontSize=32, xOffset=0, yOffset=0, id=0):
        super().__init__(width, height, xOffset, yOffset, id)
        self.font = pygame.font.Font(fontType, fontSize)

    def _draw(self, screen):
        gm = getGameManager()
        if gm.playerTurn == PlayerType.HUMAN:
            text = "Your Turn"
        else:
            text = "AI's Turn"
        text_surface = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (self.x, self.y))

class MuteButton(UIElement):
    def __init__(self,width, height, xOffset=0, yOffset=0, id=0):
        super().__init__(width, height, xOffset, yOffset, id)
        self.muteButton = UIButton(width, height, "./assets/buttons/Square/SoundOff/Default.png", "./assets/buttons/Square/SoundOff/Hover.png", lambda: getGameManager().toggleMute())
        self.unmuteButton = UIButton(width, height, "./assets/buttons/Square/SoundOn/Default.png", "./assets/buttons/Square/SoundOn/Hover.png", lambda: getGameManager().toggleMute())

    def _draw(self,screen):
        gm = getGameManager()
        if(gm.isMuted):
            self.unmuteButton.draw(screen,self.x,self.y)
        else:
            self.muteButton.draw(screen,self.x,self.y)

    def handleEvent(self, event):
        gm = getGameManager()
        if(gm.isMuted):
            self.unmuteButton.handleEvent(event)
        else:
            self.muteButton.handleEvent(event)