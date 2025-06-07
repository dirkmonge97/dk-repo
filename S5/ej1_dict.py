## diccionario con info the hotel (nombre, estrellas, habitaciones) y las habitaciones debe ser una listo con num, piso y precio

hotel_dictionary = {
    "name" : "hilton",
    "stars": 3,
    "rooms": [
        {
            "room_number": 1,
            "floor": 1,
            "night_price": 50
        },
        {
            "room_number": 2,
            "floor": 1,
            "night_price": 60
        },
        {
            "room_number": 3,
            "floor": 2,
            "night_price": 80
        },
        {
            "room_number": 4,
            "floor": 2,
            "night_price": 90
        },
        {
            "room_number": 5,
            "floor": 4,
            "night_price": 105
        },
        {
            "room_number": 6,
            "floor": 4,
            "night_price": 105
        }
    ]
}
for key, value in hotel_dictionary.items():
    print(key)
    print(value)

