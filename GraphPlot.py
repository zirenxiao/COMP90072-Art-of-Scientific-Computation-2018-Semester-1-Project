# MatPlotlib
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import pylab
# Scientific libraries
import numpy as np
from scipy import stats


class GraphPlot:
    def plotXY(self, x, y, xComment="X", yComment="Y"):
        plt.plot(x, y)
        plt.xlabel(xComment)
        plt.ylabel(yComment)
        plt.show()
    def plotBestFit(self, rawXs, rawYs, xComment="X", yComment="Y"):
        xs = np.array(rawXs)
        ys = np.array(rawYs)
        m, b = self.bestFitSlopeAndIntercept(xs, ys)
        regressionLine = [(m*x)+b for x in xs]
        plt.scatter(xs, ys)
        plt.plot(xs, regressionLine)
        plt.axis([min(xs), max(xs), min(ys), max(ys)])
        plt.xlabel(xComment)
        plt.ylabel(yComment)
        print("The equation of current line is: y = " + str(m) + "x + " + str(b))
        plt.show()
    def bestFitSlopeAndIntercept(self, xs, ys):
        m = ((mean(xs) * mean(ys)) - mean(xs*ys)) / ((mean(xs) * mean(xs) - mean(xs*xs)))
        b = mean(ys) - m*mean(xs)
        return m, b
