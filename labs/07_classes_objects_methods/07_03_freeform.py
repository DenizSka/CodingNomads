'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


# classes with str method

class House:
    def __init__(self, typeof="condo", rooms=5, location="NY"):
        self.typeof = typeof
        self.rooms = rooms
        self.location = location

    def __str__(self):
        return f"This house is a {self.typeof} and has {self.rooms} rooms."

    def __add__(self, other):
        return self.rooms + other.rooms


# its objects
class Mansion(House):
    def __init__(self, typeof, rooms, price):
        super().__init__(typeof, rooms)
        self.price = price

    def change(self, less_rooms):
        """Reduces the amount of rooms."""
        self.rooms -= less_rooms


class Townhouse(House):
    def __init__(self, typeof, rooms, location):
        super().__init__(typeof, rooms)
        self.location = location


# class
class Animal:
    def __init__(self, species="mammal", typeof="domestic"):
        self.species = species
        self.typeof = typeof

    def __str__(self):
        return f"This animal is a {self.mammal} and is {self.typeof}."


# its objects
class Dog(Animal):
    def __init__(self, species, typeof, eat_meat="yes"):
        super().__init__(species, typeof)
        self.eat_meat = eat_meat


class Fish(Animal):
    def __init__(self, species, typeof, make_sound):
        super().__init__(species, typeof)
        self.make_sound = make_sound


# class
class Plant:
    def __init__(self, name="daisy", color="white"):
        self.name = name
        self.color = color

    def __str__(self):
        return f"This plant is called {self.name} and its color is {self.color}."


# its objects
class Rose(Plant):
    def __init__(self, name, color, water_amount):
        super().__init__(name, color)
        self.water_amount = water_amount


class FigTree(Plant):
    def __init__(self, name, color, size):
        super().__init__(name, color)
        self.size = size


a = Mansion("Mansion", 6, "2 million")
print(a)
e = House("Hotel", 100)
print(a+e)
print(a.__add__(3))
print(a.change(3))

b = FigTree("Nameless", "blue", "big")
print(b.size)

c = Animal()
print(c.typeof)

