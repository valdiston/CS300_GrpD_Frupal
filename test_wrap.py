from mapMaker import *

class Player:

    def __init__(self):
        """ Integer variables - Status """
        self.money = 0
        self.energy = 0
        self.gems = 0

        """ Current Location """
        self.location = [0, 0]

        """ Item/Map Properties """
        self.ItemDict = {"obj1": {"attr 1": 0, "attr 2": 0},
                         "obj2": {"attr 1": 0, "attr 2": 0},
                         "obj3": {"attr 1": 0, "attr 2": 0}}
        self.terrainDict = {"terrain1": {"energy": 1, "item": None, "item energy": 0},
                            "terrain2": {"energy": 1, "item": None, "item energy": 0},
                            "terrain3": {"energy": 1, "item": None, "item energy": 0}}

        """ Inventory - Collected Items """
        self.inventory = [{"item": 0}]

    def add_to_inventory(self, item):
        if item is not None:
            for i in range(self.inventory.__len__()):
                if item in self.inventory[i]:
                    return 0
            to_add = {item: 0}
            self.inventory.append(to_add)
            return 1
        else:
            return -1

    def add_item(self, item):
        if item is None:
            return -1
        for i in range(self.inventory.__len__()):
            if item in self.inventory[i]:
                self.inventory[i][item] += 1
                return 1
        to_add = {item: 1}
        self.inventory.append(to_add)
        return 1

    def use_item(self, item):
        for i in range(self.inventory.__len__()):
            if item in self.inventory[i]:
                if self.inventory[i][item] > 0:
                    self.inventory[i][item] -= 1
                    return 1
                else:
                    return -1
        return -1


""" Map Configurations """
MAP_SIZE = 20

#dummy list of user added terrain
extraTerrain = ["forest", "rocks"]
reference_map = mapMaker(MAP_SIZE, extraTerrain)
        
island_map  = [ [0]* MAP_SIZE for i in range(MAP_SIZE) ]

""" Status of Hero """
coordinates = [[0],[0]]

""" Obstacle Dict"""
Obs = {"0": {"energy": 1, "item": "", "item energy": ""},
       "w": {"energy": 2, "item": "boat", "item energy": 0},
       "g": {"energy": 2, "item": "", "item energy": ""},
       "s": {"energy": 2, "item": "", "item energy": ""},
       "҉": {"energy": 1, "item": None, "item energy": ""}}


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


def checkObstacle(coordniates, reference): #skeleton of a function to check energy needed for a move based on object

    return Obs[reference_map[coordinates[0][0]][coordinates[1][0]]]["energy"]
        # nextPosit = reference[current_x][current_y]
        # if reference_map[coordinates[0][0]][coordinates[1][0]] == 0:
        #     return 1
        # elif reference_map[coordinates[0][0]][coordinates[1][0]] == 'w':
        #     return 2
        # elif reference_map[coordinates[0][0]][coordinates[1][0]] == 'g':
        #     return 1
        # elif reference_map[coordinates[0][0]][coordinates[1][0]] == 's':
        #     return 2
        # elif reference_map[coordinates[0][0]][coordinates[1][0]] == '҉':
        #     return 1
        # else:
        #     return 1
        # if Obs[reference_map[coordinates[0][0]][coordinates[1][0]]]["item"] is None:
        #     print("This obj doesn't require an item. obj = ", str(reference_map[coordinates[0][0]][coordinates[1][0]]),
        #           str(Obs[reference_map[coordinates[0][0]][coordinates[1][0]]]))


def main():    
    print("""Welcome to the Game!""")

    p = Player()
    print("inventory = ", p.inventory)
    ret = p.add_to_inventory("chainsaw")
    print("return = ", ret, "inventory = ", p.inventory)
    ret = p.add_item("chainsaw")
    print("return = ", ret, "inventory = ", p.inventory)
    ret = p.add_item("chainsaw")
    print("return = ", ret, "inventory = ", p.inventory)
    ret = p.use_item("chainsaw")
    print("return = ", ret, "inventory = ", p.inventory)
    ret = p.use_item("chainsaw")
    print("return = ", ret, "inventory = ", p.inventory)
    ret = p.use_item("chainsaw")
    print("return = ", ret, "inventory = ", p.inventory)

    exit()

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
                cost = checkObstacle(coordinates[0][0]-1, reference_map)
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
            if coordinates[0][0] < MAP_SIZE - 1:
                cost = checkObstacle(coordinates[0][0] + 1, reference_map)
                if cost < energy:
                    energy -= cost
                    print("This move cost you" + str(cost) + " energy. You have " + str(energy) + " energy left")
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
                cost = checkObstacle(coordinates[1][0] - 1, reference_map)
                if cost < energy:
                    energy -= cost
                    print("This move cost you" + str(cost)+ " energy. You have " + str(energy) + " energy left")
                    coordinates[1][0] = coordinates[1][0] - 1
                else:
                    print("You don't have enough energy to mover here")

            else:
                energy -= 1
                print("You have stepped on uncrossable water! You lost 1 energy as you were swept back ashore")
                
        #Walking West
        elif choice == 'd':
            if coordinates[1][0] < MAP_SIZE - 1:
                cost = checkObstacle(coordinates[1][0] - 1, reference_map)
                if cost < energy:
                    energy -= cost
                    print("This move cost you" + str(cost) + " energy. You have " + str(energy) + " energy left")
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
