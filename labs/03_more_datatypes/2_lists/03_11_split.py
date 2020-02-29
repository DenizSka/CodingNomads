'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''


tuple_string = input("please give us a long sentence:")
new_list = tuple_string.split()
count_ = []
for one in new_list:
    count_.append(new_list.count(one))
count_.sort()

print(count_)
