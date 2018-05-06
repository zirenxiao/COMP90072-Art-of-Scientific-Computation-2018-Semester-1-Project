import csv
from GraphPlot import GraphPlot
from Controll import Controll
from RestFrameMeson import RestFrameMeson
from MesonProbability import MesonProbability
from KineticEnergy import KineticEnergy
g = GraphPlot()
controll = Controll()
restMeson = RestFrameMeson()
prob = MesonProbability()
kinetice = KineticEnergy()

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
    # sectionOne(kurieVariable, momentum, totalEnergy)
    sectionTwo(10000, 200, 10)

# The running results of section 1
def sectionOne(kurieVariable, momentum, totalEnergy):
    # initialise classes

    # calculating variables
    kuriePeak = kinetice.positionOfPeak(kurieVariable)
    kuriePeakToEnd = kurieVariable[kuriePeak:]
    totalEnergyPeakToEnd = totalEnergy[kuriePeak:]
    betaKineticEnergy = kinetice.getGroupKineticEnergy(momentum)
    betaKineticEnergyPeakToEnd = betaKineticEnergy[kuriePeak:]
    # graph plots
    g.plotXY(totalEnergy, kurieVariable, "Total Energy", "Kurie Variable")
    g.plotXY(betaKineticEnergy, kurieVariable, "Kinetic Energy of Beta Particle (electron)", "Kurie Variable")
    print(str(betaKineticEnergy))
    g.plotBestFit(betaKineticEnergyPeakToEnd, kuriePeakToEnd)

def sectionTwo(size, mean, sd):
    pions, kaons = restMeson.generateMesons(size, mean, sd)
    # print("Number of Pions: " + str(len(pions)))
    # g.plotHist(pions)
    # print("Number of Kaons: " + str(len(kaons)))
    # g.plotHist(kaons)
    pionsDistance = controll.pionsDistanceTravelled(pions)
    kaonsDistance = controll.kaonsDistanceTravelled(kaons)
    # g.plotHist(cal.getDistance(pionsDistance))
    # g.plotHist(cal.getDistance(kaonsDistance))

    pionLabResult = controll.pionsLabMomentum(pionsDistance)
    # g.plotHist(cal.getLongitudinals(pionLabResult))
    # g.plotHist(cal.getTransverse(pionLabResult))
    kaonsLabResult = controll.kaonsLabMomentum(kaonsDistance)
    # g.plotHist(cal.getLongitudinals(kaonsLabResult))
    # g.plotHist(cal.getTransverse(kaonsLabResult))

    pionHitDetector = prob.calculatePercentHitDetector(pionLabResult)
    # kaonsHitDetector = cal.calculatePercentHitDetector(kaonsLabResult)
    print(pionHitDetector/len(pions))
    # print(kaonsHitDetector/len(kaons))

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
