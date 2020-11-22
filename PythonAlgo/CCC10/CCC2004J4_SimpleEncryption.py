import re

def SimpleEncryption(key, content):
    content = StripSymbols(content)
    #Put content into storage
    storage = []
    for i in range(len(key)):
        storage.append([])
    for i in range(len(content)):
        column = i % len(key)
        storage[column].append(content[i])
    #Encrypt Message
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            storage[i][j] = PositionToString(
                (StringToPosition(storage[i][j]) + StringToPosition(key[i]))
                % 26
            )
    # Construct new string
    result = ""
    for i in range(len(content)):
        result += storage[i % len(key)].pop(0)
    return result
def StripSymbols(content):
    return re.sub(r'[^\w]', '', content)

def PositionToString(i):
    return chr(i + 65)

def StringToPosition(c):
    return ord(c) - 65

print(SimpleEncryption(input(), input()))