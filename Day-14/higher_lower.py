from game_data import data
import art
import random
from os import system, name

is_game_on = True
score = 0

def clear():
    """"Use this to clear your screen"""

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def check_result(object1,object2,choice):
        """Compares the follower count and checks with the user choice"""

        followers_of_a = object1["follower_count"]
        followers_of_b = object2["follower_count"]
        if choice == "a" and followers_of_a > followers_of_b:
            return 1
        elif choice == "b" and followers_of_b > followers_of_a:
            return 1
        else:
            return 0

first_object = random.choice(data)

while is_game_on == True:

    print(art.logo)
    second_object = random.choice(data)
    if score > 0:
        print(f"You are right!, Current score: {score}")

    print(f"Compare A: {first_object['name']}, a {first_object['description']}, from {first_object['country']}")
    print(art.vs)
    print(f"Compare B: {second_object['name']}, a {second_object['description']}, from {second_object['country']}")

    user_choice = input("Choose who has more followers: A or B ").lower()
    output = check_result(first_object,second_object,user_choice)

    clear()
    if output == 0:
        print(art.logo)
        print(f"That's wrong, Your final score will be {score}")
        is_game_on = False
    else:
        score += 1
        first_object = second_object
        

