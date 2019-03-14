from mapMaker import *
import Player
import os


def Display(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n %sCurrent Money: %-5s Current Energy: %-5s Gems: %d/%d\n" % (' ' * (player.mapSize//3), player.money,
          player.energy, int(player.gems), int(player.totalGems)))
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
    print("     XX" + ("X" * (player.mapSize * 2)) + "X\n")
    print(" %s Press h to display the help menu\n" % (' ' * (player.mapSize//3)))


def cheat(player):
    player.energy = 1000000
    player.money = 1000000
    while len(player.gemList) > player.gems:
        Display(player)
        player.move_to(player.gemList[0], player.refMap)
    player.dispMap = player.refMap
    Display(player)


def controls():
    print(" Please enter   w   to walk\n"
          + "              a s d\n"
          + " Press q to quit\n"
          + " Press x to display map\n"
          + " Press p to shop\n"
          + " Press l to display the legend\n"
          + " If you can't win otherwise pressing c will auto win the game\n")


def main():
    print("""Welcome to the Game!""")

    NewPlayer = Player.Player()
    game = intro()
    try:
        loadGame(game, NewPlayer)
    except FileNotFoundError:
        print("\nIt looks like you don't have an previous saved custom games!")
        input("press any key to continue (game will exit)>")
        return

    os.system('mode con: cols=120 lines=%s' % (30 + NewPlayer.mapSize))
    Display(NewPlayer)
    controls()
    print(" Your Player character is represented as an \'@\' in this game. This symbol will move around as you move!\n")

    while NewPlayer.gems < NewPlayer.totalGems:
        if NewPlayer.energy == 0 and NewPlayer.money == 0:
            break

        choice = input("> ")

        if choice == 'q':
            break
        elif choice == 'x':
            Display(NewPlayer)
        elif choice == 'h':
            Display(NewPlayer)
            controls()
        elif choice == 'p':
            Display(NewPlayer)
            NewPlayer.shop()
            Display(NewPlayer)
        elif choice == 'l':
            Display(NewPlayer)
            NewPlayer.legend()
        elif choice == "i am a dirty cheater":
            cheat(NewPlayer)
        elif choice == 'c':
            cheat(NewPlayer)


        #########################################
        #           Update Status of Hero       #
        #           Game Logic                  #
        #########################################

        # Walking North
        elif choice == 'w':
            if NewPlayer.location[0] > 0:
                NewPlayer.move_to([NewPlayer.location[0] - 1, NewPlayer.location[1]], NewPlayer.refMap)
                Display(NewPlayer)

        # Walking South
        elif choice == 's':
            if NewPlayer.location[0] < NewPlayer.mapSize - 1:
                NewPlayer.move_to([NewPlayer.location[0] + 1, NewPlayer.location[1]], NewPlayer.refMap)
                Display(NewPlayer)

        # Walking East
        elif choice == 'a':

            if NewPlayer.location[1] > 0:
                NewPlayer.move_to([NewPlayer.location[0], NewPlayer.location[1] - 1], NewPlayer.refMap)
                Display(NewPlayer)

        # Walking West
        elif choice == 'd':
            if NewPlayer.location[1] < NewPlayer.mapSize - 1:
                NewPlayer.move_to([NewPlayer.location[0], NewPlayer.location[1] + 1], NewPlayer.refMap)
                Display(NewPlayer)

        else:
            print("Try a valid command""")

    # end while loop
    if NewPlayer.gems == NewPlayer.totalGems:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n Congratulations, You have collected all of the Gems on the Island and completed the game !!!\n\n")
        input(" enter any key to exit the game> ")
    elif NewPlayer.energy == 0 and NewPlayer.money == 0:
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
