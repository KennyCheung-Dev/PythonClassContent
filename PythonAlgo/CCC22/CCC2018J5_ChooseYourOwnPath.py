import sys

sys.setrecursionlimit(10**6)

pages = []
for i in range(int(input())):
    line = input().split(" ")
    pages.append({"goto": [int(j) - 1 for j in line[1:]],
                  "distance": sys.maxsize,
                  "visited" : False})

#Set first vertex's distance to 1
pages[0]["distance"] = 1

def RecurVisit(index_to_visit):
    pages[index_to_visit]["visited"] = True
    if pages[index_to_visit]["goto"] != []:
        updated = False
        for page_to_go in pages[index_to_visit]["goto"]:
            updatedDistance = pages[index_to_visit]["distance"] + 1
            if updatedDistance < pages[page_to_go]["distance"]:
                pages[page_to_go]["distance"] = updatedDistance
                updated = True
            if pages[page_to_go]["visited"] == False or updated:
                RecurVisit(page_to_go)

RecurVisit(0)

allVisited = True
shortestDistance = sys.maxsize
for page in pages:
    if page["goto"] == [] and page["distance"] < shortestDistance:
        shortestDistance = page["distance"]
    if not page["visited"]:
        allVisited = False

print("Y" if allVisited else "N")
print(shortestDistance)