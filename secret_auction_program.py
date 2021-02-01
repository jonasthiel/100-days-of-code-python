from os import system

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bidders = {}
other_bidders = "yes"
while other_bidders != "no":
	name = input("What is your name? ")
	bid = int(input("What is your bid? $"))
	bidders[name] = bid
	other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
	if other_bidders.lower() == "yes":
		system('clear')

highest_bidder = ""
highest_bid = 0
for key in bidders:
	if bidders[key] > highest_bid:
		highest_bidder = key
		highest_bid = bidders[key]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")