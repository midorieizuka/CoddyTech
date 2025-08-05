"""
Nested If-Else statements allow you to check multiple conditions by placing one if-else statement inside another.
Create a basic if-else statement:
age = 18
title = "None"
if age >= 18:
    title = "Adult"
else:
    title = "Minor"

Now let's add a nested condition inside:

age = 18
title = "None"
allowed_to_drink = False
if age >= 18:
    title = "Adult"
    if age >= 21:
        allowed_to_drink = True
    else:
        allowed_to_drink = False
else:
    title = "Minor"

In this example, the second if-else only executes when the first condition is True.
"""
# Get age as an integer
age = int(input())

# Get parental guidance as a boolean (True/False)
with_parent = input() == "true"

# Declare a variable named message with "None"
message = "None"

# Write your nested if-else code here
if age >= 18:
    message = "You can watch any movie"
elif age <18 and with_parent == True:
    message = "You can watch PG-13 movies"
else:
    message = "You can only watch G-rated movies"
# Don't change below this line
print(message)

# Challenge

level = int(input()) # Don't change this line
has_training = input() == "True" # Don't change this line
level_message = "None" # Don't change this line

# Write your code below
if level >= 1 and level <= 5:
    level_message = "Basic weapons only"
elif level >= 6 and level <= 10:
    if has_training == False:
        level_message = "Need weapon training first"
    if has_training == True:
        level_message = "Access to advanced weapons granted"
elif level >= 11:
    level_message = "Access to all weapons granted"
elif level <= 0:
    level_message = "Invalid level"
# Don't change below this line
print(level_message)