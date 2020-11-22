# icon = [["*", "x", "*"],
#         [" ", "x", "x"],
#         ["*", " ", "*"]]
#
# s = int(input())
# for i in range(3):
#         for l in range(s):
#                 for j in range(3):
#                         for k in range(s):
#                                 print(icon[i][j], end="")
#                 print()


s = int(input())
for i in range(s):
    print("*" * s + "x" * s + "*" * s)
for i in range(s):
    print(" " * s + "x" * s + "x" * s)
for i in range(s):
    print("*" * s + " " * s + "*" * s)