birthday = []
for i in range(int(input())):
    birthday.clear()
    s = input()
    birthday = [int(i) for i in s.split(" ")]
    if birthday[0] < 1989:
        print("Yes")
        continue
    elif birthday[0] == 1989:
        if birthday[1] < 2:
            print("Yes")
            continue
        elif birthday[1] == 2:
            if birthday[2] <= 27:
                print("Yes")
                continue
    print("No")