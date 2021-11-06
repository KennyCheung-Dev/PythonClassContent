'''

Input Type 1:
Numbers with space turned into list of integer

Input
1 2 3 4 5
Output
[1, 2, 3, 4, 5]

Solution:
x = list(map(int, input().split(" ")))

Notes:
- Change parameter inside .split() method, to achieve splitting numbers separated by different symbols

------------------------------------------------------------------

Input Type 2:
Multiple lines input into a list of ints
First line represents # of lines to store

Input
3
100
200
300
Output
[100, 200, 300]

Solution:
x = []
for i in range(int(input())):
    x.append(int(input()))

------------------------------------------------------------------

Input Type 3:
Nested input into a nested list of ints
"Lists inside a big list"
First line represents the number of Rows and Columns

Input
2 3
100 200 300
400 500 600
Output
[[100, 200, 300], [400, 500, 600]]

Solution:
row, column = list(map(int, input().split(" ")))
bigList = []
for i in range(row):
    bigList.append(list(map(int, input().split(" "))))

------------------------------------------------------------------

Input Type 4:
Lines of strings into list

Input
1
3
Hello
World
Good
Morning

Output
["Hello"]
["World", "Good", "Morning"]

Solution:
x = int(input())
y = int(input())
list1 = []
lits2 = []
for i in range(x):
    list1.append(input())
for i in range(y):
    list2.append(input())

------------------------------------------------------------------

Input Type 5:
Mixed int and string type
first line represents number of entries

Input
4
5 Left A
2 Right B
3 Right C
4 Left D

Output
[[5, "Left", "A"], [2, "Right", "B"], [3, "Right", "C"], [4, "Left", "D"]]


Solution:
bigList = []
for i in range(int(input())):
    line = input().split(" ")
    line[0] = int(line[0])
    bigList.append(line)

------------------------------------------------------------------

Input Type 6:
In-Line Input with numbers and following strings
Every number n represents there are n strings following
1 Hello 2 Hello World 3 Hello World Good

Output
[['Hello'], ['Hello', 'World'], ['Hello', 'World', 'Good']]

Solution:
line = input().split()
bigList = []
while len(line) > 0:
    num = int(line.pop(0))
    smallList = []
    for i in range(num):
        smallList.append(line.pop(0))
    bigList.append(smallList)
print(bigList)
------------------------------------------------------------------

'''

print(list("Hello"))