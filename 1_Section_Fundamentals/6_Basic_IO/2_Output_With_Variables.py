"""
As of now we learned how to print simple strings, but sometimes we need to insert variables values into the string.

For example:

age = 10
print("His age is: age")

This will print "His age is: age" instead of "His age is: 10"

To make it work, we will use f-strings:

age = 10
print(f"His age is: {age}")

This prints "His age is: 10"

Before the quotation marks "" we add the letter f and inside the string, wherever we put curly braces {} it will insert the value of what is written inside it.
"""
rnd = input() # Don't change this line
print(f"The input is: {rnd}")

