'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''


# Convert an int to a float
int_input = int(input('Please enter int:'))
print(float(int_input))

# Convert a float to an int
float_input = float(input('Please enter float number:'))
print(int(float_input))

# Perform floor division using a float and an int.
int_input1 = int(input('Please enter an int:'))
float_input1 = float(input('Please enter a float:'))
print(int_input1//float_input1)

# Use two user inputted values to perform multiplication.
int_input2 = int(input('Please enter an int:'))
int_input3 = int(input('Please enter another int:'))
print(int_input2*int_input3)
