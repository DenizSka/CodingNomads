# A strongness of an even number is the number of times we can successively divide by 2 until we reach
# an odd number starting with an even number n.
#
# For example, if n = 12, then
# 12 / 2 = 6
# 6 / 2 = 3
# we divided successively 2 times and we reached 3, so the strongness of 12 is 2.
# If n = 16 then
# 16 / 2 = 8
# 8 / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# we divided successively 4 times and we reached 1, so the strongness of 16 is 4
# Task
# Given a closed interval [n, m], return the even number that is the strongest in the interval.
# If multiple solutions exist return the smallest strongest even number.
# Note that programs must run within the alloted server time; a naive solution will probably time out.
# Constraints
# 1 <= n < m <= INT_MAX
#
# Examples
# for the input [1, 2] return 2 (1 has strongness 0, 2 has strongness 1)
# for the input [5, 10] return 8 (5, 7, 9 have strongness 0; 6, 10 have strongness 1; 8 has strongness 2)
# for the input [48, 56] return 48

# def strongest_even(n, m):
    # check the range of n and m and get the highest number that is divisible by 2
    # let's keep it simple -> check if n or m is divisible by 2, if both are check which one is larger.
    # make a while loop to keep on dividing that number to 2 until we reach an odd number. inside the while loop add
    # strogness as plus one in each division.
    # if (n % 2 == 0) and (m % 2 != 0):
    #     n
    # elif (n % 2 != 0) and (m % 2 == 0):
    #     m
    # elif (n % 2 == 0) and (m % 2 == 0):
    #     if m>n:
    #         m
    #     else:
    #         n
    # elif (n % 2 != 0) and (m % 2 != 0):
    #     if m>n:
    #         m-1
    #     else:
    #         n-1


def stronges_lvl(k):
    strongnes = 0
    if k % 2 == 1 or int(k) == 0:
        return 0
    while k % 2 == 0:
        k = k/2
        strongnes += 1
    return strongnes
#
# print(strongest_even(28))

# fixed
def strongest_even(m, n):
    strength_level = 0
    strong_number = 0
    for i in range(m, n+1):
        if stronges_lvl(i) >= strength_level:
            strength_level = stronges_lvl(i)
            strong_number = i
    return strong_number

print(strongest_even(0,14))

