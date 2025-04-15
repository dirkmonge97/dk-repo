full_name = input("Type your full name:")
age = int(input("Type your age:"))
if age <= 2:
    print (full_name + "is a baby")
else:
    if age <= 9:
        print (full_name + " is a kid")
    else:
        if age <= 12:
            print (full_name + " is a preadolescent")
        else:
            if age <= 17:
                print (full_name + " is an adolescent")
            else:
                if age <= 21:
                    print (full_name + " is a young adult")
                else:
                    if age <= 59:
                        print (full_name + " is an  adult")
                    else:
                        print (full_name + " is an  older adult")
                    

