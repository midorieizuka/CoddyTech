
def menu():
    print("Students Record Manager:")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Is Enrolled")
    print("4. Average Grade")
    print("5. List by Course")
    print("6. Top Students")
    print("7. Exit")

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
            print("True")
        else:
            print("False")
    else:
        print(f"Student '{name}' not found.")
        

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

student_records = {}
while True:
    menu()
    choice = input()
    if choice == "7":
        print("Exiting Students Record Manager.")
        break
    elif choice == "1":
        name = input()
        age = input()
        courses = list(input().split(", "))
        add_student(name, age, courses)
        print()
    elif choice == "2":
        name = input()
        grade = int(input())
        add_grade(name, grade)
        print()
    elif choice == "3":
        name = input()
        course = input()
        is_enrolled(name, course)
        print()
    elif choice == "4":
        name = input()
        print(calculate_average_grade(name))
        print()
    elif choice == "5":
        course = input()
        print(list_students_by_course(course))
        print()
    elif choice == "6":
        threshold = int(input())
        print(filter_top_students(threshold))
        print()
    else:
        print("Invalid choice. Try again.")
        print()
