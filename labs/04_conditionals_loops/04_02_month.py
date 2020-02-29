'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

tuple_numbers = input("please give us a number between 1 and 12:")
if 0 < int(tuple_numbers) < 13:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for one in months:
        if int(tuple_numbers) - 1 == months.index(one):
            print(one)
else:
    print("other")
