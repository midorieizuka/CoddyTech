"""
Python has three logical operators: and; or; not.

The AND operator returns TRUE if BOTH statements are true.
The OR operator returns TRUE if BOTH statements are false.
The not operator returns the oposite of the statement.
"""

age = 20
has_license = True

result = age >= 18 and has_license # a variavel has_license já é boolean então seria redundante colocar has_license = true

# Don't change the line below
print("Eligible to drive:", result)

# Challenge - Type your code below
x1 = True
x2 = False

# Don't change the lines below
x3 = x1 and x2
print(f"x3 = {x3}")