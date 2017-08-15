"""
Eric Smith
Project 2 - Part 1

April 4th, 2017

"""
import numpy
from math import pi, cos
import matplotlib.pyplot as plt
from newtonPoly import *

def f(x):
    return -1/(1+(25*(x**2)))

# uniform intervals for n = 4,8,16
xData4 = numpy.arange(-1,1.5,0.5) # n = 4
xData8 = numpy.arange(-1,1.25,0.25) # n = 8
xData16 = numpy.arange(-1,1.125,0.125) # n = 16

# Chebyshev intervals for n = 4,8,16
xDataCheby4 = [numpy.float64(-1*cos(i*(pi/4))) for i in range(0,5)]
xDataCheby8 = [numpy.float64(-1*cos(i*(pi/8))) for i in range(0,9)]
xDataCheby16 = [numpy.float64(-1*cos(i*(pi/16))) for i in range(0,17)]

# coefficients for uniform points
coeff4 = coeffts(xData4, [f(x) for x in xData4])
coeff8 = coeffts(xData8, [f(x) for x in xData8])
coeff16 = coeffts(xData16, [f(x) for x in xData16])

# coefficients for Chebyshev points
coeffCheby4 = coeffts(xDataCheby4, [f(x) for x in xDataCheby4])
coeffCheby8 = coeffts(xDataCheby8, [f(x) for x in xDataCheby8])
coeffCheby16 = coeffts(xDataCheby16, [f(x) for x in xDataCheby16])

# fine mesh
mesh = numpy.arange(-1.5,1.51,0.01)

plt.close('all')
fig, axarr = plt.subplots(3, 2,figsize=(12,8), sharex=True, sharey=True)
plt.suptitle("Interpolation on Uniform and Chebyshev Distributions")
plt.axis([ -1.5, 1.5, -1.5, 1.5 ])
plt.subplots_adjust(hspace = 0.3)

# four uniform
axarr[0, 0].plot(xData4, [f(x) for x in xData4], 'ro')
axarr[0, 0].plot(mesh, [f(x) for x in mesh])
axarr[0, 0].plot(mesh, evalPoly(coeff4, xData4, mesh), '--')
axarr[0, 0].set_title('Uniform n = 4')

# eight uniform
axarr[1, 0].plot(xData8, [f(x) for x in xData8], 'ro')
axarr[1, 0].plot(mesh, [f(x) for x in mesh])
axarr[1, 0].plot(mesh, evalPoly(coeff8, xData8, mesh), '--')
axarr[1, 0].set_title('Uniform n = 8')

# sixteen uniform
axarr[2, 0].plot(xData16, [f(x) for x in xData16], 'ro')
axarr[2, 0].plot(mesh, [f(x) for x in mesh])
axarr[2, 0].plot(mesh, evalPoly(coeff16, xData16, mesh), '--')
axarr[2, 0].set_title('Uniform n = 16')

# four Chebyshev
axarr[0, 1].plot(xDataCheby4, [f(x) for x in xDataCheby4], 'ro')
axarr[0, 1].plot(mesh, [f(x) for x in mesh])
axarr[0, 1].plot(mesh, evalPoly(coeffCheby4, xDataCheby4, mesh), '--')
axarr[0, 1].set_title('Chebyshev n = 4')

# eight Chebyshev
axarr[1, 1].plot(xDataCheby8, [f(x) for x in xDataCheby8], 'ro')
axarr[1, 1].plot(mesh, [f(x) for x in mesh])
axarr[1, 1].plot(mesh, evalPoly(coeffCheby8, xDataCheby8, mesh), '--')
axarr[1, 1].set_title('Chebyshev n = 8')

# sixteen Chebyshev
axarr[2, 1].plot(xDataCheby16, [f(x) for x in xDataCheby16], 'ro')
axarr[2, 1].plot(mesh, [f(x) for x in mesh])
axarr[2, 1].plot(mesh, evalPoly(coeffCheby16, xDataCheby16, mesh), '--')
axarr[2, 1].set_title('Chebyshev n = 16')

# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

plt.show()