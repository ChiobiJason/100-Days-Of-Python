from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
menu_item = MenuItem
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffees = coffee_menu.get_items()
coffee_lst = coffees.split("/")
COFFEE_MACHINE_ON = True

while COFFEE_MACHINE_ON:
    user_coffee = input(f"What would you like? ({coffees}): ").lower()

    for i in range(3):
        if user_coffee == coffee_lst[i]:
            drink = coffee_menu.find_drink(user_coffee)
            user_coffee_name = drink.name
            menu_item.name = user_coffee_name
            user_coffee_cost = drink.cost
            menu_item.cost = user_coffee_cost
            menu_item.ingredients = drink.ingredients
            user_coffee_water = drink.ingredients["water"]
            user_coffee_milk = drink.ingredients["milk"]
            user_coffee_coffee = drink.ingredients["coffee"]
            enough_resources = coffee_maker.is_resource_sufficient(menu_item)

            if enough_resources == True:
                if money_machine.make_payment(user_coffee_cost) == True:
                    coffee_maker.make_coffee(menu_item)

    if user_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_coffee == "off":
        COFFEE_MACHINE_ON = False
