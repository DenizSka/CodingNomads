'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

invest_input = int(input('Please enter invest amount:'))
interest_input = int(input('Please enter interest rate in percentage (without % at the end):'))
years_input = int(input('Please enter number of years to invest:'))

future_value = invest_input * (1+interest_input) ** years_input

print(future_value)
