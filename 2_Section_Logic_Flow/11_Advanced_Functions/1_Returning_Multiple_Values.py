"""
In Python, a function can return multiple values. This is achieved by packaging the values into a tuple and returning the tuple.
When the function is called, the returned tuple can be unpacked into separate variables.

Here's an example of a function that returns multiple values:

def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age

person_name, person_age = get_name_and_age()
print(person_name)
# Output: Alice
print(person_age)
# Output: 30

In this example, the function get_name_and_age returns the name and age values as a tuple. When we call the function, we unpack the returned tuple into the variables person_name and person_age.

Returning multiple values is useful when you need to return more than one piece of information from a function.
Instead of creating a complex data structure like a list or a dictionary, you can simply return the values as a tuple.

Create a function named get_student_info that takes no arguments. The function should return a tuple containing the following information about a student:

Name: "Bob"
Age: 20
Major: "Computer Science"
After defining the function, call it and unpack the returned values into three variables: student_name, student_age, and student_major. Then, print the values of these variables.
"""

def get_student_info():
    name = "Bob"
    age = 20
    major = "Computer Science"
    return name, age, major

student_name, student_age, student_major = get_student_info()
print(student_name)
print(student_age)
print(student_major)