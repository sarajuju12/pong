from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(coordinates)

    def upward(self):
        if self.ycor() < 300:
            self.goto(self.xcor(), self.ycor() + 20)

    def downward(self):
        if self.ycor() > -300:
            self.goto(self.xcor(), self.ycor() - 20)
