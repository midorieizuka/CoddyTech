"""
Now that you know the syntax of list comprehensions, let's dive into some simple examples to see how they can be used to create new lists quickly and efficiently.

Create a list of cube numbers:

cubes = [x**3 for x in range(1, 6)]
print(cubes)
# Output: [1, 8, 27, 64, 125]

Create a list of strings from characters:

chars = [char for char in "hello"]
print(chars)
# Output: ['h', 'e', 'l', 'l', 'o']

Generate a list of even numbers:

evens = [x for x in range(2, 11, 2)]
print(evens)
# Output: [2, 4, 6, 8, 10]

Convert all items in a list to uppercase:

words = ["apple", "banana", "cherry"]
uppercase = [word.upper() for word in words]
print(uppercase)
# Output: ['APPLE', 'BANANA', 'CHERRY']

List comprehensions make it easy to work with sequences, apply transformations, and even include conditions—all in one line!

Create a function named get_word_lengths that takes a list of words as an argument and returns a list of the lengths of each word using a list comprehension.
"""

def get_word_lengths(words):
    # Write code here
    length = [len(word) for word in words]
    return length

words = ["python", "list", "comprehension", "challenge"]
get_word_lengths(words)
print(get_word_lengths(words))