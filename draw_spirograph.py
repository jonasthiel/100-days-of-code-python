from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(10)

current_heading = 0
while current_heading < 360:
	R = random.random()
	G = random.random()
	B = random.random()
	timmy_the_turtle.pencolor(R, G, B)
	timmy_the_turtle.circle(100)
	current_heading = timmy_the_turtle.heading() + 10
	timmy_the_turtle.setheading(current_heading)

screen = Screen()
screen.exitonclick()