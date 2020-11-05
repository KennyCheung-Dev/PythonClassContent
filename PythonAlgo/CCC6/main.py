def PolybiusCipher(s):
    grid = [
        ["n", "a", "1", "c", "3", "h"],
        ["g", "t", "b", "2", "o", "m"],
        ["e", "5", "w", "r", "p", "d"],
        ["4", "f", "6", "g", "7", "i"],
        ["g", "j", "0", "k", "l", "q"],
        ["s", "u", "v", "x", "y", "z"]
    ]
    return "".join([grid[ord(s[i]) - 97][ord(s[i + 1]) - 97] for i in range(0, len(s) - 1, 2)])
print(PolybiusCipher("bcfbfeacbdadafcacafacacedfffffabfa"))