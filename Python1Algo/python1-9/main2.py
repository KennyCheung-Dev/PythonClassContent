import random


# 题目
# 用一个一维度列表 存 10个随机数字 范围1-10
# 用你的方法 算 10个数字完全相乘的sum总合

# sum = 0
# list = [1, 2, 3]
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)

# for i in range(len(list)):
#     for j in range(len(list)):
#         sum += list[i] * list[j]
# print(sum)

# for i in range(len(list)):
#     for j in range(i + 1, len(list)):
#         sum += list[i] * list[j]
# print(sum)


# jimmy同学的答案
# q=0
# z=0
# a = 0
# b=0
# numbers = []
# counter = 1
# for step in range(3):
#     numbers.append(counter)
#     counter += 1
# for step2 in range(step+1):
#     q += numbers[step2]-numbers[0]
#     print('q',q)
#     a += q * numbers[step2]
#     print('a',a)
# print(numbers)
# print('a',a)

hamburger = "abcdefghij"

#列表的 indexing slicing 索引取值 截取
print(hamburger[6])    #一个值
print(hamburger[3:8])  #从a到b
print(hamburger[3:])   #从a到完结
print(hamburger[:5])   #从开始到b
print(hamburger[:])    #从开始到结束
print(hamburger[-3])   #倒数第x
print(hamburger[3:-2]) #从a到b  b用倒数来算
print(hamburger[-1::-1]) #从a开始 以b的值递进
print(hamburger[::2])  #以b的值递进
print(hamburger[-1::-1][::3])  # 条件可以叠加起来

# Question
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1）  从第一到第四
# 2） 从开始到最后 每四个数字一次
# 3） 后五位数字 每第二个
# 4） 倒列 从倒数第三到正数第三  包括第三本身



'''
作业：
["Red", "Green", "Blue", "White", "Black", "Rainbow"]
把上述词汇里面的 韵母(aeiou) 全部换成"o"
Red -> Rod
Green -> Groon
Blue -> Bloo
White -> Whoto
Black -> Block
Rainbow -> Roonbow

解题阶段：
第一： 先成功把一个文字的韵母换掉
第二： 用循环 把上述的字 用同样的逻辑 换掉
第三： 输出结果
'''

#提示 需要创建一个新的文字变量
# abcde
# 新的字 obcdo




