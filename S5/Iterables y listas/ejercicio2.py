##Cree un programa que itere e imprima un string letra por letra de derecha a izquierda

reverse_phrase = "feliz navidad"
count = 0
for index in range(0, len(reverse_phrase)):
    print (reverse_phrase[-1])
    reverse_phrase=reverse_phrase[:-1]
