from turtle import Turtle

class Paddle(Turtle):

	def __init__(self, xy_cor):
		super().__init__()
		self.x_cor, self.y_cor = xy_cor
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(x=self.x_cor, y=self.y_cor)

	def go_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)