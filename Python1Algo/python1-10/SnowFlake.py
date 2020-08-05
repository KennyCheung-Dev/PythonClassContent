import turtle

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

twigLength = 30
numOfSegments = 4

def branch():
    for i in range(numOfSegments):
        twig()
        elsa.forward(twigLength)
    elsa.backward(twigLength * numOfSegments)

numOfBranches = 8
for i in range(numOfBranches):
    branch()
    elsa.right(360 / numOfBranches)

elsa.hideturtle()

turtle.mainloop()