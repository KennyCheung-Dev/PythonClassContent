s = input()

happy = 0
sad = 0

for i in range(len(s) - 2):
    if s[i:i+3] == ":-)":
        happy += 1
    elif s[i:i+3] == ":-(":
        sad += 1



if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif sad == happy and sad > 0:
    print("unsure")
else:
    print("none")

