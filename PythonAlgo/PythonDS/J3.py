pre = 0
while True:
    s = input()
    if s == "99999":
        break
    a = int(s[0]) + int(s[1]) 
    output = ""
    if a != 0:
        if a % 2 == 0:
            output += "right "
            pre = output
        else:
            output += "left "
            pre = output
    else:
        output += pre
    output += s[2:]
    print(output)