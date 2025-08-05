"""
if allows us to execute particular code if a condition is met, but what if we want to execute something else if the condition is not met?

For that we have the else statement:

age = 15
status = "None"
if age >= 18:
    status = "Adult"
else:
    status = "Young"

In the above example, age is smaller than 18 which means it enter the else code and status will hold "Young".

We can even make it more profound using the elif statement:

age = 68
status = "None"
if age < 18:
    status = "Young"
elif age >= 18 and age <= 65:
    status = "Adult"
else:
    status = "Old"

Here it checks whether age is smaller than 18, if not it will continue to the next condition and check whether age is between 18 and 65.

If that condition is also not met it will set status to "Old".
"""
wind = int(input()) # Don't change this line
status = "unset"
# Type your code below
if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <= 31:
    status = "Breeze"
elif wind > 31 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

# Don't change the line below
print(f"status = {status}")

# Challenge

temperature = int(input()) # Don't change this line
weather = "unset"
# Type your code below
if temperature < 0:
    weather = "Freezing"
elif temperature >= 0 and temperature <= 15:
    weather = "Cold"
elif temperature > 15 and temperature <= 25:
    weather = "Mild"
else:
    weather = "Hot"
# Don't change the line below
print(f"weather = {weather}")