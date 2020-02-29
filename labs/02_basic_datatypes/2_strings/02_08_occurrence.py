'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# get user input (words)
words_input = input('Please enter some words:')
# get user input (letter)
letter_input = input('Please enter a letter:')
# look for the index of the letter_input
print(words_input.find(letter_input))
