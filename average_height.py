student_heights = input("Input a list of student heights in cm: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

counter = 0
total_height = 0
for height in student_heights:
	counter += 1
	total_height += height

print(round(total_height / counter))