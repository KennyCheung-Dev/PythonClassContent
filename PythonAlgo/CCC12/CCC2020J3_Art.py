x, y = [],[]
for i in range(int(input())):
   s = input()
   x.append(int(s.split(",")[0]))
   y.append(int(s.split(",")[1]))
x.sort()
y.sort()
print(str(x[0]-1) + "," + str(y[0]-1))
print(str(x[-1]+1) + "," + str(y[-1]+1))
