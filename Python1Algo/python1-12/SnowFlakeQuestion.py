import turtle
import random

turtle.Screen().bgcolor('blue')

elsa = turtle.Turtle()
elsa.color("cyan")
elsa.shape("turtle")
elsa.speed(0)

elsa.setheading(0)

def twig():
    elsa.left(45)
    elsa.forward(30)
    elsa.backward(30)
    elsa.right(45)
    elsa.forward(30)
    elsa.backward(30)
    elsa.right(45)
    elsa.forward(30)
    elsa.backward(30)
    elsa.left(45)

# twigLength = 30
# numOfSegments = 4

def branch(numOfSegments, twigLength):
    for i in range(numOfSegments):
        twig()
        elsa.forward(twigLength)
    elsa.backward(twigLength * numOfSegments)

def drawSnowFlake(numOfBranches, numOfSegments, twigLength, xPos, yPos):
    elsa.penup()
    elsa.goto(xPos, yPos)
    elsa.pendown()
    for i in range(numOfBranches):
        branch(numOfSegments, twigLength)
        elsa.right(360 / numOfBranches)

while True:
    xRandom = random.randint(-300, 300)
    yRandom = random.randint(-300, 300)
    branchNumRandom = random.randint(4, 9)
    numOfSegmentsRandom = random.randint(2,6)
    twigLengthRandom = random.randint(10, 30)
    drawSnowFlake(branchNumRandom, numOfSegmentsRandom, twigLengthRandom, xRandom, yRandom)

elsa.hideturtle()

turtle.mainloop()