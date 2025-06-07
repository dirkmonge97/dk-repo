##Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

list = ["inicio",2,3,4,5,6,7,8,9,10,"final"]
for i in range(0,len(list)):
    a=list[0]
    b=list[-1]
    delete_a=list.pop(0)
    list.insert(0,b)
    list.insert(-1,a)
    list.pop(-1)
    print (list)
    break
