"""
Create a function named elements_of_freedom that processes a list of string elements according to specific rules.

Your function should:

Filter out elements that have fewer than 5 characters
Convert the remaining elements to uppercase
Remove any duplicate elements
Return a list of the unique uppercase elements
Use list operations to efficiently process the data.

Exemple:
Input: ["apple", "banana", "cherry", "date", "apple", "banana", "grape", "fig"]
Output: ['APPLE', 'BANANA', 'CHERRY', 'GRAPE']
"""

def elements_of_freedom(elements):
    # Your solution here
    # Step 1: Filter elements with length >= 5
    words_greater_5 = [word for word in elements if len(word) >= 5]
    # Step 2: Convert filtered elements to uppercase
    upper_words = [word.upper() for word in words_greater_5]
    # Step 3: Create a list of unique elements
    seen = set()
    unique_words = []
    for word in upper_words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    # Step 4: Return the final result
    return unique_words


elements = ["freedom", "liberty", "justice", "hope", "dreams", "hope", "peace"]
elements_of_freedom(elements)
print(elements_of_freedom(elements))
