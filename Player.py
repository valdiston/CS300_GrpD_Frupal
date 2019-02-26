import mapMaker
import Event
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
        # list of clues
        self.clues = []
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

    def setup(self):
        # todo fill keyDict, ItemDict, terrainDict, and inventory prior to setting up map
        self.refMap = mapMaker.mapMaker(self.mapSize, self.newTerrain)

    """ Key related functions"""

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

    """ Terrain Functions"""

    # returns = 1: if item is success, -1: if terrain is None
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
            answer = input("Please pick a number corresponding to an item or 0 to exit")
        return int(answer)

    def shop(self):
        print("\n --------------------------------------------")
        print("|[$][$][$] Welcome to the Item Shop [$][$][$]|\n --------------------------------------------")
        print("|             Current Gold: %4d             |" % self.money)
        print(" --------------------------------------------")
        print("|       Items Available for purchase:        |")
        print("|                                            |")
        print("|       1. Energy Bar || Cost:", self.energyBarCost, "gold        |")

        if self.view == 1:
            print("|       2. Binoculars || Cost: 5 gold        |")
        else:
            print("|       2. Binoculars || Already Purchased   |")
        i = 3
        for key in self.ItemDict.keys():
            if not self.ItemDict[key]["owned"]:
                print("|       %d. %-10s %s %d gold        |" % (i, self.getKey(key), "|| Cost:",
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
                print("Sorry you don't have enough money to purchase this item")
                return
        elif answer == 2 and self.view == 1:
            if self.money >= 5:
                self.money -= 5
                # placeholder value
                self.view += 2
                print()
            else:
                print("Sorry you don't have enough money to purchase this item")
                return
        else:
            x = 3
            keys = list(self.ItemDict.keys())
            if not self.ItemDict[keys[answer - x]]["owned"]:
                if self.money >= self.ItemDict[keys[answer - x]]["cost"]:
                    self.money -= self.ItemDict[keys[answer - x]]["cost"]
                    self.ItemDict[keys[answer - x]]["owned"] = True
                    print()
                    return
                else:
                    print("Sorry you don't have enough money to purchase this item")
                    return
            else:
                print(" Whoops! You already own this item. At the moment you cannot buy another.\n")

    """ Movement Functions """

    def move_to(self, coords, referenceMap):
        # key = self.getKey(referenceMap[coords[0]][coords[1]])
        key = referenceMap[coords[0]][coords[1]]
        if key not in (self.terrainDict or ['e', 'j', '$', 'c', ' ']):
            print("Map contains an unknown character")
            return -1
        else:
            # # Block for stepping on an item
            # if key in self.ItemDict:
            #     print("You have come across a ", key, " during your journey")
            #     if key == "gem":
            #         self.gems += 1
            #         self.location = coords
            #         referenceMap[coords[0]][coords[1]] = 'g'
            #         return 1
            #
            #     elif self.ItemDict[key]["cost"] > 0:
            #         cost = self.ItemDict[key]["cost"]
            #         answer = input("This item costs $" + cost + ". Would you like to buy it? (y/n)")
            #         if str(answer) == 'y':
            #             if self.money >= cost:
            #                 self.add_to_inventory(key)
            #                 self.money -= cost
            #                 print("You have just bought a ", key, "  and added it to your inventory")
            #                 self.location = coords
            #                 referenceMap[coords[0]][coords[1]] = 'g'
            #                 return 1
            #             else:
            #                 print("Sorry! You don't have enough money to purchase this item... Please come back when"
            #                       " you have more money")
            #                 self.location = coords
            #                 return 1
            #         else:
            #             self.location = coords
            #             return 1
            #
            #     elif self.ItemDict[key]["cost"] == 0:
            #         self.energy += self.ItemDict[key]["energy"]
            #         if self.ItemDict[key]["money"] >= 0:
            #             self.money += self.ItemDict[key]["money"]
            #         if self.ItemDict[key]["vision"] >= 0:
            #             self.view += self.ItemDict[key]["vision"]
            #             if key == "binoculars":
            #                 self.add_to_inventory(key)
            #                 print("You have just found a pair of", key, "  and added it to your inventory")
            #                 print("Your vision radius has increased to %s" % self.view)
            #                 self.location = coords
            #                 referenceMap[coords[0]][coords[1]] = 'g'
            #                 return 1
            #         self.add_to_inventory(key)
            #         print("You have just found a ", key, "  and added it to your inventory")
            #         self.location = coords
            #         referenceMap[coords[0]][coords[1]] = 'g'
            #         return 1

            # if the location contains a gem
            if key == "j":
                self.gems += 1
                self.location = coords
                referenceMap[coords[0]][coords[1]] = ' '
                print("Wow! You managed to find one of the hidden island gems!!!")
                print("Collected Gems: %d/5" % self.gems)
                return 1

            if key == "$":
                self.money += self.goldFound
                self.location = coords
                referenceMap[coords[0]][coords[1]] = ' '
                return 1

            if key == ' ':
                self.location = coords
                return 1

            # block for stepping on terrain
            elif key in self.terrainDict:
                energy = self.terrainDict[key]["energy"]
                item = self.terrainDict[key]["item"]
                itemEngery = self.terrainDict[key]["item energy"]
                if item is not None:
                    if self.ItemDict[item]["owned"]:
                        if self.energy >= itemEngery:
                            self.energy -= itemEngery
                            self.location = coords
                            return 1
                        else:
                            print("Sadly you don't have the energy to continue in this direction")
                            return 0
                    else:
                        if self.energy >= energy:
                            self.energy -= energy
                            self.location = coords
                            return 1
                        else:
                            print("Sadly you don't have the energy to continue in this direction")
                            return 0
                else:
                    if self.energy >= energy:
                        self.energy -= energy
                        self.location = coords
                        return 1
                    else:
                        print("Sadly you don't have the energy to continue in this direction")
                        return 0

            # block for stepping on an event
            elif key == "e":
                self.location = coords
                referenceMap[coords[0]][coords[1]] = ' '
                print("You have encountered an event!")
                event = Event.Energy("event")
                eventType = random.randint(1, 2)
                if eventType == 1:  # 1 signifies energy event
                    newEnrg = random.randint(5, 15)
                    self.energy += event.trigger(self.energy, newEnrg, "energy")
                    return 1
                elif eventType == 2:  # 2 signifies money event
                    newMoney = random.randint(5, 15)
                    self.money += event.trigger(self.money, newMoney, "money")
                    return 1
                else:
                    return 0

            # block for stepping on a clue
            elif key == "c":
                for clue in self.clues:
                    if clue[0][0] == coords[0] and clue[0][1] == coords[1]:
                        print("You Have found a clue to the location of a gem!")
                        print("The clue reads: ", clue[1])
                        print("There's a chance this clue could be fake. If the following statement is true, the clue"
                              " is correct")
                        print(clue[2])
                        self.clues.pop(self.clues.index(clue))
                        referenceMap[coords[0]][coords[1]] = ' '
                        break
                self.location = coords
                return 1

            else:
                print(key, "is somehow not a terrain, event, clue, or gem. Something has gone wrong setting up the "
                           "game")
                return -1
