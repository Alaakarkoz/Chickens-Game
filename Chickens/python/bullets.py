from turtle import Turtle
class Bullet(Turtle):
    def __init__(self, shape, size, color, power, speed, distance_for_shot):
        super().__init__(shape)
        self.shapesize(size[0], size[1])
        self.penup()
        self.color(color)
        self.power = power
        self.speed = speed
        self.distance_for_shot = distance_for_shot

BULLETS = [
    {
        "needed_energy" : 20,
        "repeat_shot" : 1,
        "shape" : "square",
        "size" : (1, 0.5),
        "color" : "skyblue",
        "power" : 20,
        "speed" : 20,
        "distance_for_shot" : 10,
    },
    {
        "needed_energy" : 10,
        "repeat_shot" : 2,
        "shape" : "triangle",
        "size" : (0.5, 1.5),
        "color" : "green",
        "power" : 10,
        "speed" : 30,
        "distance_for_shot" : 10,
     },
    {
        "needed_energy" : 25,
        "repeat_shot" : 0.5,
        "shape" : "circle",
        "size" : (2, 2),
        "color" : "orange",
        "power" : 30,
        "speed" : 50,
        "distance_for_shot" : 40,
    },
]