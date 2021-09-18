number = int(input())

students_grade = {}

for _ in range(number):
    student_name = input()
    grade = float(input())
    if student_name not in students_grade:
        students_grade[student_name] = [grade]
    else:
        students_grade[student_name].append(grade)

students_grade_higher_450 = { key: sum(value) / len(value) for (key,value) in students_grade.items() if  sum(value)/ len(value)>= 4.50}
aver_grade_sorted = sorted(students_grade_higher_450.items(), key = lambda x: -x[1])
for average_grades in aver_grade_sorted:
    print(f"{average_grades[0]} –> {average_grades[1]:.2f}")