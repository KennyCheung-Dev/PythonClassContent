
money = int(input())
machine1, machine2, machine3 = int(input()), int(input()), int(input())
plays = 0
while (True):
    machine1 += 1
    plays += 1
    money -= 1
    if machine1 >= 35:
        print("Reward: " + str(30))
        machine1 = 0
        money += 30
    if money <= 0:
        break


    machine2 += 1
    plays += 1
    money -= 1
    if machine2 >= 100:
        machine2 = 0
        print("Reward: " + str(60))
        money += 60
    if money <= 0:
        break


    machine3 += 1
    plays += 1
    money -= 1
    if machine3 >= 10:
        machine3 = 0
        print("Reward: " + str(9))
        money += 9
    if money <= 0:
        break

print(plays)