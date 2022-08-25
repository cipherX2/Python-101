import art
import random

print(art.logo)

print("Welcome to the number guessing game.")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1, 101)
print(number)

EASY_MODE = 10
HARD_MODE = 5

def set_difficulty(difficulty):
    """Sets the difficulty level of the game."""

    if difficulty == "easy":
        return EASY_MODE
    elif difficulty == "hard":
        return HARD_MODE
    else:
        print("Wrong input")


def check_guess(guess):
    """Checks the guess and responds accordingly."""

    if guess == number:
        return 0
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    return -1

def game():
    """Runs the game."""
    
    is_game_on = True
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempt = set_difficulty(difficulty)
    while is_game_on == True and attempt > 0:
        print(f"You have {attempt} attempts left.")
        attempt -= 1
        guess = int(input("Make a guess: "))
        result = check_guess(guess)
        if result == 0:
            print(f"You won. The number was {guess}")
            is_game_on = False
    
    if attempt == 0 and is_game_on == True:
        print("You've run out of guesses.!,You Lose.")
        print(f"The number was {number}. Try Again!")

game()
