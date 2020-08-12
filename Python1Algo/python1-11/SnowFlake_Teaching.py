import turtle

#background color
turtle.Screen().bgcolor('blue')

elsa = turtle.Turtle()
elsa.color("cyan")
elsa.shape("turtle")
elsa.speed(0)


elsa.setheading(0)

# 函数要求： 提取一个角度 一个距离 用提取到的角度距离来画
# elsa.left(45)
# elsa.forward(30)
# elsa.backward(30)
# elsa.right(90)
# elsa.forward(30)
# elsa.backward(30)
# elsa.left(45)
# elsa.forward(30)

# 答案
def twig(angle, dist):
    elsa.left(angle)
    elsa.forward(dist)
    elsa.backward(dist)
    elsa.right(angle * 2)
    elsa.forward(dist)
    elsa.backward(dist)
    elsa.left(angle)
    elsa.forward(dist)

#呼叫twig函数
twig(20, 10)

elsa.hideturtle()

turtle.mainloop()