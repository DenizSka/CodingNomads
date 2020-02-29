'''

Write a script that completes the following tasks.

'''


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

def div_by_numbs1(numb):
    if numb % 4 == 0 or numb % 7 == 0:
        return True
    else:
        return False


print(div_by_numbs1(14))


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def div_by_numbs2(numb):
    if numb % 4 == 0 and numb % 7 == 0:
        return True
    else:
        return False


print(div_by_numbs2(14))

# take in a number from the user between 1 and 1,000,000,000
user_input = input("Please provide number between 1 and 1,000,000,000:")


# call your functions, passing in the user input as the arguments, and set their output equal to new variables
def what_number(user):
    new_var = user
    return new_var


# print your new variables to display the results
print(what_number(user_input))

