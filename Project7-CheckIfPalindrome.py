"""
Check if Palindrome - Checks if the string
entered by the user is a palindrome.
That is that it reads the same
forwards as backwards like “racecar”
"""

sentence = input("Enter your word or sentence: >> ")
sentence = sentence.replace(" ", "")
sentence = list(sentence)
altered = sentence[::-1]

if sentence == altered:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
