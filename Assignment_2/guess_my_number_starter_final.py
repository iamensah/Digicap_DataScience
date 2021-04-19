"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
print("I am thinking of a number between 1 and 99")
#Generate a random number between 1 and 99
random_guess = random.randint(1, 99)
#While loop for user to guess until they get the correct answer
while True:
    try:
        # User enters a guess number
        user_guess = int(input('Enter a guess: '))
        # Check if the number is an integer
    except ValueError:
        print('Please input valid integer between(1 and 99)')
    #continue if user enter a valid integer
    else:
        #test if integer entered by user is between 1 and 99
        if 1 <= user_guess <= 99:
            #check if the number entered by user is greater than the random guess number
            if user_guess > random_guess:
                print("Your Guess is TOO HIGH")
                print("Try again")
            #check if the number entered by user is less than the random guess number
            elif user_guess < random_guess:
                print("Your Guess is TOO LOW")
                print("Try again")
            else:
                #congratulate user if their guess is same as the random guess
                print("Congrat! The number was:", random_guess)
                break
        else:
            #prompt user to enter an integer between 1 and 99
            print('Please input valid integer between(1 and 99)')
