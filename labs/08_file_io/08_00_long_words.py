'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

# (how can I make it relative path)
with open("CodingNomads/labs/08_file_io/words.txt", "r") as read_words:
    for word in read_words.readlines():
        if len(word) > 20:
            print(word)
