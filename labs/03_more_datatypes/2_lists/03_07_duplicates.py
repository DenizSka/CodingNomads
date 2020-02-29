'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]
for one in list_:
    if list_.count(one) > 1:
        list_.remove(one)
print(list_)

