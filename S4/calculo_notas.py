average_pass_grades = 0
average_fail_grades = 0
average_total_grades = 0
pass_grades = 0
fail_grades = 0
grade_count = 1
grades = int(input("Enter the number of grades:"))
while (grades >= grade_count):
    current_grade = int(input(f"Enter the grade number {grade_count}:"))
    if current_grade < 70:
        fail_grades = fail_grades + 1
        average_fail_grades = average_fail_grades + current_grade
    else:
        pass_grades = pass_grades + 1
        average_pass_grades = average_pass_grades + current_grade
    grade_count = grade_count + 1
    average_total_grades = average_total_grades + (current_grade / grades)
if fail_grades != 0:
    average_fail_grades = average_fail_grades / fail_grades
if pass_grades != 0:
    average_pass_grades = average_pass_grades / pass_grades
print (f"Number of passed grades: {pass_grades}")
print (f"the grade-point average of the passed grades is: {average_pass_grades}")
print (f"Number of failed grades: {fail_grades}")
print (f"the grade-point average of the failed grades is: {average_fail_grades}")
print (f"the total grade-point average is: {average_total_grades}")

