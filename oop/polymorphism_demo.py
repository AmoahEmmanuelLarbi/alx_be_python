"""
Docstring for polymorphism_demo

Task Description:
You are tasked with creating a Python script named polymorphism_demo.py. 
In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.
"""
import math

#create base class
class Shape:
    def __init__(self, name):
        self.name = name
    
    #instance method
    def area(self):
        raise NotImplementedError("The child class must override this instance method")
    

#create child / derived class
class Rectangle(Shape):
    #constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Rectangle of length {self.length} and width of {self.width}"
    
    def area(self):
        return self.length * self.width

#create child class Circle
class Circle(Shape):
    #constructor
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle of radius {self.radius}"
    
    def area(self):
        return math.pi * (self.radius ** 2)



r = Rectangle(4, 6)
print(r.area())

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()