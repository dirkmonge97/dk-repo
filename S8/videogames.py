
## Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.

import csv
def video_games():
    with open("video-games.csv", "w") as games_list:
        fieldnames = ["nombre", "genero", "desarrollador","clasificacion"]

        csv_writer = csv.DictWriter(games_list, fieldnames=fieldnames)

        csv_writer.writeheader()
        game_details={}
        boolean=True
        while boolean:
            for field in fieldnames:
                game_details[field] = input(f"Ingrese el/la {field} del videojuego:")
            csv_writer.writerow(game_details)
            stop=int(input("Desea salir ahora?\n1 = si\n2 = no\n"))
            if stop==1:
                boolean=False
                

video_games()
