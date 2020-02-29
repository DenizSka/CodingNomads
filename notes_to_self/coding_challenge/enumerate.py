# Create a function called my_enumerate() that mirrors the internal functionality of python's .enumerate()


def enumerate_func(list_):
    i = 0
    for one in list_:
        print(i, one)
        i += 1


enumerate_func(['eat', 'sleep', 'repeat'])
