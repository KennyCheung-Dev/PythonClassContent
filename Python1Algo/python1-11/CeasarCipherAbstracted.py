# 得到需要的资料
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# print('''
# Would you like to Encode or Decode?
# Encode: 1
# Decode: 0
# ''')
#
# while True:
#     try:
#         ende = int(input())
#         if ende == 1 or ende == 0:
#             break
#         else:
#             print("Please enter 0 or 1")
#     except:
#         print("Please enter valid number")
#
# print("Please enter a key")
# while True:
#     try:
#         key = int(input())
#         #数据没问题
#         #打破loop 继续运行项目
#         break
#     except:
#         #数据出错
#         print("Please enter a valid number")
#
# msg = input("Please enter your message")
# result = ''
#
# # 加密 （msg， key）
# for i in range(len(msg)):
#     #记录下来 是不是大写 K   # NEW
#     isUpper = False           # NEW   用来记录的变量
#     if msg[i].isupper():      # NEW   if句子 问 是不是大写
#         isUpper = True        # NEW   如果是大写 把变量改为True
#     # 一律改为小写 k
#     character = str.lower(msg[i])       # NEW    一律改为小写
#
#     # 测试 字节 是不是 英文字母
#     if character in alphabet:
#         pass
#     else:
#         # 把字节保持现况加到result里面
#         result += msg[i]
#         continue
#
#     oldPos = alphabet.find(character)  # = 0   # NEW-Change   把之前msg[i] 换成 小写的character
#
#     # Encode = 1, Decode = 0
#     if ende == 1:
#         newPos = oldPos + key
#     elif ende == 0:
#         newPos = oldPos - key
#
#     newMsg = alphabet[newPos % 26]
#     #如果是大写的话，变为大写 K
#     if isUpper:                          # NEW  翻查之前记录 如果是大写
#         newMsg = str.upper(newMsg)       # NEW  如果是大写 把加密好的信息变为 大写
#     result += newMsg
#
# # 输出
# print(result)






















# Functions that can be separated as separate features:

# Gather input, check if valid

# Encode/Decode in one function
def AskForKey():
    print("Please enter a key")
    while True:
        try:
            return int(input())
            # 数据没问题
            # 打破loop 继续运行项目
        except:
            # 数据出错
            print("Please enter a valid number")

def AskForMsg():
    return(input("Please enter your message"))

# Return True if Encode, False if Decode
def AskCipherMode():
    print('''
    Would you like to Encode or Decode?
    Encode: 1
    Decode: 0
    ''')
    while True:
        try:
            ende = int(input())
            if ende == 1:
                return True
            if ende == 0:
                return False
            else:
                print("Please enter 0 or 1")
        except:
            print("Please enter valid number")

def CaesarCipher(msg, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    # 加密 （msg， key）
    for i in range(len(msg)):
        # 记录下来 是不是大写 K   # NEW
        isUpper = False  # NEW   用来记录的变量
        if msg[i].isupper():  # NEW   if句子 问 是不是大写
            isUpper = True  # NEW   如果是大写 把变量改为True
        # 一律改为小写 k
        character = str.lower(msg[i])  # NEW    一律改为小写

        # 测试 字节 是不是 英文字母
        if character in alphabet:
            pass
        else:
            # 把字节保持现况加到result里面
            result += msg[i]
            continue

        oldPos = alphabet.find(character)  # = 0   # NEW-Change   把之前msg[i] 换成 小写的character

        # Encode = True, Decode = False
        if mode == True:
            newPos = oldPos + key
        elif mode == False:
            newPos = oldPos - key

        newMsg = alphabet[newPos % 26]

        # 如果是大写的话，变为大写 K
        if isUpper:  # NEW  翻查之前记录 如果是大写
            newMsg = str.upper(newMsg)  # NEW  如果是大写 把加密好的信息变为 大写
        result += newMsg

    # 输出
    return result


# Abstracted eUser Experience:

#(Optional)
# To Ask for encode or decode clearly
mode = AskCipherMode()

msg = AskForMsg()
key = AskForKey()

print(CaesarCipher(msg, key, mode))










msg = ""

key = 0

def UserInput():
    #问问题
    # input 放到变量
    global msg
    global key
    msg = input()
    key = int(input())


def Encode(msg, key, mode):
    #slfjalsejfa
    pass









