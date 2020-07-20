import random
import turtle

# computer = "r"
# player =  input("Please choose rock(r), paper(p) or scissor(s)")
# if computer == player:
#     print("Draw")
# if player == "s":
#     print("You lose")
# if player == "p":
#     print("You win")

# if else
# if True:
#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")
# else:
#     print("This is false")
#     print("This is false")
#     print("This is false")
#     print("This is false")


# if elif  (else + if)
# number = -70
# if number > 0:
#     print("number is greater than 0")
# elif number > 25:
#     print("number is greater than 25")
# elif number > 50:
#     print("number is greater than 50")
# else:
#     print("Number is below or equal to 0")

# 我需要一个数字 不能大于65535 不能小于0
# 请帮我把数字从用户 问出来 并且测试 如果不符合 告诉用户

# Python的模块Modules
# 文件最上面已经导入了random模块
# 可以开始试用random模块里面的randint功能
# randomNum = random.randint(1, 3)
#
# if randomNum == 1:
#     computer = "r"
# elif randomNum == 2:
#     computer = "p"
# else:
#     computer = "s"
#
# player =  input("Please choose rock(r), paper(p) or scissor(s)")

# Nested If-Statement 一层一层套起来的 if句子
# if number > 10:
#     print("Yes, greater than 10")
#     if number < 12:
#         print("Number is 11")


# 可能的情况：
# 1） 和局
# computer == player
# 2） 赢了
# player == r and computer == s   OR    player == s and computer == paper  OR ...
# 3） 输了

# if computer == player:
#     print("The computer has chosen: " + computer)
#     print("Draw")
# elif computer == "r" and player == "s" or computer == "s" and player == "p" or computer == "p" and player == "r":
#     print("The computer has chosen: " + computer)
#     print("Lose")
# elif computer == "s" and player == "r" or computer == "p" and player == "s" or computer == "r" and player == "p":
#     print("The computer has chosen: " + computer)
#     print("Win!")
# else:
#     print("Please enter a valid choice.")

#往前走
# turtle.forward(100)
# 往后走
# turtle.backward(100)

# 顺序结构
# 选择结构
# 循环结构
# 普片用法 用一个参数 表示循环次数
# For-Loop
# for step in range(5):
#     print("Hello")

# 用三个参数 分别表达 开始 结束 间距
# for step in range(50, 100, 10):
#     print(step)

#画尺子
for step in range(5):
    turtle.write(step * 10)
    turtle.forward(30)
turtle.mainloop()

# 作业
# 从 1 加到 100  用for-loop算出答案 并且在中间每一步 print加起来的和

# 1
# 3    1 + 2
# 6    3 + 3
# 10   6 + 4
# 15
# ...

# 答案 = 5050

# 提示 你应该需要一个额外的 变量 来存和