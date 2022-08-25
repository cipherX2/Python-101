from os import system, name
from blind_auction_art import logo

def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print(logo)
print("Welcome to secret auction program.")

bidders=[]

def add_bidder(name,bid_amount):

    bidders.append({
        "bidder": name,
        "amount": bid_amount,
    })


def user_input():

    name_of_bidder = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    add_bidder(name=name_of_bidder,bid_amount=amount)


def start():

    while True:
        user_input()
        more_people = input("Are there any other biders? Type 'yes' or 'no'. ")
        clear()
        if more_people == 'no':
            break

def declare_winner():

    max_bid = 0
    winner = ""
    for info in bidders:
        bidder_info = info
        if bidder_info["amount"] > max_bid:
            max_bid = bidder_info["amount"]
            winner = bidder_info["bidder"]
    print(f"The winner is {winner} and the bid amount was ${max_bid}")

start()
declare_winner()

