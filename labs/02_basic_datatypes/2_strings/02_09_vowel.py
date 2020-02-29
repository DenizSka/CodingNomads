'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''


string_input = input('Please enter a sentence:')
vowels = ['a', 'e', 'i', 'o', 'u']
vow_count = 0

# loop through the each vowel and check if they exist in the input
# string.count('a') -> returns the number of occurrences of that substring inside the string
for vow in vowels:
    vow_count += string_input.count(vow)

print(vow_count)
