MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """Returns true if ingredients are sufficient else false"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    """Returns the total amount by processing the coins inserted"""
    print("Please insert the coins:")
    total = 0
    total += int(input("How many pennies? :")) * 0.01
    total += int(input("How many nickels? :")) * 0.05
    total += int(input("How many dimes? :")) * 0.1
    total += int(input("How many quarters? :")) * 0.25

    return total


def is_transaction_successful(money_recieved, cost):
    """Returns true if money_received is enough to make the order"""
    if money_recieved < cost:
        print(f"Total money inserted: {money_recieved:.2f}.")
        print(f"Money required to make the order: {cost}")
        print(f"Sorry that's not enough money. Money refunded.")
        return False

    else:
        change = round(money_recieved - cost, 2)
        print(f"Here is your change: {change:.2f}")
        global profit
        profit += cost
        return True

def make_coffee(drink_name, ingredients):

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


    print(f"Here is your {drink_name}☕. Enjoy!")


profit = 0


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")

    elif choice not in MENU:
        print("Invalid choice.")

    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
