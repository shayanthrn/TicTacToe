Welcome to **Ultimate Tic Tac Toe** — a strategic twist on the classic game, featuring 9 mini Tic Tac Toe boards.
At first, I was trying to achieve a real AI by using genetic algorithm and NN but I failed. However, I put a more interesting HardAI as replacement.
---

## 🎯 Objective

The goal is simple:  
Win any **one mini-board** by getting **three of your marks in a row** — horizontally, vertically, or diagonally — within that mini-board.

But there's a twist — **each move determines where your opponent must play next.**

---

## 🧩 Game Setup

1. The game consists of **9 mini Tic Tac Toe boards**, arranged in a **3×3 grid**.  
2. Each mini-board is a standard **3×3 Tic Tac Toe** layout.  
3. Players take turns placing their mark (**X** or **O**) on the boards.  
4. The **first move must be made on the center mini-board**.

---

## ⚙️ Gameplay Rules

1. On your turn, you **must play on the active mini-board**.  
2. The **cell** where you place your mark determines the **next mini-board** your opponent must play in.  
   - Example: If you play in the top-right cell, your opponent must play in the **top-right mini-board**.  
3. If the target mini-board is **already full**, the game automatically selects the **next available mini-board**.  
4. Players alternate turns until a player wins a mini-board.  

---

## 🧠 Difficulty Levels

### 🟢 Easy  
- Plays **completely random moves** within the allowed mini-board.  
- No strategy involved — perfect for beginners.

### 🟡 Medium  
- Implements **basic strategic logic**:
  - Blocks opponent’s winning moves.  
  - Takes winning moves when available.

### 🔴 Hard  
- Implements **advanced strategic logic**
- I was hoping to make it work with Neural Networks but I failed. The R&D code is available in failedInvestigationCode folder.
---



## 🧠 Technology

- **Language:** Python  
- **Framework:** Pygame  
- **AI Training:** Genetic Algorithm + Neural Network - FAILED 

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pygame installed  

### How to Run
  pip install -r requirements.txt
  python launcher.py