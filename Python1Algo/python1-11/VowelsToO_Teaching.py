# 作业 把剩下的功能 放到一个独立函数里  产出同样的结果
# isVowels() 问是不是韵母  - 已完成
# TurnVowelsToConsonants(colorList):  colorList = 我们颜色列表   - 需要完成
# 得到返回的结构是 - 一个列表 里面有颜色 ["Rod", "Groon", ... ]

# 提示 要把 把isVowels（） 用在TurnVowelsToConsnants（）里面 呼叫

# 最终input ：
# colorList = ["Red", "Green"]
# print(TurnVowelsToCosonants(colorList))

# 控制台输出： ["Rod", "Groon"]

# Create list of colors
colors = ["Red", "Green", "Blue", "White", "Black", "Rainbow"]

# 输入： 1个字母    输出： True / False
def isVowels(s):
    # Lists of vowels as reference
    lowerVowels = ['a', 'e', 'i', 'o', 'u']
    upperVowels = ['A', 'E', 'I', 'O', 'U']
    if s in lowerVowels:
        return True
    if s in upperVowels:
        return True
    return False

def ChangeVowelsToO(tempList):
    # New List that will contain the result
    newColors = []
    # Loop through all old colors
    for color in tempList:
        # Create a new string to hold the new single color result
        newColor = ""
        # Loop through every letter in the old single color
        for letter in color:
            if isVowels(letter):
                if letter.isupper():
                    letter = "O"
                else:
                    letter = "o"
            # Add the resulting letter to our new single Color
            newColor += letter
        # After the letters are finished looping, add the new single Color into new List of colors
        newColors.append(newColor)
    # Finally, print the new list
    return newColors

sampleColor = ["Red", "Green"]
print( ChangeVowelsToO(sampleColor) )






