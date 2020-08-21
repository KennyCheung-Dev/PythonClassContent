# WarmUp
# Rotate Left n times
# def LeftRotate(arr, n):
#     for i in range(n):
#         LeftRotateByOne(arr)
#     return arr
# def LeftRotateByOne(arr):
#     temp = arr[0]
#     for i in range(len(arr) - 1):
#         arr[i] = arr[i+1]
#     arr[len(arr)-1] = temp
#     return arr
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# print(LeftRotate(arr, 3))

#-------------------------------------------------------------------------

# 返回列表所有值的和
# 返回0 如果列表是空的
# 数字13 为特别，13本身 和 后面 跟着的数字 不算进和
# sum13([1, 2, 2, 1]) -> 6
# sum13([1, 1,]) -> 2
# sum13([1, 2, 2, 1, 13]) -> 6
# sum13([1, 2, 2, 13, 2, 1]) -> 6
# sum13([1, 2, 2, 1, 13, 13, 2]) -> 6

# def sum13(li):
#     sum = 0
#     skipNext = False
#     for num in li:
#         if num == 13:
#             skipNext = True
#         else:
#             if not skipNext:
#                 sum += num
#             else:
#                 skipNext = False
#     return sum
#
# print(sum13([1, 2, 2, 1, 13, 13, 2]))

#-------------------------------------------------------------------------

# CCC 2000 J3: Slot Machines

# 初始币数x，轮流放进三台老虎机
# a 给30币 每35轮
# b 给60币 每100轮
# c 给9币 每10轮
# 算出在币用完前可以玩多少次
# 老虎机有被上一手玩过多少次: a, b, c

# Input/Output:
'''
How many coin do you have?
48
How many times has the first machine been played?
3
How many times has the second machine been played?
10
How many times has the third machine been played?
4
You will be able to play 66 times before going broke.
'''

def PredictTimesPlayed(coin, m1, m2, m3):
    times = 0
    while True:
        # First Machine
        coin -= 1
        m1 += 1
        times += 1
        if m1 == 35:
            coin += 30
            m1 = 0

        # Ending Condition
        if coin <= 0:
            return times

        # Second Machine
        coin -= 1
        m2 += 1
        times += 1
        if m2 == 100:
            coin += 60
            m1 = 0

        # Ending Condition
        if coin <= 0:
            return times

        # Third Machine
        coin -= 1
        m3 += 1
        times += 1
        if m3 == 10:
            coin += 9
            m3 = 0

        # Ending Condition
        if coin <= 0:
            return times

print("How many coin do you have?")
coin = int(input())
print("How many times has the first machine been played?")
m1 = int(input())
print("How many times has the second machine been played?")
m2 = int(input())
print("How many times has the third machine been played?")
m3 = int(input())
print("You will be able to play " + str(PredictTimesPlayed(coin, m1, m2, m3)) + " times before going broke.")

# -----------------------------------------------------------------

# 2001 J2

# Mod Inverse
# Provide x and m

# def ModInverse(x, m):
#     for n in range(0, m):
#         if x * n % m == 1:
#             return n
#     return "No such integer exists."
# print(ModInverse(4, 17))

# -----------------------------------------------------------------

# 2007 J3

# 一号到十号箱子分别有
# $100, $500, $1,000, $5,000, $10,000, $25,000,
# $50,000, $100,000, $500,000, $1,000,000
# 玩家先选一个箱子拿走
# 其他玩家也会选走箱子

# 一部分箱子被拿走之后，银行会提出交易，用一定价钱购买你的箱子Deal or No Deal?
# 程序帮助玩家决定Deal or No Deal，
# 我们知道已经拿走和剩下的箱子的面值
# 我们知道银行给我们的offer

# 如果offer高于average Deal
# 其他情况 No Deal

#Input:
# 拿走了多少个箱子
# 拿走的箱子
# offer
'''
2      <-  被拿走的箱子的数量
3      <-  第一个箱子的号码
8      <-  第二个箱子的号码
198000
'''
# 以上数据显示
# 拿走了两个箱子
# 3号和8号
# 银行offer 198000

# Ouput:
'''
No Deal
'''
# 剩下的箱子是1，2，4，5，6，7，9，10
# 平均值 198,825 比offer高
# 所以No Deal

'''
8
10
9
8
7
6
5
4
3
400
'''

"Deal"
# 八个箱子 剩下两个
# 平均 （100 + 500）/ 2 = 300
# Offer 400
# Deal

#Answer:
# caseValues = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
# caseTaken = int(input())
# total = 1691600
# for i in range(caseTaken):
#     total -= caseValues[int(input()) - 1]
# avg = total / (10 - caseTaken)
# offer = int(input())
# if (offer > avg):
#     print("Deal")
# else:
#     print("No Deal")

# -----------------------------------------------------------------

# 2008 J2

# 音乐播放器只能装载五首曲子
# 播放器有4个按钮 功能分别是：
# 按键1： 将第一首移到最后
# 按键2： 将最后一首移到头
# 按键3： 交换第一和第二
# 按键4： 输出歌单

# 写一音乐播放器模拟器
# 程序输入：
# 循环以下
# Button number: n
# Number of Presses: x
# 知道按键4 被按了

# 模拟输入：
# Button number: 2
# Number of Presses: 1
# Button number: 3
# Number of Presses: 1
# Button number: 2
# Number of Presses: 3
# Button number: 4
# Number of Presses: 1
# Output:
# B C D A E

# Approach 1:

# musicList = ['A', 'B', 'C', 'D', 'E']
# def Button1(times):
#     for i in range(times):
#         temp = musicList[0]
#         for j in range(len(musicList) - 1):
#             musicList[j] = musicList[j + 1]
#         musicList[-1] = temp
#
# def Button2(times):
#     for i in range(times):
#         temp = musicList[4]
#         for j in range(len(musicList) - 1, 0, -1):
#             musicList[j] = musicList[j - 1]
#         musicList[0] = temp
#
# def Button3(times):
#     for i in range(times):
#         temp = musicList[0]
#         musicList[0] = musicList[1]
#         musicList[1] = temp
#
# while True:
#     btnPressed = int(input("Button Pressed?"))
#     if btnPressed == 1:
#         Button1(int(input("Times Pressed?")))
#     elif btnPressed == 2:
#         Button2(int(input("Times Pressed?")))
#     elif btnPressed == 3:
#         Button3(int(input("Times Pressed?")))
#     elif btnPressed == 4:
#         int(input("Times Pressed?")) # Useless
#         for song in musicList:
#             print(song, end=" ")
#         break


# Approach 2:

# music = "ABCDE"
#
# while True:
#     btnPressed = int(input("Button Pressed?"))
#     if btnPressed == 1:
#         for i in range(int(input("Times Pressed?"))):
#             music = music[1:] + music[0]
#     elif btnPressed == 2:
#         for i in range(int(input("Times Pressed?"))):
#             music = music[-1] + music[0:-1]
#     elif btnPressed == 3:
#         for i in range(int(input("Times Pressed?"))):
#             music = music[1] + music[0] + music[2:]
#     elif btnPressed == 4:
#         int(input("Times Pressed?")) # Useless
#         for song in music:
#             print(song, end=" ")
#         break

# -----------------------------------------------------------------

# 2011 J3

# Sumac Sequence :
# 120, 71, 49, 22, 27
# tn+2 = tn - tn+1
# 数列结束在 tm if tm-1 < tm  包括tm

# 120, 71, 49, 22, 27
# 3rd number : 49 = 120 - 71
# Input: two positive numbers t1 and t2, 0 < t2 < t1 < 10000

# nums = [int(input("Num1:")), int(input("Num2:"))]
# while True:
#     next = nums[-2] - nums[-1]
#     nums.append(next)
#     if (nums[-2] < next):
#         break
# print(len(nums))

# -----------------------------------------------------------------

# 2015 J2

# 透过信息表情判断感情
# :-)  =  happy
# :-(  =  sad

# 如果信息没有 表情 output none
# 如果happy和sad表情数量同等 output  unsure
# 如果happy多 output happy
# 如果sad多 output sad

# Input Example：
# How are  you :-) doing :-) today :-)?
# happy
# :)
# none
# This:-(is str:-(:-(ange te:-)xt.
# sad

# text=input()
# happy = 0
# sad = 0
# for i in range(len(text)-2):
#     if text[i:i+3] == ":-)":
#         happy += 1
#     elif text[i:i+3] == ":-(":
#         sad += 1
# if sad > happy:
#     print("sad")
# elif happy  > sad:
#     print("happy")
# elif happy == 0 and sad == 0:
#     print("none")
# elif happy == sad:
#     print("unsure")





