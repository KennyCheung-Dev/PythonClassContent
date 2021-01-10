dividend = int(input())
divisor = int(input())
quotient = int(dividend / divisor)
remainder = dividend - quotient * divisor
if remainder != 0:
    for i in range(remainder, 1, -1):
        if remainder % i == 0 and divisor % i == 0:
            remainder = int(remainder / i)
            divisor = int(divisor / i)
            break
if quotient == 0:
    print(0 if remainder == 0 else str(remainder) + "/" + str(divisor))
else:
    print(quotient if remainder == 0 else str(quotient) + " " + str(remainder) + "/" + str(divisor))