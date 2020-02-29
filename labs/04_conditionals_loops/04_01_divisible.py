'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

numb = True
while numb:
    tuple_numbers = input("please give us a number between 1 and 1,000,000,000:")
    if 0 < tuple_numbers < 1000000000:
        numb = False
        if tuple_numbers % 3 is 0:
            print("it is divisible by 3")
        else:
            print("not divisible by 3")
    else:
        tuple_numbers = input("please give us a number between 1 and 1,000,000,000:")
