
#2. Cree una clase de `Bus` con:
    # 1. Un atributo de `max_passengers`.
    # 2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
    # 3. Un método para bajar pasajeros uno por uno (en cualquier orden).


class Person:
    def __init__(self,name):
        self.name=name
        

p1=Person("Dirk")
p2=Person("Juli")
p3=Person("Ric")
p4=Person("Sebas")



class Bus:

    def __init__(self, max_passengers):
        self.max_passengers=max_passengers
    passengers=[]

    def add_passengers(self, person):
        if len(self.passengers)< self.max_passengers:
            self.passengers.append(person)
        else:
            print("the bus is full")

    def remove_passengers(self,person):
        for i in range(self.passengers):
            if self.passengers[i]==person:
                self.passengers.remove(i)
                break

my_bus=Bus(max_passengers=3)
my_bus.add_passengers(p1)
my_bus.add_passengers(p2)
my_bus.add_passengers(p3)
my_bus.add_passengers(p4)
print(my_bus.passengers[0].name, my_bus.passengers[1].name, my_bus.passengers[2].name)
