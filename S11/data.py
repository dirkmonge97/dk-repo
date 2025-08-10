
import csv
from student import Student
# Export to CSV file

def export_list(student_list):
    if student_list:
        with open("student_details.csv", "w", newline="") as new_file:
            fieldnames=["Name", "Section", "Spanish",'English', 'Social Studies','Science', 'Average']
            csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
            csv_writer.writeheader()
            for student in student_list:
                csv_writer.writerow(student.to_dict())
    else:
        print("\n""*** There are 0 users to export! ***""\n")

# Import from CSV file

def import_list():
    try:
        with open("student_details.csv", "r") as file:
            fieldnames=["Name", "Section", "Spanish",'English', 'Social Studies','Science', 'Average']
            csv_reader=csv.DictReader(file, delimiter="\t")

            student_list=[]
            int_columns=["Spanish",'English', 'Social Studies','Science', 'Average']
            for row in csv_reader:
                for col in int_columns:
                    row[col]=float(row[col])
                student = Student(
                    name = row["Name"],
                    section = row["Section"],
                    spanish_grade = row["Spanish"],
                    english_grade = row["English"],
                    social_grade = row["Social Studies"],
                    science_grade = row["Science"],
                    grade_average = row["Average"]
)
                student_list.append(student)
        print("\n""The file was imported successfully!""\n")
            
        return student_list

            
    except FileNotFoundError:
            print("\n""The file was not not previously exported and does not exist in directory path""\n")
            return []

    