word_list = []
rever_list = []
with open("/Users/denizskantz/personal/python/CodingNomads/labs/08_file_io/words2.txt", "r") as file_:
    for one in file_.readlines():
        one = one.rstrip()
        word_list.append(one)
    print(word_list)
    for one in word_list:
        str_ = ""
        for o in one:
            str_ = o + str_
        rever_list.append(str_)
        print(f"this is  one {one}")
        print(f"this is str {str_}")
print(f"this is word list {word_list}")

with open("/Users/denizskantz/personal/python/CodingNomads/labs/08_file_io/words_reverse.txt", "w") as fi_:
    for i in reversed(range(len(rever_list))):
        fi_.write(f"{rever_list[i]}\n")

with open("/Users/denizskantz/personal/python/CodingNomads/labs/08_file_io/words_reverse.txt", "r") as file_:
    print(file_.readlines())
