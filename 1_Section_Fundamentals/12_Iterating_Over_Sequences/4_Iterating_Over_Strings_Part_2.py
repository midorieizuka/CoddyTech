"""
String splitting allows you to break a string into a list, while joining lets you combine list items into a string.

The split() method divides a string into a list of substrings based on a delimiter.

Split by whitespace:

text = "apple banana cherry"
fruits = text.split()
print(fruits)
# ['apple', 'banana', 'cherry']
Split with specific delimiter:

data = "john,25,new york"
data = data.split(',')
print(data)
# ['john', '25', 'new york']
The join() method combines elements of an iterable into a single string.

Basic joining:

words = ['Hello', 'World', 'Python']
text = ' '.join(words)
print(text)
# "Hello World Python"
Join with different separator:

fruits = ['apple', 'banana', 'cherry']
line = ','.join(fruits)
print(line)
# "apple,banana,cherry"
"""
"""
Write a program that takes two inputs: a text string and a delimiter character.

The program should split the text by whitespace into words, then join these words using the specified delimited character and print the resulting string.
"""

text = input()
delimiter = input()
# Write your code below
def spliter(text, delimiter):
    words = text.split()
    string = delimiter.join(words)
    return(string)
    
spliter(text, delimiter)
print(spliter(text, delimiter))

"""
Create a program that takes two inputs: a string of numbers separated by spaces, and a prefix string.

The program should split the number string into individual numbers, add the prefix to each number, then join these modified numbers back into a single string separated by spaces.

Finally, print the resulting string.
"""
numbers = input()
prefix = input()
# Write your code below
def add_prefix(numbers, prefix):
    separate = numbers.split()
    line = prefix + prefix.join(separate)
    return line

add_prefix(numbers, prefix)
print(add_prefix(numbers, prefix))