numT = 0
numS = 0
for i in range(int(input())):
    line = input()
    for j in line:
        if j == "t" or j == "T":
            numT+=1
        elif j == "s" or j == "S":
            numS+=1
if numT > numS:
    print("English")
else:
    print("French")



