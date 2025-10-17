from UIFramework import *
from gameManager import GameState, Difficulty

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
HEADER_TEXT_HEIGHT = 100
HEADER_TEXT_WIDTH = 400
DIFFICULTY_TEXT_WIDTH = 800
DIFFICULTY_TEXT_HEIGHT = 100

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
    layout.addElement(UIButton(200, 75, "./assets/buttons/Rect/OkText/Default.png", "./assets/buttons/Rect/OkText/Hover.png",lambda gm: gm.setGameState(GameState.MAIN_MENU), SCREEN_WIDTH/2 - 100))
    return layout

def GetMainMenuLayout():
    layout = UIVerticalLinearLayout(SCREEN_WIDTH,SCREEN_HEIGHT)
    layout.addElement(UILabel(HEADER_TEXT_WIDTH, HEADER_TEXT_HEIGHT, "Main Menu", "./assets/Fonts/ethnocentric.ttf", 48,SCREEN_WIDTH/2 - HEADER_TEXT_WIDTH/2))
    layout.addElement(UIImage(400,400,"./assets/images/board.png",SCREEN_WIDTH/2 - 200))
    layout.addElement(UILabel(DIFFICULTY_TEXT_WIDTH, DIFFICULTY_TEXT_HEIGHT, "Select The Difficulty", "./assets/Fonts/ethnocentric.ttf", 48,SCREEN_WIDTH/2 - DIFFICULTY_TEXT_WIDTH/2,50))
    hlayoutButtons = UIHorizontalLinearLayout(SCREEN_WIDTH,70)
    hlayoutButtons.addElement(UIButton(200, 70, "./assets/buttons/Rect/PlayIcon/Default.png", "./assets/buttons/Rect/PlayIcon/Hover.png", lambda gm: gm.setDifficultyAndStart(Difficulty.EASY),  70,0))
    hlayoutButtons.addElement(UIButton(200, 70, "./assets/buttons/Rect/PlayIcon/Default.png", "./assets/buttons/Rect/PlayIcon/Hover.png", lambda gm: gm.setDifficultyAndStart(Difficulty.MEDIUM), 70,0))
    hlayoutButtons.addElement(UIButton(200, 70, "./assets/buttons/Rect/PlayIcon/Default.png", "./assets/buttons/Rect/PlayIcon/Hover.png", lambda gm: gm.setDifficultyAndStart(Difficulty.HARD), 70,0))
    layout.addElement(hlayoutButtons)
    hlayoutLabels = UIHorizontalLinearLayout(SCREEN_WIDTH,30)
    hlayoutLabels.addElement(UILabel(200, 30, "Easy", "./assets/Fonts/ethnocentric.ttf", 24, 70,30))
    hlayoutLabels.addElement(UILabel(200, 30, "Medium", "./assets/Fonts/ethnocentric.ttf", 24, 70,30))
    hlayoutLabels.addElement(UILabel(200, 30, "Hard", "./assets/Fonts/ethnocentric.ttf", 24, 70,30))
    layout.addElement(hlayoutLabels)    
    return layout

def GetInGameLayout():
    layout = UIVerticalLinearLayout(300,300)
    layout.addElement(UIButton(50, 50, "./assets/buttons/Square/Home/Default.png", "./assets/buttons/Square/Home/Hover.png", lambda gm: gm.setGameState(GameState.MAIN_MENU)))
    return layout