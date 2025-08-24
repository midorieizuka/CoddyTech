"""
Create a function named filter_top_students that takes one argument: threshold (float).
The function should:

Iterate through the student_records dictionary and find all students whose average grade is greater than the specified threshold.
Use the calculate_average_grade function to get each student's average grade.
Return a list of names of the top students.
If no students meet the criteria, return an empty list.
Add (replace) the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list

Take a moment to reflect on how you've combined dictionaries, sets, and decision-making to create a fully functional program.
Great job! 🚀
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

def filter_top_students(threshold):
    top_students = []
    for name in student_records.keys():
        if calculate_average_grade(name) > threshold:
            top_students.append(name)
    return top_students

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list