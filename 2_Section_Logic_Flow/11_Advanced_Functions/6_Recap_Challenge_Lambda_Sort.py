"""
Lambda functions are incredibly useful with the sorted() function to customize sorting in different scenarios.
Here are a few examples:

Sorting Strings by Length:

names = ["Alice", "Bob", "Charlie", "Diana"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)
# Output: ['Bob', 'Alice', 'Diana', 'Charlie']

Sorting Dictionaries by Values:

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
sorted_grades = sorted(grades.items(), key=lambda x: x[1])
print(sorted_grades)
# Output: [('Charlie', 78), ('Alice', 85), ('Bob', 90)]

Sorting Numbers by Absolute Value:

numbers = [-10, 15, -20, 25]
sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)
# Output: [-10, 15, -20, 25]

Sorting Tuples by Multiple Criteria:

data = [("Alice", 25), ("Bob", 30), ("Charlie", 25)]
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
print(sorted_data)
# Output: [('Alice', 25), ('Charlie', 25), ('Bob', 30)]

Challenge
Create a function named sort_tuples that takes a list of tuples data as an argument.
Each tuple in data contains two elements: a string and a number.
The function should use the sorted() function along with a lambda function to sort the list of
tuples based on the second element (the number) in ascending order.
The function should return the sorted list of tuples.
"""

def sort_tuples(data):
    # Write code here
    data_list = list(data)
    sorted_data = sorted(data_list, key=lambda x: x[1])
    return sorted_data

data = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
print(sort_tuples(data))

