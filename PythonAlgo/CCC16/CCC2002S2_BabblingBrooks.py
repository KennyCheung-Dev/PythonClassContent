def RecursiveStreams(streams):
    command = input()
    resultStreams = []
    if command == "99":
        spilttingStream = int(input()) - 1
        percentage = int(input())
        for i in range(len(streams)):
            if i == spilttingStream:
                resultStreams.append(int(streams[i] * percentage / 100));
                resultStreams.append(streams[i] - int((streams[i] * percentage / 100)));
            else:
                resultStreams.append(streams[i])
        RecursiveStreams(resultStreams)
    elif command == "88":
        joiningStream = int(input()) - 1
        for i in range(len(streams)):
            if i == joiningStream:
                pass
            elif i == joiningStream+1:
                resultStreams.append(streams[i] + streams[i-1])
            else:
                resultStreams.append(streams[i])
        RecursiveStreams(resultStreams)
    elif command == "77":
        for i in streams:
            print(i, end="")
            if i != len(streams)-1:
                print(" ", end="")
        return streams
    else:
        return streams

startStreams = []
for i in range(int(input())):
    startStreams.append(int(input()))
RecursiveStreams(startStreams)