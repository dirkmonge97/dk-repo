##Experimente con el concepto de scope / Intente accesar a una variable definida dentro de una función desde afuera


def list_variable_funct():
    number_list=[1,2,3,4,5]

for i in range(len(number_list)):
    if i == 3:
        print (number_list[i])

##it fails
