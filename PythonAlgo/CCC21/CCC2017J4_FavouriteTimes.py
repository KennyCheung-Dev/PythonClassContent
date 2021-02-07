minutesPassed = int(input())
count = 0
hours = 12
minutes = 0
days = int(minutesPassed / 1440)
count += days * 62
minutesPassed = minutesPassed % 1440
if minutesPassed == 0 and days == 0:
    print(0)
else:
    for i in range(minutesPassed):
        time = ""
        passBool = True
        minutes += 1
        minutes = minutes % 60
        if minutes == 0:
            hours += 1
        hours = hours % 13
        if hours == 0:
            hours += 1
        time += str(hours)
        if minutes < 10:
            time += "0"
        time += str(minutes)
        #Checking Difference
        tempDiff = int(time[1]) - int(time[0])
        for j in range(1, len(time)):
            digit = int(time[j])
            previousDigit = int(time[j-1])
            currDiff = digit - previousDigit
            if currDiff != tempDiff:
                passBool = False
                break
        if passBool:
            count += 1
    print(count)



