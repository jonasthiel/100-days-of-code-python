import random
from os import system
import higher_lower_game_art
import higher_lower_game_data

data = higher_lower_game_data.data

print(higher_lower_game_art.logo)

A = random.randint(0, len(data) - 1)
B = random.randint(0, len(data) - 1)

while A == B:
	B = random.randint(0, len(data) - 1)

score = 0
end_of_game = False
while not end_of_game:
	print(f"Compare A: {data[A]['name']}, {data[A]['description']}, from {data[A]['country']}")

	print(higher_lower_game_art.vs)

	print(f"Against B: {data[B]['name']}, {data[B]['description']}, from {data[B]['country']}")

	guess = input("Who has more followers? Type 'A' or 'B': ")

	if data[A]['follower_count'] > data[B]['follower_count']:
		if guess == "A":
			score += 1
			system('clear')
			print(higher_lower_game_art.logo)
			print(f"You are right! Current score: {score}.")
			A = B
			B = random.randint(0, len(data) - 1)
			while A == B:
				B = random.randint(0, len(data) - 1)
		else:
			print(f"Sorry, that is wrong. Final score: {score}.")
			if input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
				system('clear')
				print(higher_lower_game_art.logo)
				A = random.randint(0, len(data) - 1)
				B = random.randint(0, len(data) - 1)
				while A == B:
					B = random.randint(0, len(data) - 1)
				score = 0
			else:
				end_of_game = True
	elif data[B]['follower_count'] > data[A]['follower_count']:
		if guess == "B":
			score += 1
			system('clear')
			print(higher_lower_game_art.logo)
			print(f"You are right! Current score: {score}.")
			A = B
			B = random.randint(0, len(data) - 1)
			while A == B:
				B = random.randint(0, len(data) - 1)
		else:
			print(f"Sorry, that is wrong. Final score: {score}.")
			if input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
				system('clear')
				print(higher_lower_game_art.logo)
				A = random.randint(0, len(data) - 1)
				B = random.randint(0, len(data) - 1)
				while A == B:
					B = random.randint(0, len(data) - 1)
				score = 0
			else:
				end_of_game = True