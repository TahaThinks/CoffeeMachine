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
    "milk": 50,
    "coffee": 100,
    "money": 0,
}

def report_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

#Penny: 0.01 | Nickel: 0.05 | Dime: 0.10 | Quarter 0.25
def process_money(cost,drink):
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    sum = quarters + dimes + nickles + pennies
    if sum < cost:
        print("Not Enough Money")
    elif sum > cost:
        change = sum - cost
        print(f"Here is ${change} in change")
        #consume_resources(drink)

def check_resources(choosen_drink):
    needed_resource = MENU[choosen_drink]["ingredients"]
    print(needed_resource)
    for key in needed_resource:
        if needed_resource[key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return
    print(f"Enjoy your {choosen_drink}")



drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

if drink == 'report':
    report_resources()
else:
    check_resources(drink)