'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# get user input (sentence)
string_input = input('Please enter sentence:')
# get user input (symbol)
symbol_input = input('Please enter symbol:')
# get first letter of sentence (from the zero'th index
first_letter = string_input[0]
# replace all occurences of first letter with symbol
print(string_input.replace(first_letter, symbol_input))
