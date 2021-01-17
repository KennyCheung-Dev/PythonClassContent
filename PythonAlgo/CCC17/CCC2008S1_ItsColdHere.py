lowestTemp = 200
lowestCity = ""
while True:
    line = input()
    tempTemp = int(line.split(" ")[1])
    tempCity = line.split(" ")[0]
    if tempTemp < lowestTemp:
        lowestTemp = tempTemp
        lowestCity = tempCity
    if tempCity == "Waterloo":
        break
print(lowestCity)