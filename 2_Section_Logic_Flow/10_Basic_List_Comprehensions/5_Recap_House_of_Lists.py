"""
Create a function named house_of_lists that takes a list of lists list_of_lists as an argument.
Each inner list contains numbers. The function should use list comprehensions to perform the following operations:

Filter out inner lists that have a sum greater than 50.
From the remaining inner lists, extract numbers that are less than 5.
Combine all extracted numbers into a single list.
Return the combined list of numbers.
"""

def house_of_lists(list_of_lists):
    # Write code here
    lst_less_than_50 = [n for inner in list_of_lists for n in inner if sum(inner) < 50]
    popping_5 = [n for n in lst_less_than_50 if n < 5]
    numbers = list(popping_5)
    return numbers

list_of_lists = [[10, 20, 30], [1, 2, 3], [5, 50, 5], [0, 3, 6, 9]]
house_of_lists(list_of_lists)
print(house_of_lists(list_of_lists))