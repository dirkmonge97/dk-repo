
## Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas

import csv
def video_games():
    with open("video-games.csv", "w") as games_list:
        fieldnames = ["nombre", "genero", "desarrollador","clasificacion"]

        csv_writer = csv.DictWriter(games_list, fieldnames=fieldnames, delimiter="\t")

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
