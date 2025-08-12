"""
The enumerate() function allows you to loop through a sequence (like a list, tuple, or string) while keeping track of the index position of each item.

without enumerate() we would access both the index and the value the following way:

fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
enumerate() is a more elegant way to get both index and value:

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

Both examples will output:

Index 0: apple
Index 1: banana
Index 2: orange
"""

# Write a program that receives a list of numbers as input (given), and prints a list of the indices of the numbers that are either below 50 or they are divisible by 5. 

lst = list(map(int, input().split(",")))
# Write your code below
new = []
for i in range(len(lst)):
    if lst[i] < 50 or lst[i] % 5 == 0:
        new.append(i)

print(new)

"""
Challenge:

Write a program that receives a list of words as input (given), and prints a list of the indices of the words that are either longer than 3 characters or start with the letter 'a' (case-sensitive).
To check if a string starts with some substring use: str.startswith("substring")
"""

lst = input().split()
# Write your code below
new = []
for index, item in enumerate(lst):
    if len(item) > 3 or item.startswith("a"):
        new.append(index)
print(new)