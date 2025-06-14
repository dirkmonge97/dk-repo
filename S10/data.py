
import csv

# Export to CSV file

def export_list(list):
    if list!=0:
        with open("student_details.csv", "w") as new_file:
            fieldnames=["Name", "Section", "Spanish",'English', 'Social Studies','Science', 'Average']
            csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
            csv_writer.writeheader()
            for i in list:
                csv_writer.writerow(i)
    else:
        print("\n""*** There are 0 users to export! ***""\n")

# Import from CSV file

def import_list(list):
    try:
        with open("student_details.csv", "r") as file:
            fieldnames=["Name", "Section", "Spanish",'English', 'Social Studies','Science', 'Average']
            csv_reader=csv.DictReader(file, delimiter="\t")

            list=[]
            int_columns=["Spanish",'English', 'Social Studies','Science', 'Average']
            for row in csv_reader:
                for col in int_columns:
                    row[col]=float(row[col])
                list.append(row)
            
        return list

            
    except FileNotFoundError:
        print("The file was not not previously exported and does not exist in directory path")
    print(list)

    