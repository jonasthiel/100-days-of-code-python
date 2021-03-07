from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

num_sides = 3
colors = ["red", "blue", "green", "yellow", "purple", "brown", "cyan", "black"]
while num_sides < 11:
	timmy_the_turtle.color(random.choice(colors))
	angle = 360 / num_sides
	for i in range(num_sides):
		timmy_the_turtle.forward(100)
		timmy_the_turtle.right(angle)
	num_sides += 1

screen = Screen()
screen.exitonclick()