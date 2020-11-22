places = []
directions = []
while True:
    directions.append(input())
    places.append(input())
    if places[len(places) - 1] == "SCHOOL":
        break

#Reverse the directions
for i in range(len(directions)):
    if directions[i] == "L":
        directions[i] = "RIGHT"
    else:
        directions[i] = "LEFT"

# Build Result Strings
for i in range(len(directions) - 1, -1, -1):
    line = ""
    line += "Turn "
    line += directions[i]
    if i > 0:
        line += " onto "
        line += places[i - 1]
        line += " street."
    else:
        line += " into your HOME."
    print(line)
