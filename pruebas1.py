#!/usr/bin/env python
import math 
from matplotlib import pyplot

def division(x,y):
	x=float(x)
	y=float(y)
	return x/y


def grafico(x):
	return math.sin(x)

x=range(-100,100)

pyplot.plot(x,[grafico(i) for i in x])

pyplot.axhline(0, color="gray")
pyplot.axvline(0, color="gray")

pyplot.xlim(-50, 50)
pyplot.ylim(-10, 10)

pyplot.show()