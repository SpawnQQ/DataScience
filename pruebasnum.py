import numpy
from matplotlib import pyplot
x=numpy.linspace(0, 2*numpy.pi, 100)
y=numpy.sin(x)
pyplot.xlim(0, 6)
print "promedio: ", x.mean()
print "desv. estandar: ", numpy.std(x)
pyplot.ylim(-2, 2)
pyplot.plot(x, y)
pyplot.show()