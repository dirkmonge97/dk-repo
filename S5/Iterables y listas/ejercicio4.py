##Cree un programa que elimine todos los números impares de una lista.


list=[1,2,3,4,5,6,7,8,11,11,2,24,19,12,13,14,18]
t_bool = True
while t_bool:
    for i in range(len(list)):
        record =list[i]
        if (record%2!=0):
            list.remove(record)
            t_bool=True
            break
        else:
            t_bool=False
            continue
print(list)


