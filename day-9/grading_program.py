def evaluate_grade(score):

    if  91 <= score <= 100:
        return 'Outstanding'
    elif  81 <= score <=90:
        return 'Exceeds Expectations'
    elif 71 <= score <= 80:
        return 'Acceptable'
    elif score <= 70:
        return 'Fail'
    else:
        return 'Invalid Score'


student_scores = {
    "Harry": 81, 
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    grade = evaluate_grade(student_scores[key])
    student_grades[key] = grade

print(student_grades)