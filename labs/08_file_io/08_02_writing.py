'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

#How would I have done it in another way?
# word_list = []
# with open("CodingNomads/labs/08_file_io/words2.txt", "r") as file_:
#     for one in file_.readlines():
#         one = one.rstrip()
#         word_list.append(one)
#
#     for one in word_list:
#         str_ = ""
#         for o in one:
#             str_ = o + str_
#         word_list.append(str_)
# print(word_list)
# with open("CodingNomads/labs/08_file_io/words_reverse.txt", "w") as fi_:
#     for i in reversed(range(len(word_list))):
#         fi_.write(word_list[i])
#
#
# with open("CodingNomads/labs/08_file_io/words_reverse.txt", "r") as file_:
#     file_.readlines()


#another way
word_list = []
with open("CodingNomads/labs/08_file_io/words2.txt", "r") as file_:
    for one in file_.readlines():
        one = one.rstrip()
        str_ = one[::-1]
        word_list.append(str_)
print(word_list)

with open("CodingNomads/labs/08_file_io/words_reverse.txt", "w") as fi_:
    for one in word_list:
        fi_.write(f"{one}\n")

with open("CodingNomads/labs/08_file_io/words_reverse.txt", "r") as file_:
    file_.readlines()
