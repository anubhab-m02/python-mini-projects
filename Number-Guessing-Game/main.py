from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#checks the user answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#sets the number of chances the user gets to 
def set_difficulty():
    level = input("Choose the number of turns. Type 'easy' for 10 turns or 'hard' for 5 turns: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Error!")

def game():
    print("The Number Guessing Game! \nThe computer thinks of a number, you win if you guess the number!")
    turns = set_difficulty()
    answer = randint(1,100)
    print("The number is between 1 and 100.")

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        #no of turns remaining for the user to guess
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The right number was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")
        

game()