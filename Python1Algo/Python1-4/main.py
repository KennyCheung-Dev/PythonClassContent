# num = 0
# for step in range(101):
#     num += step
#     print(num)
# print("Result : " + str(num))

# 导入turtle
import turtle

# 从turtle导入全部
# from turtle import *
# turtle.write(500)

# # 向前
# turtle.forward(100)
# # 不用笔
# turtle.penup()
# # 移动到位置（X， Y）
# turtle.goto(0, 100)
# #把笔继续
# turtle.pendown()
# # 向前
# turtle.forward(100)
# # 向后
# turtle.backward(100)
# # 转左（度数）
# turtle.left(90)
# # 向前
# turtle.forward(100)
# # 无限循环 让画面停留住
# turtle.mainloop()

# 控制turtle画画速度
# turtle.speed(0)
#
# for i in range(10):
#     turtle.write(i * 10)
#     turtle.right(90)
#     turtle.penup()
#     turtle.forward(30)
#     turtle.pendown()
#     turtle.forward(170)
#     turtle.penup()
#     turtle.backward(200)
#     turtle.left(90)
#     turtle.forward(40)
#
# turtle.mainloop()

# mike = turtle.Turtle()
# mike.color('#ffda96')
# mike.shape('turtle')
# mike.forward(200)
#
# turtle.mainloop()

# bits = 1 bit
# bytes = 8 bits

# 00000100
# 2 ** 8 = 256
# 0 - 255

# # 预先送到初始位置
# mike = turtle.Turtle()
# mike.speed(0)
# mike.penup()
# mike.goto(-300, 100)
# mike.left(90)
# mike.pendown()
#
# # 预先送到初始位置
# sam = turtle.Turtle()
# sam.speed(0)
# sam.penup()
# sam.goto(300, 100)
# sam.right(90)
# sam.pendown()
#
# # Loop900次
# for i in range(900):
#     #实线 走一段距离 转一点角度
#     mike.forward(7)
#     mike.right(2)
#     mike.penup()
#     #空白 走一段距离 转一点角度
#     mike.forward(7)
#     mike.right(2)
#     mike.pendown()
#
#     sam.forward(7)
#     sam.right(2)
#     sam.penup()
#     sam.forward(7)
#     sam.right(2)
#     sam.pendown()

# For-Loop
# While-Loop

# from random import randint
# num = 0
# while num < 5000 and not num == 100:
#     num += randint(0, 11)
#     print(num)


# print(input("Give me a number:") + 20)

# input()
# try:
#     # 尝试一些 有风险的 东西
#     int("Kenny")
#     # 运行没错 可以结束 无限循环
# except:
#     # 如果上面报错的话  这边会运行
#     print("Please type a valid integer")




# input（） 函数 收取一个数字
# 如果用户 写了英文字母 系统会报错并停止运行
# 透过用while loop 和try-except 我们可以进行检测
# 看看用户有没有输入正确数值
# 尝试写出检查的code

# 输出：
# Please type a number:
# kenny
# Please type a valid number!!!!
# kenyn
# Please type a valid number!!!!
# poipiesflkhasgrkalng
# Please type a valid number!!!!
# 15


#Homework Answer:
# print("Please type a number")
#
# answerReceived = False
# while answerReceived == False:
#     answer = input()
#     try:
#         answer = int(answer)
#         answerReceived = True
#     except:
#         print("Please type a valid number")

# count = 0
#
# while True:
#     print("Hello")
#     count += 1
#     if count >= 5:
#         break

# for i in range(10000):
#     print("Hello World")
#     if i >= 50:
#         break















