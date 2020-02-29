'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''


input_dict = {"item1": 5, "item2": 6, "item3": 1}
min_val = input_dict["item1"]
result_list = []

while len(result_list) < len(input_dict):
    for key, value in input_dict.items():
        if min_val > value:
            min_val = value
            result_list.append((key, value))

#  this is an infinite loop
print(result_list)
