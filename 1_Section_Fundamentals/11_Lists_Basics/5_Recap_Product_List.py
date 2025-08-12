"""
Write a function named prod which gets a list of numbers as argument and returns the product of all the numbers in the list.

Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.
"""

def prod(lst):
    # Write code here
    multiplication = 1
    for i in range(len(lst)):
        multiplication *= int(lst[i])
    return multiplication

lst = list(input().split(", "))
print(prod(lst))