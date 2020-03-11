# I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.
# You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary
# is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the
# entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.
# Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be
# changed. E.g. the mistyped term berr is more similar to beer (1 letter to be replaced) than to barrel (3 letters to be changed in total).
#
# Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.
#
# Code Examples:
#
# fruits = new Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry']);
# fruits.findMostSimilar('strawbery'); // must return "strawberry"
# fruits.findMostSimilar('berry'); // must return "cherry"
#
# things = new Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars']);
# things.findMostSimilar('coddwars'); // must return "codewars"
#
# languages = new Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript']);
# languages.findMostSimilar('heaven'); // must return "java"
# languages.findMostSimilar('javascript'); // must return "javascript" (same words are obviously the most similar ones)
# I know, many of you would disagree that java is more similar to heaven than all the other ones, but in this kata it is ;)
#
# Additional notes:
# there is always exactly one possible correct solution

class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        # break down the term to list letters
        # loop through the words class, first check if the term is in the words list. if yes return
        # if not check each word.
        diff = len(list(term))
        term = term.lower()
        similar_word = None
        cost = 1000
        sum_letters = 0
        for one in self.words:
            word = one.lower()
            if term == word:
                return one
            else:
                different_letters = [0 if letter in word else 1 for letter in term]
                diff_letter_len = abs (len (list (word)) - len (list (term)))
                if cost > sum(different_letters)+ diff_letter_len:
                    cost = sum(different_letters)+ diff_letter_len
                    similar_word = one
        return similar_word



words=['java', 'python']
test_dict = Dictionary (words)

print(test_dict.find_most_similar('heaven'))
# edit distance

