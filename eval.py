from gamePlayer import MediumAIPlayer, EasyAIPlayer
import pickle
import numpy as np

# Load the best trained player
with open("bestPlayer.pkl", "rb") as f:
    bestPlayer = pickle.load(f)

def gameSimulator(playerA, playerB):
    from gameManager import GameManager
    gm = GameManager(enableMusic=False)
    gm.initGame()
    gm.initGameAIvsAI()
    players = [playerA, playerB]
    while True:
        cell_i, cell_j = players[gm.playerTurn - 1].think(
            gm.ultimateBoard, gm.activateMiniBoard, gm.playerTurn
        )
        result = gm.makeMoveAIvsAI(cell_i, cell_j, gm.playerTurn)
        if isinstance(result, dict):
            return gm.playerTurn  # 1 means playerA won, 2 means playerB won

# === Evaluate best player against Easy AI ===
matches = 200
wins = 0
losses = 0

for i in range(matches):
    opponent = MediumAIPlayer()
    winner = gameSimulator(bestPlayer, opponent)
    if winner == 1:
        wins += 1
    else:
        losses += 1
    print(f"Match {i+1}/{matches} → {'Win' if winner == 1 else 'Loss'}")

win_rate = (wins / matches) * 100
print("\n=== Evaluation Summary ===")
print(f"🏆 Wins: {wins}")
print(f"💀 Losses: {losses}")
print(f"🔥 Win Rate: {win_rate:.2f}% against Easy AI")
