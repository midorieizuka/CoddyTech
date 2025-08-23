"""
In Python, you can convert a list to a set using the set() function.
This is called casting.
Casting to a set transforms the list into a set, which contains only unique elements.

Example:

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)
# Output: {1, 2, 3, 4, 5}

Write a function named remove_duplicates that takes a list of numbers as an argument and returns a new list with duplicates removed while preserving the original order of elements.

Example Input:

numbers = [1, 2, 2, 3, 4, 4, 5]
Example Output:

[1, 2, 3, 4, 5]
Use the properties of sets to simplify your solution while keeping the order intact!
"""

def remove_duplicates(numbers):
    # Write code here
    new_list = []
    seen_set = set()
    for item in numbers:
        if item not in seen_set:
            seen_set.add(item)
            new_list.append(item)
    return new_list

numbers = list(input().split(", "))

remove_duplicates(numbers)
print(remove_duplicates(numbers))