# HTML building
# html 用tags 把内容包起来
# 像这样 <h3>MyWebsite</h3>  <- lvl2 标题
# <p>This is a paragraph hi.</p>

# 函数
# 用户输入 内容 跟 tag
# 输出 html 代码
# 输入： "This is my paragraph|a"
# 输出： "<a>This is my paragraph</a>"

def HTMLBuilder(text):
    content, tag = text.split("|")
    return "<" + tag + ">" + content + "</" + tag + ">"

print(HTMLBuilder("Hello World Hello Good Night!|div"))

# 1) 把内容跟tag分开 （python把文字分开 的技巧）
# 2）把拿到的内容拼凑起来成为输出的样子 +

# ------------------------------------------------------------------------------------

# 往左循环2次
# Rotate Left 2
# 提供一个信息
# 输出 往左循环了两个字节的信息
# Hello -> lloHe
# java -> vaja
# Hii -> iHi
# i -> i
# HelloWorld ->  lloWorldHe
# str = "HelloWorld"
# print(str[6:])
# print(str[:4])
# def RotateLeft2(msg):
#     return msg[2:]+msg[:2]
#
# print(RotateLeft2("HelloWorld"))

# ------------------------------------------------------------------------------------

# J2 Question 2014
# 投票计算
# 5
# ABBAB
# 程序的可能结果有： A / B / Tie

# def VoteCount(count, votes):
#     num1 = 0
#     num2 = 0
#     for letter in votes:
#         if letter == "A":
#             num1 += 1
#         if letter == "B":
#             num2 += 1
#     if num1 > num2:
#         return "A"
#     elif num2 > num1:
#         return "B"
#     else:
#         return "Tie"
#
# print(VoteCount(10, "ABAABBBBAA"))

# ------------------------------------------------------------------------------------

# J2 Question 2013
# I O S H Z X N  180旋转之后 还是一样的字母
# 想用这些文字来做霓虹灯
# 写一个函数 来检测 文字符不符合
# return True / False

# Samples: SHINS -> True
# Samples: NOISE -> False
# Samples: SOS -> True
# letters = ["I", "O", "S", "H", "Z", "X", "N"]
# def RotatingLetters(text):
#     for i in range(len(text)):
#         if not text[i] in letters:
#             return False
#     return True

# letters = ["I", "O", "S", "H", "Z", "X", "N"]
# def RotatingLetters(text):
#     allCorrect = True
#     for i in range(len(text)):
#         if not text[i] in letters:
#             allCorrect = False
#     if allCorrect:
#         return True
#     else:
#         return False
#
# print(RotatingLetters("SHINS"))

# ------------------------------------------------------------------------------------------------

# Cut Strings into Bits
# 我们想把文字里 每第三个字 删除
# Hello World Kenny
# ^  ^  ^  ^  ^  ^
# elo ord eny



# def FormIndex(text): # 拿到想删除的数字 的位置
#     return list(range(len(text))[::3])  # [0, 1, 2, 3, 4, 5, 6, 7]
#
# def CutString(text):
#     newText = ""
#     removingIndex = FormIndex(text)
#     for i in range(len(text)):
#         if not i in removingIndex: #如果不在要删除的index里面
#             newText += text[i]
#     return newText
#
# print(CutString("Hello World Kenny"))

# def CutString(text):
#     newText = ""
#     for i in range(len(text)):
#         if i % 3 != 0:
#             newText += text[i]
#     return newText
#
# print(CutString("Hello World Kenny"))

# x % 26
# 0 % 3 = 0
# 1 % 3 = 1
# 2 % 3 = 2
# 3 % 3 = 0
# 4 % 3 = 1
# 0
# 1
# 2
# 0
# 1
# 2
# 0
# 1
# 2
# 0



# -----------

# CCC 2015 J3

# 俄罗斯游戏 Rovarspraket (robbers languages)
# 每一个声母 都要加密
# 加密：
# 其中的每一个声母后续都要加上两个新的字母
# 1）离这个 声母 最近的 韵母 d -> e   如果有两边韵母距离一样的情况 取前面的韵母 c -> a
# 2) 后面下一个声母 如果是z 就用z
# 韵母就照原本样子
# 韵母 [a, e, i, o, u]
# joy -> jikoyuz

    # 循环每一个字母
    # 测试 这个是声母还是韵母
    # 如果是声母：
    #     把声母自己 加进新的变量
    #      找到前面跟后面最近的韵母 （用 alphabet.index(字母)， alphabet[i]) if 字母 in vowels:
    #       比较前后两边韵母的距离
    #       把 距离较小的 韵母 加进 新变量
    #        找到后面最近的声母 （先检查是不是z，如果是z就直接用z）， 把最近的声母加进新变量
    # 如果是韵母：
    #     把韵母加进去新变量 完了
    #     跳到 下一轮 循环

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

            # Apply the result and add the consonant
            if leftDiff <= rightDiff: # left is closer, or same distance
                newText += leftVowel
            elif rightDiff < leftDiff: # right is closer
                newText += rightVowel

            # Closest Consonant:
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

print(Rovarspraket("yuzuzuz"))

#-----------------------------------------------------------------

# 作业

# 返回列表所有值的和
# 如果列表是空的 返回0
# 数字13 为特别的，13本身和13后面的数字 不加进和
# sum13([1, 2, 2, 1])  -> 6
# sum13([1, 2, 2, 1, 13]) -> 6
# sum13([1, 2, 2, 1, 13, 2]) -> 6
# sum13([1, 2, 2, 1, 13, 2, 1]) -> 7
# sum13([1, 2, 2, 1, 13, 13, 2, 6]) -> 12

def sum13(li):
    pass

#-----------------------------------------------------------------




