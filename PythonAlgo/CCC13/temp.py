# x, y = [], []
# for i in range(int(input())):
#     s = input()
#     x.append(int(s.split(",")[0]))
#     x.append(int(s.split(",")[1]))
# # [24, 44, 53, 26, 62]
# # [24, 44, 53, 26, 62]
# x.sort()
# y.sort()
# print(str(x[0]-1) + "," + str(y[0])-1)
# print(str(x[-1]+1) + "," + str(y[-1])+1)


# c1 = input()
# c2 = input()
# charge = int(input())
# x1 = int(c1.split(" ")[0])
# x2 = int(c1.split(" ")[1])
# y1 = int(c2.split(" ")[0])
# y2 = int(c2.split(" ")[1])
# distance = abs(y2-y1) + abs(x2-x1)
# if distance > charge:
#     print("N")
# elif distance == charge:
#     print("Y")
# else:
#     if distance % 2 == charge % 2:
#         print("Y")
#     else:
#         print("N")


keys = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

totalTime = 0

while True:
    s = input()
    if s == "halt":
        break
    previousKey = -1

    for i in range(len(s)): # looping the input
        for j in range(len(keys)): # looping the keys buttons
            for k in range(len(keys[j]):  # looping the letters inside a button
                # Few things for us to use:
                # s[i] <- current letter
                # keys[j][k] <- currently looping letter

                # Next steps:
                # Compare and find out if your current letter is
                # the one your are looping through,
                # If it is, for example "f", with keys[1][2]
                # If they are the same, then we get
                # 1) the button number and the -> j
                # 2) number of presses -> k
