from turtle import Turtle
from bullets import *
class Vehicle:
    def __init__(self):
        self.main_part = Turtle("square")
        self.main_part.color("yellow")
        self.main_part.penup()
        self.main_part.shapesize(2.5,2.5)
        self.main_part.goto(0, -300)
        self.parts = [Turtle("square") for _ in range(4)]
        self.positions = [(0, 40), (-30, -20), (30, -20), (0, 0)]
        self.bullets = []
        self.set_parts()
        self.energy = 100
        self.energy_turtles = []
        self.shot_speed = 4
        self.available_shot =  True
        self.livings = 5
        self.used_bullet = 1
        self.set_energy_turtles()
    
    def set_parts(self):
        for part in self.parts:
            position = self.positions[self.parts.index(part)]
            part.penup()
            part.color("white")
            part.shapesize(1.5,0.5)
            x_value = self.main_part.xcor()+position[0]
            y_value = self.main_part.ycor()+position[1]
            part.goto(x_value,y_value)
        self.parts[-1].color("blue")
    
    def set_energy_turtles(self):
        for i in range(10):
            turtle = Turtle('square')
            turtle.color("white")
            turtle.shapesize(1.5, 0.5)
            turtle.penup()
            turtle.goto(430 - i * 30, -400)
            self.energy_turtles.append(turtle)

    def move_parts(self):
            for part in self.parts:
                position = self.positions[self.parts.index(part)]
                part.goto(self.main_part.xcor()+position[0],self.main_part.ycor()+position[1])

    def move_right(self):
        if self.main_part.xcor() < 400:
            self.main_part.goto(self.main_part.xcor()+30,self.main_part.ycor())
            self.move_parts()
    
    def move_left(self):
        if self.main_part.xcor() > -400:
            self.main_part.goto(self.main_part.xcor()-30,self.main_part.ycor())
            self.move_parts()
    
    def shot(self, i, j):
        if self.energy == 100:
            self.available_shot = True
            self.parts[0].color("white")
        
        needed_energy = BULLETS[self.used_bullet - 1]["needed_energy"]
        if self.energy >= needed_energy and self.shot_speed >= 4 and self.available_shot:
            bullet_properties = BULLETS[self.used_bullet - 1]
            bullet = Bullet(bullet_properties["shape"], bullet_properties["size"], bullet_properties["color"], bullet_properties["power"], bullet_properties["speed"], bullet_properties["distance_for_shot"])
            bullet.goto(self.parts[0].position())
            self.bullets.append(bullet)

            self.energy -= needed_energy
            for _ in range(needed_energy // 10):
                for turtle in self.energy_turtles:
                    if turtle.pencolor() == "white":
                        turtle.color("red")
                        break
            self.shot_speed = 0
    
            if self.energy < needed_energy:
                self.available_shot = False
                self.parts[0].color("orange")
        
        if self.energy < needed_energy:
            self.available_shot = False
            self.parts[0].color("orange")
    
    def reapeat_shot(self):
        if self.shot_speed < 4:
            self.shot_speed += BULLETS[self.used_bullet - 1]["repeat_shot"]