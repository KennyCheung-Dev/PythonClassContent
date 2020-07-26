# 需要什么 去解题
# 1. 知道我们这个信息在英文字母里面的位置  "d位置" = 3
# 2. 钥匙：5   加密： 把位置加上钥匙  "d位置" + 5 = 3 + 5 = 8 = "i位置"
# 3. 把在加密好的位置 的 字母 找出来 然后输出

# encode("Hello", 3)  = "Khoor"
# decode("Khoor", 3)  = "Hello"

alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
key = 3
msg = 'hello'
result = ''

# 加密 （msg， key）
for i in range(len(msg)):
    oldPos = alphabet.find(msg[i])  # = 0
    newPos = oldPos + key # = 3
    newMsg = alphabet[newPos % 26]
    result += newMsg

# 输出
print(result)

# 作业：
# 用input 问用户 拿到msg 跟 key  （现在只需要handle一个文字，空格符号下节课继续）
# 如果用户填写msg 跟 key 不符合要求格式 比如在key写下英文字母
# 请无限循环 让用户重试

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




