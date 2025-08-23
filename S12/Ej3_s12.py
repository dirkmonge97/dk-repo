
#La herencia multiple es una clase que puede heredar de varias a la vez para sumar capacidades.

class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Ancho/alto deben ser > 0.")

    def area(self):
        return self.width * self.height


class ColorMixin:
    def __init__(self, color="black", **kwargs):
        self.color = str(color)
        super().__init__(**kwargs)


class StrMixin:
    def __str__(self):
        return f"{self.__class__.__name__}(area={self.area()}, color={getattr(self, 'color', None)})"


class ColoredPrintableRectangle(ColorMixin, StrMixin, Rectangle):
    pass


r = ColoredPrintableRectangle(width=3, height=4, color="red")
print(r.area())   
print(r)          
