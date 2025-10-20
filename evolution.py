from gamePlayer import HardAIPlayer, MediumAIPlayer, EasyAIPlayer
import copy
import random
import numpy as np
import pickle
import time

firstPopulationSize = 100
generations = 1000
survivalRate = 0.1
Population = [ HardAIPlayer() for _ in range(firstPopulationSize)]

def gameSimulator(player_O,player_X):
    from gameManager import GameManager, PlayerMark
    gm = GameManager(isSimulation=True)
    gm.initGame()
    players = {
        PlayerMark.O : player_O,
        PlayerMark.X : player_X
    }
    while True:
        cell_i,cell_j = players[gm.markToPlayNow].think(gm.ultimateBoard,gm.activateMiniBoard)
        result = gm.makeMove(cell_i,cell_j)
        print(gm.ultimateBoard)
        time.sleep(5)
        if(type(result) == dict):
            return gm.playerTurn
        
# def breed(parent1, parent2):
#     layer1shape=parent1.nn.layer1_weights.shape
#     layer2shape=parent1.nn.layer2_weights.shape
#     bias1shape=parent1.nn.biases1.shape
#     bias2shape=parent1.nn.biases2.shape
#     child = HardAIPlayer()
#     child.nn.layer1_weights= np.block([[parent1.nn.layer1_weights[:layer1shape[0]//2]],[parent2.nn.layer1_weights[layer1shape[0]//2:layer1shape[0]]]])
#     child.nn.layer2_weights= np.block([[parent1.nn.layer2_weights[:layer2shape[0]//2]],[parent2.nn.layer2_weights[layer2shape[0]//2:layer2shape[0]]]])
#     child.nn.biases1 = np.block([[parent1.nn.biases1[:bias1shape[0]//2]],[parent2.nn.biases1[bias1shape[0]//2:bias1shape[0]]]])
#     child.nn.biases2 = np.block([[parent1.nn.biases2[:bias2shape[0]//2]],[parent2.nn.biases2[bias2shape[0]//2:bias2shape[0]]]])
#     return child

def breed(parent1, parent2):
    child = HardAIPlayer()

    def crossover(a, b):
        mask = np.random.rand(*a.shape) < 0.5
        return np.where(mask, a, b)

    child.nn.layer1_weights = crossover(parent1.nn.layer1_weights, parent2.nn.layer1_weights)
    child.nn.layer2_weights = crossover(parent1.nn.layer2_weights, parent2.nn.layer2_weights)
    child.nn.biases1 = crossover(parent1.nn.biases1, parent2.nn.biases1)
    child.nn.biases2 = crossover(parent1.nn.biases2, parent2.nn.biases2)

    return child

# def breed(parent1, parent2):
#     child = HardAIPlayer()
#     alpha = np.random.uniform(0.3, 0.7)  # blending ratio

#     child.nn.layer1_weights = alpha * parent1.nn.layer1_weights + (1 - alpha) * parent2.nn.layer1_weights
#     child.nn.layer2_weights = alpha * parent1.nn.layer2_weights + (1 - alpha) * parent2.nn.layer2_weights
#     child.nn.biases1 = alpha * parent1.nn.biases1 + (1 - alpha) * parent2.nn.biases1
#     child.nn.biases2 = alpha * parent1.nn.biases2 + (1 - alpha) * parent2.nn.biases2

#     return child

# def breed(parent1, parent2):
#     layer1shape=parent1.nn.layer1_weights.shape
#     layer2shape=parent1.nn.layer2_weights.shape
#     bias1shape=parent1.nn.biases1.shape
#     bias2shape=parent1.nn.biases2.shape
#     child = HardAIPlayer()
#     child.nn.layer1_weights= parent1.nn.layer1_weights
#     child.nn.layer2_weights= parent2.nn.layer2_weights
#     child.nn.biases1 = np.block([[parent1.nn.biases1[:bias1shape[0]//2]],[parent2.nn.biases1[bias1shape[0]//2:bias1shape[0]]]])
#     child.nn.biases2 = np.block([[parent1.nn.biases2[:bias2shape[0]//2]],[parent2.nn.biases2[bias2shape[0]//2:bias2shape[0]]]])
#     return child
        

def mutate(player):
    rand= random.uniform(0, 1)
    if(rand<mutationRate):
        player.nn.layer1_weights+= np.random.normal(size=player.nn.layer1_weights.shape,scale=0.3)
        player.nn.layer2_weights+= np.random.normal(size=player.nn.layer2_weights.shape,scale=0.3)
        player.nn.biases1 += np.random.normal(size=player.nn.biases1.shape,scale=0.3)
        player.nn.biases2 += np.random.normal(size=player.nn.biases2.shape,scale=0.3)

def evolvePopulation(population, scores):
    scored_pairs = sorted(zip(population, scores), key=lambda x: x[1], reverse=True)
    survivors = [copy.deepcopy(p[0]) for p in scored_pairs[: int(len(population) * survivalRate)]]
    newPopulation = survivors.copy()
    while len(newPopulation) < len(population):
        parent1, parent2 = random.sample(survivors, 2)
        child = breed(parent1, parent2)
        mutate(child)
        newPopulation.append(child)

    return newPopulation


bestPlayer = None

enemy = MediumAIPlayer()
for generation in range(generations):
    mutationRate = 0.3 if generation < generations * 0.3 else 0.1
    populationScore = [0 for _ in range(len(Population))]
    for i in range(len(Population)):
        for j in range(30):
            result = gameSimulator(Population[i],enemy)
            if result == 1:
                populationScore[i]+=1

    bestScore = max(populationScore)
    bestIndex = populationScore.index(bestScore)
    bestPlayer = Population[bestIndex]
    print(f"Gen: {generation}, Max: {bestScore}, Avg: {sum(populationScore)/len(populationScore)}")
    if bestScore > 25:
        break
    Population = evolvePopulation(Population, populationScore)

with open("bestPlayer.pkl", "wb") as f:
    pickle.dump(bestPlayer, f)


