n = int(input())
calendar = []
for i in range(n):
    calendar.append(input())
interest = []
for i in range(5):
    interest.append(0)
for i in range(5):
    count = 0
    for j in range(n):
        if calendar[j][i] == "Y":
            count += 1
    interest[i] = count
maxInterest = max(interest)
indices = []
for i in range(5):
    if interest[i] == maxInterest:
        indices.append(str(i + 1))
print(",".join(indices))

