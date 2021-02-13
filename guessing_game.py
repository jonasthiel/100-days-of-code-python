import random
from os import system

logo = """
 _____                     _               _____
|  __ \                   (_)             |  __ \
| |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___
| | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                    __/ |
                                   |___/
"""

if input("Do you want to play the Guessing Game? Type 'y' or 'n': ").lower() == "y":
	game = False
	print(logo)
else:
	game = True

while not game:
	print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty == "easy":
		attempts = 10
	elif difficulty == "hard":
		attempts = 5

	random_number = random.randint(1,100)

	while attempts > 0:
		guess = int(input("Make a guess: "))
		if guess > random_number:
			attempts -= 1
			if attempts > 0:
				print(f"Too high.\nYou have {attempts} attempts remaining to guess the number.")
			else:
				print("You have run out of guesses, you lose.")
		elif guess < random_number:
			attempts -= 1
			if attempts > 0:
				print(f"Too low.\nYou have {attempts} attempts remaining to guess the number.")
			else:
				print("You have run out of guesses, you lose.")
		elif guess == random_number:
			attempts = 0
			print(f"You got it! The answer was {random_number}.")

	if input("Do you want to play the Guessing Game? Type 'y' or 'n': ").lower() == "y":
		game = False
		system('clear')
		print(logo)
	else:
		game = True