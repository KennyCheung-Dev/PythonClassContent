alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

# Loop through all the input letters
for letter in input():
    print(letter)

# Temp
letter = "g"

# check if vowels or consonant
if letter in vowels:
    print("It is a vowel")
if letter not in vowels:
    print("It is not a vowel")

# Add new character onto result
finalResult = ""
finalResult += letter

# Get the position of your character in the alphabet
print(alphabet.index("g"))   # (put in your letter)

# looking for a vowel from c
# right side
for i in range(alphabet.index(letter) + 1, len(alphabet), 1):
    if alphabet[i] in vowels:
        print("You found it!")
        print("right vowel:" + alphabet[i])
        print("Distance from your current letter :" + str(i - alphabet.index(letter)))

# left side
# loop through letters within the alphabet
for i in range(alphabet.index(letter) - 1, -1, -1):
    # check if the character is a vowel
    if alphabet[i] in vowels:
        # if it is, do something
        print("You found it again!")
        print("left vowel:" + alphabet[i])
        print("Distance from your current letter :" + str(alphabet.index(letter)) - i)

# Compare the distance and determine which to use
if leftDist < rightDist:
    print("Left side is closer!")
    # Add the left vowel into finalResult
else:
    print("Right side is closer!")
    # Add the right vowel into finalResult





















