currentBlock = 1
while True:
    step = int(input())
    if step == 0:
        print("You Quit!")
        break
    tempBlock = currentBlock
    currentBlock += step
    if currentBlock == 99:
        currentBlock = 77
    if currentBlock == 90:
        currentBlock = 48
    if currentBlock == 67:
        currentBlock = 86
    if currentBlock == 40:
        currentBlock = 64
    if currentBlock == 54:
        currentBlock = 19
    if currentBlock == 9:
        currentBlock = 34
    if currentBlock > 100:
        currentBlock = tempBlock
        print("You are now on square " + str(currentBlock))
        continue
    print("You are now on square " + str(currentBlock))
    if currentBlock == 100:
        print("You Win!")
        break

