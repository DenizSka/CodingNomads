# creating a list
bucket_list = ['climb Mt. Everest', 'eat fruits from a tree', 'raise a child']
print(bucket_list[0])  # this is how we can access individual items in the list

# let's see how lists are *mutable* by changing the second item
bucket_list += 'l'
bucket_list.extend([1])

print(bucket_list)

bucket_list.pop(-2)
print(bucket_list)

numbers = [42, 1, 10]
print(numbers)
numbers.extend([5])
print(numbers)
numbers.pop(-3)
print(numbers)
numbers.sort()
print(numbers)
