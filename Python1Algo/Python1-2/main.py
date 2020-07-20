# 我有 123 块钱

# KennyAge = 200
# yearsPassed = 50
#
# print(KennyAge + yearsPassed)

# firstName = "James"
# lastName = "Bond"
#
# money = 123
# money = 100

# Concatenation 字串串接
# print(  firstName + lastName  )
# print(  "James"  +   "Bond"   )
# print(  "我有" + str(money) + "块钱"  )
# print(  int("100") + 23  )

# Type Cast 更改数据类型
# int()
# str()

#课上练习
# print 自己的岁数
# 需要用到 age 变量
# output： "I am [] years old"

# 只可以字串串接 文字 跟 文字  不可以跟整数

# 现在的岁数 = KennyAge + yearsPassed
# print(现在的岁数)

# Assignment 赋值 - 赋予值
# number1 = 15
# number1 = 20
# print(number1)

# 变量 Variables
# 变量可以被赋值
# print（变量） 系统会吧变量的值找出来然后返还
# 变量可以重复赋值， 可以变化

# name = "Kenny"
# print(name)

#课上练习
# 给一个变量赋值 用布林值 然后用print把值输出 变量名字可以随便改
# print("hello")
#
# print(15)
#
# print(15.25)
#
# print(True)



# Function 函数
# F(x) = 10 * x
# Function(x) = 10 乘以 x
# Function(5) = 10 * 5 = 50        F(5) = 50   F(6) = 60

# 编程上的函数
# 可以不用数字来带入
# 可以带入任何数据类型
# 返还的 不一定透过数学计算得来
# 可以不返还
# F(x)


# 程序： 把用户的数字加上50 然后print
# userInput = int(input("请输入你的数字:"))
# result = userInput + 50
# print(result)

# 课上练习 程序：
# 用问题获得用户输入用户的名字，
# 跟用户打招呼
# Output: "Hi [用户的名字]"

# name = input("What's your name")
# print("Hi " + name + ".")

# 顺序结构

# 选择结构
# if statement    （  if 句子  ）
# number = 50
# if False ^ False:
#     print("True")

# >    <    >=    <=    ==    True   False    !=     not X == X   XOR: ^
# not and or xor

# 比较文字 scissor(s) rock(r)  paper(p)
# user = "s"
# computer = "s"
# if user == computer:
#     print("Draw")

# 猜拳程序
# 问题1： 如何得到用户的选择
# 用input() 加问题在里面

# 问题2： 如何得到电脑方面随机出来的结果
# 暂时假设电脑一定会出 computer = "r"

# 问题3： 具体我们要测试些什么
# 电脑肯定是石头
# 3 可能性：
# 1） 用户出拳头  =  和局
# 2） 用户出纸    = 用户赢了
# 3） 用户出剪刀   = 用户输了
# 用三个 If-statement

computer = "r"
player =  input("Please choose rock(r), paper(p) or scissor(s)")
if computer == player:
    print("Draw")
if player == "s":
    print("You lose")
if player == "p":
    print("You win")

