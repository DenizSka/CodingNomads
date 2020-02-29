'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

# need help
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for one in starting_list:
    for inside in one:
        print(inside)


# starting_list = [[[1, 2, 3, 4]], [[5, 6], [7, 8, 9]]] -> find this 
