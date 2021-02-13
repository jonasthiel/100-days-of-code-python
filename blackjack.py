import random
from os import system

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
	card = random.choice(cards)
	return card

def calculate_score(cards):
	score = sum(cards)
	if (len(cards) == 2) and (score == 21):
		score = 0
	if (11 in cards) and (score > 21):
		cards.remove(11)
		cards.append(1)
		score = sum(cards)
	return score

def compare(user_score, computer_score):
	if ((user_score > 21) and (computer_score > 21)) or (user_score > 21):
		print("You went over. You lose.")
	elif user_score == computer_score:
		print("It is a draw.")
	elif computer_score == 0:
		print("Computer has blackjack. You lose.")
	elif user_score == 0:
		print("You have blackjack. You win.")
	elif computer_score > 21:
		print("Computer went over. You win.")
	else:
		if user_score > computer_score:
			return print("You have a higher score. You win.")
		else:
			return print("You have a lower score. You lose.")

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
	game = False
	print(logo)
else:
	game = True

while not game:
	user_cards = []
	computer_cards = []

	for i in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())

	user_score = calculate_score(user_cards)
	print(f"   Your cards: {user_cards}, current score: {user_score}")
	computer_score = calculate_score(computer_cards)
	print(f"   Computer's first card: {computer_cards[0]}")

	user_game = False
	computer_game = False

	while not user_game:
		if (user_score == 0) or (user_score > 21):
			user_game = True
			computer_game = True
		else:
			add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
			if add_card == "y":
				user_cards.append(deal_card())
				user_score = calculate_score(user_cards)
				print(f"   Your cards: {user_cards}, current score: {user_score}")
				print(f"   Computer's first card: {computer_cards[0]}")
			elif add_card == "n":
				user_game = True

	while not computer_game:
		if computer_score == 0:
			computer_game = True
		elif computer_score < 17:
			computer_cards.append(deal_card())
			computer_score = calculate_score(computer_cards)
		else:
			computer_game = True

	print(f"   Your final hand: {user_cards}, final score: {user_score}")
	print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
	compare(user_score, computer_score)

	if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
		game = False
		system('clear')
		print(logo)
	else:
		game = True