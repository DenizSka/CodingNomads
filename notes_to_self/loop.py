# list_number = [7,3,6]
# number = 0;
# for(i=0; i<list_number.length; i++){
#     if (list_number[i] > number){
#         number = list_number[i]
#     }
#     print(number)
# }
#
# print(number)


# Get the smallest number is the list
list_number = [7, 3, 6, 1, 2]
number = list_number[0]

for one_number in list_number:
    if number > one_number:
        number = one_number

print(number)

#  Get the longest number in the list
list_number = [7, 3, 6, 1, 2]
number = 0

# Loop through each string and get their length
for one_number in list_number:
    if one_number > number:
        number = one_number

print(one_number)
