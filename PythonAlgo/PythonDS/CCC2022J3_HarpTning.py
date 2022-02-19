'''

Sample Input 1
AFB+8HC-4

Output for Sample Input 1
AFB tighten 8
HC loosen 4

Explanation of Sample Output 1
The input contains two tuning instructions: AFB+8 and HC-4.


Sample Input 2
AFB+8SC-4H-2GDPE+9

Output for Sample Input 2
AFB tighten 8
SC loosen 4
H loosen 2
GDPE tighten 9

Explanation of Sample Output 2
The input contains four tuning instructions: AFB+8, SC-4, H-2, and GDPE+9.

'''

line = input()
strings = ""
adjustment = []
lastCharacter = ""
tighten = True
for i in range(len(line)):
    if line[i].isalpha():
        strings += line[i]
    elif line[i].isdigit():
        adjustment.append(line[i])
    elif line[i] == "+":
        tighten = True
    elif line[i] == "-":
        tighten = False
    lastCharacter = line[i]
    #Ending a command
    if i == len(line) - 1 or (line[i].isdigit() and line[i+1].isalpha()):
        print(strings + " " + ("tighten" if tighten else "loosen") + " " + "".join(adjustment))
        strings = ""
        adjustment = []


