from requirements import MENU as menu, resources

# TODO-1: Print report

money = 0.0

# TODO-2: Check resources sufficient


def is_resources_sufficient(choice):
    """This will check for the availability of resources"""
    target = menu[choice]['ingredients']
    if resources['water'] >= target['water']:
        if resources['coffee'] >= target['coffee']:
            if choice != "espresso":
                if resources['milk'] >= target['milk']:
                    make_coffee(choice)
                else:
                    print("Insufficient coffee.")
            else:
                make_coffee(choice)
        else:
            print("Insufficient milk.")
    else:
        print("Insufficient water.")

# TODO-3: Insert coins and Make your coffee


def make_coffee(choice):
    """Making coffee.........."""
    print("Please insert coins.....")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))

    total_amount = quarter*0.25 + dime*0.10 + nickle*0.05 + penny*0.01
    coffee_price = menu[choice]["cost"]
    if total_amount >= coffee_price:
        global money
        money += coffee_price
        if coffee_price != total_amount:
            to_return = round(total_amount - coffee_price, 2)
            print(f"Here's your ${to_return} in change!")
        print(f"Enjoy your ☕, {choice}!")
        reduce_resources(choice)
    else:
        print("Money refunded, Not enough coins.....")
        make_coffee(choice)


def reduce_resources(choice):
    """Reduce the resources after the coffee is made"""
    target = menu[choice]['ingredients']
    resources['water'] -= target['water']
    resources['coffee'] -= target['coffee']
    if choice != "espresso":
        resources['milk'] -= target['milk']


def game():
    is_on = True
    while is_on:
        user_choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
        if user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif user_choice == "off":
            is_on = False
        else:
            is_resources_sufficient(user_choice)


game()
