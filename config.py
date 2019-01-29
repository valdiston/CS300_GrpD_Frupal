import csv
#from inventory import inv

# Read current config file into a dictionary
with open('config.csv', mode='r') as infile:
	reader = csv.reader(infile)
with open('config.csv', mode = 'w' as outfile):
	writer = csv.writer(outfile)
	myDict = {rows[0]:rows[1] for rows in reader)
for k,v in myDict.items():
	# Output each dictionary item
	print(k + ": " v + '\n')
	# Enter a number to change the value
	v = input("Please input the new value, or re-enter the old value.")
	# When iteration is done, output dictionary to a CSV file
	
with open('config.csv', mode = 'w') as csv_file:
fieldnames = ['item', 'value']
	new_writer = csv.DictWriter(csv_file, fieldnames=fieldnames);

new_writer.writeheader()
for k,v in myDict.items():
	new_writer.writerow('item': k, 'value': v)