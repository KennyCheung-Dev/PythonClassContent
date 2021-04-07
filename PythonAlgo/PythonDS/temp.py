

def DecToOctRecur(num):
    if num / 8 == 0:
        return num % 8
    return str(DecToOctRecur(int(num / 8))) + str(num % 8)

print(DecToOctRecur(int(input()))[1:])