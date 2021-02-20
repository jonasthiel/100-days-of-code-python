def prime_checker(number):
	counter = 0
	for i in range(1, number + 1):
		if number % i == 0:
			counter += 1
	if counter == 2:
		print("It is a prime number.")
	else:
		print("It is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)