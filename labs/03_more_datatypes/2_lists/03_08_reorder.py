'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
# if we have time review this. (kind of repetitive):
tuple_numbers = input("please give us ten numbers:")
list_ = []

for one in tuple_numbers:
    if tuple_numbers.index(one) % 2:
        list_.append(one)

for one in tuple_numbers:
    if tuple_numbers.index(one) % 2 == 0:
        list_.append(one)

print(list_)
