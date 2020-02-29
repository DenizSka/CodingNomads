# Write a function that receives two strings and returns n, where n is equal to the number of characters we should
# shift the first string forward to match the second.
#
# For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been rotated 5 characters
# forward to produce the second string, so 5 would be returned.
#
# If the second string isn't a valid rotation of the first string, the method returns -1.
# Examples:
# ``` "coffee", "eecoff" => 2 "eecoff", "coffee" => 4 "moose", "Moose" => -1 "isn't", "'tisn" => 2
# "Esham", "Esham" => 0 "dog", "god" => -1 ```
#
# shiftedDiff("coffee", "eecoff") => 2
# shiftedDiff("eecoff", "coffee") => 4
# shiftedDiff("moose", "Moose") => nil
# shiftedDiff("isn't", "'tisn") => 2
# shiftedDiff("Esham", "Esham") => 0
# shiftedDiff("dogg", "godd") => nil

def shiftedDiff(x, y):
    # We need to know if both these list have identical letters, but also we need to figure out if the sequence of
    # the letters are in order we can loop in the first one check if the letter exists in the other list, when we get
    # the first occurence of each we can save their difference
    if len(x) != len(y):
        return -1
    index_first = []
    index_second = []
    # new_list = [a for a in x if a in y]
    for i in range(0, len(x)):
        for n in range(0, len(y)):
            # print(i)
            # first check if letters exits in both strings
            if x[i] == y[n] and n not in index_second and i not in index_first:
                # print(f"this is i {i}")
                index_first.append(i)
                index_second.append(n)
    # we have a list numbers for both lists
    # print(f"this is new list {new_list}")
    # if sorted(x) == sorted(y): #trick
    #     print("same characters")
    print(f"this is index 2 {index_second}")
    print(f"this is index 1 {index_first}")
    if len(index_first) != len(x) and len(index_second) != len(y):
        return -1
    #difference can only have two values: + and - (+ list length to make +)





# print(shiftedDiff("dog", "god"))
print(shiftedDiff("eecoff", "coffee"))
# when there are two of the same letters it freaks out.
