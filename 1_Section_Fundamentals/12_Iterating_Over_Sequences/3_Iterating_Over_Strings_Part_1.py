"""
Similar to lists, you can iterate over strings:

text = "Hey"
for char in text:
    print(char)
Output:

H
e
y
Using index:

for i in range(len(text)):
    print(f"position {i}: {text[i]}")
Output:

position 0: H
position 1: e
position 2: y
"""
"""
Create a program that receives a string as input, and it prints how many times the character p (or P) is in the string.

Some chars might be uppercase, use char.lower() to convert it to lowercase.
"""

text = input()
# Write your code below
letter_p = 0
for char in text:
    if char.lower() == "p":
        letter_p += 1
print(letter_p)

"""
Challenge: 

Create a program that receives a string as input, and it prints how many times the character s is in the string.

Some chars might be uppercase, use char.lower() to convert it to lowercase.
"""

text = input()
# Write your code below
letter_s = 0
for char in text:
    if char.lower() == "s":
        letter_s += 1
print(letter_s)
