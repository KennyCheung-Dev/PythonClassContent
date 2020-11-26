
import random
timesplayed = int(input())
number = 0
pl1 = 100
pl2 = 100
while number < timesplayed:
    player1 = random.randint(1, 6)
    player2 = random.randint(1, 6)
    if player1 < player2:
        player1 = 100 - player1
    if player2 < player1:
        player2 = 100 - player2

# Things wrong:
# 1. You need to take input from user, instead of randomly generating the numbers
#    You seem to be ignoring the inputs in the next few lines for now

# 2. If player1 lose, player1's score will have to subtract the player2's roll,
#    vice versa

# 3. On the lines that calculates the remaining scores, you are using (100 - playerX)
#    What this will do is reset the score back to 100, then subtract. So you will never
#    get a score under 94 (because the max you can subtract from 100 is 6, no matter
#    how many games you played)

# 4. You seem to be also resetting the scores back to 100, when the two dice roll
#    are equal. In the case of equal, the two players' scores should remain unchanged.

# 5. You don't seem to be outputting the result? with a print()