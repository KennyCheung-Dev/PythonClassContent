def FindNucleotides(s):
    for i in range(len(s) - 3):
        if s[i:i+3] == "ATG":
            for j in range(len(s) - 3, -1, -1):
                if s[j:j + 3] == "TAA" or s[j:j + 3] == "TAG" or s[j:j + 3] == "TGA" and (j - i) % 3 == 0 :
                    return s[i:j+3]

print(FindNucleotides("ATATGTAGCTAGCATAATA"))
print(FindNucleotides("AAAAAATTTTTTGGGGTTGGGGAAATTAAAAATGTAG"))


# FindNucleotides("ATATGTAGCTAGCATAATA")