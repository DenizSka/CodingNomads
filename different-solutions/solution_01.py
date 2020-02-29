'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#while we still have values in the unsorted list
while len(unsorted_list) > 0:
    #loop through the unsorted list to find the minimum value

    #why are we defining these values inside of the while loop?
    current_value = unsorted_list[0][1] # unused value
    min_value = unsorted_list[0][1]
    index = 0
    for tuple_ in unsorted_list:
        #save the minimum value to use outside of this for loop
        if tuple_[1] <= min_value:
            min_value = tuple_[1]
            min_index = index # we are saying min index is same as index, why?
        index += 1 #increasing the index by one

    #push the minimum value onto the sorted list
    sorted_list.append(unsorted_list.pop(min_index))
    print("unsorted list is " + str(unsorted_list))

print(sorted_list)

# MY solution can we review the problem here:
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
new_list = []
index = 0

while len(unsorted_list) > 0:
    min_value = unsorted_list[0][1]
    for tuple_ in unsorted_list:
        if min_value >= tuple_[1]:
            min_value = tuple_[1]
            index = unsorted_list.index(tuple_)
    new_list.append(unsorted_list.pop(index))
print(new_list)
