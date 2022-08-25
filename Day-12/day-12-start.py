################### Scope ####################

from re import L


enemies = 1

def increase_enemies():

  enemies = 2
  print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


######## Local Scope #########

# def drink_potion():

#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# potion_strength This var is not defined outside of the function


######### Global Scope #########

player_health = 10

def change_health():

    player_health = 20
    print(player_health)

change_health()
print(player_health)


# No black scope available in python 

