import mapMaker
import Event
import random
import csv
import clueMaker


class Player:

    def __init__(self):
        """ Integer variables - Status """
        self.money = 0
        self.energy = 0
        self.gems = 0
        self.totalGems = 0
        self.energyBarCost = 0
        self.goldFound = 0
        self.binocularCost = 0
        self.newTerrain = []
        # default field of view
        self.view = 2
        # list of clues
        self.clues = []
        # list of gem locations
        self.gemList = []

        """ Map Variables """
        self.mapSize = 0
        self.refMap = None
        self.dispMap = None

        """ Current Location """
        self.location = [0, 0]


        """ Dictionary of character/key pairs - for converting map items to real items """
        self.keyDict = {}  # format: {"map_char": "item/terrain", }

        """ Item/Map Properties  """
        self.ItemDict = {}  # format: {"key/item": {"cost": x/None, "owned": False},}

        self.terrainDict = {}  # format: {"key/terrain": {"energy": x, "item": y/None, "item energy": z/0},}

    """ Setup Functions"""
    def setup(self):
        self.refMap = mapMaker.mapMaker(self.mapSize, self)
        self.dispMap = [[' '] * self.mapSize for i in range(self.mapSize)]
        self.location = [random.randint(0, self.mapSize - 1), random.randint(0, self.mapSize - 1)]
        while self.refMap[self.location[0]][self.location[1]] == '*':
            self.location = [random.randint(0, self.mapSize - 1), random.randint(0, self.mapSize - 1)]
        self.generateClues()

    def generateClues(self):
        self.gemList, clueList, terrainList, jewelString, terrainString = clueMaker.generateClues(self.refMap, 0,
                                                                                                  self.mapSize)
        for x in range(0, len(clueList)):
            self.clues.append([clueList[x], jewelString[x], terrainString[x]])
        self.refMap = clueMaker.clueMap(clueList, self.refMap)

    """ Key related functions"""
    # takes in a list of {"map_char": "item/terrain"}
    def initKeys(self):
        with open('keyDict.csv') as f:
            reader = csv.reader(f, delimiter=',')
            self.keyDict.update({row[0].strip(): row[1].strip().capitalize() for row in reader})

    # returns the corresponding key string related to the reference map character
    def getKey(self, character):
        try:
            key = self.keyDict[character]
            return key
        except KeyError:
            return -1

    """ Terrain Functions"""
    # returns = 1: if item is success, -1: if terrain is None

    # parameters:
    # terrain == char representing terraintype
    # energy == energy cost of traversing terrain
    # item == terrain's associated tool (ie. terrain/water, item/boat)
    # item_energy == energy cost of traversing terrain with item
    def add_terrain(self, terrain, energy, item, item_energy):
        if terrain is not None:
            terrainDict = {terrain: {"energy": energy, "item": item, "item energy": item_energy}}
            self.terrainDict.update(terrainDict)
            return 1
        else:
            return -1

    """ Item Functions"""
    # returns = 1: if item is success, 0: if the user has 0 of that item, 1: if the item was used
    def add_item(self, item, cost, owned):
        if item is not None:
            newItem = {item: {"cost": cost, "owned": owned}}
            self.ItemDict.update(newItem)
            return 1
        else:
            return -1

    """ Item Store """
    def __shopanswer(self):
        answer = input("   Which item would you like to purchase? ")
        while not answer.isnumeric():
            answer = input(" Please pick a number corresponding to an item or 0 to exit ")
        return int(answer)

    def shop(self):
        print("\n --------------------------------------------")
        print("|[$][$][$] Welcome to the Item Shop [$][$][$]|\n --------------------------------------------")
        print("|             Current Gold: %4d             |" % self.money)
        print(" --------------------------------------------")
        print("|       Items Available for purchase:        |")
        print("|                                            |")
        print("|       1. Energy Bar || Cost: %-3s Gold      |" % self.energyBarCost)

        if self.view == 2:
            print("|       2. Binoculars || Cost: %-3s Gold      |" % self.binocularCost)
        else:
            print("|       2. Binoculars || Already Purchased   |")
        i = 3
        for key in self.ItemDict.keys():
            if not self.ItemDict[key]["owned"]:
                print("|       %d. %-10s %s %-3s Gold      |" % (i, self.getKey(key), "|| Cost:",
                      self.ItemDict[key]["cost"]))
                i += 1
            else:
                print("|       %d. %-10s %s" % (i, self.getKey(key), "|| Already Purchased   |"))
                i += 1
        print("|                                            |")
        print("| Enter 0 to exit without making a purchase! |")
        print(" --------------------------------------------")
        answer = self.__shopanswer()
        while answer < 0 or answer > (i - 1):
                answer = self.__shopanswer()

        if answer == 0:
            print()
            return

        if answer == 1:
            if self.money >= self.energyBarCost:
                self.money -= self.energyBarCost
                # placeholder value
                self.energy += 5
                print()
                return
            else:
                print(" Sorry you don't have enough money to purchase this item")
                return
        elif answer == 2 and self.view == 2:
            if self.money >= self.binocularCost:
                self.money -= self.binocularCost
                # placeholder value
                self.view += 1
                print()
            else:
                print(" Sorry you don't have enough money to purchase this item")
                return
        else:
            x = 3
            keys = list(self.ItemDict.keys())
            if not self.ItemDict[keys[answer - x]]["owned"]:
                if self.money >= int(self.ItemDict[keys[answer - x]]["cost"]):
                    self.money -= int(self.ItemDict[keys[answer - x]]["cost"])
                    self.ItemDict[keys[answer - x]]["owned"] = True
                    print()
                    return
                else:
                    print(" Sorry you don't have enough money to purchase this item")
                    return
            else:
                print(" Whoops! You already own this item. At the moment you cannot buy another.\n")

    """ Legend Function """
    def legend(self):
        print(" [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]")
        print(" [x]                               Game Legend                                 [x]")
        print(" [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]")
        print(" %-20s | Information:                                           [x]" % "[x] Special:")
        print(" [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]")
        print(" [x] %-16s | Collect all of them to win the game!                   [x]" % "* = Gem")
        print(" [x] %-16s | A Clue that directs you to a gems location             [x]" % "c = Clue")
        print(" [x] %-16s | Gives money or energy if completed  successfully       [x]" % "e = Event")
        print(" [x] %-16s | Provides %d gold when stepped on                       [x]" % ("$ = Sack of gold",
                                                                                           self.goldFound))
        print(" [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]")
        print(" %-20s | Energy Cost: | Shop Item: |  Energy Cost w/ Item: |    [x]" % "[x] Terrain:")
        print(" [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]")
        for terrain in self.terrainDict.keys():
            if self.terrainDict[terrain]["item"] != '0':
                print(" [x] %s = %-12s |       %-6d |    %-7s |            %-10s |    [x]"
                      % (terrain, self.getKey(terrain), int(self.terrainDict[terrain]["energy"]),
                         self.getKey(self.terrainDict[terrain]["item"]), self.terrainDict[terrain]["item energy"]))
            else:
                print(" [x] %s = %-12s |       %-6d |    None    |           N/A         |    [x]" % (terrain,
                      self.getKey(terrain),int(self.terrainDict[terrain]["energy"])))
        print(" [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]\n")

    """ Movement Functions """

    def move_to(self, coords, referenceMap):
        key = referenceMap[coords[0]][coords[1]]
        if key not in list(self.terrainDict.keys()) + ['e', '*', '$', 'c', ' ']:
            print(" Map contains an unknown character")
            return -1
        else:
            # if the location contains a gem
            if key == "*":
                self.gems += 1
                self.location = coords
                referenceMap[coords[0]][coords[1]] = 'p'
                for index, location in enumerate(self.gemList):
                    if location == [coords[0], coords[1]]:
                        self.gemList.remove(location)
                print(" Wow! You managed to find one of the hidden island gems!!!")
                print(" Collected Gems: %d/%d" % (self.gems, self.totalGems))
                input("Press enter to continue > ")
                return 1

            if key == "$":
                self.money += self.goldFound
                self.location = coords
                referenceMap[coords[0]][coords[1]] = 'p'
                return 1

            if key == ' ':
                self.location = coords
                return 1

            # block for stepping on terrain
            elif key in self.terrainDict:
                energy = int(self.terrainDict[key]["energy"])
                item = self.terrainDict[key]["item"]
                itemEngery = int(self.terrainDict[key]["item energy"])
                if item != '0':
                    if self.ItemDict[item]["owned"]:
                        if self.energy >= itemEngery:
                            self.energy -= itemEngery
                            self.location = coords
                            return 1
                        else:
                            print(" Sadly you don't have the energy to continue in this direction")
                            input("Press enter to continue > ")
                            return 0
                    else:
                        if self.energy >= energy:
                            self.energy -= energy
                            self.location = coords
                            return 1
                        else:
                            print(" Sadly you don't have the energy to continue in this direction")
                            input("Press enter to continue > ")
                            return 0
                else:
                    if self.energy >= energy:
                        self.energy -= energy
                        self.location = coords
                        return 1
                    else:
                        print(" Sadly you don't have the energy to continue in this direction")
                        input("Press enter to continue > ")
                        return 0

            # block for stepping on an event
            elif key == "e":
                self.location = coords
                referenceMap[coords[0]][coords[1]] = 'p'
                print(" You have encountered an event!")
                event = Event.Energy("event")
                eventType = random.randint(1, 2)
                if eventType == 1:  # 1 signifies energy event
                    newEnrg = random.randint(5, 15)
                    self.energy = event.trigger(self.energy, newEnrg, "energy")
                    return 1
                elif eventType == 2:  # 2 signifies money event
                    newMoney = random.randint(5, 15)
                    self.money = event.trigger(self.money, newMoney, "money")
                    return 1
                else:
                    return 0

            # block for stepping on a clue
            elif key == "c":
                for clue in self.clues:
                    if clue[0][0] == coords[0] and clue[0][1] == coords[1]:
                        print("\n You Have found a clue to the location of a gem!")
                        print("\n   The clue reads: ", clue[1])
                        print("\n There's a chance this clue could be fake. If the following statement is true,"
                              " the clue is correct")
                        print("\n  ", clue[2], "\n")
                        input("Press enter to continue > ")
                        self.clues.pop(self.clues.index(clue))
                        referenceMap[coords[0]][coords[1]] = 'p'
                        break
                self.location = coords
                return 1

            else:
                print(key, "is somehow not a terrain, event, clue, or gem. Something has gone wrong setting up the "
                           "game")
                input("Press enter to continue > ")
                return -1
