
##calculadora

option_list="1) Add\n2) Subtract\n3) Multiply\n4) Divide\n5) Delete result"


def select_option():
    print(option_list)
    result=0
    print (result)
    try:
        operation=int(input("Select the action number:"))
    except ValueError as error:
            print("number of action does not exist")
    boolean=True
    while boolean:
        if operation==1:
            try:
                added=int(input("ingress the number to add:"))
            except ValueError as error:
                print(f"not a valid number:{error}")
            result=result+added
            print(option_list)
            print(result)
            operation=int(input("Select the action number:"))

        if operation==2:
            try:
                subtract=int(input("ingress the number to subtract:"))
            except ValueError as error:
                print(f"not a valid number:{error}")
            result=result-subtract
            print(option_list)
            print(result)
            operation=int(input("Select the action number:"))

        if  operation==3:
            try:
                multiply_by=int(input("ingress the number to multiply by:"))
            except ValueError as error:
                print(f"not a valid number:{error}")
            result=result * multiply_by
            print(option_list)
            print(result)
            operation=int(input("Select the action number:"))

        if  operation==4:
            try:
                divide_by=int(input("ingress the number to divide by:"))
            except ValueError as error:
                print(f"not a valid number:{error}")
            result=result/divide_by
            print(option_list)
            print(result)
            operation=int(input("Select the action number:"))

        if  operation==5:
            result=0
            print(option_list)
            print(result)
            try:
                operation=int(input("Select the action number:"))
            except ValueError as error:
                print(f"not a valid number:{error}")



select_option()
