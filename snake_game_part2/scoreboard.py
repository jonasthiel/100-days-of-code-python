from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(0, 270)
		self.score_counter = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(f"Score: {self.score_counter}", align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align=ALIGNMENT, font=FONT)

	def counter(self):
		self.score_counter += 1
		self.clear()
		self.update_scoreboard()