import csv
def main():
    current = []
    count = []
    correctCount = []
    magneticFieldStrength = []
    momentum = []
    totalEnergy = []
    totalEnergyInKeV = []
    kineticEnergy = []
    kurieVariable = []
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
    print(momentum)
if __name__== "__main__":
    main()
