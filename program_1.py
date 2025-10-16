
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

    # Write your logic to generate 2 numbers between 1 and 6 here

import random

def randDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

total_sum = 0
num_rolls = 100

for _ in range(num_rolls):
    total_sum += randDice()

average_roll = total_sum / num_rolls

print(f"The average of the 100 rolls is: {average_roll:.2f}")
    # Sum 2 numbers

    # return sum to calling function

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
