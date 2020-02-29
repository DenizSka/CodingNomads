list_1 = [20, 20, 20, 20, 20, 20]

# if all the elements in the list are the same

x = list_1[0]
list_ = []


def similar():
    for i in range(1, len(list_1)):
        if list_1[i] != list_1[0]:
            return False
    return True


print(similar())
