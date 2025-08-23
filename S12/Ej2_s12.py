
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self) -> float:
        """return the perimeter as a float"""
        raise NotImplementedError("subclasses must implement calculate_perimeter()")

    @abstractmethod
    def calculate_area(self)-> float:
        """return the area as a float"""
        raise NotImplementedError("subclasses must implement calculate_area()")

class Circle(Shape):
    def __init__(self,radius:float):
        self.radius=float(radius)
        if self.radius<=0:
            raise ValueError("Radius must be > 0")
        
    def calculate_perimeter(self) -> float:
        return 2 * math.pi *self.radius
        
    def calculate_area(self)->float:
        return math.pi *(self.radius **2)
        

class Rectangle(Shape):
    def __init__(self, width:float,height:float):
        self.width=float(width)
        self.height=float(height)

        if self.width <=0 or self.height<=0:
            raise ValueError("Weidth and Height must be above 0")
        
    def calculate_perimeter(self)->float:
        return 2*(self.width+self.height)
    def calculate_area(self):
        return self.width*self.height
    
class Square(Shape):
    def __init__(self,side:float):
        self.side=float(side)
        if self.side <=0:
            raise ValueError ("The side must be > 0")
        
    def calculate_perimeter(self)->float:
        return 4* self.side
    def calculate_area(self)-> float:
        return self.side *self.side