"""
Count Vowels - Enter a string and the
program counts the number of vowels in
the text. For added complexity have it
report a sum of each vowel found.
"""

sentence = input("Enter your word or sentence: >> ")

sentence = list(sentence)
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
total_count = 0

for i in sentence:
    if i == "a" or i == "A":
        a_count += 1
        total_count += 1
    elif i == "e" or i== "E":
        e_count += 1
        total_count += 1
    elif i == "i" or i == "I":
        i_count += 1
        total_count += 1
    elif i == "o" or i == "O":
        o_count += 1
        total_count += 1
    elif i == "u" or i == "U":
        u_count += 1
        total_count += 1

print("There a total of " + str(a_count) + " A's.")
print("There a total of " + str(e_count) + " E's.")
print("There a total of " + str(i_count) + " I's.")
print("There a total of " + str(o_count) + " O's.")
print("There a total of " + str(u_count) + " U's.")
print("There a total of " + str(total_count) + " vowels.")
