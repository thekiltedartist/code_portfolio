from turtle import Turtle
MOVE = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.forward(MOVE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False