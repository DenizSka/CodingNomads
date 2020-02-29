'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

list_ = [112121323, 231243223, 32424242, 3242424, 1111]

xyz = (x for x in list_ if x % 1111 == 0)

for i in xyz:
    print(i)
