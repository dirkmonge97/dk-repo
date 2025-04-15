##Cree una función que le de la vuelta a un string y lo retorne


phrase = "Software developer"

reverse_phrase= ""
def reverse_string(phrase,reverse_phrase):
    list=[]
    for n in phrase:
        list.insert(0, n)
    for i in list:
        reverse_phrase += i + ""
    return reverse_phrase

print (reverse_string(phrase,reverse_phrase))