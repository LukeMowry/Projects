"""
Reverse a String - Enter a string and the program will reverse it and print it out.
"""

sentence = str(input("Insert your sentence here >> "))
wordlist = list(sentence)
reversedlist = wordlist[::-1]
print("".join(reversedlist))
