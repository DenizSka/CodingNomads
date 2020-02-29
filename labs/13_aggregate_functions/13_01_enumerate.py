'''
Demonstrate the use of the .enumerate() function.
'''

fruits = ['apple', 'banana', 'orange']


def aggre(list_):
    for index, one in enumerate(list_):
        print(f"{index}: {one}")


aggre(fruits)
