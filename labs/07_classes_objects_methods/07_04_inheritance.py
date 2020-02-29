'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''


# 1

class Movie1:
    pass


# 2

class Movie2:
    def __init__(self, year, title):
        self.year = year
        self.title = title


# 3
RomCom = Movie2(1983, "you got mail")


# 4
class ActionMovie(Movie2):
    def __init__(self, year="heywy", title="hello", pg=13):
        super().__init__(year, title)
        self.pg = pg


# 5
print(RomCom.title) # why this works

# How can I call pg? And how to pass in empty class when we predefine the pg already?
print(ActionMovie.pg) # why this does not? Why I have to assign it a var
y = ActionMovie("1983")
print(y.title)
