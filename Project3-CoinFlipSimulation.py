"""
Coin Flip Simulation - Write some code that simulates flipping
a single coin however many times the user decides. The code
should record the outcomes and count the number of tails and heads.
"""
import random

number = int(input("How many times would you like to flip the coin? >> "))
heads = 0
tails = 0

for x in range(0, number):
    result = random.randint(1,2)
    if result == 1:
        print("Outcome " + str(x+1) + " is Heads")
        heads += 1
    elif result == 2:
        print("Outcome " + str(x+1) + " is Tails")
        tails += 1

print("Total Number of Heads: " + str(heads))
print("Total Number of Tails: " + str(tails))
