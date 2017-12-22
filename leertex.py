def leer_excel():	
	#Lee el fichero .ele y lo asigna a la lista lelementos
	lineas = open("lista.csv").readlines()
	#lineas = open("africa473.ele").readlines()
	vectortexto	 = [[m.strip() for m in n] for n in [linea.split(",") for linea in lineas]]
	return vectortexto
for row in leer_excel():
	if row[1].isdigit():
		if int(row[1]) != 0:
			print row
	else:
		print row