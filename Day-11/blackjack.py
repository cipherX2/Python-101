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
import art
# random.seed(int(input("Enter a seed number: ")))

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []
is_game_over = False

def calculate_score(cards):
    """Takes a lsit of card and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    card_sum = sum(cards)
    return card_sum

def deal_card():
    """Returns a random card from the deck."""

    card = random.choice(cards)
    return card

def compare(user_score,computer_score):
    """Decides the game."""

    if user_score == dealer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose the Dealer has the blackjack"
    elif user_score == 0:
        return "USer wins"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score >21:
        return "You won"
    elif user_score > computer_score:
        return "USer wins"
    else:
        return " You lose"


for _ in range(0,2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

while not is_game_over:

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"   Your cards: {user_cards}, current_score: {user_score}")
    print(f"   Dealer's first card: {dealer_cards[0]}")
            
    if user_cards == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_input = input("Typye y to get another card, type n to pass: ").lower()
        if user_input == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
    
while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards())

print(f"   Your cards: {user_cards}, current_score: {user_score}")
print(f"   Dealer's cards: {dealer_cards}")
ok = compare(user_score,dealer_score)

print(ok)