from Block import Block
import A_star
import timeit
import sys
import DFS

"""input stage 1 là màn 1, stage2 là màn 3, dòng 1 là vị trí khởi đầu, dòng 2 là goal"""
def readMap(fileMap):
    with open(fileMap) as f:
        MAP_ROW, MAP_COL, xStart, yStart = [int(x) for x in next(f).split()] # read first line
        sourceMap = []
        countMapLine = 1
        for line in f: # read map
            countMapLine += 1
            sourceMap.append([int(x) for x in line.split()])
            if countMapLine > MAP_ROW: break

        # read managedBoard
        manaBoa = []
        for line in f: # read manaBoa
            # 2 2 4 4 4 5
            manaBoa.append([int(x) for x in line.split()])

    print("\nYOUR MAP LOOK LIKE THIS:")
    for item in sourceMap:
        print(item)
    print("Start at (",xStart, ",", yStart,")")
    print("ManaBoa:")
    for item in manaBoa:
        print(item)
    print("======================================")
    return MAP_ROW, MAP_COL, xStart, yStart, sourceMap, manaBoa

passState = []

MAP_ROW, MAP_COL, xStart, yStart, sourceMap, ManaBoa \
                        = readMap('map/map'+sys.argv[1:][0]+'.txt')

block = Block(xStart, yStart, "STANDING", None, sourceMap)

if sys.argv[1:][1] == "DFS":
    print("Solve DFS")  
    DFS(block)
    
elif sys.argv[1:][1] == "A_star":
    print("Solve A*")
    A_star(block)

else:
    print("Wrong algorithms argument!")