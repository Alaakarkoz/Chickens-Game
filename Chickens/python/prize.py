from turtle import Turtle
class Prize(Turtle):
    def __init__(self, shape, color, position):
        super().__init__(shape)
        self.color(color)
        self.shapesize(0.5, 0.5)
        self.penup()
        self.goto(position)