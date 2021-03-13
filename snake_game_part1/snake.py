from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

	def __init__(self):
		self.snake_segments = []
		self.create_snake()
		self.head = self.snake_segments[0]

	def create_snake(self):
		x_pos = 0
		for i in range(3):
			snake_segment = Turtle(shape="square")
			snake_segment.fillcolor("white")
			snake_segment.penup()
			snake_segment.goto(x=x_pos, y=0)
			x_pos -= 20
			self.snake_segments.append(snake_segment)

	def move(self):
		for i in range(len(self.snake_segments) - 1, 0, -1):
			new_x = self.snake_segments[i - 1].xcor()
			new_y = self.snake_segments[i - 1].ycor()
			self.snake_segments[i].goto(new_x, new_y)
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)