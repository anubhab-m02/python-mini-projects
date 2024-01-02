# Hangman Game

## Overview

Hangman is a word guessing game where the player tries to guess a word one letter at a time. For each incorrect guess, a part of a hangman is drawn. The player wins by guessing all the letters in the word before running out of lives.

## How to Play

1. Run the script using a Python interpreter.

    ```bash
    python hangman_game.py
    ```

2. The game will randomly select a word from the provided word list.

3. The hangman art and the initial word display will be shown.

4. You will be prompted to guess a letter.

5. For each correct guess, the corresponding positions in the word will be revealed.

6. For each incorrect guess, a part of the hangman will be drawn, and you will lose a life.

7. Keep guessing until you either guess the entire word or run out of lives.


## Project Structure

- `hangman_game.py`: The main script for the Hangman game.
- `hangman_art.py`: Contains ASCII art for the Hangman stages.
- `hangman_words.py`: Contains a list of words for the game.
