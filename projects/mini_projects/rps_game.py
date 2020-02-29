# Rock-Paper-Scissors Game
# Code a game of rock paper scissors.

## Instructions

# * take in a number 0-2 from the user that represents their hand
# * generate a random number 0-2 to use for the computer's hand
# * call the function `get_hand` to get the string representation of the user's hand
# * call the function `get_hand` to get the string representation of the computer's hand
# * call the function `determine_winner` to figure out who won
# * print out the player hand and computer hand
# * print out the winner

## Some Tips

# Creating a function that gets a "hand" based on a number.
#
# The function should take in a number and return the string representation of the hand. E.g.:

import random
user = int(input("Please provide a number where 0 = scissor, 1 = rock, 2 = paper: "))


# two different functions
# one to return the string version of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        hand = "scissor"
    elif hand == 1:
        hand = "rock"
    elif hand == 2:
        hand = "paper"
    # for example if the variable hand is 0, it should return the string "scissor"
    return hand


# one for computer to generate random integer
def generate_rand():
    numb = random.randint(0, 2)
    return numb


# one to determine the winner
# winning conditions:
# paper wins over rock loses to scissor
# rock wins over scissor loses to paper
# scissor wins over paper loses to rock

def determine_winner():
    compt = generate_rand()
    # winning condition:
    if user > compt:
        if (compt == 0) and (user == 2):
            print("computer won")
        else:
            print("you won")
    elif compt > user:
        if (compt == 2) and (user == 0):
            print("you won")
        else:
            print("computer won")
    elif user == compt:
        print("its a tie")
    print(f" You put: {get_hand(user)}")
    print(f" Computer put: {get_hand(compt)}")


determine_winner()
