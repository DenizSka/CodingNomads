# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others.
# Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

def iq_test(numbers):
    n = 0
    f = 0
    m = 0
    k = 0
    z = list(numbers.split())
    print(z)
    for one in z:
        if int(one) % 2 == 0:
            n += 1
            m = int(one)
        elif int(one) % 2 == 1:
            f += 1
            k = int(one)
    if f == 1:
        return z.index(f"{k}")+1
    else:
        return z.index(f"{m}")+1


print(iq_test("88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46"))

#other optimized answer

def iq_test(numbers):
    indexEven = 0
    indexOdd = 0
    numEven = 0
    numOdd = 0
    nums = numbers.split(" ")
    for i in range(len(nums)):
        if int(nums[i])%2 == 0:
            numEven += 1
            indexEven = i+1
        else:
            numOdd += 1
            indexOdd = i+1
    if numEven == 1:
        return indexEven
    else:
        return indexOdd
