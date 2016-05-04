"""
Next Prime Number - Have the program find prime
numbers until the user chooses to stop asking for the next one.
"""

import sys

response = input("Would you like a prime number? >> ").lower()

prime_numbers = []
index = 0

def is_prime(a):
    return all(a % i for i in range(2, a))

for x in range(2, 100):
    if is_prime(x):
        prime_numbers.append(x)
while index < 100:
    if response == "yes":
        print(prime_numbers[index])
        response2 = input("Would you like another prime number? >> ").lower()
        if response2 == "yes":
            index += 1
        else:
            print("Ok, goodbye.")
            sys.exit()
    else:
        print("Ok, goodbye.")
        sys.exit()