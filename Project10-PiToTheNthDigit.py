"""
Find PI to the Nth Digit - Enter a
number and have the program generate
PI up to that many decimal places.
Keep a limit to how far the program will go.
"""
import math

limiter = int(input("How many decimal places would you like for your Pi? >> "))

while limiter > 100:
    print("That number is too large.")
    limiter = int(input("How many decimal places would you like for your Pi? >> "))
else:
    print(str(math.pi)[0: limiter + 2])