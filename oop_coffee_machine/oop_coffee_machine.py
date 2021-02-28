from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

off = False

while not off:
	user_input = input(f"What would you like? ({menu.get_items()}): ").lower()

	if user_input == "off":
		off = True
	elif user_input == "report":
		coffee_machine.report()
		money_machine.report()
	else:
		drink = menu.find_drink(user_input)
		if coffee_machine.is_resource_sufficient(drink) == True:
			if money_machine.make_payment(drink.cost) == True:
				coffee_machine.make_coffee(drink)