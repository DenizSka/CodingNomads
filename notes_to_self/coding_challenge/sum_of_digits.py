# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6

def digital_root(numb):
    sum = 0
    sum2 = 0
    # first we have to split each number and add them up.
    for one in str(numb):
        sum = sum + int(one)
        # next we have to check if we can still split them up
    while sum > 9:
        for one in str(sum):
            sum2 = int(one) + sum2
            sum = sum2
    print(sum)


# I wanna do it whit while
# def digital_root(numb):
#     sum = 0
#     while numb > 9:
#         for one in str(numb):
#             sum = sum + int(one)
#         numb = sum
#     return sum


digital_root(3596)


# recursive??
def digital_root1(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# nice
def digital_root2(n):
    while n > 9:
        digit_list = [int(digit) for digit in str(n)]
        n = sum(digit_list)
    return n
