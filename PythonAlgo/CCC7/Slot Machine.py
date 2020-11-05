# jar, x, y, z = map(int, input().split())
# def play(jar, x, y, z, cnt):
#     if jar<=0:return(cnt)
#     else:
#         if x%35==0:jar+=30
#         if y%100==0:jar+=60
#         if z%10==0:jar+=9
#         print("1 " +  str(x) + " 2 " +  str(y) + " 3 " +  str(z) + " jar " + str(jar))
#         return play(jar-23, x+1, y+1, z+1,cnt+1)
# print(play(jar, x, y, z, cnt=0))

originalcoinsinmachine1 = int(input())
originalcoinsinmachine2 = int(input())
originalcoinsinmachine3 = int(input())
Machine1 = int(input("amount of coins used on machine 1"))
coinsreturned = (originalcoinsinmachine1 + Machine1) / 35 * 30
print(coinsreturned)

Machine2 = int(input("amount of coins used on machine 2"))
coinsreturned2 = (originalcoinsinmachine2 + Machine2) / 100 * 60
print(coinsreturned2)
Machine3 = int(input("amount of coins used on machine 3"))
coinsreturned3 = (originalcoinsinmachine3 +Machine3) / 10 * 9
print(coinsreturned3)