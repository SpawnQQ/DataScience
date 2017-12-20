import numpy
def vector():
	x=[]
	for i in range(0,6):
		x.append(i)
	return x

print "Lista: ", vector()
print "Promedio: ", numpy.mean(vector())
