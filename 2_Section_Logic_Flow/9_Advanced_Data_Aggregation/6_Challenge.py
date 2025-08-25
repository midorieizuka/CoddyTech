"""
Create a function named analyze_grades that takes a dictionary of student grades as an argument.
The dictionary keys are student names, and the values are their corresponding grades.
The function should perform the following operations:

Calculate the average grade of all students.
Find the highest and lowest grades.
Identify the student(s) with the highest and lowest grades.
Return a dictionary containing the following information:
'average': The average grade (rounded to 2 decimal places)
'highest': The highest grade
'lowest': The lowest grade
'top_student': The name of the student with the highest grade
'bottom_student': The name of the student with the lowest grade

Test your function with the following dictionary:

student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
"""

def analyze_grades(grades):
    # Write code here
    all_grades = student_grades.values()
    average = sum(all_grades) / len(all_grades)
    highest_grade = max(all_grades)
    lowest_grade = min(all_grades)
    for key, value in student_grades.items():
        if value == highest_grade:
            top_student = key
        if value == lowest_grade:
            bottom_student = key
        else:
            pass
    data = {
        'average': average,
        'highest': highest_grade,
        'lowest': lowest_grade,
        'top_student': top_student,
        'bottom_student': bottom_student
    }
    return data
    

# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)