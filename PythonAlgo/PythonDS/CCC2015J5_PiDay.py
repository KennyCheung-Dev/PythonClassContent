pieces = int(input())
person = int(input())

def RecurPie(piecesStarting, piecesTaken, depth, sequence):
    global person
    global pieces
    newSequence = sequence.copy()
    newSequence.append(piecesStarting)

    if depth < person - 1:
        piecesRemaining = pieces - piecesTaken - 1
        personRemaining = person - depth - 1
        maxPossiblePiecesToStart = int(piecesRemaining / personRemaining) + 1
        subSequentCount = 0
        for i in range(piecesStarting, maxPossiblePiecesToStart):
            result = RecurPie(i, piecesTaken + i, depth + 1, newSequence)
            if result != None:
                subSequentCount += RecurPie(i, piecesTaken + i, depth + 1, newSequence)
        return subSequentCount
    elif depth == person - 1:
        if sum(newSequence) == pieces:
            return 1

#Figure out max possible starting piece:
maxStartPiece = int(pieces / person) + 1

totalCount = 0
for i in range(1, maxStartPiece):
    result = RecurPie(i, 0, 0, [])
    if result != None:
        totalCount += RecurPie(i, 0, 0, [])

print(totalCount)
