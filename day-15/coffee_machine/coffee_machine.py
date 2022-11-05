import machine_data as data

def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made , and false if ingredients are insufficient """
    for item in order_ingredients:
        if order_ingredients[item] >= data.resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins: ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """True if payment is accepted, false if money is insufficient."""
    is_enough = money_received >= drink_cost

    if not is_enough: 
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(money_received - drink_cost, 2) 
    print(f'Here is ${change} in change.')
    data.profit += drink_cost
    return True



def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        data.resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕')

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {data.resources['water']}\nMilk: {data.resources['milk']}\nCoffee: {data.resources['coffee']}\nMoney: ${data.profit}")
    elif choice in data.MENU:
        drink = data.MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print(f'⚠️  {choice} is not a option, try again ⚠️')
