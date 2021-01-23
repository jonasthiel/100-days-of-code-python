print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percentage_tip = 1 + float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
number_people = int(input("How many people to split the bill? "))
bill_per_person = total_bill / number_people * percentage_tip

print("Each person should pay: ${:.2f}".format(bill_per_person))