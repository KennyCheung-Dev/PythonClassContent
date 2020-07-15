import turtle
import os
import math
import random
import time

#Setup the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invader")

# Register the images
window.register_shape("space_invaders.gif")
window.register_shape("ship.gif")
window.register_shape("bullet.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

# Control Variables
playerSpeed = 15


#Game Sore setup and draw


#Creating the player turtle
player = turtle.Turtle()
player.shape("ship.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)

#Enemies
enemies = []
number_of_enemies = 16

def spawn_enemies():
    for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())
        enemies[i].shape("space_invaders.gif")
        enemies[i].speed(0)
        enemies[i].penup()
    xPos = -100
    yPos = 250
    for i in range(5):
        enemies[i].setposition(xPos, yPos)
        xPos += 50

    xPos = -125
    yPos = 200
    for i in range(5, 11):
        enemies[i].setposition(xPos, yPos)
        xPos += 50

    xPos = -100
    yPos = 150
    for i in range(11, 16):
        enemies[i].setposition(xPos, yPos)
        xPos += 50

spawn_enemies()

print(len(enemies))



#Player Movements - set of callback methods to call when left or right arrow is pressed
def move_left():
    x = player.xcor()
    x -= playerSpeed
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerSpeed
    player.setx(x)

#Functions to make the agme work:
bullets = []
def fire_bullet():
    bullet = turtle.Turtle()
    bullet.shape("bullet.gif")
    bullet.penup()
    bullet.speed(0)
    bullet.setposition(player.xcor(), player.ycor())
    bullets.append(bullet)


bulletSpeed = 20
def update_bullet():
    for eachBullet in bullets:
        currentY = eachBullet.ycor()
        eachBullet.sety(currentY + bulletSpeed)

def isColission(t1, t2, distThreshold):
    pass

def update_enemies():
    pass

def check_collisions():
    pass

def destroy_bullets():
    pass


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


while True:
    update_bullet()
    turtle.update()

# window.mainloop()
