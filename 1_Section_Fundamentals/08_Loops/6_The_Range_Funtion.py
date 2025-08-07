"""
The range() function in Python generates a sequence of numbers, which is commonly used with for loops to repeat code a specific number of times.

Create a range that starts at 0 and ends at 4:

for i in range(5):
    print(i)

This will output:

0
1
2
3
4

You can also specify a start value:

for i in range(2, 6):
    print(i)

This will output:

2
3
4
5

And you can specify a step value (increment):

for i in range(1, 10, 2):
    print(i)

This will output:

1
3
5
7
9
"""

"""
Create a function named print_range that takes three parameters:

start - the starting number (inclusive)
end - the ending number (exclusive)
step - the increment value
The function should print all numbers from start to end (not including end) with the given step increment, each on a new line.
"""

def print_range(start, end, step): # def = definir função
    for i in range (start, end, step): # Write your code here
        print(i)
    pass # pass = finalizar função

# Get input from user
start = int(input())
end = int(input())
step = int(input())

# Call the function
print_range(start, end, step)

# Challenge
"""
Create a program that performs the following tasks using range():

Print all numbers between 30 to 80 that are divisible by 4
Print the first 8 odd numbers starting from 15
Count backwards from 50 to 10, showing only numbers divisible by 5
Find the product of all numbers from 1 to 30 that are divisible by 3
When printing a number use the following code to print:

print(num, end=", ")
This will not create a new line after the number, instead it will add ,
"""

# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for i in range(30,81):
    if i % 4 == 0:
        print(i, end=", ")

print()  # new line
# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
count = 0
for i in range(15, 100):
    if count < 8:
        if i % 2 == 1:
            count += 1
            print(i, end=", ")

print()  # new line
# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for i in range(50, 9, -1): # para contagem decrescente colocar step como -1
    if i % 5 == 0:
        print(i, end=", ")

print()  # new line
# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
# Your code here
res = 1
for i in range(1, 31):
    if i % 3 == 0:
        res *= i
print(res)