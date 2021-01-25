import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def rock_paper_scissors(choice):
	if choice < 0 or choice > 2:
		return("You typed an invalid number, you lose!")
	elif choice == 0:
		return(rock)
	elif choice == 1:
		return(paper)
	elif choice == 2:
		return(scissors)

def referee(user_choice, computer_choice):
	if user_choice == computer_choice:
		return("It is a draw")
	elif user_choice == 0 and computer_choice == 1:
		return("You lose")
	elif user_choice == 1 and computer_choice == 0:
		return("You win!")
	elif user_choice == 2 and computer_choice == 0:
		return("You lose")
	elif user_choice == 0 and computer_choice == 2:
		return("You win!")
	elif user_choice == 1 and computer_choice == 2:
		return("You lose")
	elif user_choice == 2 and computer_choice == 1:
		return("You win!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(rock_paper_scissors(user_choice))

if user_choice >= 0 and user_choice <= 2:
	computer_choice = random.randint(0,2)
	print("Computer chose:")
	print(rock_paper_scissors(computer_choice))

	print(referee(user_choice, computer_choice))