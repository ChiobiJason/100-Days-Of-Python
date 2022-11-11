from coffee_data import MENU, resources, coins

COFFEE_MACHINE_ON = True
MONEY = 0
WATER_REMAINING = resources["water"]
MILK_REMAINING = resources["milk"]
COFFEE_REMAINING = resources["coffee"]


def calculate_user_money(quarters, dimes, nickels, pennies):
    total_quarters = quarters * coins["quarter"]
    total_dimes = dimes * coins["dime"]
    total_nickels = nickels * coins["nickel"]
    total_pennies = pennies * coins["penny"]
    total_money = total_quarters + total_dimes + total_nickels + total_pennies
    return total_money


def check_resources(coffee):
    global WATER_REMAINING, MILK_REMAINING, COFFEE_REMAINING
    amount_of_water = MENU[coffee]["ingredients"]["water"]
    amount_of_coffee = MENU[coffee]["ingredients"]["coffee"]
    amount_of_milk = MENU[coffee]["ingredients"]["milk"]
    if (
        amount_of_water <= WATER_REMAINING
        and amount_of_coffee <= COFFEE_REMAINING
        and amount_of_milk <= MILK_REMAINING
    ):
        return True
    elif amount_of_water > WATER_REMAINING:
        print("Sorry there is not enough water")
        return False
    elif amount_of_coffee > COFFEE_REMAINING:
        print("Sorry there is not enough coffee")
        return False
    elif amount_of_milk > MILK_REMAINING:
        print("Sorry there is not enough milk")
        return False
    else:
        return False


def make_coffee(coffee):
    global MONEY, WATER_REMAINING, MILK_REMAINING, COFFEE_REMAINING
    amount_of_water = MENU[coffee]["ingredients"]["water"]
    amount_of_coffee = MENU[coffee]["ingredients"]["coffee"]
    amount_of_milk = MENU[coffee]["ingredients"]["milk"]
    total_cost = MENU[coffee]["cost"]
    user_money = calculate_user_money(
        user_quarters, user_dimes, user_nickels, user_pennies
    )
    if check_resources(coffee) == True and user_money >= total_cost:
        MONEY += total_cost
        WATER_REMAINING -= amount_of_water
        MILK_REMAINING -= amount_of_milk
        COFFEE_REMAINING -= amount_of_coffee
        user_change = user_money - total_cost
        if user_change > 0:
            print(f"Here is ${user_change} in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
    elif user_money < total_cost:
        print("Sorry that's not enough money. Money refunded.")


def maintainance(keyword):
    global COFFEE_MACHINE_ON
    if keyword == "report":
        print(f"Water: {WATER_REMAINING}ml")
        print(f"Milk: {MILK_REMAINING}ml")
        print(f"Coffee: {COFFEE_REMAINING}g")
        print(f"Money: ${MONEY}")
    elif keyword == "off":
        COFFEE_MACHINE_ON = False


while COFFEE_MACHINE_ON:
    user_coffee = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if (
        user_coffee == "espresso"
        or user_coffee == "latte"
        or user_coffee == "cappuccino"
    ):
        if check_resources(user_coffee) == True:
            print("Please insert coins.")
            user_quarters = eval(input("how many quarters?: "))
            user_dimes = eval(input("how many dimes?: "))
            user_nickels = eval(input("how many nickles?: "))
            user_pennies = eval(input("how many pennies?: "))
            make_coffee(user_coffee)
    elif user_coffee == "report" or user_coffee == "off":
        maintainance(user_coffee)
