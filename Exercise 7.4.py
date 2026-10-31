# (The Fan class) Design a class named Fan to represent a fan. The class contains:
# ■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to
# denote the fan speed.
# ■ A private int data field named speed that specifies the speed of the fan.
# ■ A private bool data field named on that specifies whether the fan is on (the
# default is False).
# ■ A private float data field named radius that specifies the radius of the fan.
# ■ A private string data field named color that specifies the color of the fan.
# ■ The accessor and mutator methods for all four data fields.
# ■ A constructor that creates a fan with the specified speed (default SLOW), radius
# (default 5), color (default blue), and on (default False).
# Draw the UML diagram for the class and then implement the class. Write a test
# program that creates two Fan objects. For the first object, assign the maximum
# speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5,
# color blue, and turn it off for the second object. Display each object’s speed,
# radius, color, and on properties.

class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = FALSE):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def getSpeed(self):
        return self.__speed
    def setSpeed(self, speed):
        self.__speed = speed

    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.getColor
    def setColor(self, color):
        self.__color = color

    def getOn(self):
        return self.on
    def setOn(self, on):
        self.on = on

def fan1():
    fan1 = Fan()
    fan1.setSpeed(Fan.FAST)
    fan1.setRadius(5)
    fan1.setColor("Yellow")
    fan1.setOn(True)

    fan2 = Fan()
    fan2.setSpeed(Fan.MEDIUM)
    fan2.setRadius(5)
    fan2.setColor("Blue")
    fan2.setOn(False)

print("Fan 1 speed: ", fan1.setSpeed())
print("Fan 1 radius is: ", fan1.getRadius())
print("Fan 1 color is: ", fan1.getColor())
print("Fan 1 is : ", fan1.getOn())

print("Fan 1 speed: ", fan2.setSpeed())
print("Fan 1 radius is: ", fan2.getRadius())
print("Fan 1 color is: ", fan2.getColor())
print("Fan 1 is : ", fan2.getOn())



