import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
    # define variables
    current = []
    count = []
    correctCount = []
    magneticFieldStrength = []
    momentum = []
    totalEnergy = []
    totalEnergyInKeV = []
    kineticEnergy = []
    kurieVariable = []
    # read variables from file
    readFromFile(current, count, correctCount, magneticFieldStrength,
    momentum, totalEnergy, totalEnergyInKeV, kineticEnergy, kurieVariable)
    # Section 1
    sectionOne(totalEnergy, kurieVariable)

def sectionOne(totalEnergy, kurieVariable):
    plt.plot(totalEnergy, kurieVariable)
    plt.xlabel('Total Energy (J)')
    plt.ylabel('Kurie Variable')
    plt.show()

def plotBestFit(x, y):
    # Scatter plot
    plt.scatter(x, y)
    # Add correlation line
    axes = plt.gca()
    m, b = np.polyfit(x, y, 1)
    X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
    plt.plot(X_plot, m*X_plot + b, '-')
    plt.show()


def readFromFile(current, count, correctCount, magneticFieldStrength,
momentum, totalEnergy, totalEnergyInKeV, kineticEnergy, kurieVariable):
    with open('data_b.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        header = next(readCSV)
        for row in readCSV:
            current.append(row[0])
            count.append(row[2])
            correctCount.append(row[3])
            magneticFieldStrength.append(row[4])
            momentum.append(float(row[6]))
            totalEnergy.append(float(row[8]))
            totalEnergyInKeV.append(float(row[7]))
            kineticEnergy.append(float(row[9]))
            kurieVariable.append(float(row[10]))

if __name__== "__main__":
    main()
