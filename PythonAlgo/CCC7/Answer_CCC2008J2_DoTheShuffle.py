def Button1(s):
    return s[1:] + s[0]

def Button2(s):
    return s[-1] + s[0:-1]

def Button3(s):
    return s[1] + s[0] + s[2:]

playList = "ABCDE"
continuing = True
while (continuing):
    button = int(input())
    times = int(input())
    for i in range(times):
        if button == 1:
            playList = Button1(playList)
        elif button == 2:
            playList = Button2(playList)
        elif button == 3:
            playList = Button3(playList)
        elif button == 4:
            continuing = False


print(playList[0] + " " + playList[1] + " " + playList[2] + " " + playList[3] + " " + playList[4])

