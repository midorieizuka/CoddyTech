"""
Create a function named list_students_by_course that takes one argument: course (string).
The function should:

Iterate through the student_records dictionary and find all students enrolled in the specified course.
Return a list of names of students who are enrolled in the course.
If no students are enrolled in the course, return an empty list.
Add (replace) the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
"""

student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student {name} already exists.")
    else:
        student_records[name] = {"age": age, "grades": set(), "courses": set(courses)}
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name in student_records:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:
        print(f"Student '{name}' not found.")

def is_enrolled(name, course):
    if name in student_records:
        if course in student_records[name]["courses"]:
            return True
        else:
            return False
    else:
        print(f"Student '{name}' not found.")
        return False

def calculate_average_grade(name):
    if name in student_records:
        if student_records[name]["grades"] != "":
            sum = 0
            count = 0
            for grade in (student_records[name]["grades"]):
                sum += grade
                count += 1
            average_grade = sum / count
            return float(average_grade)
        else:
            return 0
    else:
        print(f"Student '{name}' not found.")

def list_students_by_course(course):
    students = []
    for name in student_records.keys():
        if course in student_records[name]["courses"]:
            students.append(name)
    return students

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list