"""
Find e to the Nth Digit - Just like
the previous problem, but with e instead
of PI. Enter a number and have the program
generate e up to that many decimal places.
Keep a limit to how far the program will go.
"""
import math

limiter = int(input("How many decimal places would you like for your 'e'? >> "))

while limiter > 100:
    print("That number is too large.")
    limiter = int(input("How many decimal places would you like for your 'e'? >> "))
else:
    print(str(math.e)[0: limiter + 2])