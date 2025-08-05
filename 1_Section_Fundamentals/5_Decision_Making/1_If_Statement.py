"""
If statements allow us to execute code with conditions.

For example, let's look at the following code:

age = 20
status = "Child"
if age > 18:
    status = "Adult"
age += 1

The above code checks whether the age variable is greater than 18.

If it is, it will set status to hold "Adult" string.

In the end, the code will increment age by 1 whether the age is greater than 18 or not.

To use an if statement, we need to add a colon : at the end of the if, and everything that is inside the if is indented with 4 spaces or 1 tab:

if condition:
    code
    code
    code
"""

a = 14
b = 11

# Don't change below this line
c = 0
if a >= b and not b < 10:
    c = 2

c += 1
print(f"c = {c}")

# Initialize variables
a = 11
b = 10

# Don't change below this line
c = 0
if a < b or b >= 10:
    c = 2

c += 1
print(f"c = {c}")