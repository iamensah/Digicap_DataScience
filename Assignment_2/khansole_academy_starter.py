"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random

print("Mastering two(2) digits addition:")

# count_correct variable initialised to zero. It is use to check the number of correct answer
count_correct = 0
#Wile loop. It exit when user get three correct answers in a row 
while True:    
    try:
        print('')
        # Generate two random integer numbers(operand_1 and operand_2) between 10 and 99
        operand_1 = random.randint(10, 99)
        operand_2 = random.randint(10, 99)
		#Create an addition question in the form operand_1 + operand_2
        print("What is {} + {}?".format(operand_1, operand_2))
        # User enters an  answer
        user_answer = int(input('Enter Your Answer: '))
    #Check if the answer entered by user is an integer
    except ValueError:
		#set count_correct = 0 if answer is not an integer
        count_correct = 0
        print("Enter a valid integer")
    else:
		# Calculation of correct answer
        correct_answer = operand_1 + operand_2
		#Check if answer entered by user is correct
        if user_answer == correct_answer:
            count_correct += 1 #Add 1 to count_correct if user answer is correct
            print("Correct! You've gotten {} correct answers in a row".format(count_correct))
			#Continue in loop if correct answers in a row is less than 3
            if count_correct < 3:
                continue
            else:
				#congratulate user if they get three correct answers in a row then, exit while loop with break 
                print("Congratulations! You mastered addition")
                break
        else:
			# set number of correct answers in a row to zero, if user get answer wrong
            count_correct = 0
			#Provide user with the correct answer
            print('Incorrect. The expected answer is {}'.format(correct_answer))

