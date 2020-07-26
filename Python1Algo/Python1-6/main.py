a = open("c", 'r')
b = open("b.txt", 'r')
acontent = a.read()
bcontent = b.read()
a.close()
b.close()
a = open("a.txt", 'w')
b = open("b.txt", 'a')
a.write(bcontent)
b.write(acontent)
a.close()
b.close()

# file1：
# 1
# 2
# 3

# file 2:
# 4
# 5
# 6

# 在file1 跟file2 两个读取数据 以行数分开 放进集合（list）里  用splitlines()函数
# print output：
# File 1:
# 1
# 2
# 3

# File 2:
# ['4', '5', '6']


