#function to randomly fill a 2-D array with values
#representing different terrain and objects for game

#key for every terrain and object possible in map:
#p = plain
#w = water
#f = forest
#r = rocky
#b = boat(for traversing water)
#c = chainsaw(for traversing forest)
#p = pickaxe(for traversing rocky ground)
#g = gold
#e = event
#c = clue      !!!! not sure what the difference between an event and a clue is!!!!
#b = binoculars 
#j = jewels

import random
import csv

#mapMaker() takes two args:
    #arg 1 == int representing map size
    #arg 2 == list of terrain added by user
#mapMaker() returns:
    #a 2-D array of map filled with terrain and object values

def mapMaker(mapSize, addedTerrain):

    #initialize elements in 2-D map array to 0
    map = [[0 for x in range(mapSize)] for y in range(mapSize)] 

    numOfElements = mapSize * mapSize
    #need to first populate map with single use objects(i.e. jewels, binoculars...)
    preSeededObjects = preSeedMap(map, mapSize)

    numOfElements = numOfElements - preSeededObjects

    #populate rest of map with letters representing terrain and objects
    for x in range(numOfElements):
            coord = getCoord(map, mapSize)
            row = coord[0]
            col = coord[1]

            mapObject = getMapObject()
            map[row][col] = mapObject

    return map

#preSeedMap() takes two args.
    #arg 1 = 2-D array representing map
    #arg 2 = int representing map size
#preSeedMap() returns:
    #number of unique objects placed on map (i.e. jewels, binoculars...)
def preSeedMap(map, mapSize):
    random.seed(a=None)
    objectsPlaced = 0
    adding = 1

    #only one spot for jewels
    coord = getCoord(map, mapSize)
    row = coord[0]
    col = coord[1]
    map[row][col] = 'j'
    objectsPlaced += 1

    #the larger the map size the more unique 
    # objects should be placed in map
    if(mapSize >= 30):
        adding = 2
    if(mapSize >= 50):
        adding = 3
    
    #probably going to need to have a few if statements
    #depending on what terrains user added. same with 
    #general map seeding function(i.e. will we need to 
    # be placing forests, rocks or both)
    for t in range(adding):
        for j in range(2):
            coord = getCoord(map, mapSize)
            row = coord[0]
            col = coord[1]
            map[row][col] = 'b'

            coord = getCoord(map, mapSize)
            row = coord[0]
            col = coord[1]
            map[row][col] = 'l'

            objectsPlaced += 2

    return objectsPlaced

#getCoord() takes 1 arg.
    #arg 1 = 2-D array of map
#getCoord() returns:
    #a tuple where tuple[0] = row on map and tuple[1] = collumn on map
def getCoord(map, mapSize):
    random.seed(a=None)
    free = False

    #does randrange use >mapSize or >=mapSize
    while(free == False):
        row = random.randrange(0,mapSize)
        col = random.randrange(0,mapSize)
        free = openSpace(map, row, col)

    return (row, col)

#getMapObject() will eventuall need to accept args to include 
#terrain a user adds to the map. For now it is simple

#getMapObject() returns:
    #letter representing the kind of object to fill space on map with

def getMapObject():
    
    random.seed(a=None)
    luckyNumber = random.randrange(0,100)

    if(luckyNumber<30):
        return 'p'
    if(luckyNumber<45):
        return 'w'
    if(luckyNumber<60):
        return 'g'
    if(luckyNumber<80):
        return 'c'
    if(luckyNumber<100):
        return 'e'



#openSpace() takes three args:
    #arg 1 == 2-D array of map
    #arg 2 == row for 2-D array 
    #arg 3 == col for 2-D array 
#openSpace() returns:
    #boolean indicating whether space is open(True) or is populated(False)
def openSpace(map, row, col):
    if(map[row][col] == 0):
        free = True
    else:  
        free = False
    return free


#csv
def loadGame(fileName, player, map):

    with open(fileName + '.csv') as f:
        readCSV = csv.reader(f, delimiter=',')
        mapSize = next(readCSV)
        print ("mapSize")
        print (mapSize)
        energy = next(readCSV)
        gold = next(readCSV)
        binoculars = next(readCSV)
        chainsaw = next(readCSV)
        jackHammer = next(readCSV)
        sickle = next(readCSV)

"""
#display function for testing
mapSize = 30
hiddenMap = mapMaker(mapSize, "forest")
for t in range(mapSize):
    print ()
    for j in range(mapSize):
        print (hiddenMap[t][j], end="")
""" 