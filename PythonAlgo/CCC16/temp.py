def IsPalindrome(s):
    IsPalindrome(s[1:-1])
    pass

# Case 1 : Matching head and tail
# What we do: Carry on to an inner layer with a shortened word
# Case 2 : Head and Tail does not match
# What we do: Stop the recursive function and return false
# Case 3 : When the string has 1 or 0 length
# What we do : return true!


# if len(s) == 1 or len(s) == 0:

# racecar s[1:-1]  aceca
# if s[0] == s[-1]
#