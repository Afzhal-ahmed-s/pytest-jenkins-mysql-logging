from abc import ABC, abstractmethod
# ABC stands for "Abstract Base Class."
# It is part of the abc (Abstract Base Classes) module in Python.
# Abstract Base Classes are a way to define abstract classes and interfaces in Python.


# Interface-like class with only abstract methods
# Shape inherits from ABC class here
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete subclass that implements both abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Instantiate and use the concrete subclass
rectangle = Rectangle(4, 5)
print(rectangle.area())       # Outputs: 20
print(rectangle.perimeter())  # Outputs: 18
