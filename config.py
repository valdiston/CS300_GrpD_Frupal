# Created by: 	Leesha Laforteza
# Group:	  	D
# This file contains the functions to edit the current configuration file
# line by line. Currently, it does not possess the ability to pick and choose
# what items to edit, so the user must 'go down the list' and edit (or skip)
# the items available in Frupal

# ---------------------------------------------------------------------------

import csv

# Read current config file into a dictionary
def edit_csv():
	with open('config.csv', mode='r', newline='') as infile:
		reader = csv.reader(infile)
	# with open('config.csv', mode = 'w') as outfile:
		# writer = csv.writer(outfile)
		next(reader)
		myDict = {rows[0]:rows[1] for rows in reader}
	for k,v in myDict.items():
		# Output each dictionary item
		if str.isdigit(v):
			print(k + ": " + v)
			# Enter a number to change the value
			newVal = input("Please input the new value, or re-enter the old value: ")
			myDict[k] = newVal
		# Call the function to write the file
	write_csv(myDict)

# Write the dictionary with the new values into the CSV file 
# by passing in the dictionary (myDict)
def write_csv(x):
	with open('config.csv', mode = 'w') as csv_file:
		fieldnames = ['item', 'value']
		new_writer = csv.DictWriter(csv_file,delimiter=',', lineterminator='\n', fieldnames=fieldnames)
		new_writer.writeheader()
		for k,v in x.items():
			new_writer.writerow({'item': k, 'value': v})

# End File