'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

words_input = input('Please enter some words:')
word_count = 0
longest_word = None

# Loop through each string and get their length
for each_word in words_input:
    if len(each_word) > word_count:
        # Reassign the word_Count with the longest word's count
        word_count = len(each_word)
        # IF the word's length is the same as the word count, reassign longest word
    if len(each_word) == word_count:
        longest_word = each_word
print(longest_word)
