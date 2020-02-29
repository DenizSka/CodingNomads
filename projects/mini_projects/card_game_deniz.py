from random import randint
class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']
    """Represents a standard playing card."""
    def __init__(self, a, b):
        self.suit = Card.suit_names[a]
        self.rank = Card.rank_names[b]

    def __str__(self):
        return '%s of %s' % (self.rank,
                             self.suit)


# Playing state:
# both computer and player gets 2 random cards.
# we need to see the sum of the card value of each player
# after this point we ask player input(you wanna continue or stand)
#if stannd computer now chosees to play. We no longer ask the player
# show both computers and players hand.

# if player chooses continue gets another random card. Computer decides if it wanna do any action
# show hands
rank_computer = []
rank_player = []


def generate_a_card():
    choose_rank = randint(0, 12)
    choose_suit = randint(0, 3)
    a = Card(choose_suit, choose_rank)
    return a


def during_game(state):
    if state == 'beginning':
        computer1 = generate_a_card()
        rank_computer.append(computer1.rank)
        computer2 = generate_a_card()
        rank_computer.append(computer2.rank)
        player1 = generate_a_card()
        rank_player.append(player1.rank)
        player2 = generate_a_card()
        rank_player.append(player2.rank)
        print(f"these are your cards {player1} and {player2}")
        return computer1, computer2, rank_computer, rank_player
    if state == 'continue_computer':
        computer = generate_a_card()
        rank_computer.append(computer.rank)
        return computer, rank_computer
    if state == 'continue':
        player = generate_a_card()
        rank_player.append(player.rank)
        return rank_player


def rank_to_integer(list_):
    # global sum_
    sum_ = 0
    for one in list_:
        if one == "Ace":
            rank = 1
        elif one == "Jack":
            rank = 11
        elif one == "Queen":
            rank = 12
        elif one == "King":
            rank = 13
        else:
            rank = int(one)
        sum_ = sum_ + rank
    return sum_


def who_won(computer_rank, player_rank):
    if player_rank < computer_rank < 21:
        return "Computer won"
    elif computer_rank < player_rank < 21:
        return "You won"
    elif player_rank > 21:
        return f"You got {player_rank}, bigger than 21, so you lose"
    elif computer_rank > 21:
        return f"Computer got {computer_rank}, bigger than 21, so you automatically win"
    elif player_rank == 21:
        return f"Wow you got 21 blackjack!! You won"
    elif computer_rank == 21:
        return f"Computer got 21 blackjack!! You lose"



def game_state():
    computer1, computer2, computer_list, player_list = during_game("beginning")
    computer_cards_list = [computer1, computer2]
    input_ = input("Do you wanna play say 'continue' if not say 'stop'")
    player_sum = rank_to_integer(player_list)
    computer_sum = rank_to_integer(computer_list)
    if computer_sum < 15:
        computer3, computer_list = during_game("continue_computer")
        computer_sum = rank_to_integer(computer_list)
        computer_cards_list.append(computer3)
        print(player_sum)
    if input_ == "continue":
        player_list = during_game("continue")
        player_sum = rank_to_integer(player_list)
        print(player_sum)
    if input_ == "stop":
        for one in computer_cards_list:
            print(f"Computer has {str(one)}")
    print(who_won(computer_sum, player_sum))


game_state()
