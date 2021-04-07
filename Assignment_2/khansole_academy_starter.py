"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

print("I am thinking of a number between 1 and 99")
count_correct = 0
while True:    
    try:
        print('')
        # Generate two random operands number between 10 and 99
        operand_1 = random.randint(10, 99)
        operand_2 = random.randint(10, 99)
        print("What is {} + {}?".format(operand_1, operand_2))
        # User enter a  answer
        user_answer = int(input('Your Answer: '))
        #Check if user answered an integer
    except ValueError as ve:
        count_correct = 0
        print("Enter a valid integer")
    else:
        correct_answer = operand_1 + operand_2
        if user_answer == correct_answer:
            count_correct += 1
            print("Correct! You've gotten {} correct in a row".format(count_correct))
            if count_correct < 3:
                continue
            else:
                print("Congratulations! You mastered addition")
                break
        else:
            count_correct = 0
        print('Incorrect. The expected answer is {}'.format(correct_answer))

