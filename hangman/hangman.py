import random
import hangman_art
import hangman_words
from os import system

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

display = []
for i in range(len(chosen_word)):
	display.append("_")

end_of_game = False
lives = 6
while not end_of_game:
	guess = input("Guess a letter: ").lower()

	system('clear')

	if guess in display:
		print(f"You have already guessed {guess}.")

	for i in range(len(chosen_word)):
		if chosen_word[i] == guess:
			display[i] = chosen_word[i]
	print(f"{' '.join(display)}")

	if "_" not in display:
		end_of_game = True
		print("You win.")

	if guess not in chosen_word:
		print(f"You guessed {guess}, that is not in the word. You lose a life.")
		lives -= 1

	if lives == 0:
		end_of_game = True
		print("You lose.")
		print(f"The secret word was {chosen_word}.")

	print(hangman_art.stages[lives])