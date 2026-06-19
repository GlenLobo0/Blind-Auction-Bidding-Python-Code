import time
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

report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

money_dict = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

def is_resource_sufficient(drink_ingredients):
    """Checks if there are enough ingredients in the report to make the drink."""
    for item in drink_ingredients:
        if drink_ingredients[item] > report[item]:
            print(f"Sorry, there is not enough {item}.") 
            return False
    return True

def process_coins():
    """Prompts user for coins and returns the total value calculated."""
    print("Please insert coins.") 
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    
    total = (quarters * money_dict["quarters"] + 
             dimes * money_dict["dimes"] + 
             nickels * money_dict["nickels"] + 
             pennies * money_dict["pennies"]) 
    return total

def is_transaction_successful(money_received, drink_cost):
    """Determines if the user inserted enough money, handles change, and manages profits."""
    if money_received >= drink_cost: 
        change = round(money_received - drink_cost, 2) 
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        report["money"] += drink_cost 
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    """Deducts the required ingredients from the machine resources and serves the drink."""
    for item in drink_ingredients:
        report[item] -= drink_ingredients[item]

    print("Wait while I prepare your coffee")
# adding a little animation to make it more fun
    for dots in [".", "..", "...", ".....", "......."]:
        print(dots)
        time.sleep(1)
    print(f"Here is your {drink_name}. Enjoy! ☕")

def print_report():
    """Prints the current resources and money in the machine."""
    print(f"Water: {report['water']}ml")
    print(f"Milk: {report['milk']}ml")
    print(f"Coffee: {report['coffee']}g")
    print(f"Money: ${report['money']}")

#NEW ADDITION
def admin_menu():
    """Provides an admin menu for refilling resources and checking the report."""

    password = input(
        "Enter admin password (or type 'exit' to leave admin menu): "
    ).lower().strip()

    if password == "exit":
        return

    if password != "admin123":
        print("Incorrect password.")
        return

    while True:
        admin_input = input(
            "Admin Menu: (refill / report / exit): ").lower().strip()

        if admin_input == "refill":
            report["water"] = 300
            report["milk"] = 200
            report["coffee"] = 100
            print("Resources have been refilled.")

        elif admin_input == "report":
            print_report()

        elif admin_input == "exit":
            print("Leaving admin menu.")
            break

        else:
            print("Invalid selection.")

is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino)( turn off to close the machine , type 'report' for report ): ").lower().strip()

    if user_input == "off":
        print("Turning off the machine. Goodbye!")
        is_on = False

    elif user_input == "report":
        print_report()
    elif user_input == "admin":
        admin_menu()

    elif user_input in MENU:
        drink = MENU[user_input]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()

            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])

    else:
        print("Invalid selection.")
    