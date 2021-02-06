logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

print(logo)

def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

def calculator():
	num1 = float(input("What is the first number? "))

	for key in operations:
		print(key)

	operation = input("Pick an operation from the line above: ")

	num2 = float(input("What is the second number? "))

	def calculation(num1, num2, operation):
		calculation_function = operations[operation]
		answer = calculation_function(num1, num2)
		return answer

	answer = calculation(num1, num2, operation)

	print(f"{num1} {operation} {num2} = {answer}")

	continue_flag = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'e' to exit: ")

	if continue_flag == "n":
		calculator()

	while continue_flag == "y":
		operation = input("Pick an operation: ")
		num1 = answer
		num2 = float(input("What is the next number? "))
		answer = calculation(num1, num2, operation)
		print(f"{num1} {operation} {num2} = {answer}")
		continue_flag = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'e' to exit: ")
		if continue_flag == "n":
			calculator()

calculator()