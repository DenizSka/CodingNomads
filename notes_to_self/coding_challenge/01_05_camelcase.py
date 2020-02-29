# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"


# takes in a string - need to split them in to a list so I can capitalize the first word
# make a list of split
# make each word upper case (except for the first one - leave that as is)
# Join them all together in one string
# how can i do this in list comprehension list_ = [(x,y) for x in colors for y in sizes]

# Fails here: -_ both
# https://www.codewars.com/kata/convert-string-to-camel-case/train/python
# def to_camel_case(input_):
#     new_ = []
#     split_ = ["-", "_"]
#     for one in split_:
#         list_ = input_.split(one)
#         if len(list_) > 1:
#             new_ = list_
#     word = new_[0]
#     for one in range(1, len(new_)):
#         word += new_[one].capitalize()
#     return word


# print(to_camel_case("the-stealth-warrior"))


# list_ = [x for x in input_ for ]

# Rewrite the function without using slice or index. This version also takes in to account if the string has _ and same time -.

def to_camel_case(input_):
    list_ = list(input_)
    new = ""
    for i in range(0, len(list_)):
        if list_[i] == "_" or list_[i] == "-":
            list_[i] = ""
            list_[i + 1] = list_[i + 1].capitalize()
        new += list_[i]
    return new


print(to_camel_case("the-stealth_warrior"))


# other option
# def to_camel_case1(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


# best solution? look up translate
# def to_camel_case2(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s


# other:
# def to_camel_case3(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#     if len(removed) == 0:
#         return ''
#     return removed[0] + ''.join([x.capitalize() for x in removed[1:]])
