"""
Slicing allows us to extract portions of a list using the following syntax: lst[start:stop]. For example consider this list:

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Getting a portion of the list:

print(numbers[2:6])
# Output: [2, 3, 4, 5]
This gets elements from index 2 (inclusive) to index 6 (exclusive)

Omitting start parameter:

print(numbers[:5])
# Output: [0, 1, 2, 3, 4]
When start is omitted, slice begins from index 0

Omitting stop parameter:

print(numbers[5:])
# Output: [5, 6, 7, 8, 9]
When stop is omitted, slice goes until the end

Create a program that receives a list as input (given) and prints the following sliced list (depends on the list length):

For odd-length lists: take the middle item and one item on each side (3 items total)
For even-length lists: take the two middle items
When dividing numbers:

/ gives you a decimal number (5/2 = 2.5)
// removes the decimal part (5//2 = 2)
For this challenge, use // because list slicing only works with whole numbers.
"""
lst = input().split(",")
# Write your code below
def slicing(lst):
    if len(lst) % 2 == 0:
        print(lst[(len(lst) // 2 - 1):(len(lst) // 2 + 1)])
    else:
        print(lst[(len(lst) // 2 -1):(len(lst) // 2 + 2)])

slicing(lst)

"""
Create a program that takes a list and prints:

For lists with 5 or more items: the first two and last two items
For lists with less than 5 items: the first and last item only
"""

input_list = input().split(', ')
# Write your code below
def if_slice(input_list):
    new = []
    if len(input_list) >= 5:
        new = (input_list[:2]) + (input_list[-2:]) 
    else:
        new.append(input_list[0])
        new.append(input_list[-1])
    print(new)

if_slice(input_list)