first_number = int(input("Type the first number:"))
second_number = int(input("Type the second number:"))
third_number = int(input("Type the third number:"))
if third_number > second_number and third_number > first_number:
    print (f"the highest number is {third_number}")
else:
    if second_number > third_number and second_number > first_number:
        print (f"the highest number is {second_number}")
    else:
        print (f"the highest number is {first_number}")
