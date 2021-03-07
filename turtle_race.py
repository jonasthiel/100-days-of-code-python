from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = -125
for i in range(5):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colors[i])
	new_turtle.penup()
	new_turtle.goto(x=-230, y=y_pos)
	y_pos += 50
	all_turtles.append(new_turtle)

if user_bet:
	is_race_on = True

while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() > 230:
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You have won! The {winning_color} turtle is the winner!")
			else:
				print(f"You have lost! The {winning_color} turtle is the winner!")
			is_race_on = False

		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)

screen.exitonclick()