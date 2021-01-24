'''

Scanner sc = new Scanner(System.in);
int low = sc.nextInt();
int high = sc.nextInt();
int cool = 0;

for (int i = low; i <= high; i++)
    if (Math.sqrt(i) % 1 == 0)
        if (Math.cbrt(i) % 1 == 0)
            cool++;

System.out.println(cool);

'''

import math

def IsCubeRoot(x):
    for i in range(round(x**(1./3.)) + 1):
        if i ** 3 == x:
            return True
    return False


low = int(input())
high = int(input())
cool = 0
for i in range(low, high+1):
    if IsCubeRoot(i):
        if math.sqrt(i).is_integer():
            cool += 1
print(cool)

# print(64**(1./3))