# Write a function that accepts an array of 10 integers (between 0 and 9), that returns
# a string of those numbers in the form of a phone number.

#
# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# list_ = [9, 4, 7, 5, 3, 4, 2, 8, 0, 6] # whats up with the numbers
list_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# k = ""
# z = ""
# y = ""

# no need a for loop - you can just do as string -slack list[0:3]
def create_phone_number(arr_):
    k = ""
    z = ""
    y = ""
    # need a loop to get each num and add them in to a string?
    # first get first 3 numbers in parenthesis
    for one in arr_:
        if arr_.index(one) < 3:
            k += str(one)
        elif 2 < arr_.index(str(one)) < 6:
            z += str(one)
        elif arr_.index(str(one)) >= 6:
            y += str(one)
    return f"({k}) {z}-{y}"


# print(create_phone_number(list_))

list_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def create_phone_number(arr_):
    k = ""
    z = ""
    y = ""
    for i in range(0, len(arr_)):
        if i < 3:
            k += str(arr_[i])
        elif 2 < i < 6:
            z += str(arr_[i])
        elif i >= 6:
            y += str(arr_[i])
    return f"({k}) {z}-{y}"


print(create_phone_number(list_))

phone_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]



# Fixed

def create_phone_number(arr_):
    list_ = []
    for one in arr_:
        list_.append(str(one))
    x = list_[0:3]
    y = list_[3:6]
    z = list_[6:]
    x = "".join(x)
    y = "".join(y)
    z = "".join(z)
    return f"({x}) {y}-{z}"


print(create_phone_number(phone_))
