# Funny Dots
# You will get two Integer n (width) and m (height) and your task is to draw following pattern. Each line is seperated with '\n'.
#
# Both integers are equal or greater than 1. No need to check for invalid parameters.
#
# e.g.:
#
#
#                                           +---+---+---+
#             +---+                         | o | o | o |
# dot(1,1) => | o |          dot(3,2) =>    +---+---+---+
#             +---+                         | o | o | o |
#                                           +---+---+---+

# n is width, m is height
# there is 3 lines needed for one box
# top and bottom lines are same.
# when m is 2 it means there should be 2+1 number of lines
# when n is 2 it means there should be 2+1 number of lines vertical
# first start with one square
# print('+---+')
# loop through the amount of n or m and print out this shape
def dot(n,m):
    list_shape = ['+---+']
    list_vertical = ['|']
    end_shape = []
    for i in range(1,n):
        list_shape.append('---+')
    str_shape = "".join(list_shape)

    for y in range(0,n):
        list_vertical.append(' o |')
    str_vertical = "".join(list_vertical)
    z=0
    while z<m:
        end_shape.append(f"{str_shape}\n{str_vertical}\n")
        z+=1
    end_shape.append(str_shape)
    end_shape_joined = "".join(end_shape)
    return end_shape_joined

print(dot(8,5))


# simple solution
def dot2(n, m):
    sep = '+---' * n + '+'
    dot = '| o ' * n + '|'
    return '\n'.join([sep, dot] * m + [sep])
