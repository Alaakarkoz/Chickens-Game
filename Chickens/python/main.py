# import everything that we need
from turtle import Screen
from vehicle import Vehicle
from board import   Board
from enemies import *
import random
import time
import winsound

# set the screen
screen = Screen()
screen.setup(900, 900)
screen.title("CHICKENS GAME")
screen.bgpic("E:\Python\level2\Chickens\imgs\\background.png")
screen.tracer(0)


# make object of the imported classes
vehicle = Vehicle()
board = Board()

# let the user move the vehicle and fire
screen.listen()
screen.onkey(vehicle.move_right, "Right")
screen.onkey(vehicle.move_left, "Left")
screen.onclick(vehicle.shot)

enemies = []
prizes = []
game_on = True
while board.livings and game_on:
    if len(enemies) == 0:
        for y in range(450, 750, 100):
            random_enemy = random.randint(1,4)
            for x in range(-400, 500, 100):
                if random_enemy == 1:
                    enemies.append(Spider((x, y)))

                elif random_enemy == 2:
                    enemies.append(Octupos((x, y)))
                
                elif random_enemy == 3:
                    enemies.append(Ship((x, y)))

                else:
                    enemies.append(Star((x, y)))

    for enemy in enemies:
        if random.randint(1,enemy.shot_percent) == 1 and enemy.main_part.isvisible():
            enemy.shot()
        
        if enemy.main_part.ycor() > enemy.position[1]-350:
            enemy.main_part.goto(enemy.main_part.xcor(), enemy.main_part.ycor() - enemy.speed)
            for part in enemy.parts:
                position = enemy.positions[enemy.parts.index(part)]
                x_value = enemy.main_part.xcor()+position[0]
                y_value = enemy.main_part.ycor()+position[1]
                part.goto(x_value,y_value)
        
        for bullet in enemy.bullets:
            if bullet.ycor() > -450:
                bullet.forward(enemy.speed_bullet)
                if bullet.distance(vehicle.main_part) < 40:
                    winsound.PlaySound("E:\Python\level2\Chickens\\aud\explosion.wav", winsound.SND_ASYNC)
                    vehicle.main_part.goto(0, -700)
                    vehicle.move_parts()
                    vehicle.shot_speed = 4
                    vehicle.energy = 100
                    bullet.goto(0, -450)
                    board.livings -= 1
            
            else:
                enemy.bullets.remove(bullet)

    # move the bullets
    for bullet in vehicle.bullets:
        if bullet.ycor() < 500:
            bullet.goto(bullet.xcor(), bullet.ycor()+bullet.speed)
            for enemy in enemies:
                if (bullet.distance(enemy.main_part) < bullet.distance_for_shot + 10 * (enemy.main_part.shapesize()[0] + enemy.main_part.shapesize()[1]) 
                   and enemy.main_part.isvisible() 
                   and bullet.ycor() < 450):
                    winsound.PlaySound("E:\Python\level2\Chickens\\aud\shot.wav", winsound.SND_ASYNC)
                    enemy.livings -= bullet.power
                    if enemy.livings <= 0:
                        enemy.die(prizes)
                        board.killed_enemies += 1
                    bullet.goto(0, 500)

    if vehicle.energy < 100:
        vehicle.energy += 2
        turtle = vehicle.energy_turtles[::-1][vehicle.energy // 10 - 1]
        turtle.color("white")

    for enemy in enemies:
        if len(enemy.bullets) == 0 and not enemy.main_part.isvisible():
            enemies.remove(enemy)
    
    vehicle.reapeat_shot()
    
    if vehicle.main_part.ycor() != -300:
        vehicle.main_part.goto(vehicle.main_part.xcor(), vehicle.main_part.ycor() + 40)
        vehicle.move_parts()
    
    for prize in prizes:
        if prize.ycor() > -450:
            prize.goto(prize.xcor(), prize.ycor() - 20)
            if vehicle.main_part.distance(prize) < 60:
                if prize.color()[0]  == "skyblue" and prize.shape() == "square":
                    vehicle.used_bullet = 1
                elif prize.color()[0]  == "green" and prize.shape() == "triangle":
                    vehicle.used_bullet = 2
                elif prize.color()[0]  == "orange" and prize.shape() == "circle":
                    vehicle.used_bullet = 3
                vehicle.shot_speed = 4
                vehicle.energy = 100
                for turtle in vehicle.energy_turtles:
                    turtle.color("white")
                prize.hideturtle()
    
    time.sleep(0.1)
    screen.update()
    board.show_results()
screen.exitonclick()
