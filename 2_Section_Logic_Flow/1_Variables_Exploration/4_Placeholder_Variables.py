"""
In programming, a placeholder variable is a variable that is used to hold a value temporarily, often during the execution of a specific block of code.
Placeholder variables are commonly used in situations where you need to perform operations on a value without changing the original variable.
In Python, a common convention for placeholder variables is to use an underscore _ as the variable name.

Using a Single Underscore _:

# Example of using _ as a placeholder in a loop
for _ in range(5):
    print("Looping")
# Output:
# Looping
# Looping
# Looping
# Looping
# Looping

In this example, _ is used as a placeholder because the loop variable is not needed in the body of the loop.

Using Multiple Single Underscores:

In cases where you have multiple values and you only need some of them, you can use the underscore character multiple times as separate placeholder variables.
For example:

data = (1, 2, 3, 4, 5)
first, _, _, _, last = data
print(first)  # Output: 1
print(last)   # Output: 5
Here, _ is used to ignore the second, third, and fourth elements of the tuple.

Write a Python program that demonstrates the use of placeholder variables in different scenarios:

Create a loop that iterates 5 times. Use a placeholder variable (an underscore) since the loop variable is not used within the loop.
In each iteration, print the word Iteration.

You have a list of numbers: [10, 20, 30, 40, 50].
Unpack this list into three variables: first, middle, and last.
Use a placeholder variable to ignore the second and fourth values.
Then, print the values of first, middle, and last.
Check the test case for the output format!
"""

# Loop 5 times using a placeholder variable
for _ in range(5):
    print("Iteration")
# List of numbers
numbers = [10, 20, 30, 40, 50]
first, _, middle, _, last = numbers

# Unpack the list using placeholder variables

# Print the values of first, middle, and last
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")