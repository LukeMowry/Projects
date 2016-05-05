"""
Binary to Decimal and Back Converter -
Develop a converter to convert a decimal
number to binary or a binary number to its decimal equivalent.
"""

number = input("Enter your integer or binary number? >> ")

if "0b" in number:
    print(int(number, 2))
else:
    transformed = int(number)
    print(bin(transformed))
