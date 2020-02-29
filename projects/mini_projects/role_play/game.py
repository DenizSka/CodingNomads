from characters import Hero, Opponent
from random import randint

import random

list_ = ["black widow", "iron man", "super man", "thor", "spider man", "batman"]


def generate_hero():
    level = randint(1, 500)
    b = Hero("Superwoman", level)
    return b


def generate_opponent():
    level = randint(1, 500)
    a = Opponent(random.choice(list_), level)
    return a


def remove_from_list(opponent):
    for i in range(0, len(list_)):
        if list_[i] == opponent.name:
            list_.pop(i)
            return list_


def winning_state(hero, opponent, number_):
    print(f"Our hero {hero.name} attacks {opponent.name}!")
    hero_roll = hero.level * number_
    opponent_roll = opponent.level * number_
    print(f"You roll {hero_roll}...")
    print(f"opponent rolls {opponent_roll}...")
    if hero_roll > opponent_roll:
        remove_from_list(opponent)
        return "You win"
    else:
        print(f"{opponent.name} wins")
        print("You need to wait to recharge")
        print("Ready to fight again!")


def game_state():
    print("welcome to the game, you are superwoman, you are flying through the air what is this you see:")
    opponent = generate_opponent()
    print(f"It is {opponent.name} at level {opponent.level}")
    input_ = input("Do you want to [a]ttack, [r]unaway, or [l]ook around?:")
    while input_ != "q":
        if input_ =="a":
            hero = generate_hero()
            number_ = randint(1, 10)
            print(winning_state(hero, opponent, number_))
        elif input_ == "r":
            print("You got away safely...")
        elif input_ == "l":
            print(f"These are the opponents around you {list_}")
        print("Do you wanna continue fighting you can press [a]ttack, [r]unaway, or [l]ook around")
        input_ = input("if you wanna exit game type [q]")

print(game_state())
