#function to randomly fill a 2-D array with values
#representing different terrain and objects for game

#key for every terrain and object possible in map:
#p = plain
#w = water
#f = forest
#r = rocky
#b = boat(for traversing water)
#c = chainsaw(for traversing forest)
#j = pickaxe(for traversing rocky ground)
#g = gold
#e = event
#c = clue      !!!! not sure what the difference between an event and a clue is!!!!
#l = binoculars 
#z = jewels

import random
import csv
from Player import *

# mapMaker() takes two args:
# arg 1 == int representing map size
# arg 2 == list of terrain added by user
# mapMaker() returns:
# a 2-D array of map filled with terrain and object values


def mapMaker(mapSize, addedTerrain):

    # initialize elements in 2-D map array to 0
    map = [[0 for x in range(mapSize)] for y in range(mapSize)] 

    numOfElements = mapSize * mapSize
    # need to first populate map with single use objects(i.e. jewels, binoculars...)
    preSeededObjects = preSeedMap(map, mapSize)

    numOfElements = numOfElements - preSeededObjects

    # populate rest of map with letters representing terrain and objects
    for x in range(numOfElements):
            coord = getCoord(map, mapSize)
            row = coord[0]
            col = coord[1]

            mapObject = getMapObject()
            map[row][col] = mapObject

    return map

# preSeedMap() takes two args.
    # arg 1 = 2-D array representing map
    # arg 2 = int representing map size
# preSeedMap() returns:
    # number of unique objects placed on map (i.e. jewels, binoculars...)


def preSeedMap(map, mapSize):
    random.seed(a=None)
    objectsPlaced = 0
    adding = 1

    # only one spot for jewels
    coord = getCoord(map, mapSize)
    row = coord[0]
    col = coord[1]
    map[row][col] = 'j'
    objectsPlaced += 1

    # the larger the map size the more unique
    # objects should be placed in map
    adding = 1

    if mapSize >= 30:
        adding = 2
    if mapSize >= 50:
        adding = 3
    
    # probably going to need to have a few if statements
    # depending on what terrains user added. same with
    # general map seeding function(i.e. will we need to
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

# getCoord() takes 1 arg.
    # arg 1 = 2-D array of map
# getCoord() returns:
    # a tuple where tuple[0] = row on map and tuple[1] = column on map


def getCoord(map, mapSize):
    random.seed(a=None)
    free = False

    # does randrange use >mapSize or >=mapSize
    while not free:
        row = random.randrange(0, mapSize)
        col = random.randrange(0, mapSize)
        free = openSpace(map, row, col)

    return (row, col)

# getMapObject() will eventual need to accept args to include
# terrain a user adds to the map. For now it is simple
# getMapObject() returns:
    # letter representing the kind of object to fill space on map with


def getMapObject(addedTerrain):
    random.seed(a=None)
    luckyNumber = random.randrange(0, 100)
    if addedTerrain != 0:
        if luckyNumber < 35:
            pass
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # find another lucky number depending on how many terrains
            # were added and return the corresponding char.
    
    # if you didn't add from addedTerrain get another lucky number
    # and return corresponding char
    if luckyNumber < 30:
        return 'p'
    if luckyNumber < 45:
        return 'w'
    if luckyNumber < 60:
        return 'g'
    if luckyNumber < 80:
        return 'c'
    if luckyNumber < 100:
        return 'e'


# openSpace() takes three args:
    # arg 1 == 2-D array of map
    # arg 2 == row for 2-D array
    # arg 3 == col for 2-D array
# openSpace() returns:
    # boolean indicating whether space is open(True) or is populated(False)
def openSpace(map, row, col):
    if map[row][col] == 0:
        free = True
    else:  
        free = False
    return free


def intro():
    print("\nWelcome to the Island of Frupal\n")
    print("Somewhere on Frupal there are jewels and it is your job to find them!")
    print("Walking around the island is hard work and saps you of your energy.")
    print("If you run out of energy before finding the jewels you lose and die alone.")
    print("Even worse, some terrain is tougher to walk through and saps you of even more energy!")
    print("Luckily you have gold and can buy items like chainsaws and boats to make things easier on you.")

    print("Would you like to load a game or Easy, Medium or Hard game...\nOr would you like to make your own game?")
    pick = False
    while not pick:
        print("[1]Load Game\n[2]Easy\n[3]Medium\n[4]Hard\n[5]Create New Game")
        game = input("Enter Number: ")
        if game.isnumeric():
            if int(game) < 1 or int(game) > 5:
                pick = True
            else:
                print("\nJust a number between 1 and 5 please\n")
        else:
            print("\nThose aren't even numbers. How are you going to survive on Frupal??")
            print("Just a number between 1 and 5 please\n")
    
    return game


def loadGame(game, player):
    if game == 1:
        title = getTitle()
        load(title, player)
    if game == 2:
        load("easy", player)
    if game == 3:
        load("medium", player)
    if game == 4:
        load("hard", player)
    if game == 5:
        # circle back and do an input check
        title = input("what do you want your game to be called: ")
        # edit_csv()
        # edit_csv_tuple()
        load(title, player)


def load(fileName, player):
    # open up file and set up player and map

    # open game file and read in item and terrain info. store in player object
    with open(fileName + '.csv') as f:
        reader = csv.reader(f, delimiter=',')

        gold = next(reader)
        player.money = gold[1]
        energy = next(reader)
        player.energy = energy[1]
        size = next(reader)
        player.mapSize = size[1]
        energyBarCost = next(reader)
        newTerrain = []
        newTerrain[0] = 0

        next(reader)
        
        for row in reader:
            # if terrain/item is used in this instance of a game
            if row[1] == 1:
                # if row contains a terrain
                if row[2] == 1:
                    player.add_to_terrain(row[0], row[3], row[6], row[7])
                    if row[0] != 'w' and row[0] != 'p':
                        newTerrain[0] += 1
                        newTerrain.append(row[0])
                # else row must contain item
                else:
                    player.add_to_itemlist(row[0], row[3], row[8], row[4], row[5])
        # player.addedTerrain == newTerrain

    # build a dictionary with all possible characters and what they represent
    with open('keyDict.csv') as f:
        reader = csv.reader(f, delimiter=',')

        keyDict = {row[0]: row[1] for row in reader}
        player.initKeys(keyDict)


def getTitle():
    with open('savedGames.txt', 'r') as f:
        games = [row for row in reader]
            

