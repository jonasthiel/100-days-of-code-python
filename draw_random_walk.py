from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(10)
timmy_the_turtle.pensize(15)

directions = [0, 90, 180, 270]
for i in range(200):
	R = random.random()
	G = random.random()
	B = random.random()
	timmy_the_turtle.pencolor(R, G, B)
	timmy_the_turtle.setheading(random.choice(directions))
	timmy_the_turtle.forward(30)

screen = Screen()
screen.exitonclick()