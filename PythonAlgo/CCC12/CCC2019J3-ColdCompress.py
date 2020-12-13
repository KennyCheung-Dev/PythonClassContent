for i in range(int(input())):
    s = input() # +++===!!!!
    count = 0
    previousChar = s[0]
    for j in range(len(s)):
        # Case 1: this character we are looping is the same with previous
        # Case 2: Different from previous
        if s[j] == previousChar:
            count += 1
        else:
            print(str(count) + " " + previousChar + " ", end="")
            count = 1
        previousChar = s[j]
    print(str(count) + " " + previousChar, end="")
    print()







