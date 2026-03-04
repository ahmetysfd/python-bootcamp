MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")


    def check_enough_resources(coffee):
        """Checks if there are enough ingredients to make the selected coffee."""
        ingredients = MENU[coffee]["ingredients"]

        for ingredient, amount_needed in ingredients.items():
            if resources[ingredient] < amount_needed:
                print(f"Sorry, there is not enough {ingredient}.")
                return False  # Not enough resources
        return True  # Enough resources


    check_enough_resources(user_choice)


    if user_choice == "espresso":
        print(MENU["espresso"])
        resources["water"] -= 50
        resources["coffee"] -= 18

        user_money = int(input("Please insert money: "))
        if user_money >= 1.5:
            profit += 1.5
            print(f"Here is your change {user_money - 1.5}")
            print("Enjoy Your Coffee!")
        else:
            print("NOT ENOUGH MONEY TRY AGAIN!")

    if user_choice == "cappuccino":
        print(MENU["cappuccino"])
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        user_money2 = int(input("Please insert your money"))
        if user_money2 >= 3:
            profit += 3.0
            print(f"Here is your change {user_money2 - 3}")
            print("Enjoy Your Coffee!")
        else:
            print("NOT ENOUGH MONEY TRY AGAIN!")

    if user_choice == "latte":
        print(MENU["latte"])
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        user_money3 = int(input("Please Insert Your Money"))
        if user_money3 >= 2.5:
            profit += 2.5
            print(f"Here is your change {user_money3 - 2.5}")
            print("Enjoy Your Coffee!")
        else:
            print("NOT ENOUGH MONEY TRY AGAIN!")

    if user_choice == "report":
        print(resources)
        print(f"your profit is {profit}")

    check_enough_resources(user_choice)