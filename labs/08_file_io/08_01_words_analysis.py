'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

with open("CodingNomads/labs/08_file_io/words.txt", "r") as words_file:
    shortest = words_file.readline()
    longest = words_file.readline()
    sum = 0
    for word in words_file:
        sum += 1
        if len(word) <= len(shortest):
            shortest = word
        elif len(word) >= len(longest):
            longest = word
    print(sum)
    print(shortest)
    print(longest)
