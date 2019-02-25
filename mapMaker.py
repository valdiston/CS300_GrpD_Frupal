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

def intro():
    print ("\nWelcome to the island of Frupal\n")
    print ("Somewhere on frupal there are jewels and it is your job to find them!")
    print ("Walking around the island is hard work and saps you of your energy.")
    print ("If you run out of energy before finding the jewels you lose and die alone.")
    print ("Even worse, some terrain is tougher to walk through and saps you of even more energy!")
    print ("Luckily you have gold and can buy items like chainsaws and boats to make things easier on you.")

    print ("Would you like an Easy, Medium or Hard game...Or would you like to make your own game?") 
    pick = False
    while pick == False:
        print ("[1]Easy\n[2]Medium\n[3]Hard\n[4]Create New Game")
        game = input("Enter Number: ")
        if game.isnumeric():
            if int(game) >= 1 and int(game) <= 4:
                pick = True
            else:
                print ("\nJust a number between 1 and 4 please\n") 
        else:
            print ("\nThose aren't even numbers. How are you going to survive on Frupal??")
            print ("Just a number between 1 and 4 please\n") 
    
    return game


def loadGame(game, player):
    if game == 1:
        load("easy", player)
    if game == 2:
        load("medium", player)
    if game == 3:
        load("hard", player)
    if game == 4:
        #circle back and do an input check
        title = input("what do you want your game to be called: ")
        #edit_csv()
        #edit_csv_tuple()
        load(title, player)


def load(fileName, player):
    #open up file and set up player and map




"""
#display function for testing
mapSize = 30
hiddenMap = mapMaker(mapSize, "forest")
for t in range(mapSize):
    print ()
    for j in range(mapSize):
        print (hiddenMap[t][j], end="")
""" 