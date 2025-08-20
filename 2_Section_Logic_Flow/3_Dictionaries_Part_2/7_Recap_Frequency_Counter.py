"""
Create a function named frequency_counter that takes a list data_list as an argument.
The function should count the frequency of each item in the list and return a dictionary where the keys
are the unique items from the list and the values are the counts of how many times each item appears.

For example, if the input list is [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], the function should return a dictionary like this:

{1: 1, 2: 2, 3: 3, 4: 4}
"""

def frequency_counter(data_list):
    # Write code here
    dictionary = {}
    count = 0
    for item in data_list:
        if item in dictionary.keys():
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary
