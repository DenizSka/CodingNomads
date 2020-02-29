'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


# can we do together
def multiple_func(x, y):
    def double_time(x):
        return x ** 2

    def difference_two(y, double_time):
        return double_time - y

    def print_all(difference_two, double_time):
        print(f"this is x: {difference_two} and this is {double_time}")

    return print_all


print(multiple_func(5, 7))
