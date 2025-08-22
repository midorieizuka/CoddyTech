"""
Create a function named manage_list that takes three arguments: list1 (a list of integers), element_to_append, and index_to_remove.
The function should perform the following operations:

Append element_to_append to the end of list1.
Attempt to remove the element at index index_to_remove from list1.
If the index is out of range, do nothing.
Check if list1 has more than 3 elements.
If it does, return the string "The list has more than 3 elements".
Otherwise, return the string "The list has 3 or fewer elements"
"""

def manage_list(list1, element_to_append, index_to_remove):
    # Write code here
    list1.append(element_to_append)
    if index_to_remove <= len(list1):
        list1.pop(index_to_remove)
    if len(list1) > 2:
        return "The list has more than 3 elements"
    else:
        return "The list has 3 or fewer elements"
    
list1 = list(input())
element_to_append = int(input())
index_to_remove = int(input())

manage_list(list1, element_to_append, index_to_remove)
print(manage_list(list1, element_to_append, index_to_remove))