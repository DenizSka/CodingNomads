'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''


fahrenheit_input = int(input('Please enter current Fahrenheit:'))
celsius = (fahrenheit_input-32)*(float(5)/9)
print("%s degrees fahrenheit =  %s degrees celsius" % (fahrenheit_input, celsius))
