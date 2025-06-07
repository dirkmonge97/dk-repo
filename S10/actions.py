

#get details for n users and calculate individual average

def input_details():
    loop=1
    student_list=[]
    while loop==1:
        
        while True:
            student_name=input("Please add the Name of the student:")
            if student_name!="":
                break
            print("The Name cannot be empty!")
        while True:
            student_section=input("Please add the section of the student:")
            if student_section!="":
                break
            print("The section cannot be empty!")

        while True:
            try:
                spanish_grade=int(input("Please add the spanish grade of the student:"))
                if spanish_grade<=100 and spanish_grade>=0:
                    break
                else:
                    print("The value is outside of range (0-100)")
            except ValueError:
                print("The input is not a valid number")
        
        while True:
            try:
                english_grade=int(input("Please add the english grade of the student:"))
                if english_grade<=100 and english_grade>=0:
                    break
                else:
                    print("The value is outside of range (0-100)")
            except ValueError:
                print("The input is not a valid number")
        
        while True:
            try:
                social_grade=int(input("Please add the social studies grade of the student:"))
                if social_grade<=100 and social_grade>=0:
                    break
                else:
                    print("The value is outside of range (0-100)")
            except ValueError:
                print("The input is not a valid number")

        while True:
            try:
                science_grade=int(input("Please add the science grade of the student:"))
                if science_grade<=100 and science_grade>=0:
                    break
                else:
                    print("The value is outside of range (0-100)")
            except ValueError:
                print("The input is not a valid number")

        grade_average=(spanish_grade + english_grade + social_grade + science_grade)/4
        print(f"the Average was:{grade_average}")
        
        new_student={
            "Name":student_name,
            "Section":student_section,
            "Spanish":spanish_grade,
            "English":english_grade,
            "Social Studies":social_grade,
            "Science":science_grade,
            "Average":grade_average
            }
        student_list.append(new_student)
        grade_average=(spanish_grade + english_grade + social_grade + science_grade)/4
        
        while True:
            try:
                loop=int(input("Type 1 to add another student or type 2 to return to the menu:"))
                if loop==1 or loop==2:
                    break
                else:
                    print("\n""** The option does not exist, please try again! **""\n")
            except ValueError:
                print("\n""This is not a valid option number, please try again!""\n")
    return student_list
    




#Calculate global average grade off all students

def global_average(list):
    global_average=0
    if list!=0:
        for i in range(len(list)):
            student_info=list[i]
            global_average = global_average + student_info.get("Average") 
        divisor=len(list)
        global_average=global_average/divisor
        print(f"The global average is{global_average}")
    else:
        print("\n""*** Please add students or import a file first! ***""\n")



# create top 3 list

def top_3(list):
    average_list=[]
    if list!=0:
        for i in range(len(list)):
            student_info=list[i]
            average_list.append(student_info.get("Average"))
        average_list.sort(reverse=True)
        new_avrg_list=[]
        if len(average_list)>=3:
            for i in range(3):
                new_avrg_list.append(average_list[i])
        else:
            new_avrg_list=average_list
        
        highest_avrg={
            "Name":"",
            "Average":"",
        }
        second_highest={
            "Name":"",
            "Average":"",
        }
        third_highest={
            "Name":"",
            "Average":"",
        }
        for i in range(len(list)):
            student_info=list[i]
            Name=student_info["Name"]
            grade= student_info["Average"]
            if grade==new_avrg_list[0]:
                highest_avrg.update({'Name':Name, "Average":grade})
            elif grade==new_avrg_list[1]:
                second_highest.update({'Name':Name, "Average":grade})
            elif grade==new_avrg_list[2]:
                third_highest.update({'Name':Name, "Average":grade})
        top_3=[highest_avrg,second_highest,third_highest]
        print (top_3)
    else:
        print("\n""*** Please add students or import a file first! ***""\n")



# see all students added

def see_students(list):

    if list!=0:
        for i in range(len(list)):
            print(list[i])
        
    else:
        print("\n""*** Please add students or import a file first! ***""\n")

