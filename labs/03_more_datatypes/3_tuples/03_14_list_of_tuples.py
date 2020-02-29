'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

tuple_string = input("please give us a sentence:")
list_word = tuple_string.split()
new_list = []
for one in list_word:
    list_letters = list(one)
    list_letters = tuple(list_letters)
    new_list.append(list_letters)
print(new_list)
