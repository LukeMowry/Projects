"""
Count Words in a String - Counts the number
of individual words in a string. For added
complexity read these strings in from a text
file and generate a summary:
"""

sentence = input("Type your statement here: >> ")

sentence = list(sentence)

space_count = 1

for i in sentence:
    if i == " ":
        space_count += 1

print("There are " + str(space_count) + " words in your statement.")