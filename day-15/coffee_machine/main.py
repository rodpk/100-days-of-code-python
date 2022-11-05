# import machine_data as data

# def show_report():
#     report = f"""
#             Water: {data.resources['water']}ml
#             Milk: {data.resources['milk']}ml
#             Coffee: {data.resources['coffee']}g
#             Money: ${data.resources['money']}
#             """
#     print(report)

# def check_resources(drink):
#     ingredients = drink["ingredients"]

#     ingredients["water"] - data.resources["water"] < 0
#     ingredients["coffee"] - data.resources["coffee"] < 0


# turned_on = True
# options = ["espresso", "latte", "cappuccino", "off", "report"]

# while turned_on:
#     print(data.logo)

#     option = input("What would you like? (espresso/latte/capuccino) - (report/off):\n>> ").lower()

#     if option not in options:
#         print("Invalid option")
    
#     if option == "report":
#         show_report()
#     elif option == "off":
#         break

#     selected_drink = data.MENU[option]
#     check_resources(selected_drink)


# # 1. Print report

# # 2. Check resources sufficient

# # 3. Process coins

# # 4. Check transaction successful

# # 5. Make coffee
