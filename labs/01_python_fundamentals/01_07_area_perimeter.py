'''

Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.4 and a height of 6.4.

'''


def perimeter_area(x, y):
    perimeter = (x + y) * 2
    area = x * y
    return "This is perimeter %s and this is area %s" % (perimeter, area)
    # return f"This is perimeter {perimeter} and this is area {area}"


print(perimeter_area(2.4, 6.4))
