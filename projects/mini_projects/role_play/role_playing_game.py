# Using OOP with python to create a text-based command-line interface role-playing game.
# Digital dice included!
#
# Task Instructions
# Build a text-based role-playing game that has at least 2 classes:
#
# a Hero() class
# an Opponent() class
# The Hero should encounter multiple Opponents of different strengths (or levels) and be able
# to perform different actions in regards to them - at a minimum:

#
# attack and run away.
# If the Hero chooses to attack, the program decides through a simulated dice throw that
# takes the current level into account, whether the Hero or the Opponent wins this round.
#
# Implement consequences for winning and losing, e.g. forcing the Hero to wait a few seconds
# before continuing the game in case they lose, or removing the Opponent from the Opponent pool
# in case the Hero wins.
#
# Hints
# There is a finished possible solution available in this repo, that allows you to safely defuse
# your digital rage against Paywalls, PHP and even Wordpress sites. ;-)
#
# However, I strongly suggest to build out your own idea. Using what you are interested in
# makes for the most fun coding experiences and the biggest learning effect!
#
# How to play the pre-made game
# To inspect the pre-made solution, download the repo and run the file main.py in a Python 3
# environment. The rest is about typing l for lookaround, a for attacking, and r for runaway.


# make two classes hero and opponents both will have strength level and name. strength will be chosen
# randomly with each function call. (there will be multiple opponents)
# a separate function of if call for winning and losing. If hero wins remove the opponent from opponent list
# if hero loses hero has to wait
