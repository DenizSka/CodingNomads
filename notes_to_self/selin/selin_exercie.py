def exercise_test():
    values = []
    rolling = open("./text_main.txt", 'r')

    # Append each line in the file to the values list
    for line in rolling.readlines():
        values.append(line)
    # loop through each value make make each element in the list its own list of numbers.
    for i in range(1, len(values)):
        new_list = values[i].split(" ")
        # # here we are removing the line number
        new_list.pop(0)
        for j in range(0, len(new_list)):
            # if statement is needed due to out of index issue
            if j < len(new_list)-1:
                # reassign this list item as a string
                new_list[j] = f"{new_list[j]} {new_list[j+1]} {new_list[j+2]}\n"
                # delete the next 2 list items since I added them as a string to list item j
                del new_list[j+1:j+2]
        with open(f"./text{i}.txt", "w") as file_var:
            for one in new_list:
                file_var.write(one)


# way 2 :
#             # when we reach the 3rd number add a \n to its end
#             if j < len(new_list)-1:
#                 new_list[j] = f"{new_list[j]} {new_list[j+1]} {new_list[j+2]}\n"
#                 del new_list[j+1:j+2]
#         #     if (j + 1) % 3 == 0:
#         #         new_list[j] = f"{new_list[j]}\n"
#         # str1 = " "
#         print(new_list)
#         with open(f"./text{i}.txt", "w") as file_var:
#             for one in new_list:
#             # file_var.write(str1.join(new_list))
#                 file_var.write(one)
exercise_test()
