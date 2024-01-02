import random 
from art import logo
import os

def deal_card():
    
    # Function to randomly select a card from a set of card values.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):

    # Function to calculate the total score of a set of cards.
    # Handles the case where an Ace can be counted as 1 or 11.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(user_score, computer_score):

    # Function to compare the scores of the user and the computer.
    # Returns the result of the game based on the scores.
    if user_score > 21 and computer_score > 21:
        return "You went over 21, you lose."
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose, computer has a BlackJack."
    elif user_score == 0:
        return "You win, you have a BlackJack!"
    elif user_score > 21:
        return "You went over 21, you lose."
    elif computer_score > 21:
        return "Computer went over, you win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():

    # Function to start and play a game of Blackjack.
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial two cards for the user and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check if the game is over for the user
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to play
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    # Display the final hands and scores
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

# Start the game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')  # Clear the console if the user wants to play again
    play_game()
