# ATATGTAGCTAGCATAATA

possibleEnds = ['TAA', 'TAG', 'TGA']
line = input()
line = line[line.index("ATG"):]
for i in range(len(line) - 3, 2, -1):
    if line[i:i+3] in possibleEnds:
        if i % 3 == 0:
            print(line[0:i+3])
            break




