##Cree una función que retorne la suma de todos los números de una lista
##La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos)


list = []

def list_suma(list):
    current_amount = 0
    for i in range(len(list)):
        current_amount= current_amount + list[i]
    return current_amount

print (list_suma([5,10,7]))