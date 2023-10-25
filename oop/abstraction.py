from abc import ABC, abstractmethod

# Create an abstract class 'Shape' that inherits from ABC (Abstract Base Class).
class Shape(ABC):

    # Define an abstract method 'area'.
    @abstractmethod
    def area(self):
        pass

    # Define another abstract method 'perimeter'.
    @abstractmethod
    def perimeter(self):
        pass

# Create a concrete subclass 'Circle' that inherits from 'Shape'.
class Circle(Shape):

    # Constructor to initialize the radius.
    def __init__(self, radius):
        self.radius = radius

    # Implement the 'area' method for the Circle.
    def area(self):
        return 3.14 * self.radius * self.radius

    # Implement the 'perimeter' method for the Circle.
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create a concrete subclass 'Square' that inherits from 'Shape'.
class Square(Shape):

    # Constructor to initialize the side length.
    def __init__(self, side_length):
        self.side_length = side_length

    # Implement the 'area' method for the Square.
    def area(self):
        return self.side_length ** 2

    # Implement the 'perimeter' method for the Square.
    def perimeter(self):
        return 4 * self.side_length

# Create instances of Circle and Square.
circle = Circle(5)
square = Square(4)

# Use the 'area' and 'perimeter' methods without worrying about implementation details.
print("Circle Area:", circle.area())       # Circle Area: 78.5
print("Circle Perimeter:", circle.perimeter()) # Circle Perimeter: 31.400000000000002
print("Square Area:", square.area())       # Square Area: 16
print("Square Perimeter:", square.perimeter()) # Square Perimeter: 16
