import turtle
import random

# Variables 变量
# Twig(angle, dist)

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
# twig(65, 60)

#循环twig（）四次 画树枝  branch
def branch(times, angle, dist):
    for i in range(times):
        twig(angle, dist)

# 函数snow要求
# 提取branch Number 决定多少根树干
# 根据树干数量 决定每次转向角度
# 每画完一个树干 进行位置角度调整 让下一根树干能从原点开始画
def snow(branchNum, times, angle, dist):
    for i in range(branchNum):
        branch(times, angle, dist)
        elsa.backward(times * dist)
        elsa.right(360 / branchNum)

# 用snow（）  在随机位置 随机branchNum, times， angle， dist 无限循环的画 雪花
while True:
    elsa.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    elsa.goto(x, y)
    elsa.pendown()
    branchNumRandom = random.randint(1, 12)
    timesRandom = random.randint(2, 10)
    angleRandom = random.randint(20, 80)
    distRandom = random.randint(20, 60)
    snow(branchNumRandom, timesRandom, angleRandom, distRandom)


# 结尾
elsa.hideturtle()
turtle.mainloop()