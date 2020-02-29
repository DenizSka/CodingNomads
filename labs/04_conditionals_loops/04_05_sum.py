'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

one_numb1 = int(input("Please write a number:"))
one_numb2 = int(input("Please write another number:"))
sum = 0
for numbs in range(one_numb1, one_numb2+1):
    sum += numbs
print(sum)
