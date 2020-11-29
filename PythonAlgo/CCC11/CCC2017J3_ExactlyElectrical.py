c1 = input()
c2 = input()
charge = int(input())
x1 = int(c1.split(" ")[0])
y1 = int(c1.split(" ")[1])
x2 = int(c2.split(" ")[0])
y2 = int(c2.split(" ")[1])
distance = abs(y2 - y1) + abs(x2 - x1)
if distance > charge:
    print("N")
elif distance == charge:
    print("Y")
else:
    if distance % 2 == charge % 2:
        print("Y");
    else:
        print("N");

