#SumacSequence

li = [int(input()), int(input())]
while li[-2]-li[-1]>=0:
    li.append(li[-2] - li[-1])
print(len(li))
