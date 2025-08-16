"""
Python provides several operators that can be used with sequences like lists, strings, and tuples.

Concatenation with the + operator joins two sequences together:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
After executing the above code, combined_list contains:

[1, 2, 3, 4, 5, 6]
Repetition with the * operator repeats a sequence a specified number of times:

numbers = [1, 2, 3]
repeated_numbers = numbers * 3
After executing the above code, repeated_numbers contains:

[1, 2, 3, 1, 2, 3, 1, 2, 3]
These operators work with other sequences too:

# String concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# String repetition
stars = "*" * 5  # "*****"

Create a function named create_pattern that takes two arguments:

A list of numbers (numbers).
An integer (repeats).
The function should:

Concatenate the list with itself (list + list).
Repeat the resulting list repeats times using the * operator.
Return the final pattern.
"""
def create_pattern(numbers, repeats):
    # Write your code here
    final = (numbers + numbers) * repeats
    return final

numbers = list(input().split(", "))
repeats = int(input())
create_pattern(numbers, repeats)
print(create_pattern(numbers, repeats))

"""
Create a program that receives a list of numbers as input and prints a new list that:

Contains the original list followed by its reverse
Has the first element of the original list inserted at the beginning and the last element inserted at the end
Repeats this entire sequence twice
"""

numbers = input().split()
# Write your code below
def new_list(numbers):
    list1 = numbers + numbers[::-1]
    list2 = [numbers[0]] + list1 + numbers[-1:] 
    """ Só dá pra concatenar lista com lista, numbers[0] viraria uma string, por isso colocar entre [] para virar formato lista e somar lista com lista.
    O slicing numbers[-1:] vem como lista então não precisa"""
    new = list2 * 2
    print(new)

new_list(numbers)
