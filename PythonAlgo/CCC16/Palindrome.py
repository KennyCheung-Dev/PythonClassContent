# abcba

#Check if a string is a palindrome with recursion

# abcba
# ^   ^

# bcb
# ^ ^

# c
# ^

# abba
# bb

# RecursivePalindrome:
# Case 1: If the substring has 0 or 1 length
# Case 2: If the substrings head and tail matches
# Case 3: If the substrings head and tail doens't match

def isPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[-1] == s[0]:
        return isPalindrome(s[1:-1])
    else:
        return False

print(isPalindrome("AbcBA"))



