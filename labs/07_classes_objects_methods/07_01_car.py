'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car:
    def __init__(self, model, year, max_speed):
        """Initialiser"""
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 5

    def __str__(self):
        return f"details model: {self.model}, year {self.year}, max_speed: {self.max_speed}"


toyota = Car("toyota", 1985, 45)
print(toyota)
mazda = Car("mazda", 1975, 50)
print(mazda)
mazda.increase_speed()
print(mazda.max_speed)


