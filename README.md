<div align="center">

# 🐍 Python Mini Projects Collection

### A curated collection of beginner-to-intermediate Python projects demonstrating core programming concepts.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Projects](https://img.shields.io/badge/Projects-7-blueviolet?style=for-the-badge)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Outfit&weight=700&size=22&pause=1000&color=7C3AED&center=true&vCenter=true&width=600&lines=CLI+Games+%7C+Utilities+%7C+OOP+%7C+Algorithms;Built+by+Muhammad+Suleman;Learning+%2B+Building+%2B+Shipping+%F0%9F%9A%80" alt="Typing SVG" />

</div>

<br/>

---

## 📂 Project Directory

| # | Project | File | Category | Key Concepts |
|---|---------|------|----------|-------------|
| 1 | 🎮 [Hangman Game](#-1-hangman-game) | `Hangman.py` | 🎲 Game | Loops, Sets, ASCII Art, Input Validation |
| 2 | 🔢 [Number Guessing Game (with ASCII Hangman)](#-2-number-guessing-game-with-ascii-hangman) | `guessing_game.py` | 🎲 Game | Random, ASCII Art, Game State Management |
| 3 | 🎯 [Random Number Guessing](#-3-random-number-guessing) | `RandNUM.py` | 🎲 Game | Random, Loops, Conditionals |
| 4 | 🧮 [Calculator](#-4-calculator) | `calculator.py` | 🛠️ Utility | Functions, Error Handling, Menu Loop |
| 5 | 📝 [To-Do List App](#-5-to-do-list-app) | `todo_list.py` | 🛠️ Utility | Lists, CRUD Operations, Menu System |
| 6 | 🏦 [Bank Account System](#-6-bank-account-system) | `Bank_sys.py` | 🏗️ OOP | Classes, Methods, Encapsulation |
| 7 | 🔐 [FizzBuzz & Patterns](#-7-fizzbuzz--patterns) | `RandomPass.py` | 🧠 Algorithm | Math, Modular Arithmetic, Patterns |

---

## 📋 Detailed Project Descriptions

### 🎮 1. Hangman Game
**`Hangman.py`** — A classic word-guessing CLI game.

```
  +---+
  O   |
 /|\  |
 / \  |
      |
=========
Word to guess: p y _ _ _ n
Attempts remaining: 3
```

**Features:**
- 🎯 Random word selection from a programming-themed word bank
- 🔤 Letter-by-letter guessing with duplicate detection
- ⚡ Real-time display of guessed letters and remaining attempts
- ✅ Input validation (single letters only)
- 🏆 Win/lose detection with emoji feedback

**Concepts Demonstrated:** `random`, `sets`, `loops`, `string manipulation`, `input validation`

---

### 🔢 2. Number Guessing Game (with ASCII Hangman)
**`guessing_game.py`** — A full-featured Hangman game with visual ASCII art gallows.

**Features:**
- 🖼️ **7-stage ASCII art gallows** that progressively draws as wrong guesses increase
- 🎯 Programming-themed word bank (`python`, `variable`, `dictionary`, etc.)
- 📊 Live game state: remaining attempts, tried letters, word progress
- 🔄 Duplicate guess detection with warning messages
- 🎉 Victory and Game Over screens with emoji art

**Concepts Demonstrated:** `lists`, `ASCII art`, `game state management`, `set operations`, `f-strings`

---

### 🎯 3. Random Number Guessing
**`RandNUM.py`** — A quick number guessing game (1–50 range).

**Features:**
- 🎲 Random target number generation (1–50)
- ⬆️⬇️ Higher/lower feedback after each guess
- 🚪 Quit option with `Q` key
- ✅ Instant win detection

**Concepts Demonstrated:** `random.randint()`, `while True` loops, `type casting`, `conditionals`

---

### 🧮 4. Calculator
**`calculator.py`** — A clean, menu-driven arithmetic calculator.

**Features:**
- ➕➖✖️➗ Four operations: Add, Subtract, Multiply, Divide
- 🛡️ Division-by-zero protection with `ValueError`
- 🔄 Continuous calculation loop (keeps running until user quits)
- ⚠️ Input validation for non-numeric entries
- 📐 Clean function-based architecture

**Concepts Demonstrated:** `functions`, `error handling (try/except)`, `modular design`, `f-strings`

---

### 📝 5. To-Do List App
**`todo_list.py`** — A terminal-based task management application.

**Features:**
- 📋 **View** all tasks with numbered indices
- ➕ **Add** new tasks dynamically
- 🗑️ **Remove** tasks by number with boundary checking
- 🔄 Persistent menu loop until user exits
- ⚠️ Error handling for invalid task numbers

**Concepts Demonstrated:** `lists`, `CRUD operations`, `enumerate()`, `input validation`, `menu-driven architecture`

---

### 🏦 6. Bank Account System
**`Bank_sys.py`** — A simple OOP-based banking system.

**Features:**
- 💰 **Credit** money into account with balance update
- 💳 **Debit** money with insufficient balance detection
- 📊 **Balance inquiry** method
- 🏗️ Object-oriented design with `__init__`, instance methods

**Concepts Demonstrated:** `classes`, `__init__` constructor`, `instance methods`, `self`, `OOP principles`

---

### 🔐 7. FizzBuzz & Patterns
**`RandomPass.py`** — Classic FizzBuzz algorithm implementation.

**Features:**
- 🔢 FizzBuzz logic (divisible by 3 → Fizz, by 5 → Buzz, by 15 → FizzBuzz)
- 📐 Mathematical pattern generation (repunit squares)
- 🧠 Clean, Pythonic implementation

**Concepts Demonstrated:** `modular arithmetic`, `for loops`, `conditionals`, `math patterns`

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** installed on your system

### Run Any Project
```bash
# Clone the repository
git clone https://github.com/Sallo70/python-mini-projects.git

# Navigate to the project folder
cd python-mini-projects

# Run any project
python Hangman.py
python calculator.py
python todo_list.py
python guessing_game.py
python RandNUM.py
python Bank_sys.py
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Usage |
|-----------|-------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core language for all projects |
| `random` | Random number/word generation |
| `OOP` | Bank Account System design |
| `CLI` | All projects use terminal I/O |

</div>

---

## 👤 Author

<div align="center">

**Muhammad Suleman**

[![GitHub](https://img.shields.io/badge/GitHub-Sallo70-181717?style=for-the-badge&logo=github)](https://github.com/Sallo70)
[![Email](https://img.shields.io/badge/Email-salimananp@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:salimananp@gmail.com)

</div>

---

<div align="center">

### ⭐ If you found this useful, give it a star!

Made with ❤️ by **Muhammad Suleman**

</div>
