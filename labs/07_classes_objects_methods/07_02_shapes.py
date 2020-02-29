'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        return self.length*self.width

    def perimeter_rectangle(self):
        return 2*(self.length + self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        return int((self.radius**2)*3.14)

    def circumference_circle(self):
        return int(self.radius*3.14*2)


circle = Circle(10)
print(circle.area_circle)
print(circle.circumference_circle)

rectangle = Rectangle(5, 10)
print(rectangle.area_rectangle)
print(rectangle.perimeter_rectangle)
