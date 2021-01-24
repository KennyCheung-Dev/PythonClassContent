
year = int(input())
while True:
    year+=1
    yearString = str(year)
    dict = {}
    for i in yearString:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    match = True
    for i in dict.values():
        if i > 1:
            match = False
    if match:
        print(yearString)
        break
