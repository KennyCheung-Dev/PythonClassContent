pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
total = int(input())

combination = 0
minimumTicket = total

for i in range(total + 1):
    for j in range(total + 1):
        for k in range(total + 1):
            for m in range(total + 1):
                if i * pink + j * green + k * red + m * orange == total:
                    print("# of PINK is {} # of GREEN is {} # of RED is {} # of ORANGE is {}".format(i, j, k, m))
                    combination += 1
                    if i + j + k + m < minimumTicket:
                        minimumTicket = i + j + k + m;
print("Total combinations is {}.".format(combination))
print("Minimum number of tickets to print is {}.".format(minimumTicket))