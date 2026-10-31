# (The Rectangle class) Following the example of the Circle class in Section
# 7.2, design a class named Rectangle to represent a rectangle. The class
# contains:
# ■ Two data fields named width and height.
# ■ A constructor that creates a rectangle with the specified width and height.
# The default values are 1 and 2 for the width and height, respectively.
# ■ A method named getArea() that returns the area of this rectangle.
# ■ A method named getPerimeter() that returns the perimeter.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that creates two Rectangle objects—one with width 4 and height 40
# and the other with width 3.5 and height 35.7. Display the width, height, area,
# and perimeter of each rectangle in this order.


class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return  2 * (self.height + self.width)

Rectangle1 = Rectangle(4,40)
print("Width is: ",Rectangle1.width)
print("Height is : ",Rectangle1.height)
print("Area is: ",Rectangle1.getArea())
print("Perimeter is: ", Rectangle1.getPerimeter())

Rectangle2 = Rectangle(3.5,35.7)
print("Width is: ", Rectangle2.width)
print("Height is: ", Rectangle2.height)
print("Area is: ", Rectangle2.getArea())
print("Perimeter is: ", Rectangle2.getPerimeter())
