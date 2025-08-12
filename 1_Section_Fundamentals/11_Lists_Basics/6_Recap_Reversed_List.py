"""
Write a function named reverse which gets a list of numbers as argument and returns the reversed list.

For example, for [1, 2, 3], the expected output is [3, 2, 1].
"""

def reverse(lst):
    # Write code here
    lst.reverse()
    return lst

lst = list(input().split(", "))
print(reverse(lst))