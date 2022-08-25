################### Global Scope ####################

enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


######## Global constants #############

PI = 3.14159
URL = "https://www.google.com"
GITHUB = "https://www.github.com"

# which you donot want to change during the entire program

