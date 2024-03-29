# Password Generator Project
import random

# Define character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# User input for password composition
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Password generation without randomizing order
password = ""
for letter in range(1, nr_letters + 1):
    letter = random.choice(letters)
    password += letter

for symbol in range(1, nr_symbols + 1):
    symbol = random.choice(symbols)
    password += symbol

for number in range(1, nr_numbers + 1):
    number = random.choice(numbers)
    password += number

print("Password without randomizing order:", password)

# Password generation with randomizing order
password = []
for letter in range(1, nr_letters + 1):
    letter = random.choice(letters)
    password += letter

for symbol in range(1, nr_symbols + 1):
    symbol = random.choice(symbols)
    password += symbol

for number in range(1, nr_numbers + 1):
    number = random.choice(numbers)
    password += number

random.shuffle(password)
randomized_password = "".join(password)

print("Password with randomizing order:", randomized_password)
