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


def consume_resources(needed_resources):
    print(f"Consuming resources {needed_resources}")
    for key in needed_resources:
        resources[key] -= needed_resources[key]
    print(f"Remaining resources {resources}")
  

#Penny: 0.01 | Nickel: 0.05 | Dime: 0.10 | Quarter 0.25
def process_money(drink_cost,needed_resource):
    print(f"Drink costs {drink_cost}")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    sum = quarters + dimes + nickles + pennies

    if sum < drink_cost:
        print(f"Sorry not enough money. Money Refunded ${sum}")
        return
    elif sum > drink_cost:
        change = round(sum - drink_cost, 2)
        resources["money"] += drink_cost
        print(f"Here is ${change} in change")
    
    consume_resources(needed_resource)
    

def check_resources(choosen_drink):
    needed_resource = MENU[choosen_drink]["ingredients"]
    print(needed_resource)
    for key in needed_resource:
        if needed_resource[key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return
    # print(f"Enjoy your {choosen_drink}")
    # Process Money Entered
    needed_payment = MENU[choosen_drink]["cost"]
    process_money(needed_payment,needed_resource)
    print(f"Enjoy your {choosen_drink.title()}")


def refill_resources():
    milk = int(input("How much milk will you add in ml"))
    water = int(input("How much water will you add in ml"))
    coffee = int(input("How much coffee will you add in g"))
    refill = {
        'water': water,
        'milk': milk,
        'coffee': coffee,
    }
    for key in refill:
        resources[key] += refill[key]

    print(f"Reousrces are now: {resources}")

def main():
    machineState = True
    while machineState:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink == 'report':
            report_resources()
        elif drink == 'off':
            print("Turning off the Machine")
            machineState = False
        else:
            check_resources(drink)
    
main()
