from abc import ABC, abstractmethod

# Abstract class with an abstract method and a concrete method
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def description(self):
        return "This is a shape."

# Concrete subclass of the abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

# Instantiate and use the concrete subclass
circle = Circle(3)
print(circle.description())  # Outputs: This is a shape.
print(circle.area())         # Outputs: 28.274333882308138
