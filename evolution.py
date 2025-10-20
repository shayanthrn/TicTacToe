from gamePlayer import HardAIPlayer, MediumAIPlayer, EasyAIPlayer
import random
import numpy as np
import pickle
import copy

firstPopulationSize = 200
generations = 100
survivalCount = 10
eliteCopy = 1

from gameManager import GameManager, PlayerMark

Population = [ HardAIPlayer(PlayerMark.X) for _ in range(firstPopulationSize)]

def gameSimulator(player_O,player_X):
    gm = GameManager(isSimulation=True)
    gm.initGame()
    players = {
        PlayerMark.O : player_O,
        PlayerMark.X : player_X
    }
    while True:
        cell_i,cell_j = players[gm.markToPlayNow].think(gm.ultimateBoard,gm.activateMiniBoard)
        result = gm.makeMove(cell_i,cell_j)
        if(result):
            return result
        
# def breed(parent1, parent2):
#     layer1shape=parent1.nn.layer1_weights.shape
#     layer2shape=parent1.nn.layer2_weights.shape
#     bias1shape=parent1.nn.biases1.shape
#     bias2shape=parent1.nn.biases2.shape
#     child = HardAIPlayer(parent1.mark)
#     child.nn.layer1_weights= np.block([[parent1.nn.layer1_weights[:layer1shape[0]//2]],[parent2.nn.layer1_weights[layer1shape[0]//2:layer1shape[0]]]])
#     child.nn.layer2_weights= np.block([[parent1.nn.layer2_weights[:layer2shape[0]//2]],[parent2.nn.layer2_weights[layer2shape[0]//2:layer2shape[0]]]])
#     child.nn.biases1 = np.block([[parent1.nn.biases1[:bias1shape[0]//2]],[parent2.nn.biases1[bias1shape[0]//2:bias1shape[0]]]])
#     child.nn.biases2 = np.block([[parent1.nn.biases2[:bias2shape[0]//2]],[parent2.nn.biases2[bias2shape[0]//2:bias2shape[0]]]])
#     return child

def breed(parent1, parent2):
    child = HardAIPlayer(parent1.mark)

    def crossover(a, b):
        mask = np.random.rand(*a.shape) < 0.5
        return np.where(mask, a, b)

    child.nn.layer1_weights = crossover(parent1.nn.layer1_weights, parent2.nn.layer1_weights)
    child.nn.layer2_weights = crossover(parent1.nn.layer2_weights, parent2.nn.layer2_weights)
    child.nn.biases1 = crossover(parent1.nn.biases1, parent2.nn.biases1)
    child.nn.biases2 = crossover(parent1.nn.biases2, parent2.nn.biases2)

    return child

def mutate(player, mutationRate):
    rand= random.uniform(0, 1)
    if(rand<mutationRate):
        player.nn.layer1_weights+= np.random.normal(size=player.nn.layer1_weights.shape,scale=0.3)
        player.nn.layer2_weights+= np.random.normal(size=player.nn.layer2_weights.shape,scale=0.3)
        player.nn.biases1 += np.random.normal(size=player.nn.biases1.shape,scale=0.3)
        player.nn.biases2 += np.random.normal(size=player.nn.biases2.shape,scale=0.3)



def evolvePopulation(population, scores, mutationRate, bestPlayer):
    scored_pairs = sorted(zip(population, scores), key=lambda x: x[1], reverse=True)
    survivors = [copy.deepcopy(p[0]) for p in scored_pairs[: survivalCount]]
    newPopulation = survivors.copy()
    if bestPlayer:
        newPopulation += [copy.deepcopy(bestPlayer) for _ in range(eliteCopy)]
    while len(newPopulation) < len(population):
        parent1, parent2 = random.choices(newPopulation, k=2)
        child = breed(parent1, parent2)
        mutate(child,mutationRate)
        newPopulation.append(child)

    return newPopulation


bestPlayer = None
bestScoreOverall = 0

enemy = MediumAIPlayer(PlayerMark.O)
for generation in range(generations):
    mutationRate = 0.8 if generation < generations * 0.3 else 0.3
    populationScore = [0 for _ in range(len(Population))]
    for i in range(len(Population)):
        for i in range(10):
            result = gameSimulator(enemy,Population[i])
            if result == PlayerMark.X:
                populationScore[i]+=1

    bestScore = max(populationScore)
    bestIndex = populationScore.index(bestScore)
    if bestScore > bestScoreOverall:
        bestScoreOverall = bestScore
        bestPlayer = copy.deepcopy(Population[bestIndex])
    print(f"Gen: {generation}, Max: {bestScore}, Avg: {sum(populationScore)/len(populationScore)}")
    if bestScore > 18:
        break
    Population = evolvePopulation(Population, populationScore, mutationRate,bestPlayer)

with open("bestPlayer.pkl", "wb") as f:
    pickle.dump(bestPlayer, f)


