x,y,z = int(input("Input:")),list(input("Input:")),list(input("Input:"))
print(sum([1 if y[i] == "C" and z[i] == "C" else 0 for i in range(x)]))

x,y,z = int(input("Input:")),list(input("Input:")),list(input("Input:"))
count = 0
for i in range(x):
    if y[i] == z[i] == "C":
        count+=1
print(count)