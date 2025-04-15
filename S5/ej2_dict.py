##Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_a = ["item:", "brand:", "color:", "price($):"]
list_b = ["laptop", "Mac", "gray", 1200]

new_dict = {
    list_a[0]:list_b[0],
    list_a[1]:list_b[1],
    list_a[2]:list_b[2],
    list_a[3]:list_b[3]
}

#show iteration
for k, v in new_dict.items():
    print(k)
    print(v)

#show dictionary
print (new_dict)