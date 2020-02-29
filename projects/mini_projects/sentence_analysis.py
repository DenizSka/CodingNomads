# Sentence Analysis Tool
# Write a script that takes a sentence from the user and returns:
#
# - the number of lower case letters
# - the number of uppercase letters
# - the number of punctuations characters
# - the total number of characters
#
# Use a dictionary to store the count of each of the above.
# **Note**: ignore all spaces.
#
# Example input:
# ```
# I love to work with dictionaries!
# ```
# Example output:
# ```
# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28
# ```
sent = input("please write a sentence:")
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
sum = 0
upp = 0
punc = 0
empt = 0

for x in sent:
    if x == " ":
        empt += 1
    for y in alphabet:
        if x.upper() == y:
            sum += 1
            if x == x.upper():
                upp += 1

punc = len(sent) - (sum + empt)

print(f"This is sum {sum}, punctuation: {punc}, uppercase {upp}, lowercase {sum-upp}")
