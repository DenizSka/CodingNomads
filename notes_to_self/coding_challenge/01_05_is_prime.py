# Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */
# Assumptions
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
# There are no fancy optimizations required, but still the most trivial solutions might time out.
# Try to find a solution which does not loop all the way up to n.


# divisible by 2 -> should be even
# divisible by 3 -> sum of its integers should de divisible by 3
# divisible by 4 -> is also div by 2
# div by 5 -> does it end with 0 or 5?
# div by 6 -> should be div by 3 but also 2 - should  even
# div by 7 ->   take the last digit off the number, double it and subtract the doubled number from the remaining number. If the result is evenly divisible by 7 (e.g. 14, 7, 0, -7, etc.), then the number is divisible by seven.
# 8 -> 4 and 2
# 9 -> 3
# 10 -> 0 even
import math

list_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]


def is_prime(num):
    list_ = list(str(num))
    if num > 2:
        if int(list_[-1]) == 0 or int(list_[-1]) % 2 == 0 or int(list_[-1]) == 5:
            return False
    for one in list_primes:
        if num != one and num % one == 0:
            print(one)
            return False
        elif num == one:
            print(num)
            return True
        else:
            return False


# print(is_prime(73)) #??

def is_prime_simple(num):
    for one in range(2, num):
        if num % one == 0:
            return False
    return True


# print(is_prime_simple(4))


def prime_optimized(num):
    list_ = [2, 3, 5, 7]
    if num < 2:
        return False
    if num in list_:
        return True

    for one in range(2, int(math.sqrt(num)) + 1):
        print(one)
        if one % 2 != 0 and one % 3 != 0 and one % 5 != 0 and one % 7 != 0:
            list_.append(one)

    print(list_)
    for one in list_:
        if num % one == 0:
            return False
    return True

print(f" this is sqrt {math.sqrt(997)}")
print(prime_optimized(81))

# n = x * y
# y = n / x

# read about sqrt
