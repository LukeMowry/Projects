"""
Fibonacci Sequence - Enter a number
and have the program generate the Fibonacci
sequence to that number or to the Nth number.
"""

sequence_finder = int(input("Feel free to enter a number. If it's a number in the Fibonacci Sequence, " + "\n"
                            "then the sequence up to that number will be returned, otherwise the sequence up " + "\n"
                            "to the index specified will be returned. >> "))
i = 0
x = 0
numbers = [0, 1, 1]

while i < 1000000:
    i = numbers[-1] + numbers [-2]
    if i < 1000000 :
        numbers.append(i)


if sequence_finder in numbers:
    for x in numbers:
        if x > sequence_finder:
            break
        else:
            print(x)
else:
    print(numbers[:sequence_finder])
