n = int(input("Input the maximal range for which all even numbers should be summed up starting at 1: "))

sum = 0
for i in range(1, n + 1):
	if i % 2 == 0:
		sum += i

print(sum)