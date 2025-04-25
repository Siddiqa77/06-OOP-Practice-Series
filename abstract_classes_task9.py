from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class inherits from Shape and implements the area method
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create an instance of Rectangle
rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area())
