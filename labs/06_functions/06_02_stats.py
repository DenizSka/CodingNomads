'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(list_):
    min_ = list_[0]
    max_ = list_[0]
    sum_ = 0
    ave_ = 0
    for x in list_:
        if min_ > x:
            min_ = x
        elif max_ < x:
            max_ = x
        sum_ += x
        ave_ = sum_ / len(list_)
    print(f"this is min: {min_}, this is max {max_}, this is sum: {sum_}, and this is avg: {ave_}")


# call the function below here
print(stats(example_list))
