
#1. Cree una clase de `Circle` con:
    #1. Un atributo de `radius` (radio).
    #2. Un método de `get_area` que retorne su área.

class Circle:
    def __init__(self, radius):
        self.radius=radius
    def get_area(self):
        area=3.14*self.radius**2
        print(area)

my_area=Circle(5)
my_area.get_area()