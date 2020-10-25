def Rovarspraket(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    newText = ""
    for letter in text:
        if letter not in vowels:
            # Add the letter back into the result
            newText += letter

            # Determine what are the two closest vowels
            # and their distances
            leftDiff = 99
            rightDiff = 99
            leftVowel = ""
            rightVowel = ""

            # Right Side Vowel
            for i in range(alphabet.index(letter) + 1, 26, 1):
                if alphabet[i] in vowels:
                    rightVowel = alphabet[i]
                    rightDiff = i - alphabet.index(letter)
                    break

            # Left Side Vowel
            for i in range(alphabet.index(letter) - 1, -1, -1):
                if alphabet[i] in vowels:
                    leftVowel = alphabet[i]
                    leftDiff = alphabet.index(letter) - i
                    break

            # Check which one is closer and apply
            if leftDiff <= rightDiff:
                newText += leftVowel
            else:
                newText += rightVowel


            # Add the next closest consonant
            if letter != "z":
                for i in range(alphabet.index(letter) + 1, 26, 1):
                    if alphabet[i] not in vowels:
                        newText += alphabet[i]
                        break
            else:
                newText += "z"
        else:
            newText += letter


    return newText

print(Rovarspraket("ham"))
