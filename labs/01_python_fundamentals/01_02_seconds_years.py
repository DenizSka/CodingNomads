'''

Write the code to calculate how many seconds are in a year in this file,
so you can execute it as a script and receive the output to your console.

'''


def seconds(days):
    seconds_in_hour = 60 * 60
    total_hours_in_year = days * 24
    total_seconds = seconds_in_hour * total_hours_in_year
    return total_seconds


print(seconds(365))
#  python 01_python_fundamentals/01_02_seconds_years.py
