# Use Recursion, output a reverse version of input

def ReverseRecur(num, result):
    if num < 10:
        result += str(num)
        return result
    else:
        result += ReverseRecur(int(str(num)[1:]), result)
        result += str(num)[0]
        return result

print(ReverseRecur(int(input()), ""))