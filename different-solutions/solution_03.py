'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

for x in range(0, len(unsorted_list)):  # Why do we have two loops doing the same thing?
    #x is never used (Think of this like a while loop. We set up the while loop to loop through 3 times. Nw we are doing the same thing with rage
    min = unsorted_list[0][1] #these couple have been defined out side of this loop - yes probably on this example
    print(min)
    index = 0

    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < min:
            min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index]) # we dont need to remove it from unsorted? Range is already set up to loop 3 times right? Why?


print(unsorted_list)
print(sorted_list)
