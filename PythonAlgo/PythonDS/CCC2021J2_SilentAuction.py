highestName = ""
highestBid = -1
for i in range(int(input())):
    name = input()
    bid = int(input())
    if bid > highestBid:
        highestName = name
        highestBid = bid
print(highestName)