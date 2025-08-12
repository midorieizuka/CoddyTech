"""
Iteration means going through elements one by one in a sequence. With lists, we can access each element systematically using different methods.

The most common way to iterate through a list is using a for loop:

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
Output:

apple
banana
orange
"""

# Create a program that receives a list as input (given), and prints a new list containing only the words longer than 5 characters

lst = input().split(",")
# Write your code below
def longer(lst):
    new = []
    for item in lst:
        if len(item) > 5:
            new.append(item)
    return new

longer(lst)
print(longer(lst))

# Challenge: Create a program that receives a list of numbers as input (given), and prints the sum of all even numbers in the list.

numbers = input().split(',')
# Write your code below
sum_even = 0
for item in numbers:
    if int(item) % 2 == 0:
        sum_even += int(item)

print(sum_even)
