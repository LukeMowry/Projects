"""
Calculator - A simple calculator to do basic operators.
Make it a scientific calculator for added complexity.
"""

operation = input("Would you like to add, subtract, multiply, or divide? >> ").lower()
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

total = 0


def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


def multiply(x,y):
    return x * y


def divide(x,y):
    return x / y

if operation == "add":
    print(add(num1,num2))
elif operation == "subtract":
    print(subtract(num1,num2))
elif operation == "multiply":
    print(multiply(num1,num2))
elif operation == "divide":
    print(divide(num1,num2))
