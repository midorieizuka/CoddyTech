"""
In addition to accessing the elements of a list, you can also modify them.

To modify a specific element in a list, you can assign a new value to it using its index.

Here's an example:

my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
print(my_list)
Output:

["apple", "orange", "cherry"]
banana was changed to an orange
"""
"""
Create a function named change_element that receives 3 arguments:

First argument is a list
Second argument is an index
Third argument is a new element
The function will return a modified list by changing the element in an index that is stored in the second argument with the value in the third argument.

For example with the following arguments: change_element([1, 2, 3], 0, 9) the function will return [9, 2, 3]
"""

def change_element(lst, index, new_element):
    # Write code here
        lst[index] = new_element
        return lst

lst = list(input().split(", "))
index = int(input())
new_element = input()

change_element(lst, index, new_element)
print(lst)

# Challenge

"""
Create a function named change_element that receives 3 arguments:

First argument is a list
Second argument is an index
Third argument is another list
The function should replace the element at the given index in the first list with the first element from the second list.

Example:

change_element([1, 2, 3], 1, [5, 6, 7]) should return [1, 5, 3]
"""
def change_element_2(list1, index2, list2):
    # Write your code below
    list1[index2] = list2[0]
    return list1

list1 = list(input().split(", "))
index2 = int(input())
list2 = list(input().split(", "))

change_element_2(list1, index2, list2)
print(list1)
