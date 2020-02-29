# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
# result.
# It should remove all values from list a, which are present in list b.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]


# loop with in a loop, get the occurrences of list items, save them as a str.
def array_diff(a, b):
    new_arr = []
    if len(b) > 0:
        for i in range(len(a)):
            if not a[i] in b:
                new_arr.append(a[i:i + 1])
        flattened_list = [x[0] for x in new_arr]
        return flattened_list
    else:
        return a


print(array_diff([-1, -2, 6, 8, 15, 0, 5, 18, -14, 0, 1, 5, -17, 14, -11, 13, -11, -11], [-1, -2, 6, 10, 8, 6, -12, 12, -3, -5, -20, 16]))

def array_diff(a, b):
    return [x for x in a if x not in b]
