'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5
s = 0

while s < n:
    s += 1
    print('*'*s)



#nested:

for x in range(0, 5):
    for y in range(0, 5):
        if x == y:
            z = "*"*y
            print(z)


for x in range(1, 6):
    for y in range(x):
        print(f"this is {y}")
        print("*", end="")
    print()

