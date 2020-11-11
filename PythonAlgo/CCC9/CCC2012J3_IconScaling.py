icon = [["*", "x", "*"],
        [" ", "x", "x"],
        ["*", " ", "*"]]
s = int(input())
for i in range(3):
    for j in range(s):
        for k in range(3):
            for l in range(s):
                print(icon[i][k], end="")
        print()


# s = int(input())
# for i in range(s):
#     print("*" * s, "x" * s, "*" * s)
# for i in range(s):
#     print(" " * s, "x" * s, "x" * s)
# for i in range(s):
#     print("*" * s, " " * s, "*" * s)

