"""
List comprehensions become even more powerful when you add conditional logic.
This allows you to create new lists based on existing lists, filtering and transforming elements based on specified conditions.

The syntax for adding a condition to a list comprehension is:

new_list = [expression for item in iterable if condition]

Here's a breakdown of the syntax:

new_list: The new list that will be created.
expression: The value to be included in new_list. This can be a modified version of item.
for item in iterable: A loop that iterates over each element in the iterable (e.g., a list, tuple, or range).
item: The current element being processed in the loop.
if condition: A filter that determines whether the current item should be included in new_list. The expression is only evaluated if the condition is True.

Here's an example:

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
# Output: [2, 4, 6]
In this example, the list comprehension creates a new list called evens by taking each element n from the numbers list and including it only if it is even (i.e., n % 2 == 0).

Create a function named filter_and_square that takes a list of numbers numbers as an argument.
The function should use a list comprehension to create a new list that includes the squares of only the positive numbers from the original list.
The function should return the new list.
"""

def filter_and_square(numbers):
    # Write code here
    new = [n*n for n in numbers if n > 0]
    return new

numbers = [-3, -2, 0, 1, 2, 3]
filter_and_square(numbers)
print(filter_and_square(numbers))