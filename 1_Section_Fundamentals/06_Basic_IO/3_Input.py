"""
As of now we stored values that we thought about in variables.

Programs usually don't work this way. We receive values from an outer source, a user for example.

To get input from a user or the system we need to write:

var = input()

This will store the input in the variable var.

The input is always of type string.

For example, if the input is 56 then var will hold the string "56".
"""
name = input()
print(f"Hello, {name}!")

# Challenge

"""
Create a program that receives that user's name and age, then calculates and prints how old they will be in 10 years.

The output should be in the format: "In 10 years, [name] will be [age] years old."

You will need to:

Use input() to get the user's name and age.
Store the inputs in variables.
Convert the age to an integer and add 10 to it.
Print the result using an f-string.
"""

name = input()
age = int(input())
# Write code here
in_ten_years = age + 10
print(f"In 10 years, {name} will be {in_ten_years} years old.")