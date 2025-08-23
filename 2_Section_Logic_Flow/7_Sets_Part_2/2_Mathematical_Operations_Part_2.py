"""
Let's continue exploring mathematical operations with sets, focusing on more advanced concepts such as the intersection of multiple sets
and the difference between multiple sets.

Intersection of Multiple Sets (& or intersection()): You can find the common elements among multiple sets by using the & operator or the intersection() method
repeatedly or by passing multiple sets to the intersection() method.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

intersection_result = set1 & set2 & set3
# Or
intersection_result = set1.intersection(set2, set3)
print(intersection_result)
# Output: {3}

Difference Between Multiple Sets (- or difference()): You can find the elements that are unique to the first set compared to multiple other
sets by using the - operator or the difference() method. This is done by subtracting multiple sets from the first set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set3 = {5, 6, 7}
difference_result = set1 - set2 - set3
# Or
difference_result = set1.difference(set2, set3)
print(difference_result)
# Output: {1, 2, 3}

In these examples, we first find the intersection of three sets, resulting in a set containing only the element common to all three sets.
Then, we find the difference between multiple sets, resulting in a set containing only the elements that are unique to set1 after subtracting
the elements of set2 and set3.

Imagine you are managing an exclusive club where members are split into different groups based on their interests. You want to find out:

Who are the members that share a common interest in all groups?
Who are the truly unique members who belong only to the first group and not to any others?

Write a program that:

Takes three sets, group1, group2, and group3, representing members of three interest groups.
Finds and prints the intersection of all three groups (members common to all groups).
Finds and prints the difference of group1 from the other two groups (members only in the first group).
"""

group1 = eval(input())
group2 = eval(input())
group3 = eval(input())

# Write your code below

intersection_result = group1 & group2 & group3
difference_result = group1 - group2 - group3

# Print the results
print("Members in all groups:", sorted(list(intersection_result)))
print("Unique members in group1:", sorted(list(difference_result)))