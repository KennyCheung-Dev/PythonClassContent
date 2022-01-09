import sys

#问题 A: 统计字符的个数

'''

从键盘中任意输入一串字符,直至输入"#"字符代表结束.请编程统计输入的字符中的大写字母,小写字母和数字字符的个数分别是多少?
Input a string of characters from the keyboard until you enter the "#" character to represent the end.
Write a program to counter the number of uppercase characters,
lowercase characters and numeric characters in the input stream.

输入
Input  输入只有一行,包括一串字符.(长度小于20)
Input: There is only one line, a string of characters. (Length is less than 20)

输出
Output 输出只有一行（这意味着末尾有一个回车符号），包括3个整数。分别代表大写字符，小写字符和数字字符的个数。
Output: The output is only one line (which means there is a carriage return at the end), includes 3 integers,
representing the number of uppercase characters, lowercase characters and numeric characters respectively.

样例输入 Copy
daDSALDdcada3240#
样例输出 Copy
5 7 4

'''

# line = input()
# line = line.split("#")[0]
# upperCount = 0
# lowerCount = 0
# numCount = 0
# for c in line:
#     if c.isdigit():
#         numCount += 1
#     elif c.isalpha():
#         if c.isupper():
#             upperCount += 1
#         else:
#             lowerCount += 1
# print(upperCount, lowerCount, numCount)







'''

问题 B: 组合数的生成

题目描述
从 1、2、3、4、5、6 这 6 个数字中任取 4 个数的组合有1 2 3 4、1 2 3 5、1 2 3 6、1 2 4 5、1 2 4 6、1 2 5 6、1 3 4 5、1 3 4 6、1 3 5 6、1 4 5 6、2 3 4 5、2 3 4 6、2 3 5 6、2 4 5 6、3 4 5 6，共 15 种。若把它们看成 4 位数，发现是递增的。


The combinations of any 4 numbers from the 6 numbers 1, 2, 3, 4, 5, and 6 are 1 2 3 4, 1 2 3 5, 1 2 3 6, 1 2 4 5, 1 2 4 6, 1 2 5 6, 1 3 4 5, 1 3 4 6, 1 3 5 6, 1 4 5 6, 2 3 4 5, 2 3 4 6, 2 3 5 6, 2 4 5 6, 3 4 5 6, There are 15 kinds in total. If you regard them as 4 digit numbers, you will find that they are increasing in value.

输入
输入 n 和 r，1≤r≤n≤20


Input n and r, 1≤r≤n≤20


输出
按照以上顺序，输出从 n 个数字（1~n）中任取 r 个数的所有组合


According to the above sequence, output all combinations of r numbers from n numbers (1~n)


样例输入 Copy
3 2
样例输出 Copy
1 2
1 3
2 3

'''

# maxNum, maxDigit = [int(i) for i in input().split(" ")]
#
# numList = []
# def NumRecur(currentNum, currentDigit, combination):
#     combination = combination.copy()
#     if currentDigit < maxDigit and currentNum + 1 > maxNum:
#         return
#     if currentDigit > maxDigit:
#         return
#     combination.append(str(currentNum))
#     if currentDigit == maxDigit:
#         numList.append(combination)
#         return
#     for i in range(currentNum, maxNum):
#         NumRecur(i + 1, currentDigit + 1, combination)
# for i in range(1, maxNum+1):
#     NumRecur(i, 1, [])
# for i in numList:
#     print(" ".join(i))




'''

问题 C: 合并果子
时间限制: 1 Sec  内存限制: 128 MB
提交: 37  解决: 14
[提交] [状态] [讨论版] [命题人:外部导入]
题目描述
在一个果园里，多多已经将所有的果子打了下来，而且按果子的不同种类分成了不同的堆。多多决定把所有的果子合成一堆。每一次合并，多多可以把两堆果子合并到一起，消耗的体力等于两堆果子的重量之和。可以看出，所有的果子经过n-1次合并之后，就只剩下一堆了。多多在合并果子时总共消耗的体力等于每次合并所耗体力之和。
因为还要花大力气把这些果子搬回家，所以多多在合并果子时要尽可能地节省体力。假定每个果子重量都为1，并且已知果子的种类数和每种果子的数目，你的任务是设计出合并的次序方案，使多多耗费的体力最少，并输出这个最小的体力耗费值。
例如有3种果子，数目依次为1，2，9。可以先将 1、2堆合并，新堆数目为3，耗费体力为3。接着，将新堆与原先的第三堆合并，又得到新的堆，数目为12，耗费体力为 12。所以多多总共耗费体力=3+12=15。可以证明15为最小的体力耗费值。


In an orchard, Dodo had already knocked down all the fruits, and divided them into different piles according to the different types of fruits. Dodo decided to combine all the fruits into one pile. Every time you merge, Dodo can merge two piles of fruits together, and the energy consumed is equal to the sum of the weight of the two piles of fruits. It can be said that after all the fruits are merged n-1 times, there is only one pile left. The total stamina consumed by Dodo when merging the fruits is equal to the sum of the stamina consumed for each merge.
Because it will take great effort to move these fruits home, Dodo should save as much energy as possible when merging the fruits. Assuming that the weight of each fruit is 1, and the number of fruit types and the number of each fruit are known, your task is to design a combined sequence plan to minimize the amount of physical effort that Dodo consumes, and output the minimum value of energy spent.
For example, there are 3 kinds of fruits, the numbers are 1, 2, and 9. You can merge piles 1 and 2 first, the number of the new pile is 3, and the energy spent is 3. Then, merge the new pile with the original third pile, and get a new pile, the number is 12, and the physical effort is 12. So Dodo consumes a total of physical energy: 3 + 12 = 15. We have proven that 15 is the minimum physical expenditure value.


输入
输入文件fruit.in包括两行，第一行是一个整数n（1 <= n <= 10000），表示果子的种类数。第二行包含n个整数，用空格分隔，第i个整数ai（1 <= ai <= 20000）是第i种果子的数目。


The input file fruit.in consists of two lines. The first line is an integer n (1 <= n <= 10000), which represents the number of fruit types. The second line contains n integers, separated by spaces. The i-th integer ai (1 <= ai <= 20000) is the number of the i-th fruit.
 


输出
输出文件fruit.out包括一行，这一行只包含一个整数，也就是最小的体力耗费值。输入数据保证这个值小于231。


The output file fruit.out includes one line, which contains only an integer, is the minimum physical exertion value. The input number ensures that this value is less than 231.
 


样例输入 Copy
3
1 2 9
样例输出 Copy
15
提示
【数据规模】
对于30%的数据，保证有n <= 1000；
对于50%的数据，保证有n <= 5000；
对于全部的数据，保证有n <= 10000。


For 30% of the data, it is guaranteed that n <= 1000;
For 50% of the data, it is guaranteed that n <= 5000;
For all data, it is guaranteed that n <= 10000.

'''


import bisect
n = int(input())
numList = [int(i) for i in input().split(" ")]
if n <= 0:
    print(0)
else:
    numList.sort()
    energyConsumed = 0
    while (len(numList) > 1):
        sum = 0
        sum += numList.pop(0)
        sum += numList.pop(0)
        energyConsumed += sum
        bisect.insort(numList, sum)
        print(numList)
    print(energyConsumed)




'''

问题 D: USACO 2017 US Open Contest, Bronze Problem 1. The Lost Cow
时间限制: 1 Sec  内存限制: 128 MB
提交: 129  解决: 12
[提交] [状态] [讨论版] [命题人:michael703]
题目描述
10points
English:
Farmer John has lost his prize cow Bessie, and he needs to find her!
Fortunately, there is only one long path running across the farm, and Farmer John knows that Bessie has to be at some location on this path. If we think of the path as a number line, then Farmer John is currently at position x and Bessie is currently at position y (unknown to Farmer John). If Farmer John only knew where Bessie was located, he could walk directly to her, traveling a distance of |x−y|. Unfortunately, it is dark outside and Farmer John can't see anything. The only way he can find Bessie is to walk back and forth until he eventually reaches her position.
Trying to figure out the best strategy for walking back and forth in his search, Farmer John consults the computer science research literature and is somewhat amused to find that this exact problem has not only been studied by computer scientists in the past, but that it is actually called the "Lost Cow Problem" (this is actually true!).
The recommended solution for Farmer John to find Bessie is to move to position x+1, then reverse direction and move to position x−2, then to position x+4, and so on, in a "zig zag" pattern, each step moving twice as far from his initial starting position as before. As he has read during his study of algorithms for solving the lost cow problem, this approach guarantees that he will at worst travel 9 times the direct distance |x−y| between himself and Bessie before he finds her (this is also true, and the factor of 9 is actually the smallest such worst case guarantee any strategy can achieve).
Farmer John is curious to verify this result. Given x and y, please compute the total distance he will travel according to the zig-zag search strategy above until he finds Bessie.

chinese:
农夫约翰失去了他的牛贝西（Bessie），他需要找到她！
幸运的是，整个农场只有一条漫长的道路，而农夫约翰知道贝肯定在这条道路上的某个位置。如果我们将路径视为数字线，那么农夫约翰当前位于x位置，而Bessie当前处于y位置（农夫约翰不知道y的值）。如果农夫约翰只知道贝西的位置，那么他可以直接向她走去，前进| x-y |步。不幸的是，外面一片漆黑，农夫约翰什么也看不到。他找到贝茜的唯一方法就是来回走动，直到他最终到达她的位置。
为了找出在搜索中来回走动的最佳策略，农夫约翰查阅了计算机科学研究文献，觉得很有趣，发现这个确切的问题不仅是过去计算机科学家研究的，而且是实际上被称为“迷失的牛”（这确实是事实！）。
建议的解决方案是：农民约翰移动到位置x + 1，然后反向并移动到位置x−2，然后移动到位置x + 4，依此类推，以“ 之字形”模式进行每一步，每一步距离他的初始起始位置两倍的距离。正如他在研究的那样，这种方法保证了他在最坏的情况下将走的距离是| x-y |的9倍。在他和贝西找到他之前找到了他（这也是事实，并且9实际上是任何策略都能保证的最小的最坏情况）。
农夫约翰很好奇，想要验证这个结果。给定x和y，请根据上面的之字形搜索，计算出他找到贝西将要走的总距离。

输入
The single line of input contains two distinct space-separated integers x and y. Both are in the range 0…1,000.
整数x和y以空格分，范围都在0…1,000之间

输出
Print one line of output, containing the distance Farmer John will travel to reach Bessie.
给一行输出，其中包含农夫约翰到达贝西的距离。

样例输入 Copy
3 6
样例输出 Copy
9

'''

# x, y = [int(i) for i in input().split(" ")]
#
# currentPos = x
# targetPos = x + 1
# displacement = 1
# positive = True
# accumulatedStep = 0
# while y not in range(currentPos, targetPos + 1) and y not in range(targetPos, currentPos + 1) :
#     accumulatedStep += abs(targetPos - currentPos)
#     currentPos = targetPos
#     positive = not positive
#     displacement *= 2
#     if positive:
#         targetPos = x + displacement
#     else:
#         targetPos = x - displacement
# accumulatedStep += abs(y - currentPos)
# print(accumulatedStep)

'''

问题 E: 合并数字(Combined Numbers)
时间限制: 1 Sec  内存限制: 128 MB
提交: 32  解决: 27
[提交] [状态] [讨论版] [命题人:whitycatty]
题目描述
30points
English:

Pompong was at home due to the impact of the epidemic. He was bored and began to entertain himself. He thought of a game of combining numbers. The rules of the game are as follows: Initially, there are n numbers in a sequence, and each time Pengpeng can combine m (m ≥ 2 and m less than or equal to the current sequence length) numbers on the left of the sequence, that is, delete these m numbers, and the sum of these m numbers is added to the leftmost side of the sequence, and the sum of these m numbers is added to his own score. When the sequence length is 1 or Peng thinks he cannot get a higher score, the game ends. Pompong’s score is initially 0. Peng Peng asked you to help him calculate the highest score possible.


Chinese:
蓬蓬因疫情影响闲在家中，他一人无聊开始自娱自乐，想到了一个合并数字的游戏。游戏规则如下：初始共有 n 个数字排成一个序列，蓬蓬每次可以将这个序列左边的 m（m ≥ 2 且 m 小于等于当前序列长度）个数字合并，即删除这 m 个数字，然后将这 m 个数字的和加入到序列最左边，并且将这 m 个数字的和加到自己的分数上. 当序列长度为 1 或小蓬认为他无法获得更高分的时候，游戏结束。蓬蓬的分数初始为 0。蓬蓬找来聪明的你帮助他计算他能够获得的最高分是多少？
输入


The first line of the input data is a positive integer n, which means there are n (1 ≤ n ≤ 105) numbers in total. The second line is n integers, and each number ci satisfies |ci| ≤ 10000.

输入数据的第一行为一个正整数 n，表示共有 n(1 ≤ n ≤ 105) 个数字。第二行为 n 个整数，每个数 ci 满足 |ci| ≤ 10000。
输出
One line represents the highest score that Peng Peng can get.

一行，表示蓬蓬能获得的最高分。
样例输入 Copy
3
2 -1 2
样例输出 Copy
4

'''


# n = int(input())
# nums = [int(i) for i in input().split(" ")]
# result = []
# def Merge(nums, points):
#     if len(nums) <= 1:
#         return points
#     highest = -sys.maxsize - 1
#     for i in range(2, len(nums) + 1):
#         tempNums = nums.copy()
#         tempPoints = points
#         sum = 0
#         for j in range(i):
#             sum += tempNums.pop(0)
#         tempPoints += sum
#         tempNums.insert(0, sum)
#         highest = max(highest, Merge(tempNums, tempPoints))
#     return highest
# print(Merge(nums, 0))

