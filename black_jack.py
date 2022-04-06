############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
machine_hand= []
sum_machine_hand = sum(machine_hand)

def blackjack():
    more_cards = True
    sum_machine_hand = 0
    for x in range (2):
       player_hand.append(deck[random.randint(0,12)])
    print(f"{player_hand} Player hand total {sum(player_hand)}")
    for y in range(2):
        machine_hand.append(deck[random.randint(0,12)])
    print(f"{machine_hand} Machine hand total {sum(machine_hand)}")
    while more_cards:
        game_continue = input(f"Do you want another card ? y or n ") .lower()
        print("\n")
        if game_continue == "y":
            player_hand.append(deck[random.randint(0,12)])
            if sum(player_hand) > 21:
                print(f"Machine wins, you take {sum(player_hand)} points. {player_hand}")
                more_cards = False
        print(f"{player_hand}, Player hand total {sum(player_hand)}")
        print(f"{machine_hand}, Machine hand total {sum(machine_hand)}")
        if game_continue == "n":
            while sum(machine_hand) < 16:
                machine_hand.append(deck[random.randint(0,12)])
                sum_machine_hand = sum(machine_hand)
                if sum_machine_hand > 21:
                    print(f"Player wins, Machine took more {sum_machine_hand} points. {machine_hand}")
                    more_cards = False
            more_cards = False
    if sum(player_hand) > sum(machine_hand) and sum(player_hand)<22:
        print(f" Player's hand {sum(player_hand)} wins against Machine's hand {machine_hand}.\n")
    elif sum(machine_hand) > sum(player_hand) and sum_machine_hand<22:
        print(f" Machine's hand {sum_machine_hand} wins against Player's hand {player_hand}.\n")
blackjack()

if input("Do you wanna play Blackjack again? y or n ") .lower() == "y":
    player_hand.clear()
    machine_hand.clear()
    blackjack()
