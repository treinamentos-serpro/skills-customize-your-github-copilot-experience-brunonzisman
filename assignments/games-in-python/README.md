
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses strings, loops, conditionals, and user input to let the player guess a hidden word.

## 📝 Tasks

### 🛠️ Word Selection and Display

#### Description
Create the game logic that selects a random word from a list and displays the word progress with underscores for unguessed letters.

#### Requirements
Completed program should:

- Select a random word from a predefined list.
- Display the current word progress using `_` for letters that are still hidden.
- Reveal letters in the correct positions when the player guesses correctly.

### 🛠️ Guess Input and Tracking

#### Description
Handle player input for letter guesses and keep track of correct and incorrect guesses.

#### Requirements
Completed program should:

- Accept a letter guess from the player.
- Prevent repeated guesses from counting multiple times.
- Track incorrect guesses and remaining attempts.

### 🛠️ Game End Conditions

#### Description
Finish the game by checking win and loss conditions, then display a final message.

#### Requirements
Completed program should:

- End the game when the player guesses all letters in the word.
- End the game when the player runs out of allowed incorrect attempts.
- Display a clear win or lose message at the end.
