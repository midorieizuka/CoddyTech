"""
Create a function named filter_and_square_set that takes a set input_set as an argument.
The function should iterate over the elements in the set, filter out even numbers, and square the remaining odd numbers.
The function should return a new set containing only the squared values of the odd numbers from the input set.

For example, if the input set is {1, 2, 3, 4, 5}, the function should return {1, 9, 25}.
"""

def filter_and_square_set(input_set):
    # Write code here
    new_set = set()
    for element in input_set:
        if int(element) % 2 == 1:
            _ = int(element) * int(element)
            new_set.add(_)
    return new_set


input_set = set(input().split(", "))
filter_and_square_set(input_set)
print(filter_and_square_set(input_set))