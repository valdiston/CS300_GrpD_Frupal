from mapMaker import *
import Player
import clueMaker
import os

""" Map Configurations """
# MAP_SIZE = 5

# dummy list of user added terrain
# extraTerrain = ["forest", "rocks"]
# reference_map = mapMaker(MAP_SIZE, extraTerrain)

""" Map Configurations """
# MAP_SIZE = 20
# extraTerrain = ["forest", "rocks"]
# reference_map = mapMaker(MAP_SIZE, extraTerrain)
#
# island_map  = [ [0]* MAP_SIZE for i in range(MAP_SIZE) ]

""" Manual Test Map """
# reference_map = [['e'] * MAP_SIZE for i in range(MAP_SIZE)]
# reference_map[4][4] = 'j'
# reference_map[4][3] = 'j'
# reference_map[0][1] = 'c'

# island_map = [[0] * MAP_SIZE for i in range(MAP_SIZE)]

""" Status of Hero """
coordinates = [[0], [0]]


def display():
    for i in range(0, MAP_SIZE):
        display()
        for j in range(0, MAP_SIZE):
            if i == coordinates[0][0] and j == coordinates[1][0]:
                print('웃', end=' ')
            elif abs(i - coordinates[0][0]) < 2 and abs(j - coordinates[1][0]) < 2:
                                print(str(reference_map[i][j]), end=' ')
            else:
                print(str(' '), end=' ')
        print("")


def testDisplay(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Current Money: %-5s Current Energy: %-5s Gems: %s" % (player.money, player.energy, abs(-5 + player.gems)))
    for i in range(0, player.mapSize):
        for j in range(0, player.mapSize):
            if i == player.location[0] and j == player.location[1]:
                print('웃', end=' ')
                player.dispMap[i][j] = player.refMap[i][j]
            elif abs(i - player.location[0]) < player.view and abs(j - player.location[1]) < player.view:
                                player.dispMap[i][j] = player.refMap[i][j]
                                print(str(player.refMap[i][j]), end=' ')
            else:
                print(str(player.dispMap[i][j]), end=' ')
        print("")


def controls():
    print("Please enter   w   to walk\n"
          + "             a s d\n"
          + "Press h for help\n"
          + "Press q to quit\n"
          + "Press x to display map\n"
          + "Press p to shop\n")


def main():    
    print("""Welcome to the Game!""")

    # #we'll need a menu for the user to choose preloaded games ie. easy, med, saved games...
    # #I'll use that to open up the correct file.
    # fileName = "config"
    # testPlayer = Player()
    # blankMap  = [ [0]* MAP_SIZE for i in range(MAP_SIZE) ]
    # print ("about to load game")
    # loadGame(fileName, testPlayer, blankMap)
    #
    # p = Player()
    # print("inventory = ", p.inventory)
    # ret = p.add_to_inventory("chainsaw")
    # print("return = ", ret, "inventory = ", p.inventory)
    # ret = p.add_item("chainsaw")
    # print("return = ", ret, "inventory = ", p.inventory)
    # ret = p.add_item("chainsaw")
    # print("return = ", ret, "inventory = ", p.inventory)
    # ret = p.use_item("chainsaw")
    # print("return = ", ret, "inventory = ", p.inventory)
    # ret = p.use_item("chainsaw")
    # print("return = ", ret, "inventory = ", p.inventory)
    # ret = p.use_item("chainsaw")
    # print("return = ", ret, "inventory = ", p.inventory)
    #
    # exit()

    testPlayer = Player.Player()
    game = intro()
    loadGame(game, testPlayer)
    
    """ Testing Player class creation"""
    # p = Player.Player()
    # dictList = [{"e": "event"}, {"c": "clue"}, {"h": "Hammer"}, {"s": "Shovel"}, {"b": "Boat"}]
    # p.initKeys(dictList)
    # p.money = 100
    # p.add_item('h', 5, False)
    # p.add_item('s', 5, False)
    # p.add_item('b', 5, False)

    """ Testing clues """
    # reference_map = [['e'] * MAP_SIZE for i in range(MAP_SIZE)]
    # reference_map[2][4] = 'j'
    # reference_map[4][3] = 'j'

    jewelList, clueList, terrainList, jewelString, terrainString = clueMaker.generateClues(testPlayer.refMap, 0, testPlayer.mapSize)
    for x in range(0, len(clueList)):
        testPlayer.clues.append([clueList[x], jewelString[x], terrainString[x]])
    testPlayer.refMap = clueMaker.clueMap(clueList, testPlayer.refMap)

    """placeholder variables"""
    energy = 10
    money = 10

    controls()
    # display()
    testDisplay(testPlayer)

    while True:
        choice = input("")

        if choice == 'q':
            break
        elif choice == 'x':
            # display()
            testDisplay(testPlayer)
        elif choice == 'h':
            controls()
        elif choice == 'p':
            testPlayer.shop()

        #########################################
        #           Update Status of Hero       #
        #           Game Logic                  #
        #########################################

        # Walking North
        elif choice == 'w':
            """ Testing Player Move """
            if testPlayer.location[0] > 0:
                testPlayer.move_to([testPlayer.location[0] - 1, testPlayer.location[1]], testPlayer.refMap)
            """ End Test """

            # if coordinates[0][0] > 0:
            #     # cost = checkObstacle(coordinates[0][0]-1, reference_map)
            #     cost = 0
            #     if cost < energy:
            #         energy -= cost
            #         print("This move cost you " + str(cost) + " energy. You have " + str(energy) + " energy left")
            #         coordinates[0][0] = coordinates[0][0] - 1
            #     else:
            #         print("You don't have enough energy to mover here")
            # else:
            #     energy -= 1
            #     print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")
                
        # Walking South
        elif choice == 's':
            """ Testing Player Move """
            if testPlayer.location[0] < testPlayer.mapSize - 1:
                testPlayer.move_to([testPlayer.location[0] + 1, testPlayer.location[1]], testPlayer.refMap)
            """ End Test """

            # if coordinates[0][0] < MAP_SIZE - 1:
            #     # cost = checkObstacle(coordinates[0][0] + 1, reference_map)
            #     cost = 0
            #     if cost < energy:
            #         energy -= cost
            #         print("This move cost you " + str(cost) + " energy. You have " + str(energy) + " energy left")
            #         coordinates[0][0] = coordinates[0][0] + 1
            #     else:
            #         print("You don't have enough energy to mover here")
            # #Coordinates exceed map
            # else:
            #     energy -= 1
            #     print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")
                
        # Walking East
        elif choice == 'a':
            """ Testing Player Move """
            if testPlayer.location[1] > 0:
                testPlayer.move_to([testPlayer.location[0], testPlayer.location[1] - 1], testPlayer.refMap)
            """ End Test """

            # if coordinates[1][0] > 0:
            #     # cost = checkObstacle(coordinates[1][0] - 1, reference_map)
            #     cost = 0
            #     if cost < energy:
            #         energy -= cost
            #         print("This move cost you " + str(cost)+ " energy. You have " + str(energy) + " energy left")
            #         coordinates[1][0] = coordinates[1][0] - 1
            #     else:
            #         print("You don't have enough energy to mover here")
            #
            # else:
            #     energy -= 1
            #     print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")
                
        # Walking West
        elif choice == 'd':
            """ Testing Player Move """
            if testPlayer.location[1] < testPlayer.mapSize - 1:
                testPlayer.move_to([testPlayer.location[0], testPlayer.location[1] + 1], testPlayer.refMap)
            """ End Test """

            # if coordinates[1][0] < MAP_SIZE - 1:
            #     # cost = checkObstacle(coordinates[1][0] - 1, reference_map)
            #     cost = 0
            #     if cost < energy:
            #         energy -= cost
            #         print("This move cost you " + str(cost) + " energy. You have " + str(energy) + " energy left")
            #         coordinates[1][0] = coordinates[1][0] + 1
            #     else:
            #         print("You don't have enough energy to mover here")
            #
            # else:
            #     energy -= 1
            #     print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")

        else:
            print("Try a valid command""")
            
        # display()
        testDisplay(testPlayer)


if __name__ == '__main__':
    main()
