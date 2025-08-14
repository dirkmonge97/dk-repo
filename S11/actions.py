
from student import Student

## ADDING NEW STUDENTS

def input_details():
    student_list = []
    loop = True
    while loop:
        student = create_student()
        student_list.append(student)

        # Preguntar si quiere agregar otro
        while True:
            try:
                option = int(input("Type 1 to add another student or 2 to return to menu: "))
                if option == 1:
                    break  # Sigue en el while loop para crear otro
                elif option == 2:
                    loop = False  # Salir del ciclo principal
                    break
                else:
                    print("** The option does not exist, please try again! **")
            except ValueError:
                print("This is not a valid option number, please try again!")
    return student_list


## CREATING A NEW STUDENT     
def create_student():
    name=input("Add the student's name:")
    section=input("Add the student's section:")
    spanish_grade=request_grade("Spanish Grade")
    english_grade=request_grade("English Grade")
    social_grade=request_grade("Social Studies Grade")
    science_grade=request_grade("Science Grade")
    grade_average=(spanish_grade+english_grade+social_grade+science_grade)/4
    return Student(name, section, spanish_grade, english_grade, social_grade, science_grade,grade_average)

## VALIDATING THE GRADE INPUT IS VALID
def request_grade(grade_name):
    while True:
        try:
            grade=int(input(f"Please add the {grade_name} of the student:"))
            if grade<=100 and grade>=0:
                return grade
            else:
                print("The value is outside of range (0-100)")
        except ValueError:
            print("The input is not a valid number")

student_list = []

def show_student(student_list):
    if student_list:
        for student in student_list:
            print(f"{student}\n")
    else:
        print("\n""*** Please add students or import a file first! ***""\n")

#Calculate global average grade off all students

def global_average(student_list):
    if student_list:
        total = 0
        for student in student_list:
            total += student.grade_average
        average = total / len(student_list)
        print(f"The global average is {average:.2f}")
    else:
        print("\n*** Please add students or import a file first! ***\n")


# create top 3 list

def top_3(student_list):
    if not student_list:
        print("\n*** Please add students or import a file first! ***\n")
        return
    
    sorted_students = sorted(student_list, key=lambda s: s.grade_average, reverse=True)
    
    top_students = sorted_students[:3]
    
    print("\nTop 3 students by average grade:")
    for i, student in enumerate(top_students, start=1):
        print(f"{i}. {student.name} - Average: {student.grade_average:.2f}")

