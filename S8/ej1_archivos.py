

##Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.


def read_file(ordered_songs):
    with open("songs.txt") as file:
        with open(ordered_songs, "w") as o:
            o.write("\n".join(sorted(file.read().splitlines())))
    with open("ordered_songs.txt") as file:
        for line in file.readlines():
            print(line)


read_file("ordered_songs.txt")