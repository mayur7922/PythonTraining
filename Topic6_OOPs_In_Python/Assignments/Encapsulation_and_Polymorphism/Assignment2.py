import math

class Shape:
    def area(self):
        print("Nothing has been calculated yet")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 7),
        Triangle(6, 8)
    ]
    
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
