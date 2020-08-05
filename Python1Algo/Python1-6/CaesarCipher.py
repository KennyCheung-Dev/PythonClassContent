# 需要什么 去解题
# 1. 知道我们这个信息在英文字母里面的位置  "d位置" = 3
# 2. 钥匙：5   加密： 把位置加上钥匙  "d位置" + 5 = 3 + 5 = 8 = "i位置"
# 3. 把在加密好的位置 的 字母 找出来 然后输出

# encode("Hello", 3)  = "Khoor"
# decode("Khoor", 3)  = "Hello"



# 3  =  d
# print(alphabet[3])
# "a" = 0
# print(alphabet.find('z'))


# 钥匙 = 3
# 信息 = 'a'
# 旧位置 = alphabet.find(信息)  # = 0
# 新位置 = 旧位置 + 钥匙 # = 3
# 加密好的信息 = alphabet[新位置]
#
# print(加密好的信息)

#得到需要的资料
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print("Please enter a key")
while True:
    try:
        key = int(input())
        #数据没问题
        #打破loop 继续运行项目
        break
    except:
        #数据出错
        print("Please enter a valid number")

msg = input("Please enter your message")
result = ''

# 加密 （msg， key）
for i in range(len(msg)):
    #记录下来 是不是大写 K   # NEW
    isUpper = False           # NEW   用来记录的变量
    if msg[i].isupper():      # NEW   if句子 问 是不是大写
        isUpper = True        # NEW   如果是大写 把变量改为True
    # 一律改为小写 k
    character = str.lower(msg[i])       # NEW    一律改为小写

    # 测试 字节 是不是 英文字母
    if character in alphabet:
        pass
    else:
        # 把字节保持现况加到result里面
        result += msg[i]
        continue

    oldPos = alphabet.find(character)  # = 0   # NEW-Change   把之前msg[i] 换成 小写的character
    newPos = oldPos + key # = 3
    newMsg = alphabet[newPos % 26]
    #如果是大写的话，变为大写 K
    if isUpper:                          # NEW  翻查之前记录 如果是大写
        newMsg = str.upper(newMsg)       # NEW  如果是大写 把加密好的信息变为 大写
    result += newMsg

# 输出
print(result)

# 0 % 5 = 0
# 1 % 5 = 1
# 2 % 5 = 2
# 3 % 5 = 3
# 4 % 5 = 4
# 5 % 5 = 0
# 6 % 5 = 1
# 7 % 5 = 2
# 8 % 5 = 3
# 9 % 5 = 4
# 10 % 5 = 0
# 1001 % 5 = 1

# 旧作业：
# 用input 问用户 拿到msg 跟 key  （现在只需要handle一个文字，空格符号下节课继续）
# 如果用户填写msg 跟 key 不符合要求格式 比如在key写下英文字母
# 请无限循环 让用户重试

# 新作业：
# 在问key跟msg 之前 问：请问你想 加密 还是 解密
# 根据回答 加密或解密
# Input:  加密，  3   Hello    Output： Khoor
# Input:  解密，  3   Khoor    Output: Hello

#不用处理的难点：
# newPos = oldPos - key 难点： 如果key大于等于26， 我们会得到 -27 或以下的newPos
# Assume假设 key不大于25




