print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lowerCase = name1.lower()
name2_lowerCase = name2.lower()

trueScore = 0
loveScore = 0

trueScore += name1_lowerCase.count("t") + name2_lowerCase.count("t")
trueScore += name1_lowerCase.count("r") + name2_lowerCase.count("r")
trueScore += name1_lowerCase.count("u") + name2_lowerCase.count("u")
trueScore += name1_lowerCase.count("e") + name2_lowerCase.count("e")
loveScore += name1_lowerCase.count("l") + name2_lowerCase.count("l")
loveScore += name1_lowerCase.count("o") + name2_lowerCase.count("o")
loveScore += name1_lowerCase.count("v") + name2_lowerCase.count("v")
loveScore += name1_lowerCase.count("e") + name2_lowerCase.count("e")

totalScore = int(str(trueScore) + str(loveScore))

if totalScore < 10 or totalScore > 90:
	print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore > 40 and totalScore < 50:
	print(f"Your score is {totalScore}, you are alright together.")
else:
	print(f"Your score is {totalScore}.")