import random

# Importing the word list and hangman art from external modules
from hangman_words import word_list
from hangman_art import logo, stages

# Select a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize game variables
end_of_game = False
lives = 6

# Display the Hangman logo
print(logo)

# Create a list to store the displayed word with underscores
display = ["_" for _ in range(word_length)]

# Main game loop
while not end_of_game:
    # User input for guessing a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check each position in the chosen word for the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            # Update the display with the guessed letter
            display[position] = letter

    # Check if the guessed letter is not in the chosen word
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        # Decrease the number of lives
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Display the current state of the word with underscores and guessed letters
    print(f"{' '.join(display)}")

    # Check if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current hangman stage
    print(stages[lives])
