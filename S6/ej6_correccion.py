
##Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente

string= input("Ingrese las palabras separadas por guion:")

def build_list(string):
    count=0
    list_of_strings=string.split("-")
    return list_of_strings

def sort_list():
    list = build_list(string)
    list.sort(key=str.lower)
    return list

def concatenate_order_list():
    concatenated_string_list=""
    new_ordered_list_variable=sort_list()
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