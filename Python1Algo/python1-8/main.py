# 作业题目
# 不用上述方法 直接把列表写出来
# 把嵌套列表 用嵌套循环 造出来
# Hint1: 用嵌套循环for-loop
# Hint2: 如果想要赋值 可以number[2][0] = x
# Hint(optional): 也可以用number[x].append(y) 来赋值
# 最后把列表print出来

number = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12],
          [13, 14, 15]]

# [[],[],[],[],[]]

#Approach 1

#Setting up the base list
numbers = []
for i in range(5):
    numbers.append([])
#Filling list with number 0
for i in range(5):
    for j in range(3):
        numbers[i].append(0)
#Assigning correct values with counter
counter = 1
for i in range(5):
    for j in range(3):
        numbers[i][j] = counter
        counter+=1
print(numbers)



#Approach 2

#Setting up the base list
numbers = []
for i in range(5):
    numbers.append([])
#Filling list with correct number
counter = 1
for i in range(5):
    for j in range(3):
        numbers[i].append(counter)
        counter += 1
print(numbers)