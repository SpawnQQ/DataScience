import numpy
import math 
from matplotlib import pyplot

def division(x,y):
	x=float(x)
	y=float(y)
	return x/y


def grafico(x):
	return x**x

x=numpy.linspace(-10,10,200)

pyplot.plot(x,[grafico(i) for i in x])

pyplot.axhline(0, color="gray")
pyplot.axvline(0, color="gray")

pyplot.xlim(-10, 10)
pyplot.ylim(-2, 2)

pyplot.show()