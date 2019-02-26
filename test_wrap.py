from mapMaker import *
import Player
import clueMaker

""" Map Configurations """
MAP_SIZE = 5

# dummy list of user added terrain
# extraTerrain = ["forest", "rocks"]
# reference_map = mapMaker(MAP_SIZE, extraTerrain)

""" Manual Test Map """
# reference_map = [['e'] * MAP_SIZE for i in range(MAP_SIZE)]
# reference_map[4][4] = 'j'
# reference_map[4][3] = 'j'
# reference_map[0][1] = 'c'

island_map = [[0] * MAP_SIZE for i in range(MAP_SIZE)]

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


def testDisplay(coords, reference_map):
    for i in range(0, MAP_SIZE):
        for j in range(0, MAP_SIZE):
            if i == coords[0] and j == coords[1]:
                print('웃', end=' ')
            elif abs(i - coords[0]) < 2 and abs(j - coords[1]) < 2:
                                print(str(reference_map[i][j]), end=' ')
            else:
                print(str(' '), end=' ')
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

    """ Testing Player class creation"""
    p = Player.Player()
    dictList = [{"e": "event"}, {"c": "clue"}, {"h": "Hammer"}, {"s": "Shovel"}, {"b": "Boat"}]
    p.initKeys(dictList)
    p.money = 100
    p.add_item('h', 5, False)
    p.add_item('s', 5, False)
    p.add_item('b', 5, False)

    """ Testing clues """
    reference_map = [['e'] * MAP_SIZE for i in range(MAP_SIZE)]
    reference_map[2][4] = 'j'
    reference_map[4][3] = 'j'

    jewelList, clueList, terrainList, jewelString, terrainString = clueMaker.generateClues(reference_map, 0, 5)
    for x in range(0, len(clueList)):
        p.clues.append([clueList[x], jewelString[x], terrainString[x]])
    reference_map = clueMaker.clueMap(clueList, reference_map)

    """placeholder variables"""
    energy = 10
    money = 10

    controls()
    # display()
    testDisplay(p.location, reference_map)

    while True:
        choice = input("")

        if choice == 'q':
            break
        elif choice == 'x':
            # display()
            testDisplay(p.location, reference_map)
        elif choice == 'h':
            controls()
        elif choice == 'p':
            p.shop()

        #########################################
        #           Update Status of Hero       #
        #           Game Logic                  #
        #########################################

        # Walking North
        elif choice == 'w':
            """ Testing Player Move """
            if p.location[0] > 0:
                p.move_to([p.location[0] - 1, p.location[1]], reference_map)
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
            if p.location[0] < MAP_SIZE - 1:
                p.move_to([p.location[0] + 1, p.location[1]], reference_map)
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
            if p.location[1] > 0:
                p.move_to([p.location[0], p.location[1] - 1], reference_map)
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
            if p.location[1] < MAP_SIZE - 1:
                p.move_to([p.location[0], p.location[1] + 1], reference_map)
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
        testDisplay(p.location, reference_map)


if __name__ == '__main__':
    main()
