pieces = int(input())
person = int(input())
visited = {}

def RecurPie(piecesStarting, piecesTaken, depth, sequence):
    global person
    global pieces
    newSequence = sequence.copy()
    newSequence.append(piecesStarting)

    if depth < person - 1:
        piecesRemaining = pieces - piecesTaken
        personRemaining = person - depth - 1
        maxPossiblePiecesToStart = int(piecesRemaining / personRemaining) + 1
        if (piecesStarting, piecesTaken, depth) in visited:
            return visited[(piecesStarting, piecesTaken, depth)]
        subSequentCount = 0
        for i in range(piecesStarting, maxPossiblePiecesToStart):
            result = RecurPie(i, piecesTaken + i, depth + 1, newSequence)
            if result != None:
                subSequentCount += result
        visited[(piecesStarting, piecesTaken, depth)] = subSequentCount
        return subSequentCount
    elif depth == person - 1:
        if sum(newSequence) == pieces:
            # print(newSequence)
            visited[(piecesStarting, piecesTaken, depth)] = 1
            return visited[(piecesStarting, piecesTaken, depth)]

#Figure out max possible starting piece:
maxStartPiece = int(pieces / person) + 1

totalCount = 0
for i in range(1, maxStartPiece):
    visited = {}
    result = RecurPie(i, 0, 0, [])
    if result != None:
        totalCount += RecurPie(i, 0, 0, [])
# totalCount = RecurPie(2, 0, 0, [])

print(totalCount)