
#1. Cree una clase de `Circle` con:
    #1. Un atributo de `radius` (radio).
    #2. Un método de `get_area` que retorne su área.

class Circle:
    def get_area(self,radius):
        area=3.14*radius**2
        print(area)

my_area=Circle()
my_area.get_area(5)