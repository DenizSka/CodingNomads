'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Food:
    def __init__(self, calorie, amount):
        self.calorie = calorie
        self.amount = amount


class Vegetable(Food):
    def __init__(self, calorie, amount, color):
        super().__init__(calorie, amount)
        self.color = color

class Lettuce(Vegetable):
    def __init__(self, calorie, amount, color, taste):
        super().__init__(calorie, amount, color)
        self.taste = taste


a = Lettuce("None", "5gr", "green", "good")

print(a.calorie)
