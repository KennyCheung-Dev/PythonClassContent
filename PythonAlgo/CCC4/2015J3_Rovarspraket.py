def Rovarspraket(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    newText = ""
    for letter in text:
        if not letter in vowels:
            newText += letter
            leftDiff = 99  # 26, because if no letter is found
            rightDiff = 99  # then the other one will be comparing to a bigger number
            rightVowel = ""
            leftVowel = ""

            # Right Vowel:
            for i in range(alphabet.index(letter) + 1, 26):
                if alphabet[i] in vowels:
                    rightVowel = alphabet[i]
                    rightDiff = i - alphabet.index(letter)
                    break

            # Left Vowel:
            for j in range(alphabet.index(letter)-1, -1, -1):
                if alphabet[j] in vowels:
                    leftVowel = alphabet[j]
                    leftDiff = alphabet.index(letter) - j
                    break

            # Apply the result and add the consonant
            if leftDiff <= rightDiff: # left is closer, or same distance
                newText += leftVowel
            elif rightDiff < leftDiff: # right is closer
                newText += rightVowel

            # Closest Consonant:
            if not letter == "z":
                for i in range(alphabet.index(letter) + 1, 26):
                    if not alphabet[i] in vowels:
                        newText += alphabet[i]
                        break
            else:
                newText += "z"
        # If the letter is a vowel
        else:
            newText += letter # Add the vowel back
    return newText

print(Rovarspraket("yuzuzuz"))