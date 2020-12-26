x, y = [int(i) for i in input().split(' ')]

ans = 0
by = 1
ddir = 1

while True:
    if (ddir == 1 and x <= y and y <= (x+by)) or (ddir==-1 and x-by<=y and y<=x):
        ans += abs(y-x)
        print(ans)
        break
    else:
        ans += by*2;
        by *= 2;
        ddir *= -1;