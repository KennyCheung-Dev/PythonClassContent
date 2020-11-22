currentIndex = [0, 0]
steps = [[0,0]]
total = 0
keys = [
   ["A", "B", "C", "D", "E", "F"],
   ["G", "H", "I", "J", "K", "L"],
   ["M", "N", "O", "P", "Q", "R"],
   ["S", "T", "U", "V", "W", "X"],
   ["Y", "Z", " ", "-", ".", "enter"]
]

word = input()

for letter in word:
   for i in range(len(keys)):
       for j in range(len(keys[i])):
           if keys[i][j] == letter:
               steps.append([i,j])
steps.append([4,5])

for i in range(1, len(steps)):
   total += abs(steps[i][0] - steps[i-1][0])
   total += abs(steps[i][1] - steps[i-1][1])
print(total)
