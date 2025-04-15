##Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

list_one = ["hoy","un","dia","estudiar"]
list_two = ["es","buen","para","programación"]

for index in range (0,len(list_one)):
    print (list_one[index], list_two[index])
    index = index + 1
