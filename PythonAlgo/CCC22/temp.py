import sys

pageNum = int(input())
pages = []

for i in range(pageNum):
    line = input().split(" ")
    pages.append([])
    pages[i].append([])
    pages[i].append(sys.maxsize)
    for j in range(1, len(line)):
        pages[i][0].append(line[j])
print(pages)

def RecurVisit(index_to_visit):
    # Turn current visited node to visited!
    # Check if page is 0, or has options, if has options
        # For each option nodes
            # update distance ONLY when new distance is smaller
            # if updated new distance, visit again no matter if visited before
            # if option node is not visited
                # Recursively visit the node
    pass




