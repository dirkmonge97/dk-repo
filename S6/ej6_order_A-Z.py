

##Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente

string= input("Ingrese las palabras separadas por guion:")

def separate_strings(string):
    count=0
    list_of_strings=string.split("-")
    return list_of_strings

def order_list():
    ordered_list=[]
    current_highest=97
    while current_highest<=124:
        for e in separate_strings(string):
            if e[0]==chr(current_highest):
                ordered_list.append(e)
        current_highest += 1
    return ordered_list

def concatenate_order_list():
    concatenated_string_list=""
    new_ordered_list_variable=order_list()
    for i in range(len(new_ordered_list_variable)):
        if i==0:
            current_element=new_ordered_list_variable[i]
            concatenated_string_list=(f"{current_element}")
        elif i == len(new_ordered_list_variable):
            last=new_ordered_list_variable[i]
            concatenated_string_list= (concatenated_string_list+{last})
        else:
            current_element=new_ordered_list_variable[i]
            concatenated_string_list=(f"{concatenated_string_list}-{current_element}")
    return concatenated_string_list


print (concatenate_order_list())