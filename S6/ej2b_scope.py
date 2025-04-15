##Intente accesar a una variable global dede una función y cambiar su valor 


list=[1,2,3,4,5]

def edit_list(list):
    for n in range(len(list)):
        list[n] =10
    print(list)

edit_list(list)