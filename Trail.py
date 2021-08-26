from numpy import random
from matplotlib import pyplot
x = random.rand(100)
c = random.rand(100)
pyplot.plot(x,2*x+c,'s')
pyplot.xlabel("X Value")
pyplot.ylabel("Y Value")
pyplot.show()