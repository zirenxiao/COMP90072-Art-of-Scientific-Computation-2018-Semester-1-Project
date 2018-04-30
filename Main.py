import csv
from GraphPlot import GraphPlot
from Calculation import Calculation
import numpy as np

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
    # start each sections
    sectionOne(kurieVariable, momentum, totalEnergy)

# The running results of section 1
def sectionOne(kurieVariable, momentum, totalEnergy):
    # initialise classes
    g = GraphPlot()
    cal = Calculation()
    # calculating variables
    kuriePeak = cal.positionOfPeak(kurieVariable)
    kuriePeakToEnd = kurieVariable[kuriePeak:]
    totalEnergyPeakToEnd = totalEnergy[kuriePeak:]
    betaKineticEnergy = cal.getGroupKineticEnergy(momentum)
    betaKineticEnergyPeakToEnd = betaKineticEnergy[kuriePeak:]
    # graph plots
    g.plotXY(totalEnergy, kurieVariable, "Total Energy", "Kurie Variable")
    g.plotXY(betaKineticEnergy, kurieVariable, "Kinetic Energy of Beta Particle (electron)", "Kurie Variable")
    print(str(betaKineticEnergy))
    g.plotBestFit(betaKineticEnergyPeakToEnd, kuriePeakToEnd)

# Read data from data set
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
