mazeList = [[1,0,0,2],
            [1,0,4,1],
            [3,0,0,0]]
entrance = [2,0]

mazeList1 = [[1,3,0,1,0],
             [1,0,0,0,0],
             [0,0,1,0,4],
             [1,0,0,0,0]]
entrance1 = [0,1]

def findMazeExit(mazeList, entrance) :
    position = entrance
    pathStack = [position]

    while mazeList[position[0]][position[1]] != 2:
        position = checkRoadAvaliable(position,mazeList)

        if position == [-1,-1]:
            pathStack.pop()
            position = pathStack[-1]
        else:pathStack.append(position)

    return pathStack

# Check avaliable path around the position. return next position if avaliable else return [-1,-1]
def checkRoadAvaliable(position, mazeList):
    next = [-1,-1]
    # Mark the road traveled
    mazeList[position[0]][position[1]] = 5

    for i in range(4):
        diffX = 0
        diffY = 0

        if i == 0: diffX = 1
        if i == 1: diffX = -1
        if i == 2: diffY = 1
        if i == 3: diffY = -1
        
        if 0 <= position[0]+diffY < len(mazeList) and 0<= position[1]+diffX < len(mazeList[position[0]]) and mazeList[position[0] + diffY][position[1] + diffX] not in [1 ,4, 5]:
            next = [position[0] + diffY,position[1] + diffX]

            if mazeList[next[0]][next[1]] == 2:
                return next

    return next


print(findMazeExit(mazeList1,entrance1))
