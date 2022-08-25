from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

to_continue = True
menu = Menu()
resources = CoffeeMaker()
payment = MoneyMachine()

while to_continue:
    options = menu.get_items()
    choice = input(f"What would you like?: {options}: ").lower()
    if choice == "off":
        to_continue = False
    elif choice == "report":
        resources.report()
        payment.report()
    else:
        drink = menu.find_drink(choice)
        if resources.is_resource_sufficient(drink):
            if payment.make_payment(drink.cost):
                resources.make_coffee(drink)
