from turtle import Turtle, register_shape
from prize import Prize
import random

class Enemy:
    def __init__(self, position, size, positions, color, shape, speed, speed_bullet, shot_percent, livings):
        self.position = position
        self.positions = positions
        self.main_part = Turtle(shape)
        self.main_part.color(color)
        self.main_part.penup()
        self.main_part.goto(position)
        self.main_part.shapesize(size[0], size[1])
        self.parts = [Turtle("square") for _ in range(len(positions))]
        self.bullets = []
        self.speed = speed
        self.speed_bullet = speed_bullet
        self.shot_percent = shot_percent
        self.livings = livings
    
    def set_parts(self, color, sizes):
        for part in self.parts:
            position = self.positions[self.parts.index(part)]
            part.penup()
            part.color(color)
            part.shapesize(sizes[self.parts.index(part)][0], sizes[self.parts.index(part)][1])
            x_value = self.main_part.xcor()+position[0]
            y_value = self.main_part.ycor()+position[1]
            part.goto(x_value,y_value)
    
    def shot(self, bullet_shape, bullet_color, bullet_size1, bullet_size2 , angle):
        bullet = Turtle(bullet_shape)
        bullet.color(bullet_color)
        bullet.shapesize(bullet_size1, bullet_size2)
        bullet.penup()
        bullet.goto(x for x in self.main_part.position())
        bullet.right(angle)
        self.bullets.append(bullet)
    
    def die(self, prizes):
        self.main_part.hideturtle()
        for part in self.parts:
            part.hideturtle()
        
        random_number = random.randint(1, 5)
        if random_number == 1:
            prize = Prize("square", "skyblue", self.main_part.position())

        elif random_number == 2:
            prize = Prize("triangle", "green", self.main_part.position())
        
        elif random_number == 3:
            prize = Prize("circle", "orange", self.main_part.position())
        
        try:
            prizes.append(prize)
        
        except NameError:
            return None


class Spider(Enemy):
    def __init__(self, position):
        super().__init__(position, (1.25, 1.25), [(17.5, 17.5), (-17.5, 17.5), (17.5, -17.5), (-17.5, -17.5)], "green", "square", 5, 10, 150, 40)
        self.set_parts("green", [(0.5, 0.5) for _ in range(4)])
    
    def shot(self):
        return super().shot("circle", "red", 1, 0.5, 90)

class Octupos(Enemy):
    def __init__(self, position):
        super().__init__(position, (2, 2), [(7.5, -17.5), (-7.5, -17.5), (17.5, -10.5), (-17.5, -10.5), (9, 0), (-5, 0)], "red", "circle", 3, 15, 250, 50)
        self.set_parts("red", [(1.5, 0.1) for _ in range(4)] + [(0.2, 0.4), (0.2, 0.4)])
        self.parts[-1].color("blue")
        self.parts[-2].color("blue")
    
    def shot(self):
        register_shape("shape1", ((-10, -17), (-7, 5), (-4, 5), (0, 12), (4, 5), (7, 5), (10, -17)))
        super().shot("shape1", "white", 1.5, 0.75, 90)

class Ship(Enemy):
    def __init__(self, position):
        super().__init__(position, (1, 3.25), [(x, 0) for x in [-30, -10, 10, 30]], "white", "square", 5, 10, 250, 50)
        self.set_parts("blue", [(0.2,0.3) for _ in range(4)])
    
    def shot(self):
        register_shape("shape2", ((-5, -20), (-10, -7.5), (0, 7.5), (-5, 20), (5, 20), (10, 7.5), (0, -7.5), (5, -20)))
        super().shot("shape2", "yellow", 1.25, 1, random.randint(45, 135))

class Star(Enemy):
    def __init__(self, position):
        super().__init__(position , (1.5, 1.5), [(0, 20), (20, 20), (-20, 20), (-20, -20), (20, -20)], "orange", "square", 5, 10, 250, 70)
        self.set_parts("orange", [(1.5,0.75) for _ in range(5)])
        self.parts[1].right(45)
        self.parts[3].right(45)
        self.parts[2].left(45)
        self.parts[4].left(45)
    
    def shot(self):
        super().shot("classic", "purple", 1, 1, 90)