"""
A list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
The basic syntax of a list comprehension is:

new_list = [expression for item in iterable]

Here's a breakdown of the syntax:

new_list: The new list that will be created.
expression: The value to be included in new_list. This can be a modified version of item.
for item in iterable: A loop that iterates over each element in the iterable (e.g., a list, tuple, or range).
item: The current element being processed in the loop.

Here's a simple example:

numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)
# Output: [1, 4, 9, 16, 25]

In this example, the list comprehension creates a new list called squares by taking each element n from the numbers list and squaring it.

Create a function named double_numbers that takes a list of numbers numbers as an argument.
The function should use a list comprehension to create a new list where each number in the original list is doubled.
The function should return the new list.
"""

def double_numbers(numbers):
    # Write code here
    double = [2 * n for n in numbers]
    return double

