import csv
with open('lista.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
			#print ', '.join(row)
	print spamreader[0]
	
