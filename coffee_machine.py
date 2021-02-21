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
    "money": 0
}

def resource_checker(drink):
	for i in MENU[drink]['ingredients'].keys():
		if MENU[drink]['ingredients'][i] > resources[i]:
			print(f"Sorry there is not enough {i}.")
			return False
	return True

def coins():
	total = 0
	coins = {
			'quarters': 0,
			'dimes': 0,
			'nickles': 0,
			'pennies': 0
	}

	print("Please insert coins.")

	for i in coins.keys():
		coins[i] = float(input(f"How many {i}? "))
		if i == 'quarters':
			total += coins[i] * 0.25
		elif i == 'dimes':
			total += coins[i] * 0.1
		elif i == 'nickles':
			total += coins[i] * 0.05
		elif i == 'pennies':
			total += coins[i] * 0.01

	return total

def transaction(drink, total_coins):
	if MENU[drink]['cost'] > total_coins:
		print("Sorry that is not enough money. Money refunded.")
	elif MENU[drink]['cost'] <= total_coins:
		resources['money'] += MENU[drink]['cost']
		if MENU[drink]['cost'] < total_coins:
			change = round(total_coins - MENU[drink]['cost'], 2)
			print(f"Here is ${change} in change.")
		for i in MENU[drink]['ingredients'].keys():
			resources[i] -= MENU[drink]['ingredients'][i]
		print(f"Here is your {user_input}. Enjoy!")

off = False

while not off:
	user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

	if user_input == "off":
		off = True
	elif user_input == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: ${resources['money']}")
	else:
		if resource_checker(user_input) == True:
			total_coins = round(coins(), 2)
			transaction(user_input, total_coins)