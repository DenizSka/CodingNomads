# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the
# total time

# required for all the customers to check out!
#
# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value
# is the
# amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.
# Important
# Please look at the examples and clarifications below, to ensure you understand the task correctly :)

# Examples
# queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

# queue_time([2,3,10], 2) should return 12
# Clarifications There is only ONE queue serving many tills, and The order
# of the queue NEVER changes, and The front person in the queue (i.e. the first element in the array/list) proceeds
# to a till as soon as it becomes free. N.B. You should assume that all the test input will be valid, as specified
# above.
#
# P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool,
# with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

# customers is an array of numbers, and they are in order. n is the amount of cashiers
# we need to get the average number of the input. And if that average number is below the first item in the array,
# return the first number of the array as the average time

# we should get the median of the list to know if up to that point it will skew the average


def queue_time_old(customers, n):
    ave_ = sum(customers) / n
    sum_up_to_now = 0
    median_ = (len(customers) + 1) / 2
    i = 0
    if len(customers) == 0:
        return 0
    elif len(customers) < n:
        list_ = sorted(customers)
        return list_[-1]
    else:
        while i < median_:
            i += 1
            # while i is smaller than the median if the sum up to the median is bigger than
            if sum_up_to_now > ave_:
                sum_up_to_now += customers[i]
                return sum_up_to_now
                break
            else:
                return int(ave_)


# no ave or median
# greedy approach

def get_smallest_number(list_):
    smallest = list_[0]
    for one_client in list_:
        if smallest >= one_client:
            smallest = one_client
    return smallest


def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    else:
        if n == 1:
            sum_ = 0
            for one in customers:
                sum_ += one
            return sum_
        elif n > len(customers):
            customers.sort(reverse=True)
            return customers[0]
        elif len(customers) > n:
            # First we take n (cashier) number of customers from the current customer in line list
            customers_in_line = customers[n:]
            # Second we make a cashier list with the current clients
            cashier_queues_list = customers[0:n]
            # Third we find the fastest customer in that cashier list
            fastest_queue = get_smallest_number(cashier_queues_list)
            # I am basically trying to get the index of the fastest queue here:
            while len(customers_in_line) > 0:
                # print(f"customers_in_line  while -- {customers_in_line}")
                for i in range(0, len(cashier_queues_list)):
                    # print(f"customer_to_move {i} --- {customer_to_move}")
                    if fastest_queue == cashier_queues_list[i] and len(customers_in_line) > 0:
                        customer_to_move = customers_in_line.pop(0)
                        # Remove the customer that moved to a cashier from the customers in line list
                        # this is the next customer to move from the customers in line list
                        print(f"fastest queue {i} -- {fastest_queue}")
                        # We wanna move this customer to the fastest cashier first
                        # The time of that cashier now is first customer plus next customer
                        cashier_queues_list[i] = fastest_queue + customer_to_move
                        # Now we have a new cashier queue list, find the fastest cashier now
                        fastest_queue = get_smallest_number(cashier_queues_list)
                        print(f"cashier queue list {i} {cashier_queues_list}")
            cashier_queues_list.sort(reverse=True)
            return cashier_queues_list[0]

# print(queue_time([10,2,3,3], 2))
# print(queue_time([2,2,3,3,4,4], 2))
# print(queue_time([], 1))
# print(queue_time([21, 32, 3, 31, 38, 38, 35, 42, 4, 44, 4, 28, 39, 11, 36, 22, 7, 7, 20], 4))
# print(queue_time([1,2,3,4,5], 100))
