# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# solved
def unique_in_order(iterable):
    z = []
    y = list(iterable)
    if len(y) != 0:
        z.append(y[0])
        for i in range(0, len(y)):
            if y[i] != z[len(z)-1]:
                z.append(y[i])
    return z


print(unique_in_order(''))

# other solution

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

# other solution
def unique_in_order(iterable):
    k = []
    for i in iterable:
        if k == []:
            k.append(i)
        elif k[-1] != i:
            k.append(i)
    return k
#
# def unique_in_order(iterable):
#     a = iterable.upper()
#     y = list(a)
#     z = []
#     for i in range(0, len(y)):
#         if i<len(y)-1 and y[i] == y[i+1]:
#             z.append(y[i])
#         elif iterable.count(y[i]) == 1:
#             z.append(y[i])
#     print(z)

# print(unique_in_order([1,2,2,3,3]))


# can not split a string
