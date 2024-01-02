# ASCII art representations of rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of ASCII art for rock, paper, and scissors
sign = [rock, paper, scissors]

# Import the random module for computer's choice
import random

# Generate a random number for the computer's choice (0 for rock, 1 for paper, 2 for scissors)
comp_chose = random.randint(0, 2)
comp = sign[comp_chose]

# Get user's choice (0 for rock, 1 for paper, 2 for scissors)
you_chose = int(input("Choose between 0, 1, 2. 0 means rock, 1 means paper, 2 means scissors. \n"))

# Check if the user's choice is valid
if you_chose >= 3 or you_chose < 0:
    print("Invalid!")
else:
    you = sign[you_chose]
    print(f"You Chose: {you}")
    print(f"Computer Chose:  {comp}")

    # Determine the winner or if it's a draw
    if you_chose == 0 and comp_chose == 2:
        print("You Win!")
    elif you_chose == 2 and comp_chose == 1:
        print("You Win!")
    elif you_chose == 1 and comp_chose == 0:
        print("You Win!")
    elif you_chose == 0 and comp_chose == 1:
        print("You Lose!")
    elif you_chose == 2 and comp_chose == 0:
        print("You Lose!")
    elif you_chose == 1 and comp_chose == 2:
        print("You Lose!")
    elif you_chose == comp_chose:
        print("Draw, try again!")
    else:
        print("Invalid")
