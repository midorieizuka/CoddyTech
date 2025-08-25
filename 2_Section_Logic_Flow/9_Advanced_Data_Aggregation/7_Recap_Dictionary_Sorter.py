"""
Create a function named dictionary_sorter that takes a dictionary data_dict as an argument.
The function should sort the dictionary by its values in ascending order and return a new dictionary containing the sorted key-value pairs.

For example, if the input dictionary is {'a': 3, 'b': 1, 'c': 2}, the function should return a dictionary like this:

{'b': 1, 'c': 2, 'a': 3}
"""

def dictionary_sorter(data_dict):
    # Write code here
    new = {}
    order = sorted(data_dict.values())
    for key, value in data_dict.items():
        if val