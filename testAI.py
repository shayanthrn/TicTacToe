from gamePlayer import HardAIPlayer,MediumAIPlayer, EasyAIPlayer
from gameManager import GameManager

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

matches = 200
wins = 0
losses = 0

from gameManager import PlayerMark

easy = EasyAIPlayer(PlayerMark.O)
mid = MediumAIPlayer(PlayerMark.O)
hard = HardAIPlayer(PlayerMark.O)
AgentToTest = HardAIPlayer(PlayerMark.X)

for i in range(matches):
    winner = gameSimulator(easy,AgentToTest)
    if winner ==  PlayerMark.X:
        wins += 1
    else:
        losses += 1

win_rate = (wins / matches) * 100
print("\n=== Evaluation Summary ===")
print(f"🏆 Wins: {wins}")
print(f"💀 Losses: {losses}")
print(f"🔥 Win Rate: {win_rate:.2f}% against Easy AI")

wins = 0
losses = 0

for i in range(matches):
    winner = gameSimulator(mid,AgentToTest)
    if winner ==  PlayerMark.X:
        wins += 1
    else:
        losses += 1

win_rate = (wins / matches) * 100
print("\n=== Evaluation Summary ===")
print(f"🏆 Wins: {wins}")
print(f"💀 Losses: {losses}")
print(f"🔥 Win Rate: {win_rate:.2f}% against Mid AI")

wins = 0
losses = 0

for i in range(matches):
    winner = gameSimulator(hard,AgentToTest)
    if winner ==  PlayerMark.X:
        wins += 1
    else:
        losses += 1

win_rate = (wins / matches) * 100
print("\n=== Evaluation Summary ===")
print(f"🏆 Wins: {wins}")
print(f"💀 Losses: {losses}")
print(f"🔥 Win Rate: {win_rate:.2f}% against Hard AI")
