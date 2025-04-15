## Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string


def count_caps(string=""):
    upper_count = 0 
    lower_count=0
    for n in range(len(string)):
        if string[n]>="A" and  string[n]<= "Z":
            upper_count += 1
        elif string[n]>="a" and  string[n]<= "z":
            lower_count+=1
        else:
            continue
    
    print (f"There's {upper_count} upper cases and {lower_count} lower cases")

count_caps("Vamos a Paris Hoy y dentro de 3 dias a Roma, Italia")