'''

http://www.usaco.org/index.php?page=viewproblem2&cpid=691

You have probably heard of the game "Rock, Paper, Scissors". The cows like to play a similar game they call "Hoof, Paper, Scissors".
The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each-other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. Hoof beats scissors (since a hoof can smash a pair of scissors), scissors beats paper (since scissors can cut paper), and paper beats hoof (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.

Farmer John wants to play against his prize cow, Bessie, at N games of "Hoof, Paper, Scissors" (1≤N≤100,000). Bessie, being an expert at the game, can predict each of FJ's gestures before he makes it. Unfortunately, Bessie, being a cow, is also very lazy. As a result, she tends to play the same gesture multiple times in a row. In fact, she is only willing to switch gestures at most once over the entire set of games. For example, she might play "hoof" for the first x games, then switch to "paper" for the remaining N−x games.

Given the sequence of gestures FJ will be playing, please determine the maximum number of games that Bessie can win.

INPUT FORMAT (file hps.in):
The first line of the input file contains N.
The remaining N lines contains FJ's gestures, each either H, P, or S.

OUTPUT FORMAT (file hps.out):
Print the maximum number of games Bessie can win, given that she can only change gestures at most once.
SAMPLE INPUT:
5
P
P
H
P
S
SAMPLE OUTPUT:
4
Problem credits: Mark Chen and Brian Dean

'''

n = int(input())

prefix = [[0, 0, 0]] # H P S

for i in range(n):
    tempPrefixEntry = prefix[-1].copy()
    gesture = input()
    if gesture == "H":
        tempPrefixEntry[0] += 1
    elif gesture == "P":
        tempPrefixEntry[1] += 1
    elif gesture == "S":
        tempPrefixEntry[2] += 1
    prefix.append(tempPrefixEntry)

highestWins = -1
for i in range(n + 1):
    beforeChangeWins = max(prefix[i][0], max(prefix[i][1], prefix[i][2]))
    afterChangeWins = max(prefix[n][0] - prefix[i][0], max(prefix[n][1] - prefix[i][1], prefix[n][2] - prefix[i][2]))
    combinedWins = beforeChangeWins + afterChangeWins
    highestWins = max(highestWins, combinedWins)
print(highestWins)


