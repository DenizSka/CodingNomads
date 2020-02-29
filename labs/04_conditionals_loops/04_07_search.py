'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
tuple_numbers = int(input("please give us a number between 0 and 1,000,000,000:"))
numb = True
x = 0

while numb:
    if x != tuple_numbers:
        x += 1
    else:
        numb = False
        print("the number is: {}".format(x))

