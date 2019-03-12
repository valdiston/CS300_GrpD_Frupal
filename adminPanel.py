import csv


def save():
    # open game file and read in item and terrain info. store in player object
    with open('custom.csv', mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')

        gold = input("  How much gold would you like to start the game with? ")
        while not gold.isnumeric():
            gold = input("  Gold value must be an integer value >= 0: ")

        writer.writerow(['gold', gold])

        energy = input("  How much energy would you like to start the game with? ")
        while not energy.isnumeric():
            energy = input("  Energy value must be an integer value >= 0: ")

        writer.writerow(['energy', energy])

        size = input("  How would you like the play area to be? Note: size can be between 5 and 50"
                     "\n  Map Size: ")

        try:
            if not size.isnumeric():
                end = False
            elif int(size) < 5 or int(size) > 50:
                end = False
            else:
                end = True
        except Exception as e:
            end = False

        while not end:
            size = input("  Map Size must be an integer value between 5 and 50: ")
            try:
                if not size.isnumeric():
                    end = False
                elif int(size) < 5 or int(size) > 50:
                    end = False
                else:
                    end = True
            except Exception as e:
                end = False

        writer.writerow(['mapSize', size])


    #     energyBarCost = next(reader)
    #     player.energyBarCost = int(energyBarCost[1])
    #     goldFound = next(reader)
    #     player.goldFound = int(goldFound[1])
    #     gems = next(reader)
    #     player.totalGems = int(gems[1])
    #
    #     newTerrain = []
    #     newTerrain.append(0)
    #     next(reader)
    #
    #     for row in reader:
    #             if int(row[1]) == 1:
    #                 player.add_terrain(row[0].strip(), row[2].strip(), row[3].strip(), row[5].strip())
    #                 #if not standard terrain make list of addedTerrain for building map
    #                 if row[0] != 'w' and row[0] != 'p':
    #                     newTerrain[0] += 1
    #                     newTerrain.append(row[0].strip())
    #             # else row must contain item
    #             else:
    #                 player.add_item(row[0].strip(), row[4].strip(), False)
    # player.newTerrain = newTerrain
    # if fileName not in ['easy', 'medium', 'hard']:
    #     player.initKeys(fileName)
    # else:
    #     player.initKeys()
    # player.setup()


if __name__ == '__main__':
    save()
