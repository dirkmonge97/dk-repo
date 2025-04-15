
#Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON
#1. Debe leer el archivo para importar los Pokémones existentes.
#2. Luego debe pedir la información del Pokémon a agregar.
#3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json
# returns json content as py string
def read_json():
    with open("pokemons.json", "r") as f:
        python_object=json.load(f)

    return python_object

#gets new pokemon
def new_pokemon():
    empty_details= {
        "name": {
            "english": ""
        }, 
        "type":[],
        "base": {
            "HP": 0,
            "Attack": 0,
            "Defense": 0,
            "SP. Attack": 0,
            "SP. Defense": 0,
            "Speed": 0
        }
    }
    empty_details.update({"name": {"english": input("Add the name of the pokemon in english:")}})
    empty_details.update({"type":[input("Add the pokemon type:")]})
    empty_details.update({"base": {
        "HP": int(input("Add the HP:")),
        "Attack": int(input("Add the Attack:")),
        "Defense": int(input("Add the Defense:")),
        "SP. Attack": int(input("Add the SP. Attack:")),
        "SP. Defense": int(input("Add the SP. Defense:")),
        "Speed": int(input("Add the Speed:"))
    }})
    new_dict_list = empty_details
    return new_dict_list


def create_last_list():

    current_list=read_json()
    new_item=new_pokemon()
    current_list.append(new_item)
    return current_list



#add new pokemon in the file

def export_write(list):
    
    json_string=json.dumps(list, indent=2)
    with open("pokemons.json", "w") as f:
        f.write(json_string)

def main_loop():
    exit=2
    while exit!= 1:
        list=create_last_list()
        export_write(list)
        exit=int(input("Type 1 to exit or 2 to add more:"))

main_loop()


