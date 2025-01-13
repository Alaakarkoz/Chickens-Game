from turtle import Turtle
class Board(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.score = 0
        self.killed_enemies = 0
        self.livings = 5
        self.show_results()

    def show_results(self):
        self.clear()
        self.goto(0, -400)
        self.write(f"Score : {self.score}\nKilled enemy : {self.killed_enemies}", align="center", font=("arial", 16, "normal"))
        self.goto(-400, -400)
        self.write(f"Livings : {self.livings}", align="center", font=("arial", 16, "normal"))