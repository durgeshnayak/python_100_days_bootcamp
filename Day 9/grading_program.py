student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {
}


# TODO-2: Write your code below to add the grades to student_grades.👇
student_grade = ""
for student in student_scores:
    student_score = student_scores[student]
    if student_score >= 91:
        student_grade = "Outstanding"
    elif student_score >= 81:
        student_grade = "Exceeds Expectations"
    elif student_score >= 71:
        student_grade = "Acceptable"
    else:
        student_grade = "Fail"
    student_grades[student] = student_grade

# 🚨 Don't change the code below 👇
print(student_grades)
