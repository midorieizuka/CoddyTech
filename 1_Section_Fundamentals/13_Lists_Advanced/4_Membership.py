"""
You can check whether an element is in the a list or not (in, not in):

2 in [1, 2]      # True
3 not in [1, 2]  # True
3 in [1, 2]      # False

Create a program that receives two lists and prints a new list of all elements that are in the first list but NOT in the second list.
"""

lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
new_lst = []
for item in lst1:
    if item not in lst2:
        new_lst.append(item)
print(new_lst)

"""
Create a function called not_mutual_friends that takes two lists of names representing two people's friend lists.
The function should return a list of names that are friends with only one person (not mutual friends).

Let's say we have:

Person A's friends: ["John", "Emma", "Mike", "Sarah"]
Person B's friends: ["Emma", "Tom", "Sarah", "Peter"]
When we call not_mutual_friends with these two lists, it should return: ["John", "Mike", "Tom", "Peter"]

Explanation:

"John" and "Mike" are only friends with Person A
"Tom" and "Peter" are only friends with Person B
"Emma" and "Sarah" are mutual friends (friends with both people), so they are not included in the result
"""

def not_mutual_friends(list1, list2):
    # Write your code below
    not_mutual = []
    for item in list1:
        if item not in list2:
            not_mutual.append(item)
    for item in list2:
        if item not in list1:
            not_mutual.append(item)
    print(not_mutual)

list1 = input().split(",")
list2 = input().split(",")
not_mutual_friends(list1, list2)