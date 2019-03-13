import csv


def checkSize(mapSize):
    if not mapSize.isnumeric():
        mapSize = input("  Map Size must be an integer value between 5 and 50: ")
        return checkSize(mapSize)
    elif int(mapSize) > 50 or int(mapSize) < 5:
        mapSize = input("  Map Size must be an integer value between 5 and 50: ")
        return checkSize(mapSize)
    else:
        return mapSize


def checkGems(gems, size):
    if not gems.isnumeric():
        gems = input("  The number of gems must be a non-negative number: ")
        return checkGems(gems, size)
    elif int(gems) >= ((3/4) * int(size)):
        gems = input("  That's probably too many gems. Try something smaller than " + str((3//4) * int(size)) + ": ")
        return checkGems(gems, size)
    else:
        return gems

def askObstacle(used, keydict, items):
    answer = input("  Would you like to add any more obstacles to the game? [Yes/No]: ")
    while not (answer.lower() != 'yes' or answer.lower() != 'no'):
        answer = input("  Please enter Yes or No: ")
    if answer.lower() == 'yes':
        getObstacle(used, keydict, items)
        return True
    else:
        return False

def getObstacle(used, keydict, items):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("X                                                Add Obstacle                                              X")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
    print("  Choose a name to be displayed for your new obstacle.\n")
    obstacle = input("  Obstacle name (limited to 12 chars): ")
    obstacle = obstacle[0:12]

    print("\n\n  Choose a character that will represent this obstacle on the island")
    print("  Currently these characters are already in use and cannot be chosen: " + str(used) + "\n")
    obChar = input("  Character for \"" + obstacle + "\": ")
    while obChar[0] in used:
        obChar = input("  You must choose a character that isn't already taken: ")
    obChar= obChar[0]
    keydict.update({obChar:obstacle})
    used.append(obChar)

    print("\n\n  Obstacles take their toll on you while you explore the island by draining your energy.")
    print("  The harder the obstacle the more energy it should likely expend when you travel through it.")
    print("  How much energy should " + obstacle + " expend when you cross it?\n")
    energy = input("  Energy expended: ")
    while not energy.isnumeric():
        energy = input("  The energy cost must be a number: ")

    print("\n\n  Some obstacles will have items that can be purchased from the shop that will aid in traversing them.")
    print("  These items will reduce the amount of energy that you expend while crossing " + obstacle + " after purchase.\n")
    answer = input("  Would you like to add an item for " + obstacle + "? [Yes/No]: ")
    while not (answer.lower() != 'yes' or answer.lower() != 'no'):
        answer = input("  You must pick yes or no: ")
    if answer == 'yes':
        print("\n\n  What is the name of the item that will assist you in traversing " + obstacle + "?\n")
        item = input("  Item Name(10 char limit):  ")
        item = item[0:10]

        print("\n\n  Just as with the Obstacle you must choose a character to represent this item.")
        print("  This character will not be shown during the game so feel free to use numbers")
        print("  Currently these characters are already in use and cannot be chosen: " + str(used) + "\n")
        itemChar = input("  Item Character: ")
        while itemChar[0] in used:
            itemChar = input("  You must choose a character that isn't already taken: ")
        itemChar = itemChar[0]
        keydict.update({itemChar: item})
        used.append(itemChar)

        print("\n\n  Now you must choose how much energy you expend crossing " + obstacle + " while you have " + item + ".\n")
        itemEnergy = input("  Energy expended with item: ")
        while not itemEnergy.isnumeric():
            itemEnergy = input("  The energy cost must be a number: ")

        print("\n\n  These items are available to you via the in game shop.")
        print("  How much gold will your item \"" + item + "\" cost?\n")
        cost = input("  Item cost: ")
        while not cost.isnumeric():
            cost = input("  The gold cost must be a number: ")
        print()
        items.append([obChar, 1, energy, itemChar, 0, itemEnergy])
        items.append([itemChar, 0, 0, 0, cost, 0])
    else:
        items.append([obChar, 1, energy, 0, 0, 0])

def save():

    print("\n                                 Welcome to the custom game creator!!!")
    print("\n       The following questions will guide you through the setup of your own custom game of Frupal")

    with open('custom.csv', mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')

        # starting gold input
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                             Starting Gold                                                X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        gold = input("How much gold would you like to start the game with? ")
        while not gold.isnumeric():
            gold = input("  Gold value must be an integer value >= 0: ")
        writer.writerow(['gold', gold])

        # starting energy input
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                             Starting Energy                                              X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        energy = input("  How much energy would you like to start the game with? ")
        while not energy.isnumeric():
            energy = input("  Energy value must be an integer value >= 0: ")
        writer.writerow(['energy', energy])

        # Map size input
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                             Size of Map                                                  X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        print("  How large of an island would you like to have for your game? (AxA grid where 5 <= A <= 50)\n")
        mapSize = input("  Map Size: ")
        mapSize = checkSize(mapSize)
        writer.writerow(['mapSize', mapSize])

        # number of gems input
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                             Number of Gems                                               X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        print("  How many gems will you need to collect on your island?\n")
        gems = input("  Number of Gems: ")
        gems = checkGems(gems, mapSize)
        writer.writerow(['gems', gems])

        # cost of energy bar input
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                              Energy Bars                                                 X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        print("  Energy bars are how you can recover your energy in the game of Frupal.")
        print("  These are purchased from the store in this game at a cost of gold.")
        print("  How much gold should Energy Bars cost you to purchase?\n")
        energyBarCost = input("  Energy Bar cost: ")
        while not energyBarCost.isnumeric():
            energyBarCost = input("  The Energy Bar cost must be a non negative number: ")
        writer.writerow(['energyCost', energyBarCost])
        print("\n  How much energy should energy bars give you?\n")
        energyBar = input("  Energy bar recovery: ")
        while not energyBar.isnumeric():
            energyBarCost = input("  The amount of energy must be a non negative number: ")
        writer.writerow(['energyCBar', energyBar])

        # gold found from treasures input
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                                Treasures                                                 X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        print("  On the island of Frupal you will occasionally come across a small treasure represented by a \'$\'.")
        print("  Each time you find one you will gain a specific amount of gold that can be used to buy items.")
        print("  How much gold would you like treasures to give?\n")
        goldFound = input("  Amount of gold: ")
        while not goldFound.isnumeric():
            goldFound = input("  The amount of gold must be a non negative number: ")
        writer.writerow(['goldFound', goldFound])


        # cost of binoculars input
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                                Binoculars                                                X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        print("  There is a special item that you can buy in the shop called Binoculars.")
        print("  Purchasing this will increase the amount of terrain you uncover in your travels")
        print("  How much would you like this item to cost?\n")
        binocularCost = input("  Cost of Binoculars: ")
        while not binocularCost.isnumeric():
            binocularCost = input("  The cost of the Binoculars must be a non negative number: ")
        writer.writerow(['binocularCost', binocularCost])



        # terrain and items
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                               Game Obstacles                                             X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        used = ['p', 'w', '$', '*', 'c', 'e', 'b']
        keydict = {'p': "Plain", 'w': "Water", '$': "Sack of Gold", '*': "Gem", 'c': "Clue", 'e': "Event", 'b': "Boat"}
        items = [['w', 1, 5, 'b', 0, 1], ['p', 1, 1, 0, 0, 1], ['b', 0, 0, 0, 20, 0]]
        writer.writerow(['key', ' terrain', ' energy', ' item', ' cost', ' item energy'])

        print("  In the following section you will decide which obstacles and items will be available in your game.")
        print("  By default the terrain types Water and Plains will be part of the game and cannot be modified\n")

        result = askObstacle(used, keydict, items)
        while result:
            result = askObstacle(used, keydict, items)

        dictFile = open('customKeyDict.csv', mode='w', newline='')
        dictwriter = csv.writer(dictFile, delimiter=',')
        for key in keydict:
            dictwriter.writerow([key, keydict[key]])
        dictFile.close()
        for item in items:
            writer.writerow(item)


if __name__ == '__main__':
    save()
