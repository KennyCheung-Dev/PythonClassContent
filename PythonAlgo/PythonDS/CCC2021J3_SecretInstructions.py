lastDirection = ""
while (True):
    line = input()
    if line == "99999":
        break
    directionNum = int(line[0]) + int(line[1])

    lastDirection = lastDirection if directionNum == 0 else \
        "right" if directionNum % 2 == 0 else \
            "left" if directionNum % 2 == 1 \
                else None

    print(lastDirection + " " + line[2:5])
