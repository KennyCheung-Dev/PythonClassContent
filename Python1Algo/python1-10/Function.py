# # Create list of colors
# colors = ["Red", "Green", "Blue", "White", "Black", "Rainbow"]
# # Lists of vowels as reference
# lowerVowels = ['a', 'e', 'i', 'o', 'u']
# upperVowels = ['A', 'E', 'I', 'O', 'U']
# # New List that will contain the result
# newColors = []
#
# # Loop through all old colors
# for color in colors:
#     # Create a new string to hold the new single color result
#     newColor = ""
#     # Loop through every letter in the old single color
#     for letter in color:
#         # Swap the letter if it is a vowel
#         if letter in lowerVowels:
#             letter = "o"
#         if letter in upperVowels:
#             letter = "O"
#         # Add the resulting letter to our new single Color
#         newColor += letter
#     # After the letters are finished looping, add the new single Color into new List of colors
#     newColors.append(newColor)
# # Finally, print the new list
# print(newColors)


# Change of requirements:
# Change this into a software that takes in an entire sentence,
# and change all the vowels

# # Gather input
# sentence = input("Please type a sentence:")
# # Lists of vowels as reference
# lowerVowels = ['a', 'e', 'i', 'o', 'u']
# upperVowels = ['A', 'E', 'I', 'O', 'U']
# # New string that will contain the result
# newSentence = ""
#
# # Loop through all old colors
# for letter in sentence:
#     # Swap the letter if it is a vowel
#     if letter in lowerVowels:
#         letter = "o"
#     if letter in upperVowels:
#         letter = "O"
#     # Add the resulting letter to our new single Color
#     newSentence += letter
# # Finally, print the new list
# print(newSentence)




# Now turn it into functions so the code becomes much clearer
# First,  decide what features can be separated as reusable code
# 1) Gather Input
# 2) Swap Letters
# 3) The entire software as one method with string sentence input

def getInput():
    return input("Please type a sentence:")

def isVowels(s):
    # Lists of vowels as reference
    lowerVowels = ['a', 'e', 'i', 'o', 'u']
    upperVowels = ['A', 'E', 'I', 'O', 'U']
    if s in lowerVowels or s in upperVowels:
        return True
    return False

def TurnSentenceVowelsToO(s):
    # New string that will contain the result
    newSentence = ""
    # Loop through all old colors
    for letter in s:
        # Swap the letter if it is a vowel
        if isVowels(letter):
            if letter.isupper():
                letter = 'O'
            else:
                letter = 'o'
        # Add the resulting letter to our new single Color
        newSentence += letter
    # Finally, print the new list
    return newSentence



# Finally, abstracted user experience:

# Turn all vowels to O
print(TurnSentenceVowelsToO(getInput()))





