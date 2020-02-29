# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation
# of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit
# with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as
# 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
# Example:
# solution(1000) # should return 'M'
# Help: (1-12)
# I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.
# The largest number that can be represented in this notation is 3,999

# # CCC - 300
# # CD - 400
# # D - 500
# # DC - 600
# # DCC - 700
# # CCM - 800
# # CM - 900


# is it bigger than 1000?
# this is a list that contains all numbers that equal to a roman number (based on the number passed in)

# A smaller number in front of a larger number means subtraction, all else means addition. For example:
# IV means 4, -> subtracts
# VI means 6. -> addition
# You would not put more than one smaller number in front of a larger number to subtract. So IIV would not mean 3


# variables
list_numbers = [1000, 500, 100, 50, 10, 5, 1]  # this is the rules
roman_letters = ["M", "D", "C", "L", "X", "V", "I"]


# partial functions:

# this converts the passed number in to a list of digits -> 490 [400, 90, 0]
def get_list_of_digits(number_):
    single_numbers = []
    numb_str = str(number_)
    for i in range(len(numb_str)):
        if i == len(numb_str) - 1:
            single_numbers.append(numb_str[i])
        else:
            single_numbers.append(f"{numb_str[i]}{'0' * (len(numb_str) - i - 1)}")
    single_numbers_ints = [int(i) for i in single_numbers]
    return single_numbers_ints


# this makes 2 new lists, one for all possible subtraction results of existing roman numerals and their corresponding
# roman numerals
def make_two_new_roman_num_lists():
    subtract_list = []
    new_roman_list = []
    for i in range(len(list_numbers)):
        for y in range(len(list_numbers)):
            subtracted_number = list_numbers[i] - list_numbers[y]
            if subtracted_number > 0 and subtracted_number not in list_numbers:
                first_roman = get_roman_meaning(list_numbers[i])
                second_roman = get_roman_meaning(list_numbers[y])
                new_roman = convert_subtract(first_roman, second_roman)
                new_roman_list.append(new_roman)
                subtract_list.append(abs(subtracted_number))
    return subtract_list, new_roman_list


# this one checks if the list we passed in has any of the numbers in the subtract number list.
# if there is get me the roman numeral equivalent of that number
def check_existing_possibilities(single_list, subtract_number_list, new_roman_list):
    new_list_with_roman_nums = []
    for i in range(len(single_list)):
        if single_list[i] in subtract_number_list:
            new_list_with_roman_nums.append(find_the_equivalent(single_list[i], subtract_number_list, new_roman_list))
        elif single_list[i] in list_numbers:
            new_list_with_roman_nums.append(find_the_equivalent(single_list[i], list_numbers, roman_letters))
        elif single_list[i] != 0:
            new_list_with_roman_nums.append(single_list[i])
    return new_list_with_roman_nums


# this loop is used for checking two lists and returning the element on the second list with the same index
def find_the_equivalent(numb, list_of_numbers, list_of_letters):
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == numb:
            roman_letter = list_of_letters[i]
            return roman_letter


def get_roman_meaning(numb):
    for i in range(len(list_numbers)):
        if list_numbers[i] == numb:
            roman_num = roman_letters[i]
            return roman_num


# this one converts the two numbers passed in to a single roman number (assuming we do subtraction)
def convert_subtract(rom1, rom2):
    subtract_roman = f"{rom2}{rom1}"
    return subtract_roman


# this one finds the roman number inside the roman list, appends the next list item in the roman list to the
# beginning of repeated_letter
def convert_repetitive(repeated_letter):
    for i in range(len(roman_letters)):
        if roman_letters[i] == repeated_letter:
            repeated_letter = f"{repeated_letter}{roman_letters[i - 1]}"
    return repeated_letter


# this one checks if there any repeated numbers, if so convert repetitive
def check_repetition(list_):
    i = 0
    new_list_with_repeated_letters = []
    while i < len(list_):
        if list_.count(list_[i]) > 3:
            new_list_with_repeated_letters.append(convert_repetitive(list_[i]))
        elif list_.count(list_[i]) <= 3:
            new_list_with_repeated_letters.append(list_[i])
        i += 1
    return new_list_with_repeated_letters


# this one loops each item in list_ and redefine that item to be the roman num if it matches the num in rules
def reassign_roman_meaning(numb, roman, list_):
    for i in range(len(list_)):
        if list_[i] == numb:
            list_[i] = roman


# this one converts the list to a string
def convert_list_to_string(list_roman):
    str_ = ""
    for one in list_roman:
        for inside in one:
            str_ += inside
    return str_


# this one is called to check if we can convert any numbers in the passed in list to an existing roman rule
def calling_functions(number_):
    list_of_subtract = []
    for one in list_numbers:
        # rule list has numbers that have known roman numbers, in this function while the number we pass in is bigger
        # than rule, subtract the rule from that number and append rule to a new list
        while number_ >= one:
            number_ = number_ - one
            list_of_subtract.append(one)
    # go through each item in list_of_subtract and redefine that item to be the roman num if it matches the num in
    # list_numbers
    for i in range(len(list_numbers)):
        reassign_roman_meaning(list_numbers[i], roman_letters[i], list_of_subtract)
    new_list_with_repeated_letters = check_repetition(list_of_subtract)
    return new_list_with_repeated_letters


# this one creates a new list of roman numerals that includes if the roman numeral is subtracted or added. This is
# the last step on roman numeral creation list
def verify_new_list(list_passed):
    for i in range(len(list_passed)):
        if type(list_passed[i]) == int:
            new_list_with_repeated_letters = calling_functions(list_passed[i])
            convert_list_to_string(new_list_with_repeated_letters)
            list_passed[i] = new_list_with_repeated_letters
    return list_passed


def roman_numeral_method(number_):
    single_list = get_list_of_digits(number_)
    subtract_number_list, new_roman_list = make_two_new_roman_num_lists()
    new_list_with_roman_nums = check_existing_possibilities(single_list, subtract_number_list, new_roman_list)
    print(subtract_number_list)
    print(new_roman_list)
    # so far we only have a list with subtraction used roman numerals, we need to check if there needs to be an addition
    new_list = verify_new_list(new_list_with_roman_nums)
    return convert_list_to_string(new_list)


print(roman_numeral_method(2789))
print(roman_numeral_method(3000))


# simple solution
def solution(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


print(solution(2789))
