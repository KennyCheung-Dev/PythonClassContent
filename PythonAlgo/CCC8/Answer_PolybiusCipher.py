def PolybiusCipher(s):
    grid = [
        ["n", "a", "l", "c", "3", "h"],
        ["g", "t", "b", "2", "o", "m"],
        ["e", "5", "w", "r", "p", "d"],
        ["4", "f", "6", "g", "7", "i"],
        ["g", "j", "0", "k", "l", "q"],
        ["s", "u", "v", "x", "y", "z"]
    ]
    result = ""
    for i in range(0, len(s)-1, 2):
        result += grid[ord(s.lower()[i])-97][ord(s.lower()[i+1])-97]
    return result
print(PolybiusCipher("bcfbfeacbdadafcacafacacedfffffabfa"))

