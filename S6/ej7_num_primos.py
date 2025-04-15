##Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.


def accepted_list():
    index_count= int(input("cuantos numeros desea ingresar a la lista?"))
    print (index_count)

    list=[]
    insert_count=0
    while (insert_count< index_count):
        list.append(int(input("Agregue el siguiente numero a la lista:")))
        insert_count+=1
    return list


def prime_true(value):
    count=1
    compare=0
    while count <=value:
        if value%count==0:
            count+=1
            compare+=1
        else:
            count +=1
    if compare==2:
        return True
    else:
        return False
    
def prime_list():
    new_list=[]
    list=accepted_list()
    for i in range(len(list)):
        if prime_true(list[i]):
            new_list.append(list[i])
    return new_list

print (prime_list())



