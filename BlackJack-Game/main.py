import random 
# importing the random module to select cards at random
from art import logo
# importing the ascii art for blackjack from art.py
import os
#importing the os library to use os.system('cls') so the console is cleared if the user wants to play again

# the cards are chosen at random using the deal_card function from a selected set of card values
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

#the score of the given set of cards is calculated
def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# the scores of the user and the computer are compared using the compare_scores function
def compare_scores(user_score, computer_score):
    if user_score>21 and computer_score>21:
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

# play_game function is defined
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

# the game starts bruh
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()
