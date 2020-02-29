'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Planet():
    def __init__(self, color, name):
        """Initialiser"""
        self.color = color
        self.name = name

    def __str__(self):
        return f"planet {self.name} and color is {self.color}"


earth = Planet('blue', 'earth')
print(earth)
