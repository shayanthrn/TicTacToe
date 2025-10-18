from gamePlayer import HardAIPlayer, MediumAIPlayer


firstPopulationSize = 50
generations = 20
Population = [ HardAIPlayer() for _ in range(firstPopulationSize)]

def gameSimulator(playerA,playerB):
    from gameManager import GameManager
    gm = GameManager(enableMusic=False)
    gm.initGame()
    gm.initGameAIvsAI()
    players = [playerA,playerB]
    while True:
        cell_i,cell_j = players[gm.playerTurn - 1].think(gm.ultimateBoard,gm.activateMiniBoard,gm.playerTurn)
        result = gm.makeMoveAIvsAI(cell_i,cell_j,gm.playerTurn)
        if(type(result) == dict):
            return gm.playerTurn
        

for generation in range(generations):
    populationScore = [0 for _ in range(len(Population))]
    for i in range(len(Population)):
        for j in range(i+1,len(Population)):
            result = gameSimulator(Population[i],Population[j])
            if result == 1:
                populationScore[i]+=1
            else:
                populationScore[j]+=1

    print(populationScore)
