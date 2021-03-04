s = input()
l = list(s)
l.sort()
fix_s = "".join(l)

l1,l2,m1,m2,s1,s2 = 0,0,0,0,0,0

for i in range(len(s)):
    if fix_s[i] == 'L':
        if s[i] == 'M':
            l1 += 1
        if s[i] == 'S':
            l2 += 1
    if fix_s[i] == 'M':
        if s[i] == 'L':
            m1 += 1
        if s[i] == 'S':
            m2 += 1
    if fix_s[i] == 'S':
        if s[i] == 'L':
            s1 += 1
        if s[i] == 'M':
            s2 += 1

#print(l1,l2,m1,m2,s1,s2)
print(s1+m1+min(m2,s2)+abs(s1-l2))
