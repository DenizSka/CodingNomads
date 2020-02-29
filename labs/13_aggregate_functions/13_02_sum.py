'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''


def sum(list_):
    sum = 0
    for i, one in enumerate(list_):
        sum = sum+one
    return sum


print(sum([1,2,3,4,5,7]))
