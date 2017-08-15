"""
Eric Smith
Project 2 - Part 2

April 4th, 2017

"""
import numpy as numpy
from cubicSpline import *
from math import pi, cos
import matplotlib.pyplot as plt

def f(x):
    return -1/(1+(25*(x**2)))

# uniform intervals for n = 2,4,8,16
xData2 = numpy.asarray(numpy.arange(-1.0,2.0)) # n = 2
xData4 = numpy.asarray(numpy.arange(-1,1.5,0.5)) # n = 4
xData8 = numpy.asarray(numpy.arange(-1,1.25,0.25)) # n = 8
xData16 = numpy.asarray(numpy.arange(-1,1.125,0.125)) # n = 16

yData2 = numpy.asarray([f(x) for x in xData2])
yData4 = numpy.asarray([f(x) for x in xData4])
yData8 = numpy.asarray([f(x) for x in xData8])
yData16 = numpy.asarray([f(x) for x in xData16])

k2 = curvatures(xData2, yData2)
k4 = curvatures(xData4, yData4)
k8 = curvatures(xData8, yData8)
k16 = curvatures(xData16, yData16)

mesh = numpy.arange(-1.5, 1.51, 0.01)

plt.close('all')
fig, axarr = plt.subplots(2, 2, sharex=True, sharey=True)
plt.suptitle('Cubic Spline Interpolation')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

# n = 2
axarr[0, 0].plot(xData2, yData2, 'ro')
axarr[0, 0].plot(mesh, [f(x) for x in mesh])
axarr[0, 0].plot(mesh, [evalSpline(xData2, yData2, k2, mesh[i]) for i in range(len(mesh))], '--')
axarr[0, 0].set_title('n = 2')

# n = 4
axarr[0, 1].plot(xData4, yData4, 'ro')
axarr[0, 1].plot(mesh, [f(x) for x in mesh])
axarr[0, 1].plot(mesh, [evalSpline(xData4, yData4, k4, mesh[i]) for i in range(len(mesh))], '--')
axarr[0, 1].set_title('n = 4')

# n = 8
axarr[1, 0].plot(xData8, yData8, 'ro')
axarr[1, 0].plot(mesh, [f(x) for x in mesh])
axarr[1, 0].plot(mesh, [evalSpline(xData8, yData8, k8, mesh[i]) for i in range(len(mesh))], '--')
axarr[1, 0].set_title('n = 8')

# n = 16
axarr[1, 1].plot(xData16, yData16, 'ro')
axarr[1, 1].plot(mesh, [f(x) for x in mesh])
axarr[1, 1].plot(mesh, [evalSpline(xData16, yData16, k16, mesh[i]) for i in range(len(mesh))], '--')
axarr[1, 1].set_title('n = 16')

# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

plt.show()