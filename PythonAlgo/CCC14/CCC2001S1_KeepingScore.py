totalPoint = 0
cardCount = 0
currentSuit = ""
currentHand = []
currentPoint = 0
lineLen = 31

s = input()

#First Line
print("Cards Dealt              Points")
#Set Starting Suit
if s[0] == "C":
    currentSuit = "Clubs"
if s[0] == "D":
    currentSuit = "Diamonds"
if s[0] == "H":
    currentSuit = "Hearts"
if s[0] == "S":
    currentSuit = "Spades"

# Loop through the line
for i in range(1, len(s)):
    currentChar = s[i]
    # Accumulate hands
    if not currentChar == "C" and \
        not currentChar == "D" and\
        not currentChar == "H" and\
        not currentChar == "S":
        currentHand.append(currentChar)
        cardCount += 1
        if currentChar == "A":
            currentPoint += 4
        elif currentChar == "K":
            currentPoint += 3
        elif currentChar == "Q":
            currentPoint += 2
        elif currentChar == "J":
            currentPoint += 1

    # Handling Ending of a Sequence
    if currentChar == "C" or\
        currentChar == "D" or \
        currentChar == "H" or \
        currentChar == "S" or \
        i == len(s) - 1:

        # Calculating suit combo points
        if len(currentHand) == 0:
            currentPoint += 3
        if len(currentHand) == 1:
            currentPoint += 2
        if len(currentHand) == 2:
            currentPoint += 1

        # Print the result line
        print(currentSuit + " ", end="")
        for j in range(len(currentHand)):
            print(currentHand[j] + " ", end="")
        pointDigit = len(str(currentPoint))
        spaceNeeded = lineLen - len(currentSuit) - 1 - len(currentHand) * 2 - len(str(currentPoint))
        for j in range(spaceNeeded):
            print(" ", end="")
        print(currentPoint)
        totalPoint += currentPoint

        # Resetting data
        if currentChar == "C":
            currentSuit = "Clubs"
        if currentChar == "D":
            currentSuit = "Diamonds"
        if currentChar == "H":
            currentSuit = "Hearts"
        if currentChar == "S":
            currentSuit = "Spades"
        cardCount = 0
        currentHand.clear()
        currentPoint = 0
# Print total points
spaceNeeded = lineLen - len("Total ") - len(str(totalPoint))
for i in range(spaceNeeded):
    print(" ", end="")
print("Total " + str(totalPoint))