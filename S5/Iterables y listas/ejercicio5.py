##Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.


num_a=int(input("ingrese un numero a la lista:"))
num_b=int(input("ingrese otro numero a la lista:"))
num_c=int(input("ingrese otro numero a la lista:"))
num_d=int(input("ingrese otro numero a la lista:"))
num_e=int(input("ingrese otro numero a la lista:"))
num_f=int(input("ingrese otro numero a la lista:"))
num_g=int(input("ingrese otro numero a la lista:"))
num_h=int(input("ingrese otro numero a la lista:"))
num_i=int(input("ingrese otro numero a la lista:"))
num_j=int(input("ingrese el ultimo numero a la lista:"))

list = [num_a,num_b,num_c,num_d,num_e,num_f,num_g,num_h,num_i,num_j]
counter=0
current_highest=1
for i in range(len(list)):
    if list[i]==0:
        counter+=1
        continue
    if list[i]>=current_highest:
        current_highest = list[i]
        counter+=1
    if counter==(len(list)):
        break

#remove highest number from the list
for i in range(len(list)):
    if list[i]==current_highest:
        list.pop(i)
        break
list.insert(0,current_highest)
print (f"this is the highest number: {current_highest}")
print (f"this is the current list starting with the highest number: {list}")






