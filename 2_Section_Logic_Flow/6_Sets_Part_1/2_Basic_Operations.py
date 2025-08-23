"""
Sets come with built-in operations that allow you to perform common set-related tasks efficiently.
These operations include adding elements, removing elements, and checking for the presence of elements.

Adding an element to a set:

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Output: {1, 2, 3, 4}

Removing an element from a set: (raises an error if it does not exist!)

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# Output: {1, 3}

Checking for the presence of an element:

my_set = {1, 2, 3}
print(2 in my_set)
# Output: True
print(4 in my_set)
# Output: False

Create a function named manage_set that takes three arguments: set1 (a set), element_to_add, and element_to_remove.
The function should perform the following operations:

Add element_to_add to set1.
Attempt to remove element_to_remove from set1. If the element is not in the set, do nothing.
Check if the number 5 is in set1. If it is, return the string "5 is in the set". Otherwise, return the string "5 is not in the set".
"""

def manage_set(set1, element_to_add, element_to_remove):
    # Write code here
    set1.add(element_to_add)
    if element_to_remove in set1:
        set1.remove(element_to_remove)
    if 5 in set1:
        return "5 is in the set"
    else:
        return "5 is not in the set"

set1 = set(input())
element_to_add = int(input())
element_to_remove = int(input())
print(manage_set(set1, element_to_add, element_to_remove))