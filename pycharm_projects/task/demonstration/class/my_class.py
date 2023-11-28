# Access Modifiers in Python:

class Base:
    # A class is declared using the class keyword, followed by the class name.
    # The class can have methods, attributes, and a special constructor method called __init__.
    def __init__(self):
        self.public_var = "I'm a public variable"
        self._protected_var = "I'm a protected variable"
        self.__private_var = "I'm a private variable"

    def show_access(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)


class Subclass(Base):
    def access_base_vars(self):
        # We can access public and protected variables from the base class.
        print(self.public_var)
        print(self._protected_var)
        # Private variable is name-mangled, so it can't be accessed directly.
        # To access it, we can use _Base__private_var.
        print(self._Base__private_var)


# Access Modifiers:
base_obj = Base()
base_obj.show_access()
sub_obj = Subclass()
sub_obj.access_base_vars()


# Inheritance in Python:

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Inheritance:
dog = Dog()
cat = Cat()
print(dog.speak())  # Outputs: Woof!
print(cat.speak())  # Outputs: Meow!


# Method Declaration, Encapsulation, and Polymorphism in Python:

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


# Method Declaration, Encapsulation, and Polymorphism:
rect = Rectangle("Rectangle", 4, 5)
circle = Circle("Circle", 3)
print(rect.area())  # Outputs: 20
print(circle.area())  # Outputs: 28.274333882308138

# Built-in Object-Oriented Features in Python:

class A:
    common_var = "Variable in class A"

    def common_method(self):
        return "Method in class A"

class B:
    common_var = "Variable in class B"

    def common_method(self):
        return "Method in class B"

class C(B, A):
    pass


# Built-in Object-Oriented Features:

# Accessing common_var and common_method from class C
obj_c = C()

# Accessing the common variable
common_var = obj_c.common_var
print(common_var)  # Outputs: Variable in class A

# Accessing the common method
common_method = obj_c.common_method()
print(common_method)  # Outputs: Method in class A
