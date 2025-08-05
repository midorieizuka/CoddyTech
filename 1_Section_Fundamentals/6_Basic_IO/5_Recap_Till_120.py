"""
Write a program that gets the user's age as input.

The program will output (print) the number of missing years till 120 (in a specific format, shown below).

For example, for input 25, the expected output is "95 years till 120".
"""
age = int(input())
var = 120 - age
print(f"{var} years till 120")