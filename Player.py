import mapMaker
import clueMaker
import Event
import config
import random


class Player:

    def __init__(self):
        """ Integer variables - Status """
        self.money = 0
        self.energy = 0
        self.gems = 0
        self.energyBarCost = 0
        self.goldFound = 0
        self.newTerrain = []
        # default field of view
        self.view = 1

        """ Map Variables """
        self.mapSize = 0
        self.refMap = None

        """ Current Location """
        self.location = [0, 0]

        """ Dictionary of character/key pairs - for converting map items to real items """
        self.keyDict = {}  # format: {"map_char": "item/terrain", }

        """ Item/Map Properties  """
        self.ItemDict = {}  # format: {"key/item": {"cost": x/None, "owned": False},}

        self.terrainDict = {}  # format: {"key/terrain": {"energy": x, "item": y/None, "item energy": z/0},}

        """ Inventory - Collected Items """
        self.inventory = {}  # format: {"item1": x, "item2": y, }

    def setup(self):
        # todo fill keyDict, ItemDict, terrainDict, and inventory prior to setting up map
        self.refMap = mapMaker.mapMaker(self.mapSize, self.newTerrain)

    """ Key related functionss"""

    # takes in a list of {"map_char": "item/terrain"}
    def initKeys(self, dictList):
        if dictList is not None:
            for dict in dictList:
                self.keyDict.update(dict)
        else:
            return -1

    # returns the corresponding key string related to the reference map character
    def getKey(self, character):
        try:
            key = self.keyDict[character]
            return key
        except KeyError:
            return -1

    """ Inventory functions """

    # returns = 1: if item is success
    def add_to_inventory(self, item):
        if item is not None:
            self.inventory.update([(item, 0)])
            return 1
        else:
            return -1

    # returns = 1: if item is successfully incremented, -1: if item is None
    def add_item(self, item):
        if item is None:
            return -1
        try:
            self.inventory[item] += 1
        except KeyError:
            self.inventory.update([(item, 1)])
        return 1

    # returns = 1: if item doesnt exist, 0: if the user has 0 of that item, 1: if the item was used
    def use_item(self, item):
        try:
            if self.inventory[item] > 0:
                self.inventory[item] -= 1
                return 1
            else:
                return 0
        except KeyError:
            return -1

    """ Terrain Functions"""

    # returns = 1: if item is success, -1: if terrain is None
    def add_to_terrain(self, terrain, energy, item, item_energy):
        if terrain is not None:
            terrainDict = {terrain: {"energy": energy, "item": item, "item energy": item_energy}}
            self.terrainDict.update(terrainDict)
            return 1
        else:
            return -1

    """ Item Functions"""

    # returns = 1: if item is success, 0: if the user has 0 of that item, 1: if the item was used
    def add_to_itemlist(self, item, energy, vision, money, cost):
        if item is not None:
            itemDict = {item: {"energy": energy, "vision": vision, "money": money, "cost": cost}}
            self.ItemDict.update(itemDict)
            return 1
        else:
            return -1

    """ Movement Functions """

    def move_to(self, coords, referenceMap, clues):
        key = self.getKey(referenceMap[coords[0]][coords[1]])
        if key == -1:
            return -1
        else:
            # Block for stepping on an item
            if key in self.ItemDict:
                print("You have come across a ", key, " during your journey")
                if key == "gem":
                    self.gems += 1
                    self.location = coords
                    referenceMap[coords[0]][coords[1]] = 'g'
                    return 1

                elif self.ItemDict[key]["cost"] > 0:
                    cost = self.ItemDict[key]["cost"]
                    answer = input("This item costs $" + cost + ". Would you like to buy it? (y/n)")
                    if str(answer) == 'y':
                        if self.money >= cost:
                            self.add_to_inventory(key)
                            self.money -= cost
                            print("You have just bought a ", key, "  and added it to your inventory")
                            self.location = coords
                            referenceMap[coords[0]][coords[1]] = 'g'
                            return 1
                        else:
                            print("Sorry! You don't have enough money to purchase this item... Please come back when"
                                  " you have more money")
                            self.location = coords
                            return 1
                    else:
                        self.location = coords
                        return 1

                elif self.ItemDict[key]["cost"] == 0:
                    self.energy += self.ItemDict[key]["energy"]
                    if self.ItemDict[key]["money"] >= 0:
                        self.money += self.ItemDict[key]["money"]
                    if self.ItemDict[key]["vision"] >= 0:
                        self.view += self.ItemDict[key]["vision"]
                        if key == "binoculars":
                            self.add_to_inventory(key)
                            print("You have just found a pair of", key, "  and added it to your inventory")
                            print("Your vision radius has increased to %s" % self.view)
                            self.location = coords
                            referenceMap[coords[0]][coords[1]] = 'g'
                            return 1
                    self.add_to_inventory(key)
                    print("You have just found a ", key, "  and added it to your inventory")
                    self.location = coords
                    referenceMap[coords[0]][coords[1]] = 'g'
                    return 1

            # block for stepping on terrain
            elif key in self.terrainDict:
                ecost = self.terrainDict[key]["energy"]
                item = self.terrainDict[key]["item"]
                ienrg = self.terrainDict[key]["item energy"]
                if item is not None:
                    if self.inventory[item] >= 1:
                        answer = input("You can use your " + item + " to reduce the energy cost of this move to " +
                                       ienrg + "\nWould you like you use your item? (y/n)")
                        if str(answer).lower() == 'y':
                            if self.energy >= ienrg:
                                self.inventory[item] -= 1
                                self.location = coords
                                self.energy -= ienrg
                                return 1
                            else:
                                return 0
                        else:
                            if self.energy >= ecost:
                                self.location = coords
                                self.energy -= ecost
                                return 1
                            else:
                                return 0
                    else:
                        if self.energy >= ecost:
                            self.location = coords
                            self.energy -= ecost
                            return 1
                        else:
                            return 0
                else:
                    return 0

            # block for stepping on an event
            elif key == "event":
                self.location = coords
                referenceMap[coords[0]][coords[1]] = 'g'
                print("You have encountered an event!")
                event = Event.Energy("event")
                eventType = random.randint(1, 2)
                if eventType == 1:  # 1 signifies energy event
                    newEnrg = random.randint(5, 15)
                    self.energy = event.trigger(self.energy, newEnrg,"energy")
                    return 1
                elif eventType == 2:  # 2 signifies money event
                    newMoney = random.randint(5, 15)
                    self.money = event.trigger(self.money, newMoney,"money")
                    return 1
                else:
                    return 0

            # block for stepping on a clue
            elif key == "clue":
                for clue in clues:
                    if clue[0][0] == coords[0] and clue[0][1] == coords[1]:
                        print("You Have found a clue to the location of a gem!")
                        print("The clue reads: ", clue[1])
                        print("There's a chance this clue could be fake. If the following statement is true, the clue"
                              " is correct")
                        print(clue[2])
                        clues.pop(clues.index(clue))
                        referenceMap[coords[0]][coords[1]] = 'g'
                        break
                self.location = coords
                return 1

            else:
                return -1
