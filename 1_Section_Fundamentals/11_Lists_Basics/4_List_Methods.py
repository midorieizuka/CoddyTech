"""
Lists are packed with many methods (functionalities). To access a method, write:

some_list.method()
Here is a list of the basic methods:

append(element) - adds an element to the end of the list
clear() - removes all elements from the list
pop(index) - removes an element at the specified index
reverse() - reverses the order of the list
sort() - sorts the list in ascending order
Here is an example of how to use the append method:

my_list = ["orange", "banana", "apple"]
my_list.append("strawberry")
print(my_list)
This will output ["orange", "banana", "apple", "strawberry"].

Example of the clear method:

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)
This will output [].

Example of the sort method:

my_list = [1, 9, 2, 3]
my_list.sort()
print(my_list)
This will output [1, 2, 3, 9].
"""

def merge(lst1, lst2):
    # Write code here
    new = lst1 + lst2
    new.sort()
    return new

lst1 = list(input().split(", "))
lst2 = list(input().split(", "))

print(merge(lst1, lst2))

"""
Create a function named combine_and_filter that receives 2 arguments:

First argument is a list of numbers
Second argument is an integer threshold value
The function should:

Filter out all numbers that are less than or equal to the threshold value
Sort the remaining numbers
Return the resulting list
For example, calling combine_and_filter([1, 5, 3, 2, 7, 4], 3) should return [4, 5, 7].
"""

def combine_and_filter(lst, threshold):
    # Write code here
    new = []
    for i in range(len(lst)):
        if int(lst[i]) > threshold:
            new.append(lst[i])
    new.sort()
    print(new)

lst = list(input().split(", "))
threshold = int(input())

combine_and_filter(lst, threshold)
