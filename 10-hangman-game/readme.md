# 🎯 Hangman Game

A simple **command-line Hangman game built with Python**.

In this game, a random **Bible book name** is selected, and the player has to guess the word one letter at a time before running out of lives.

This is **Project 10** in my Python learning journey.

## 🎮 How It Works

- The game randomly selects a Bible book name.
- The selected word is hidden using underscores.
- You guess one letter at a time.
- Correct guesses reveal the matching letters.
- Incorrect guesses reduce your remaining lives.
- You start with **6 lives**.
- Reveal the complete word to win.
- Lose all 6 lives and the game is over.

## ✨ Features

- 🎲 Random word selection
- ❤️ 6 lives
- 🔤 Letter-by-letter guessing
- 🪦 ASCII Hangman graphics
- 🏆 Win and game-over messages
- 📖 Bible book names used as the word list

## 🛠️ Technologies Used

- Python 3
- `random` module
- Lists
- Loops
- Conditional statements
- User input
- Custom Python modules

## 📂 Project Structure

```text
10-hangman-game/
│
├── main.py
├── booknames.py
├── hangmanpics.py
└── readme.md
```

### main.py

Contains the main game logic:

- Random word selection
- User input
- Letter matching
- Lives management
- Win/loss conditions
- Game progress

### booknames.py

Contains the list of Bible book names that can be randomly selected by the game.

### hangmanpics.py

Contains the ASCII-art Hangman stages displayed according to the number of remaining lives.

## ▶️ How to Run

Make sure **Python 3** is installed.

Clone the repository:

```bash
git clone https://github.com/nandikikarunakar/my-python-projects.git
```

Navigate to the project:

```bash
cd my-python-projects/10-hangman-game
```

Run the game:

```bash
python main.py
```

## 🧠 What I Learned

This project helped me practice:

- Using the `random` module
- Working with strings and lists
- Using `for` and `while` loops
- Handling user input
- Using conditional statements
- Managing game state
- Importing custom Python modules
- Splitting a program into multiple files

## 🚀 Future Improvements

- Prevent repeated guesses from reducing lives
- Track previously guessed letters
- Validate user input
- Add a score system
- Add difficulty levels
- Add a replay option
- Add more word categories

## 📚 Python Learning Journey

This project is part of my ongoing Python practice, where I build small projects to strengthen my programming fundamentals.

> **Learn → Build → Practice → Improve → Repeat 🔁**

---

⭐ More Python projects coming soon!
