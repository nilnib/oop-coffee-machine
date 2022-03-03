#importing modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#initialize machine status
status = True
# creating objects
item = Menu()
coffee_make = CoffeeMaker()
money = MoneyMachine()

while status:
    user_choice = input(f"What would you like? {item.get_items()}:").lower().strip()

    if user_choice == "off":
        status = False
    elif user_choice == "report":
        coffee_make.report()
    elif (coffee_make.is_resource_sufficient(item.find_drink(user_choice))):
        #Check that suufficient money is inserted or not

        if money.make_payment(item.find_drink(user_choice).cost):
            coffee_make.make_coffee(item.find_drink(user_choice))
            coffee_make.report()
            money.report()








