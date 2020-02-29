'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

value_list = []

for tuple_ in unsorted_list:  # I like the idea of separating loops and having one loop do one thing and than another loop do another thing. Makes the code easier to understand.
    value_list.append(tuple_[1])

print(value_list)
value_list.sort()

for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_) # this is not a while loop, loop will end after it goes through each tuple in list. We do not need to remove tuples from this list
            break  # Is this necessary? Loop will end.

print(sorted_list)
