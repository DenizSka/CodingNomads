'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

list_ = [112121323, 231243223, 32424242, 3242424, 1111]

xyz = (x for x in list_ if x % 1111 == 0)

for i in xyz:
    print(i//1111)

