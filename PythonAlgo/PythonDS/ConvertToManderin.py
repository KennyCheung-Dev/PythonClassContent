nums = {
    '0' : "ling",
    '1': "yi",
    '2' : "er",
    '3' : "san",
    '4' : "si",
    '5' : "wu",
    '6' : "liu",
    '7' : "qi",
    '8' : "ba",
    '9' : "jiu",
    '10' : "shi"
}

def convert_to_manderin(num):
    if 0 <= num <= 10:
        return nums[str(num)]
    elif 11 <= num <= 19:
        return nums['10'] + " " + nums[int(str(num)[1])]
    else:
        return \
            (nums[str(num)[0]] if str(num)[0] != '0' else "") + \
            " " + nums['10'] + " " + \
            (nums[str(num)[1]] if str(num)[1] != '0' else "")

print(convert_to_manderin(int(input())))