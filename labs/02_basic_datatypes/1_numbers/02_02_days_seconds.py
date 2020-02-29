'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() function to collect users input. An example is demonstrated below.

'''

# the input of the user will be saved in the variable days.
# because the input() function collects the input as a string, we have to convert it to an int
# The string passed to the input() function is what the user is prompted with
days = int(input("Please enter a number in days between 1 and 1,000,000,000: "))

total_hours_in_day = days * 24
seconds_in_hour = 60 * 60
total_seconds = total_hours_in_day * seconds_in_hour
print("This is total seconds %s in %s days" % (total_seconds, days))
