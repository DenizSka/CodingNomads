# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 21445 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

# learnings you can sort list of strings, also you can turn a string in to list with out looping.
def descending_order(num):
    z = []
    for one in str(num):
        z.append(one)
        z.sort(reverse=True)
    str_ = "".join(z)
    return str_


print(descending_order(12394))

# other solution:
# def descending_order(num):
#     s = str(num)
#     s = list(s)
#     s = sorted(s)
#     s = reversed(s)
#     s = ''.join(s)
#     return int(s)
