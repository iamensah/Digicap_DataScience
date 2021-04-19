"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
print("I am thinking of a number between 1 and 99")
#Generate a random number between 1 and 99
random_guess = random.randint(1, 99)
while True:
    try:
        # User enter a guess number
        user_guess = int(input('Enter a guess: '))
        # Check if the number is between 1 and 99
    except ValueError:
        print('Please input valid integer between(1 and 99)')
    else:
        if 1 <= user_guess <= 99:
            if user_guess > random_guess:
                print("Your Guess is TOO HIGH")
                print("Try again")
            elif user_guess < random_guess:
                print("Your Guess is TOO LOW")
                print("Try again")
            else:
                print("Congrat! The number was:", random_guess)
                break
