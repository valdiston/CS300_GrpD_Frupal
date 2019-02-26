#Andrew Bespaly clueMaker.py
import random
import mapMaker

#finds all 'j' in given map argument
def findJewels(map):
    jList = []
    for i in range(len(map)):
        for j in range(len(map)):
            if (map[i][j] == 'j'):
                jCoord = [i, j]
                jList += [jCoord]
    return jList

#returns item in map at coordinates
def findTerrain(map, coord):
    return map[coord[0]][coord[1]]

#takes a direction North, East, South, West
#starting coordinates
#size of the map
#maximum distance away from coordinates
def getNewCoord(direction, curCoord, mapSize, distance):
    if(direction == "North"):
        if(curCoord[0] == 0):
            return getNewCoord("South", curCoord, mapSize, distance)
        if(curCoord[0] <= distance):
            newDirec = [random.randint(0,curCoord[0]-1), curCoord[1]]
        else:
            newDirec = [curCoord[0]-random.randint(1, distance), curCoord[1]]
        return newDirec

    if(direction == "East"):
        if(curCoord[1] == mapSize-1):
            return  getNewCoord("West", curCoord, mapSize, distance)
        if((mapSize - curCoord[1]) <= distance):
            newDirec = [curCoord[0], random.randint((curCoord[1]+1), mapSize-1)]
        else:
            newDirec = [curCoord[0], random.randint((curCoord[1]+1), (curCoord[1]+distance))]
        return newDirec

    if(direction == "South"):
        if(curCoord[0] == mapSize-1):
            return getNewCoord("North", curCoord, mapSize, distance)
        if((mapSize - curCoord[0]) <= distance):
            newDirec = [random.randint((curCoord[0]+1),mapSize-1), curCoord[1]]
        else:
            newDirec = [curCoord[0]+random.randint(1, distance), curCoord[1]]
        return newDirec

    if(direction == "West"):
        if(curCoord[1] == 0):
            return getNewCoord("East", curCoord, mapSize, distance)
        if(curCoord[1] <= distance):
            newDirec = [curCoord[0], curCoord[1]-random.randint(1, curCoord[1])]
        else:
            newDirec = [curCoord[0], curCoord[1]-random.randint(1, distance)]
        return newDirec

#takes to coordinates
#returns the direction and distance apart
def distFromCoord(fromList, toList):
    direction = ''
    distance = 0
    if(fromList[0] < toList[0]):
        direction = 'South'
        distance = toList[0] - fromList[0]

    elif(fromList[0] > toList[0]):
        direction = 'North'
        distance = fromList[0] - toList[0]

    elif(fromList[1] < toList[1]):
        direction = 'East'
        distance = toList[1] - fromList[1]

    elif(fromList[1] > toList[1]):
        direction = 'West'
        distance = fromList[1] - toList[1]

    return direction, distance

#takes a list of coordinates, the max distance the new coordinates could be, and a list of the last related direction
#to avoid  repetion in the same direction for the terrain proof and the jewel
#iterates through a list and creates a new coordinate for every item
#returns a new list of coordinates
def randGenDirection(list, distance, lastDirec, mapSize):
    newList = []
    for item in list:
        randDirNum = random.randint(0, 3)

        if (lastDirec[list.index(item)] == 0 and randDirNum == 2):
            randDirNum = int(random.choice('013'))
        if (lastDirec[list.index(item)] == 1 and randDirNum == 3):
            randDirNum = int(random.choice('012'))
        if (lastDirec[list.index(item)] == 2 and randDirNum == 0):
            randDirNum = int(random.choice('123'))
        if (lastDirec[list.index(item)] == 3 and randDirNum == 1):
            randDirNum = int(random.choice('023'))


        if (randDirNum == 0):
            newCoord = getNewCoord("North", item, mapSize, distance)
        if (randDirNum == 1):
            newCoord = getNewCoord("East", item, mapSize, distance)
        if (randDirNum == 2):
            newCoord = getNewCoord("South", item, mapSize, distance)
        if (randDirNum == 3):
            newCoord = getNewCoord("West", item, mapSize, distance)

        newList += [newCoord]
    return newList

def randGenDirectionFirst(list, distance, mapSize):
    newList = []
    directionList = []
    for item in list:
        randDirNum = random.randint(0, 3)
        directionList += [randDirNum]

        if (randDirNum == 0):
            newCoord = getNewCoord("North", item, mapSize, distance)
        if (randDirNum == 1):
            newCoord = getNewCoord("East", item, mapSize, distance)
        if (randDirNum == 2):
            newCoord = getNewCoord("South", item, mapSize, distance)
        if (randDirNum == 3):
            newCoord = getNewCoord("West", item, mapSize, distance)

        newList += [newCoord]
    return newList, directionList

#takes three lists of coordinates and an option for real terrain direction and fake
#Creates the strings used to display the direction and distance away from the jewels and the terrain block
#returns newly created strings
def createStringLists(islandMap, jewelList, clueList, terrainList, real):
    jewelString = []
    terrainString = []
    for i in range(0, len(jewelList)):
        jewelDir, jewelDist = distFromCoord(clueList[i], jewelList[i])
        terrainDir, terrainDist = distFromCoord(clueList[i], terrainList[i])
        jewelString += ["A Jewel is " + str(jewelDist) + " to the " + jewelDir]
        if(real == True):
            terrainString += ["The block " + str(terrainDist) + " blocks to the " + terrainDir +
                          " is a: " + findTerrain(islandMap, terrainList[i])]
        else:
            randTerrainOptions = 'pwgue'
            randTerrain = random.choice(randTerrainOptions)
            while(randTerrain == findTerrain(islandMap, terrainList[i])):
                randTerrain = random.choice(randTerrainOptions)
            terrainString += ["The block " + str(terrainDist) + " blocks to the " + terrainDir +
                              " is a: " + randTerrain]

    return jewelString, terrainString

#takes amount of fake clues, and original map
#checks original map to make fake jewels aren't randomly generated on real ones
#returns new list of fake jewel coordinates
def fakeJewels(fakeClueAmount, originalMap):
    mapSize = len(originalMap)
    fakeJewelList = []
    for i in range(0, fakeClueAmount):
        fakeJewelCoord = [random.randint(0,mapSize-1), random.randint(0,mapSize-1)]
        while(originalMap[fakeJewelCoord[0]][fakeJewelCoord[1]] == 'j'):
            fakeJewelCoord = [random.randint(0,mapSize-1), random.randint(0,mapSize-1)]

        fakeJewelList += [fakeJewelCoord]
    return fakeJewelList

#main function that produces everything
#returns 3 lists to all coordinates and strings to be used when stepping on a clue
#takes a map of the island, the amount of fake clues the user would like, and the maximum distance
#the terrain proofs should spawn away from the clue
def generateClues(islandMap, fakeJewelAmount, maxTerrainDist):
    jewelList = findJewels(islandMap)
    clueList, jewelDirec = randGenDirectionFirst(jewelList, len(islandMap), len(islandMap))
    terrainList = randGenDirection(clueList, maxTerrainDist, jewelDirec, len(islandMap))
    jewelString, terrainString = createStringLists(islandMap, jewelList, clueList, terrainList, True)
    fakeJewelList = fakeJewels(fakeJewelAmount, islandMap)
    fakeClueList, fakeJewelDirec = randGenDirectionFirst(fakeJewelList, len(islandMap), len(islandMap))
    fakeTerrainList = randGenDirection(fakeClueList, maxTerrainDist, fakeJewelDirec, len(islandMap))
    fakeJewelString, fakeTerrainString = createStringLists(islandMap, fakeJewelList, fakeClueList, fakeTerrainList, False)
    jewelList += fakeJewelList
    clueList += fakeClueList
    terrainList += fakeTerrainList
    jewelString += fakeJewelString
    terrainString += fakeTerrainString
    return jewelList, clueList, terrainList, jewelString, terrainString

#replaces any item where a clue spawned to a 'c'
#returns the map
def clueMap(clueList, islandMap):
    for item in clueList:
        islandMap[item[0]][item[1]] = 'c'
    return islandMap

# islandMap = mapMaker.mapMaker(30, "forest")

'''islandMap[12][12] = 'j'
islandMap[15][15] = 'j'
islandMap[1][1] = 'j'
islandMap[2][2] = 'j'
'''

#returns a list of coordinates for the corresponding jewel locations, clue locations, terrain locations, and strings
#that say where the jewels and terrain block is from the clue.
#generate clues takes the map of terrain, the amount of fake clues wanted, and the maximum distance needed to walk to
#prove a clue is true
# jewelList, clueList, terrainList, jewelString, terrainString = generateClues(islandMap, 0, 5)

#clueMap takes the map of terrain and replaces the coordinates where there should be a clue with a 'c'
# clueIsland = clueMap(clueList, islandMap)
'''print(jewelList)
print(clueList)
print(terrainList)
print(jewelString)
print(terrainString)'''


'''for item in jewelList:
    print("A Clue is at: ", clueList[jewelList.index(item)])
    print("A Jewel is at: ", item)
    print("A Terrain block for proof is at: ", terrainList[jewelList.index(item)])
    print(jewelString[jewelList.index(item)])
    print(terrainString[jewelList.index(item)])
    print('\n')'''


#use in full program should be used something like this
#every time the player moves onto a new coordinates, compare the coordinates with every spot in the clueList.
#If the coordinates match, the same index in the jewelString and terrainString contain the corresponding information
#for the clue.
'''playerCoord = [2,3]
for item in clueList:
    if(item[0] == playerCoord[0] and item[1] == playerCoord[1]):
        print(jewelString[clueList.index(item)], terrainString[clueList.index(item)])
'''
