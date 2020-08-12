'''
作业：
["Red", "Green", "Blue", "White", "Black", "Rainbow"]
把上述词汇里面的 韵母(aeiou) 全部换成"o"
Red -> Rod
Green -> Groon
Blue -> Bloo
White -> Whoto
Black -> Block
Rainbow -> Roonbow

解题阶段：
第一： 先成功把一个文字的韵母换掉
第二： 用循环 把上述的字 用同样的逻辑 换掉
第三： 输出结果
'''

#提示 需要创建一个新的文字变量
# abcde
# 新的字 obcdo

# Approach 1

# # Create list of colors
# colors = ["Red", "Green", "Blue", "White", "Black", "Rainbow"]
# # List of vowels as reference
# vowels = ['a', 'e', 'i', 'o', 'u']
# # New List that will contain the result
# newColors = []
#
# # Loop through all old colors
# for color in colors:
#     # Create a new string to hold the new single color result
#     newColor = ""
#     # Loop through every letter in the old single color
#     for letter in color:
#         # Create a variable to keep track of whether the character is uppercase or lowercase
#         upper = False
#         # Apply status to upper, to keep track
#         if letter.isupper():
#             upper = True
#         # Make every character lowercase to  process
#         tempLetter = letter.lower()
#         # Swap the letter if it is a vowel
#         if tempLetter in vowels:
#             tempLetter = "o"
#         # Turn the letter back to upper case if it was one
#         if upper:
#             tempLetter = tempLetter.upper()
#         # Add the resulting letter to our new single Color
#         newColor += tempLetter
#     # After the letters are finished looping, add the new single Color into new List of colors
#     newColors.append(newColor)
# # Finally, print the new list
# print(newColors)


# Approach 2:

# Create list of colors
colors = ["Red", "Green", "Blue", "White", "Black", "Rainbow"]
# Lists of vowels as reference
lowerVowels = ['a', 'e', 'i', 'o', 'u']
upperVowels = ['A', 'E', 'I', 'O', 'U']
# New List that will contain the result
newColors = []

# Loop through all old colors
for color in colors:
    # Create a new string to hold the new single color result
    newColor = ""
    # Loop through every letter in the old single color
    for letter in color:
        # Swap the letter if it is a vowel
        if letter in lowerVowels:
            letter = "o"
        if letter in upperVowels:
            letter = "O"
        # Add the resulting letter to our new single Color
        newColor += letter
    # After the letters are finished looping, add the new single Color into new List of colors
    newColors.append(newColor)
# Finally, print the new list
print(newColors)

# 8 lines less



