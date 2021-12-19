"""
ID: kennych3
LANG: PYTHON3
PROG: ride
"""
letters = {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26
}
# comet = input()
# group = input()
fin = open("ride.in", "r")
fout = open("ride.out", "w")
comet = fin.readline()
group = fin.readline()
cometNum = 1
groupNum = 1

for letter in comet:
    if letter == '\n':
        continue
    cometNum *= letters[letter]
for letter in group:
    if letter == '\n':
        continue
    groupNum *= letters[letter]
if cometNum % 47 == groupNum % 47:
    fout.write("GO\n")
else:
    fout.write("STAY\n")
