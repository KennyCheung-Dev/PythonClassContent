coins = int(input())
timesPlayed1 = int(input())
timesPlayed2 = int(input())
timesPlayed3 = int(input())
machine1 = 35 - timesPlayed1
machine2 = 100 - timesPlayed2
machine3 = 10 - timesPlayed3
machines = [machine1, machine2, machine3]
while coins > 0:
    for i in range(3):
        machines[i] -= 1
        coins -= 1
        print(machines[i])
    print("")
