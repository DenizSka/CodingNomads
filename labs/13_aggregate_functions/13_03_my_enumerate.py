'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(list_):
    sum = 0
    for i in list_:
        print(f"({sum}, {i})")
        sum = sum+1

my_enumerate(["hello", "yolo", "hi", "ciao"])
