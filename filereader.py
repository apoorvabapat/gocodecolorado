key ='AIzaSyDi2FIo6urHJi2UDakMvvyjRiqBqkKwhUk'


import csv 


def read_file():
	file =open('crime.csv','r')
	lines = 0
	lat=[]
	lang=[]
	crimeID = []
	with open('crime.csv'):
		csv_reader = csv.reader(file)
		for row in csv_reader:
			

			if not row[12].startswith('G') :
				lat.append(float(row[13]))
			if not row[13].startswith('G'):
				lang.append(float(row[12]))
			if not row[5].startswith('O'):
				crimeID.append(str(row[5]))
				print row[5]
			lines+=1
			if lines > 150:
					break
	return lat,lang,crimeID
