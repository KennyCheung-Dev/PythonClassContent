# Use Recursion, turn decimal numbers into Octal

def DecToOctRecur(quotient, result):
    if quotient < 8:
        return quotient
    if quotient >= 8:
        newQuotient = quotient // 8
        newRemainder = quotient % 8
        result += str(DecToOctRecur(newQuotient, result))
        result += str(newRemainder)
        return result
print(DecToOctRecur(int(input()), ""))