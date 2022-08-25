import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice < 0 or user_choice >= 3: 
    print("You lose... Invalid Number....")
else:
    computer_choice = random.randint(0,len(options)-1)

    print("User Choice: ")
    print(options[user_choice])

    print("Computer Choice: ")
    print(options[computer_choice])

    if user_choice == computer_choice:
        print("It is a tie.....")
    elif user_choice == 0 and computer_choice == 2:
        print("User Wins.....")
    elif user_choice == 1 and computer_choice == 0:
        print("User Wins.....")
    elif user_choice == 2 and computer_choice == 1:
        print("User Wins.....")
    else:
        print("Computer Wins....")
