# HTML building
# html uses tags to wrap around content
# <h2>Header</h2>
# <p>Paragraph</p>

# Build a function that asks for content then a tag
# Output the string html code

# content = input("Content?")
# tag = input("Tag?")
# def BuildHTML(content, tag):
#     return "<" + tag + ">" + content + "</" + tag + ">"
# print(BuildHTML(content, tag))

#-----------------------------------------------------------------

# Input a string, return "rotated left 2"
# 向左旋转2位
# 头两位字母转移到最后
# Hello -> lloHe
# java -> vaja
# Hii -> iHi
# i -> i

# def RotateLeft2(msg):
#     if len(msg) <= 2:
#         return msg
#     return msg[2:len(msg)] + msg[0:2]
# print(RotateLeft2("Hello World"))

#-----------------------------------------------------------------

# J2 Question 2014
# 投票计算
# 投票input结构：
# 28 (投票总数）
# ABBAABAAAABBABBABBBBBABAAABB
# 程序可能的Output:
# A
# B
# Tie

# def VoteCount(count, votes):
#     A = 0
#     B = 0
#     for i in range(count):
#         for j in votes:
#             if j == "A":
#                 A += 1
#             if j == "B":
#                 B += 1
#     if A > B:
#         return "A"
#     elif B > A:
#         return "B"
#     else:
#         return "Tie"
#
# voteNum = int(input("Number of Votes"))
# votes = (input("Votes?"))
#
# print(VoteCount(voteNum, votes))

#-----------------------------------------------------------------

# J2 Question 2013
# I O S H Z X N 180度旋转还是一样的字母
# 想要用这些字母来做会旋转的霓虹灯
# 函数来检测文字符不符合
# SHINS -> True
# NOISE -> False
# def RotatingLetters(text):
#     good = True
#     for letter in text:
#         if letter not in ["I","O","S","H","Z","X","N","i","o","s","h","z","x","n"]:
#             good = False
#     return good
# print(RotatingLetters("NOISE"))
# print(RotatingLetters("SHINS"))

#-----------------------------------------------------------------

# Cut strings into bits,
# Excluding every third letter
# Hello World -> elo ord
# ^  ^  ^  ^
# Taken Out

# def formIndex(text):
#     return list(range(len(text)))[::3]
#
# def CutString(text):
#     newText = ""
#     indexOut = formIndex(text)
#     for i in range(len(text)):
#         if i not in indexOut:
#             newText += text[i]
#     return newText
#
# print(CutString("Hello World"))

#-----------------------------------------------------------------

# 2015 J3
# 俄罗斯游戏Rovarspraket （robbers Language)
# 每一个声母要进行加密
# 加密：
# 声母自己
# 最近的韵母（如果前后韵母距离一样，用前面的韵母） ex. d -> e, c -> a
# 后面下一个声母， 如果是z 就用z
# joy -> jikoyuz

def Rovarspraket(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    newText = ""
    for letter in text:
        if not letter in vowels:
            newText += letter
            leftDiff = 99  # 26, because if no letter is found
            rightDiff = 99  # then the other one will be comparing to a bigger number
            rightVowel = ""
            leftVowel = ""

            # Right Vowel:
            for i in range(alphabet.index(letter) + 1, 26):
                if alphabet[i] in vowels:
                    rightVowel = alphabet[i]
                    rightDiff = i - alphabet.index(letter)
                    break

            # Left Vowel:
            for j in range(alphabet.index(letter)-1, -1, -1):
                if alphabet[j] in vowels:
                    leftVowel = alphabet[j]
                    leftDiff = alphabet.index(letter) - j
                    break

            #Check For Debug
            # print("Left Index: " + str(leftDiff))
            # print("Right Index: " + str(rightDiff))

            # Apply the result and add the consonant
            if leftDiff <= rightDiff: # left is closer, or same distance
                newText += leftVowel
            elif rightDiff < leftDiff: # right is closer
                newText += rightVowel

            # Closest vowel:
            if not letter == "z":
                for i in range(alphabet.index(letter) + 1, 26):
                    if not alphabet[i] in vowels:
                        newText += alphabet[i]
                        break
            else:
                newText += "z"
        # If the letter is a vowel
        else:
            newText += letter # Add the vowel back
    return newText

print(Rovarspraket("joy"))

#-----------------------------------------------------------------
