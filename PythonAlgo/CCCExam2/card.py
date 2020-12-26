n = int(input())

nums = [int(num) for num in input().split(' ')]

ave = 2*sum(nums)/n
vis = [0] * n


for i in range(len(nums)):
	if vis[i] == 0:
		for j in range(i+1,n):
			if vis[j] == 0 and nums[i]+nums[j]==ave:
				print('%d %d'%(i+1,j+1))
				vis[i]=1
				vis[j]=1
				break