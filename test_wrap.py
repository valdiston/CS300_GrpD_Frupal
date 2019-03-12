from mapMaker import *
import Player
import os
from time import sleep

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
# coordinates = [[0], [0]]


# def display():
#     for i in range(0, MAP_SIZE):
#         display()
#         for j in range(0, MAP_SIZE):
#             if i == coordinates[0][0] and j == coordinates[1][0]:
#                 print('웃', end=' ')
#             elif abs(i - coordinates[0][0]) < 2 and abs(j - coordinates[1][0]) < 2:
#                                 print(str(reference_map[i][j]), end=' ')
#             else:
#                 print(str(' '), end=' ')
#         print("")


def testDisplay(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n Current Money: %-5s Current Energy: %-5s Gems: %d/%d\n" % (player.money, player.energy, int(player.gems),
                                                                    int(player.totalGems)))
    print("     XX" + ("X" * (player.mapSize * 2)) + "X")
    for i in range(0, player.mapSize):
        print("     X", end=' ')
        for j in range(0, player.mapSize):
            if i == player.location[0] and j == player.location[1]:
                # print('웃', end=' ')
                print('@', end=' ')
                player.dispMap[i][j] = player.refMap[i][j]
            elif abs(i - player.location[0]) < player.view and abs(j - player.location[1]) < player.view:
                                player.dispMap[i][j] = player.refMap[i][j]
                                print(str(player.refMap[i][j]), end=' ')
            else:
                print(str(player.dispMap[i][j]), end=' ')
        print("X", end=' ')
        print("")
    print("     XX" + ("X" * (player.mapSize * 2)) + "X\n\n")


def cheat(player):
    # player.dispMap = player.refMap
    # os.system('cls' if os.name == 'nt' else 'clear')
    while len(player.gemList) > 0:
        testDisplay(player)
        player.move_to(player.gemList[0], player.refMap)
        # sleep(2)

def controls():
    print(" Please enter   w   to walk\n"
          + "              a s d\n"
          + " Press h for help\n"
          + " Press q to quit\n"
          + " Press x to display map\n"
          + " Press p to shop\n"
          + " Press l to display the legend\n")


def main():    
    print("""Welcome to the Game!""")

    # #we'll need a menu for the user to choose preloaded games ie. easy, med, saved games...
    # #I'll use that to open up the correct file.
    # fileName = "config"
    # testPlayer = Player()
    # blankMap  = [ [0]* MAP_SIZE for i in range(MAP_SIZE) ]
    # print ("about to load game")
    # loadGame(fileName, testPlayer, blankMap)

    testPlayer = Player.Player()
    game = intro()
    loadGame(game, testPlayer)

    testDisplay(testPlayer)
    controls()
    # input("Press enter to continue > ")

    while testPlayer.gems < testPlayer.totalGems:
        if testPlayer.energy == 0 and testPlayer.money == 0:
            break

        choice = input("> ")

        if choice == 'q':
            break
        elif choice == 'x':
            # display()
            testDisplay(testPlayer)
        elif choice == 'h':
            testDisplay(testPlayer)
            controls()
        elif choice == 'p':
            testDisplay(testPlayer)
            testPlayer.shop()
            testDisplay(testPlayer)
        elif choice == 'l':
            testDisplay(testPlayer)
            testPlayer.legend()
        elif choice == "i am a dirty cheater":
            cheat(testPlayer)
        elif choice == "test":
            testPlayer.energy = 0
            testPlayer.money = 0

        #########################################
        #           Update Status of Hero       #
        #           Game Logic                  #
        #########################################

        # Walking North
        elif choice == 'w':
            if testPlayer.location[0] > 0:
                testPlayer.move_to([testPlayer.location[0] - 1, testPlayer.location[1]], testPlayer.refMap)
                testDisplay(testPlayer)
                
        # Walking South
        elif choice == 's':
            if testPlayer.location[0] < testPlayer.mapSize - 1:
                testPlayer.move_to([testPlayer.location[0] + 1, testPlayer.location[1]], testPlayer.refMap)
                testDisplay(testPlayer)
                
        # Walking East
        elif choice == 'a':

            if testPlayer.location[1] > 0:
                testPlayer.move_to([testPlayer.location[0], testPlayer.location[1] - 1], testPlayer.refMap)
                testDisplay(testPlayer)

        # Walking West
        elif choice == 'd':
            if testPlayer.location[1] < testPlayer.mapSize - 1:
                testPlayer.move_to([testPlayer.location[0], testPlayer.location[1] + 1], testPlayer.refMap)
                testDisplay(testPlayer)

        else:
            print("Try a valid command""")

    # end while loop
    if testPlayer.gems == testPlayer.totalGems:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n Congratulations, You have collected all of the Gems on the Island and completed the game !!!\n\n")
        input(" enter any key to exit the game> ")
    elif testPlayer.energy == 0 and testPlayer.money == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n         Oh No, you have run out of Money and Energy. With no alternatives left you slowly parish "
              "and die!", "\n\n\n                                                   You Lose!",
              "\n\n\n If you can't win any other way! - enter 'i am a dirty cheater' at the movement prompt to "
              "automatically win the game.\n\n")
        input(" enter any key to exit the game> ")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n Thanks for playing. Sorry you were not able to complete the game before quiting.\n\n")
        input(" enter any key to exit the game> ")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        input()
