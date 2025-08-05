"""
AND: The only way to get a True for the and operator is if both a and b are True

OR: In this case, to get a True result, either a or b should be True.

NOT: Here the value of a is reversed. If a is False then not a is True

Truth table for the and operator:
a	    b	    a and b
False	False	False
False	True	False
True	False	False
True	True	True

Truth table for the or operator:
a	    b   	a or b
False	False	False
False	True	True
True	False	True
True	True	True

Truth table for the not operator:
a   	not a
False	True
True	False
"""
# Replace the values with numbers
b1 = 3
b2 = 3

# This line checks if b1 * b2 is greater than b1 + b2
b3 = (b1 * b2) > (b1 + b2)

# Don't change the line below
print(f"b3 = {b3}")

# Challenge - Replace the values with booleans
a = True
b = False
c = False

# This line checks if (a or b) and not c is True
result = (a or b) and not c

# Don't change the line below
print(f"result = {result}")