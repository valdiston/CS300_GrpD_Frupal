import csv

with open('easyGame.csv', 'r') as f:
    csv_reader = csv.reader(f)

    #first read in the number of objects in maze
    #then read in size of maze
    #then read in the objects 
    for row in csv_reader:
        if row == 0:
            mazeSize = {row[0]}
        if row == 1:
            objectCount = {row[0]}
        if row == 2:
            for x in (0, objectCount):



#
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
    for c in r:
        #function to randomly select object for maze element        