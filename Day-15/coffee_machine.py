from requirements import MENU as menu,resources

is_on = True

profit = 0


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Not enough {item}")
            return False
    return True


def process_coins():
    print("Insert coins.....")
    total = int(input("How many quarters?: "))
    total += int(input("How many dimes?: "))
    total += int(input("How many nickles?: "))
    total += int(input("How many pennies?: "))
    return total


def is_transaction_successful(money_received, drink_cost):
    """returns true when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your #{change} in change")
        global profit
        profit += drink_cost
        return True
    print("Sorry that's not enough money. Money refunded..")
    return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(drink, drink['ingredients'])

