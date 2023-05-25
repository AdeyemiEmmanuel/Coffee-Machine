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


def get_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters? ")) * 0.25
    dimes = int(input("how many dimes? ")) * 0.10
    nickels = int(input("how many nickles? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def check_ingredients(coffee):
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def process_money(coffee, money):
    if MENU[coffee]["cost"] > money:
        print("Sorry that's not enough money. Money refunded")
        return False
    return True


def use_ingredients(coffee):
    resources["water"] = resources["water"] - MENU[coffee]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]


def give_change(money, coffee):
    change = round((money - MENU[coffee]["cost"]), 2)
    print(f"Here is ${change} in change.")


def make_coffee():
    prompt = input("What would you like? ")
    money_made = 0
    while prompt != 'off':
        if prompt != 'report':
            ingredients = check_ingredients(prompt)
            if ingredients:
                user_money = get_money()
                if process_money(prompt, user_money):
                    use_ingredients(prompt)
                    money_made += MENU[prompt]["cost"]
                    give_change(user_money, prompt)
                    print(f"Here is your {prompt}☕. Enjoy!")
        else:
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money_made}")
        prompt = input("What would you like? ")


make_coffee()
