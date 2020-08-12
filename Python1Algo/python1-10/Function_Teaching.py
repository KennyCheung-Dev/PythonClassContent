# 函数要求: Function
# print 一个文字
# def printAWord():
#     print("Hello World")

# 运行函数 Function Call
# printAWord()


# 函数要求: Function
# 提取一个文字， print拿到的文字
# def printWord(word):
#     print(word)
#
# printWord("Kenny")

# 函数要求: Function
# 提取两个文字， print两个文字
# def printWord(word, word2):
#     print(word)
#     print(word2)

# printWord(5, "Kenny" )


# 题目：
# 请创造一个函数 提取两个数字
# print 两个数值的和
# 呼叫 函数
def sum(num1, num2):
    return num1 + num2
# ^ 用return 关键词 把一些结果返回  用在呼叫的地方 继续运算

# 加四个数字
# sum(num1, num2) + sum(num3, num4)
# sum(sum(num1, num2), sum(num3, num4))

# Add 1, 2, 3, 4
print(sum(1, 2) + sum(3, 4))


# Computerphile

# 题目：
# 函数： 提取两个数字，返回积
# 算 以下算式： 5X8X2
# 只能用新建的函数 不能用*

# 参考：
def sum(num1, num2):
    return num1 + num2

# 答案：
#函数
def product(num1, num2):
    return num1 * num2
#呼叫
print(product(3, 5))
























