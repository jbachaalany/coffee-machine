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

coins = {
    "penny": 0.01,
    "dime": 0.1,
    "nickle": 0.05,
    "quarter": 0.25
}

money = 0
is_on = True


def check_available_resources(drink):
    if MENU[drink]['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water")
        return False
    elif MENU[drink]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    elif 'milk' in MENU[drink]['ingredients'] and MENU[drink]['ingredients']['milk'] > resources['milk']:
        print("Sorry there is not enough milk")
        return False
    return True


def validate_amount(drink):
    print("Please insert coins.")
    drink_price = MENU[drink]['cost']
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    amount = (quarters * coins['quarter']) + (dimes * coins['dime']) + \
             (nickles * coins['nickle']) + (pennies * coins['penny'])
    if amount > drink_price:
        print(f"Here is ${round((amount - drink_price),2)} in change.")
        print("Here is your latte ☕. Enjoy!")
        return drink_price
    elif amount < drink_price:
        print("Sorry that's not enough money. Money refunded")
        return 0
    else:
        print("Here is your latte ☕. Enjoy!")
        return drink_price


while is_on:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "off":
        is_on = False
    elif option == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif option in MENU:
        if check_available_resources(option):
            amount_entered = validate_amount(option)
            if amount_entered > 0:
                resources['water'] -= MENU[option]['ingredients']['water']
                resources['coffee'] -= MENU[option]['ingredients']['coffee']
                if 'milk' in MENU[option]['ingredients']:
                    resources['milk'] -= MENU[option]['ingredients']['milk']
                    money += amount_entered
    else:
        print("Item does not exist, please try again")
        