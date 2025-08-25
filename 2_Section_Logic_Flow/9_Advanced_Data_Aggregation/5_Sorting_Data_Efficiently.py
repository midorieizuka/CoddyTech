"""
Sorting is a fundamental operation in computer science, and Python offers powerful built-in tools to sort data efficiently.
The primary function for sorting is sorted(), which can be used to sort various types of data, including numbers, strings, and more complex objects.

Basic Sorting:

The sorted() function takes an iterable (e.g., a list, tuple, or set) as its argument and returns a new list containing the sorted elements.
By default, it sorts in ascending order.

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
# Output: [1, 1, 2, 3, 4, 5, 6, 9]

In this example, sorted() sorts the numbers list in ascending order.

Reverse Sorting:

To sort in descending order, you can use the reverse parameter and set it to True.

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)
# Output: [9, 6, 5, 4, 3, 2, 1, 1]

Here, sorted() sorts the numbers list in descending order.

Sorting Strings:

The sorted() function can also sort strings based on their lexicographical order (i.e., the order they would appear in a dictionary).

words = ["apple", "banana", "cherry"]
sorted_words = sorted(words)
print(sorted_words)
# Output: ['apple', 'banana', 'cherry']

In this example, sorted() sorts the words list in alphabetical order.

Custom Sorting with Key Function:

For more complex sorting needs, you can use the key parameter to specify a function that determines the sorting order.
The key function is applied to each element before sorting, and the returned values are used for comparison.

words = ["apple", "banana", "cherry"]
sorted_words_by_length = sorted(words, key=len)
print(sorted_words_by_length)
# Output: ['apple', 'banana', 'cherry']

In this case, sorted() sorts the words list based on the length of each word, using the len() function as the key.

Write a program that performs the following sorting tasks using the sorted() function:

Sort a list of numbers in ascending order.
Sort the same list of numbers in descending order.
Sort a list of strings in alphabetical order.
Sort the same list of strings based on their length.
"""

# Starter inputs
numbers = [5, 3, 8, 1, 2]
words = ["elephant", "cat", "dolphin", "bee"]

# Task 1: Sort numbers in ascending order
# Task 2: Sort numbers in descending order
# Task 3: Sort words alphabetically
# Task 4: Sort words by length

# Replace 'pass' with your code for each task
ascending_numbers = sorted(numbers)
descending_numbers = sorted(numbers, reverse=True)
alphabetical_words = sorted(words)
length_sorted_words = sorted(words, key=len)

# Print the results
print("Ascending:", ascending_numbers)
print("Descending:", descending_numbers)
print("Alphabetical:", alphabetical_words)
print("By Length:", length_sorted_words)