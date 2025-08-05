"""
When working with logical expressions, sometimes we need to simplify or rearrange them.

For example, not in front of two conditions joined by and, can be split into two separate parts.

The and becomes or, and each part gets its own not:

not (A and B) is the same as (not A) or (not B)

# Let's check if a number is NOT (between 1 and 10)
number = 15

# These two expressions are equivalent:
result1 = not (number >= 1 and number <= 10)
result2 = (not number >= 1) or (not number <= 10)

print(result1)  # True
print(result2)  # True

The opposite is also correct: not (A or B) is the same as (not A) and (not B)
For example:

# Checking if a person is NOT (a student or employed)
is_student = False
is_employed = False

# These two expressions are equivalent:
result1 = not (is_student or is_employed)
result2 = (not is_student) and (not is_employed)

print(result1)  # True
print(result2)  # True
"""

# Initialize variables
has_license = True
has_space = True
has_experience = False

# Calculate conditions
can_sell_regular_pet = not (has_license == True and has_experience == True) and has_space == True
"""
Linha do Victor:
can_sell_regular_pet = has_space == True and (has_license == True or has_experience == True)
"""
can_sell_exotic_pet = has_space == True and has_license == True and has_experience == True
cannot_sell_any_pet = has_space == False or (has_license == False and has_experience == False)

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)

# Challenge

"""
You're helping a transportation company create a system to determine if a person can drive certain vehicles.

Initialize the following variables:

has_license with the value True
has_experience with the value False
has_clean_record with the value True
Write the following logical expressions to determine if:

can_drive_car: Person needs a license AND a clean record
can_drive_truck: Person needs a license AND experience AND a clean record
cannot_drive_any: Person has NO license OR NO clean record
"""
# Initialize variables
has_license = True
has_experience = False
has_clean_record = True

# Calculate conditions
can_drive_car = has_license == True and has_clean_record == True
can_drive_truck = has_license == True and has_experience == True and has_clean_record == True
cannot_drive_any = has_license == False or has_clean_record == False

# Don't delete the lines below
print("Can drive car:", can_drive_car)
print("Can drive truck:", can_drive_truck)
print("Cannot drive any:", cannot_drive_any)