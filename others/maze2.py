mazeList = [[1,0,0,2],
            [1,0,4,1],
            [3,0,0,0]]
entrance = [2,0]

mazeList1 = [[1,3,0,1,0],
             [1,0,0,0,0],
             [0,0,1,0,4],
             [2,0,0,0,0]]
entrance1 = [0,1]


def findMazeExit(mazeList, entrance) :
    ways = []

    findWay(mazeList, entrance, ways)
    

def findWay(mazeList, position, ways):
    x = position[1]
    y = position[0]
    mazeList[y][x] = 1
    nextAvaliable = []

    for i in range(4):
        diffX = 0
        diffY = 0

        # Right Down Left Up
        if i == 0: diffX = 1
        if i == 1: diffY = -1
        if i == 2: diffX = -1
        if i == 3: diffY = 1
        
        if 0 <= y + diffY < len(mazeList) and 0<= x + diffX < len(mazeList[y]):
            if mazeList[y + diffY][x + diffX] == 0:
                nextAvaliable.append([y + diffY,x + diffX])

    # Check if 2 is nearby
    for next in nextAvaliable:
        if mazeList[next[0]][next[1]] == 2:
            return 

    for next in nextAvaliable:
        print(next)
        findWay(mazeList,next,ways)

print(findMazeExit(mazeList1,entrance1))
print(mazeList1)
