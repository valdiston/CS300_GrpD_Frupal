from mapMaker import *
import Player

""" Map Configurations """
MAP_SIZE = 20

# dummy list of user added terrain
extraTerrain = ["forest", "rocks"]
reference_map = mapMaker(MAP_SIZE, extraTerrain)

""" Manual Test Map """
# reference_map = [['e'] * MAP_SIZE for i in range(MAP_SIZE)]

island_map  = [ [0]* MAP_SIZE for i in range(MAP_SIZE) ]

""" Status of Hero """
coordinates = [[0],[0]]


def display():
    for i in range(0, MAP_SIZE):
        for j in range(0, MAP_SIZE):
            if i == coordinates[0][0] and j == coordinates[1][0]:
                print('웃', end =' ')
            elif abs(i - coordinates[0][0] ) < 2 and abs(j - coordinates[1][0]) < 2:
                                print(str(reference_map[i][j]), end = ' ')
            else:
                print(str(' '), end=' ')
        print("")

def controls():
    print(  "Please enter   w   to walk\n"
          + "             a s d\n"
          + "Press h for help\n"
          + "Press q to quit\n"
          + "Press x to display map")


def main():    
    print("""Welcome to the Game!""")

    """ Testing Player class creation"""
    # p = Player.Player()
    # dictList = [{"e":"event"}, {"c":"clue"}, {"g":"grass"}]
    # p.initKeys(dictList)




    """placeholder variables"""
    energy = 10
    money = 10

    controls()
    display()

    while True:
        choice = input("")

        if choice == 'q':
            break
        elif choice == 'x':
            display()
        elif choice == 'h':
            controls()

        #########################################
        #           Update Status of Hero       #
        #           Game Logic                  #
        #########################################

        #Walking North
        elif choice == 'w':
            if coordinates[0][0] > 0:
                # cost = checkObstacle(coordinates[0][0]-1, reference_map)
                cost = 0
                if cost < energy:
                    energy -= cost
                    print("This move cost you " + str(cost) + " energy. You have " + str(energy) + " energy left")
                    coordinates[0][0] = coordinates[0][0] - 1
                else:
                    print("You don't have enough energy to mover here")
            else:
                energy -= 1
                print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")
                
        #Walking South
        elif choice == 's':
            """ Testing Events """
            # if p.location[1] < MAP_SIZE - 1:
            #     p.move_to([p.location[0],p.location[1] + 1], reference_map)
            if coordinates[0][0] < MAP_SIZE - 1:
                # cost = checkObstacle(coordinates[0][0] + 1, reference_map)
                cost = 0
                if cost < energy:
                    energy -= cost
                    print("This move cost you " + str(cost) + " energy. You have " + str(energy) + " energy left")
                    coordinates[0][0] = coordinates[0][0] + 1
                else:
                    print("You don't have enough energy to mover here")
            #Coordinates exceed map
            else:
                energy -= 1
                print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")
                
        #Walking East
        elif choice == 'a':
            if coordinates[1][0] > 0:
                # cost = checkObstacle(coordinates[1][0] - 1, reference_map)
                cost = 0
                if cost < energy:
                    energy -= cost
                    print("This move cost you " + str(cost)+ " energy. You have " + str(energy) + " energy left")
                    coordinates[1][0] = coordinates[1][0] - 1
                else:
                    print("You don't have enough energy to mover here")

            else:
                energy -= 1
                print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")
                
        #Walking West
        elif choice == 'd':
            if coordinates[1][0] < MAP_SIZE - 1:
                # cost = checkObstacle(coordinates[1][0] - 1, reference_map)
                cost = 0
                if cost < energy:
                    energy -= cost
                    print("This move cost you " + str(cost) + " energy. You have " + str(energy) + " energy left")
                    coordinates[1][0] = coordinates[1][0] + 1
                else:
                    print("You don't have enough energy to mover here")

            else:
                energy -= 1
                print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")

        else:
            print("Try a valid command""")
            
        display()


if __name__ == '__main__':
    main()
