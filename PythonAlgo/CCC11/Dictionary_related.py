# //Given two String[], find the intersection of the two
# # //Only counts those that is intersected once only
# # //Try Practicing counting with dictionary!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# String[] ​arr1​ = ​new​ String[] {​"1"​, ​"abc"​, ​"3"​, ​"6"​, ​"9"​, ​"Is"​, ​"3"​, ​"1"​};
# # String[] ​arr2​ = ​new​ String[] {​"4"​, ​"bc"​, ​"8"​, ​"Is"​, ​"9"​, ​"9"​, ​"4"​, ​"6"​};
# # //Return String[] {"Is", "6"} <- do not count 9
# # //Print out each String in result :
# # //Intersected at Is
# # //Intersected at 6

l1 = ["1", "abc", "3", "6", "9", "Is", "3", "1"]
l2 = ["4", "bc", "8", "Is", "9", "9", "4", "6"]

dict = {}

for i in l1:
    if i in dict:
        dict.pop(i)
    else:
        dict[i] = 1
for i in l2:
    if i in dict:
        dict[i] += 1
    if i in dict and dict[i] > 2:
        dict.pop(i)


for (key, value) in dict.items():
    if value == 2:
        print("Intersected at " + str(key))



