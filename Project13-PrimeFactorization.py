"""
Prime Factorization - Have the user
enter a number and find all Prime Factors
(if there are any) and display them.
"""

import math
number = int(input("Which number would you like the prime factors of? >> "))
prime_factors =[]

def is_prime(a):
    return all(a % i for i in range(2, a))

for x in range(2, number):
    if is_prime(x) and (number % x == 0):
        prime_factors.append(x)
print(prime_factors)